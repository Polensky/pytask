from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import tools
from apiclient.discovery import build
import httplib2
import argparse
import json
import os
from .tasklist import TaskList
from .task import Task

SCOPE = 'https://www.googleapis.com/auth/tasks'

class TaskAPI:
    def __init__(self):
        cwd = os.path.dirname(__file__)
        self.client_id = json.loads(open(cwd + '/client_id.json').read())
        self.cl_id = self.client_id['installed']['client_id']
        self.cl_secret = self.client_id['installed']['client_secret']
        self.flow = OAuth2WebServerFlow(client_id=self.cl_id, client_secret=self.cl_secret, scope='https://www.googleapis.com/auth/tasks', redirect_uri='http://google.com')
        self.storage = Storage('a_storage')


    def connect(self):
        self.credentials = self.storage.get()

        # oof
        if not os.path.isfile('a_storage'): self._authenticate()
        if not self.credentials.has_scopes(SCOPE): self._authenticate()

        self.service = build('tasks', 'v1', credentials=self.credentials)
        return self.service

    def _authenticate(self):
        parser = argparse.ArgumentParser(parents=[tools.argparser])
        flags = parser.parse_args()
        self.credentials = tools.run_flow(self.flow, self.storage, flags)
        self.storage.put(self.credentials)

    def get_taskslists(self):
        tsk_lst = self.service.tasklists().list().execute()['items']
        l = []
        for tasklist in tsk_lst:
            l_name = tasklist['title']
            l_id = tasklist['id']
            t = self.get_tasks(l_id)
            l.append(TaskList(l_name, l_id, t))

        return l

    def get_tasks(self, list_id):
        tasks = self.service.tasks().list(tasklist=list_id).execute()

        if not 'items' in tasks: return None

        t = []
        for task in tasks['items']:
            name = task['title']
            id = task['id']
            status = task['status']
            t.append(Task(name, id, status))

        return t

