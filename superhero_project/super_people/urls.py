from django.urls import path

from . import views

app_name = 'super_people'
urlpatterns = [
    path('', views.index, name='index')
]
