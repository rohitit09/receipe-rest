from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    "testing user model"
    def test_create_user_with_email_successfully(self):
        "test user model emial is successfully"

        email="rohit@gmail.com"
        password="rohit"
        user=get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,password="test123")


    def test_create_super_user(self):
        user=get_user_model().objects.create_super_user("rohit@gmail.com","test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)