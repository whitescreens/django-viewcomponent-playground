from django.urls import path
from django.conf import settings

from . import views


urlpatterns = [
    path(
        "fruits/",
        views.FruitsView.as_view(),
        name="fruits",
    ),
]