"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTest(TestCase):
    """ Test model."""

    def test_create_user_with_email_successful(self):
        """ Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "testpass123"
        user = User.objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
