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

from .services.routineservice import get_routine

@skill.intent_handler('TEAM_10_RETRIEVE_ROUTINE')
def handler(routine_time: str) -> Response:
    """ Handler for retrieving todos

    :param: str routine_time
    :return:        Response
    """
    print(get_routine(routine_time))
    routine = get_routine(routine_time)
    
    # We get a translated message
    msg = _('TEAM_10_RETRIEVE_ROUTINE_SUCCESS_MESSAGE', routine_time = routine_time, routine_description =  ",".join(routine.values.tolist()))
    print(msg)
    # We create a simple response
    response = tell(msg)
    # We return the response
    return response
