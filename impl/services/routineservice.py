#
#   routineservice
#

import pandas as pd

df_routines = pd.DataFrame(columns=['routine_description', 'routine_time'])

def add_routine(routine_description: str, routine_time: str):
    global df_routines
    df_routines = df_routines.append({'routine_description': routine_description, 'routine_time': routine_time}, ignore_index=True)  

def get_routine(routine_time):
    global df_routines
    return df_routinesf.loc[df_routines['routine_time'] == routine_time]['routine_description']