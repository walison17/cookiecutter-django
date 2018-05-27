from django.test import TestCase
from model_mommy import mommy


class ModelTestCase(TestCase):
    def test_model_profile(self):
        user = mommy.make('User')
        assert hasattr(user, 'created')
        assert hasattr(user, 'updated')
        assert user.profile is not None
