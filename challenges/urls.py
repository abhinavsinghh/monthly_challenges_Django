from django.urls import path
from . import views


urlpatterns = [
    # path("January", views.january),
    # path("February", views.february),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month_challenge"),
]