#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from unittest import mock
import unittest

from impl.add_todo import skill
from typing import List, Set, Dict, Tuple, Optional


class TestMain(unittest.TestCase):

    @mock.patch('impl.add_todo.add_task')
    def test_todo_without_deadline(self, add_mock):
        """ Add task with no deadline
        """
        response = skill.test_intent('TEAM_10_ADD_TASK', task_to_add=["ML Homework"])
        self.assertEqual(response.text, 'TEAM_10_ADD_TASK_NO_DEADLINE_SUCCESS_MESSAGE')


    @mock.patch('impl.add_todo.add_task')
    def test_todo_with_deadline(self, get_mock):
        """ Add task with deadline
        """
        response = skill.test_intent('TEAM_10_ADD_TASK', task_to_add=["ML Homework"], deadline=["morgen"])
        self.assertEqual(response.text, 'TEAM_10_ADD_TASK_PLUS_DEADLINE_SUCCESS_MESSAGE')
