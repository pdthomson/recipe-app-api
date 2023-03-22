from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core import models


def create_user(email='user@exampl.com', password='testpass123'):
    return get_user_model().objects.create_user(email, password)


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

    def test_new_user_without_email_raises_error(self):
        """Tests that creating a user without and email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'password')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'DirleyShCesari@example.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe works"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample title',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description',
        )
        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag successfully"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name="Tag1")

        self.assertEqual(str(tag), tag.name)
