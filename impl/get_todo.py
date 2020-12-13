#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _

from .services.taskservice import get_tasks

@skill.intent_handler('TEAM_10_RETRIEVE_TASK')
def handler() -> Response:
    """ Handler for retrieving todos
    
    :return:        Response
    """
    print(get_tasks())
    my_tasks = get_tasks()
    # We get a translated message
    msg = _('TEAM_10_RETRIEVE_TODOS_SUCCESS_MESSAGE')
    print(msg)
    # We create a simple response
    response = tell(msg)
    # We return the response
    return response
