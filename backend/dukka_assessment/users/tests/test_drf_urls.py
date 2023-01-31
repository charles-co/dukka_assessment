from django.urls import resolve, reverse

from dukka_assessment.users.models import User


def test_user_enpoints(user: User):
    assert reverse("api:users") == "/api/v1/users/"
    assert resolve("/api/v1/users/").view_name == "api:users"
