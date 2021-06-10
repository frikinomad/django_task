from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        print(User)
        print('hiiiiii')
        User.objects.create_user(email='normal@user.com', password='foo')

        user = User.objects.get(email='normal@user.com')
        print(user)
        self.assertEqual(user, 'normal@user.com')

    # def test_create_superuser(self):
    #     User = get_user_model()
    #     admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
    #     self.assertEqual(admin_user.email, 'super@user.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(admin_user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(ValueError):
    #         User.objects.create_superuser(
    #             email='super@user.com', password='foo', is_superuser=False)