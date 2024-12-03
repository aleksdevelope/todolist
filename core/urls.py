from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index),
    path('editing_note', views.editing_note),
    path('about', views.about)
]