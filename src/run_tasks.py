import os

from mlboardclient.api import client


SUCCEEDED = 'Succeeded'
FAILED = 'Failed'


def main():
    ml = client.Client()

    current_task_name = os.environ.get('TASK_NAME')
    current_app = os.environ['APP_NAME']

    app = ml.apps.get(current_app)
    
    for task in app.tasks:
        

if __name__ == '__main__':
    main()
