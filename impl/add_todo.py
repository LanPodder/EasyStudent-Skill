#
# voice-skill-sdk
#
# (C) 2020, Alan I-Shref (Hackathon_Team_10), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _

from .services.taskservice import add_task

@skill.intent_handler('TEAM_10_ADD_TASK')
def handler(task_to_add: str, deadline: str = None) -> Response:
    """ Handler for adding TODOs with deadlines

    :param task_to_add:    str
    :param deadline: str = None
    :return:        Response
    """
    # We get a translated message
    msg = _('TEAM_10_ADD_TASK_NO_DEADLINE_SUCCESS_MESSAGE') 
    if(deadline is not None):
        msg = _('TEAM_10_ADD_TASK_PLUS_DEADLINE_SUCCESS_MESSAGE')
    
    
    add_todo(task_to_add)

    print(msg)
    # We create a simple response
    response = tell(msg)
    # We return the response
    return response
