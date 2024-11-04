from django.urls import path
from MainApp.views import home

urlpatterns = [
    path('', home, name='home'),
]
