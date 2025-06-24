from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create user"""

        email = "test@example.com"
        password = "password"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test create a superuser"""

        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "password",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
