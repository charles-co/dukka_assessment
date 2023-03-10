from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):

    email = Faker("email")
    name = Faker("name")
    country = Faker("country")
    sex = Faker("random_element", elements=("M", "F", "O"))
    phone_number = "+2348098488484"

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        if not isinstance(self, dict):
            self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["email"]
