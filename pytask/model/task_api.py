from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import tools
from apiclient.discovery import build
import argparse
import json
import os

SCOPE = 'https://www.googleapis.com/auth/tasks'


class TaskAPI:
    def __init__(self):
        cwd = os.path.dirname(__file__)
        self.client_id = json.loads(open(cwd + '/client_id.json').read())
        self.cl_id = self.client_id['installed']['client_id']
        self.cl_secret = self.client_id['installed']['client_secret']
        self.flow = OAuth2WebServerFlow(
                client_id=self.cl_id,
                client_secret=self.cl_secret,
                scope='https://www.googleapis.com/auth/tasks',
                redirect_uri='http://google.com'
        )
        self.storage = Storage('a_storage')
        self.connected = False

    def _connect(self):
        if self.connected:
            return
        self.credentials = self.storage.get()

        if not os.path.isfile('a_storage'):
            self._authenticate()
        if not self.credentials.has_scopes(SCOPE):
            self._authenticate()

        self.service = build('tasks', 'v1', credentials=self.credentials)
        self.connected = True

    def _authenticate(self):
        parser = argparse.ArgumentParser(parents=[tools.argparser])
        flags = parser.parse_args()
        self.credentials = tools.run_flow(self.flow, self.storage, flags)
        self.storage.put(self.credentials)

    def get_tasklists(self):
        self._connect()
        return self.service.tasklists().list().execute()['items']

    def get_tasks(self, list_id):
        self._connect()
        return self.service.tasks().list(tasklist=list_id).execute()
