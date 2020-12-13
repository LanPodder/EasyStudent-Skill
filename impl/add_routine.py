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

from .services.routineservice import add_routine

@skill.intent_handler('TEAM_10_ADD_ROUTINE')
def handler(routine_description: str, routine_time: str) -> Response:
    """ Handler that adds a routine

    :param routine_description:    str
    :param routine_time: str = None
    :return:        Response
    """

    msg = _('TEAM_10_ADDED_ROUTINE', routine_description, routine_time)
    
    add_routine(routine_description, routine_time)
    
    response = tell(msg)
    return response
