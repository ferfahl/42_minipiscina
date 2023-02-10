from django.urls import path
from ex00 import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='first_page'), # Notice the URL has been named
]