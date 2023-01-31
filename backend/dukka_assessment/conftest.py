import pytest
from rest_framework.test import APIClient

from dukka_assessment.users.models import User
from dukka_assessment.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def client() -> APIClient:
    return APIClient()
