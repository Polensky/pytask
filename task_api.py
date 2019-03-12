from oauth2client.client import OAuth2WebServerFlow 
from oauth2client.file import Storage
from oauth2client import tools
from apiclient.discovery import build
import httplib2
import argparse
import json
import os
from tasklist import TaskList


SCOPE = 'https://www.googleapis.com/auth/tasks'

class TaskAPI:
    def __init__(self):
        self.client_id = json.loads(open('client_id.json').read())
        self.cl_id = self.client_id['installed']['client_id']
        self.cl_secret = self.client_id['installed']['client_secret']
        self.flow = OAuth2WebServerFlow(client_id=self.cl_id, client_secret=self.cl_secret, scope='https://www.googleapis.com/auth/tasks', redirect_uri='http://google.com')
        self.storage = Storage('a_storage')


    def connect(self):
        self.credentials = self.storage.get()

        # oof
        if not os.path.isfile('a_storage'): self.authenticate()
        if not self.credentials.has_scopes(SCOPE): self.authenticate()

        self.service = build('tasks', 'v1', credentials=self.credentials)
        return self.service

    def get_taskslists(self):
        tsk_lst = self.service.tasklists().list().execute()['items']
        l = []
        for tasklist in tsk_lst:
            name = tasklist['title']
            id = tasklist['id']
            l.append(TaskList(name, id))

        return l

    def authenticate(self):
        parser = argparse.ArgumentParser(parents=[tools.argparser])
        flags = parser.parse_args()
        self.credentials = tools.run_flow(self.flow, self.storage, flags)
        self.storage.put(self.credentials)


    def get_tasks(self, list_id):
        tasks = service.tasks().list(tasklist=list_id).execute()['items']

        for task in tasks:
            print(task)

