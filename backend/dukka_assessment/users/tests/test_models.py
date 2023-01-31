import pytest

from dukka_assessment.users.models import User

pytestmark = pytest.mark.django_db


class TestUserModels:
    def test_user_creation(self, user: User):
        assert user.pk is not None

    def test_user_unique_email(self, user: User):
        with pytest.raises(Exception):
            User.objects.create_user(email=user.email, password="test")

    def test__str__(self, user: User):
        assert user.__str__() == f"{user.email} - {user.name}"
