from django.urls import path

from dukka_assessment.users.api.views import user_endpoints

app_name = "api"
urlpatterns = [
    path("users/", user_endpoints, name="users"),
]
