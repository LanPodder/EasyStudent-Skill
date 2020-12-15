#
# voice-skill-sdk
#
# (C) 2020, Alan I-Shref (Hackathon_Team_10), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _

from .services.taskservice import add_task, update_deadline

temp = None

@skill.intent_handler('TEAM_10_ADD_TASK')
def handler(task_to_add: str, deadline: str = None) -> Response:
    """ Handler for adding TODOs with deadlines

    :param task_to_add:    str
    :param deadline: str = None
    :return:        Response
    """
    global temp
    # We get a translated message
    task = task_to_add
    deadl = deadline

    if task_to_add is not None:
        temp = task_to_add
        add_task(task_to_add, deadline)    
    
    if deadline is not None:
        task, deadl = update_deadline(temp, deadline)

    
    msg = _('TEAM_10_ADD_TASK_NO_DEADLINE_SUCCESS_MESSAGE', task_to_add = task)
    if(deadline is not None):
        msg = _('TEAM_10_ADD_TASK_PLUS_DEADLINE_SUCCESS_MESSAGE', task_to_add = task, deadline = deadl)
        
    # We create a simple response
    response = tell(msg)

    # We return the response
    if deadline is None:
        return ask(_('TEAM_10_ASK_TASK_DEADLINE', task_to_add = task_to_add))
    
    return response
