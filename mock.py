from tasklist import TaskList
from task import Task


def gen_mock(nb):
    tasklists = []
    for i in range(nb):
        tasks = []
        for j in range(nb):
            tasks.append(Task(f'a task {j}', j, 'ok'))
        tasklist.append(TaskList(f'a Tasklist {i}', i, tasks))
        return tasklists
