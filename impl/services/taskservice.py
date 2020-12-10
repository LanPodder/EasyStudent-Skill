#
#   dataservice
#

from skill_sdk.services.persistence import BaseService
import pandas as pd

df_tasks = pd.DataFrame(columns=['task', 'deadline'])

def add_task(task: str, deadline):
    df_tasks.iloc[len(df_tasks)] = [task, deadline]
    df_tasks = df_tasks.sort_values(by=['deadlines'])

def get_tasks():
    return df_tasks['task']

def get_priority_task():
    return df_tasks.iloc[0]['task']