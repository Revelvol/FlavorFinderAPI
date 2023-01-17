from django.test import TestCase , SimpleTestCase
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError

#test for django management command
@patch('core.management.commands.wait_for_db.Command.check') #mocking the wait for db, biar di test ini ga actually edit the db
class CommandTest(SimpleTestCase):
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])
