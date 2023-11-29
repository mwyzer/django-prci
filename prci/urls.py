from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon/favicon.ico'))),
    path("", views.index, name="index"),
    path("publisher/", views.publisher_data, name="publisher"),

]
