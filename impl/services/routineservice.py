#
#   routineservice
#

import pandas as pd

df_routines = pd.DataFrame(columns=['routine_description', 'routine_time'])

def add_routine(routine_description: str, routine_time: str):
    df_routines.iloc[len(df_routines)] = [routine_description, routine_time]

def get_routine(routine_time):    
    return df.loc[df['routine_time'] == routine_time]['routine_description']