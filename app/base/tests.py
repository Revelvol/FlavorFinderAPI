from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.management import call_command
from django.db.utils import OperationalError
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error


@patch('base.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test for Database """
    def test_wait_for_db_ready(self, patched_check):
        """Test Waiting for Database if database ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test Waiting for Database if Database return Operational Error"""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True] #noqa

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(databases=['default'])

class ModelTest(TestCase):
    """Test for Model"""
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpassword1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email , expected)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class AdminTest(TestCase):
    def test_admin(self):
        pass