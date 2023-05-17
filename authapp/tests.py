from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import FndUserManager
from django.contrib.auth.models import User

# Create your tests here.
class FndUserManagerTest(TestCase):
    def setUp(self):
        self.test = User(username = 'test',email = 'anne@gmail.com', password ='1234')
        self.test = FndUserManager( email='anne@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.test,FndUserManager))

    def test_save_FndUserManager(self):
        self.save_FndUserManager()
        all_FndUserManagers = FndUserManager.objects.all()
        self.assertTrue(len(all_FndUserManagers),0)

    def test_delete_profile(self):
        self.test.delete_profile()
        all_profiles = FndUserManager.objects.all()
        self.assertEqual(len(all_profiles),0)

