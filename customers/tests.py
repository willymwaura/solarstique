from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.test = User(username = 'test',email = 'tess@gmail.com')
        self.test = Profile( email='tess@gmail.com', Upload_Cv ='image.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.test,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.test.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)