from django.urls import path , include
from .views import home, results
from . import views

urlpatterns = [
    path('',home.as_view()),
    path('results/',results.as_view()),
]
