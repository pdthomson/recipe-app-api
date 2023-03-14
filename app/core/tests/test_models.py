from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'Haisall@example.com'
        password = 'dodokilla'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['beannahdurke@EXAMPLE.com', 'beannahdurke@example.com'],
            ['Bethussy@EXAMPLE.com', 'Bethussy@example.com'],
            ['SIAGOTHILVEIRA@EXAMPLE.COM', 'SIAGOTHILVEIRA@example.com'],
            ['PacharyZrince@eXaMpLe.com', 'PacharyZrince@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)