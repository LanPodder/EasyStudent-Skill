#
#   dataservice
#

from skill_sdk.services.persistence import BaseService
import pandas as pd

df_tasks = pd.DataFrame(columns=['task', 'deadline'])

def add_task(task: str, deadline):
    global df_tasks
    df_tasks = df_tasks.append({'task': task, 'deadline': deadline}, ignore_index = True)
    df_tasks = df_tasks.sort_values(by=['deadline'])

def get_tasks():
    global df_tasks
    return df_tasks['task']

def get_priority_task():
    global df_tasks
    return df_tasks.iloc[0]['task']