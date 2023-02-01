import factory
import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from dukka_assessment.users.api.serializers import UserSerializer
from dukka_assessment.users.api.views import UserViewSet
from dukka_assessment.users.models import User

from .factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == UserSerializer(user).data

    @pytest.mark.parametrize("method", ["put", "patch", "get"])
    def test_no_authorization(self, method: str, client: APIClient):
        methods = {"put": client.put, "patch": client.patch, "get": client.get}
        response = methods[method](reverse("api:users"))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create(self, client: APIClient):
        obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        obj["password2"] = obj["password"] = "password"
        response = client.post(reverse("api:users"), obj)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["email"] == User.objects.last().email

    def test_create_with_wrong_password(self, client: APIClient):
        obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        obj["password2"] = "test"
        obj["password"] = "password"
        response = client.post(reverse("api:users"), obj)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update(self, client: APIClient):

        obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        new_obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        user = UserFactory(**obj)
        client.force_authenticate(user=user)
        response = client.put(reverse("api:users"), obj | new_obj)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == new_obj["name"]
        assert response.data["email"] == obj["email"]

    @pytest.mark.parametrize("field", ["name", "sex", "country"])
    def test_partial_update(self, field: str, client: APIClient):
        obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        new_obj = factory.build(dict, FACTORY_CLASS=UserFactory)
        user = UserFactory(**obj)

        client.force_authenticate(user=user)
        response = client.patch(reverse("api:users"), {field: new_obj[field]})

        assert response.status_code == status.HTTP_200_OK
        assert response.data[field] == new_obj[field]

    def test_auth_token(self, client: APIClient):

        user = UserFactory(password="test")
        response = client.post(
            reverse("auth-token"), {"email": user.email, "password": "test"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert "token" in response.data
