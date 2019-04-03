from .task_api import TaskAPI


_task_api = TaskAPI()


class Record:
    @staticmethod
    def all():
        raise NotImplementedError

    @staticmethod
    def api():
        return _task_api
