from django.urls import path
from . import views
urlpatterns = [
    path('finalmeetups/',views.index)
]