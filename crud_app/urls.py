from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="home"),
    path("form/",form,name="form"),
    path("contact/",contact,name="contact"),
    path("about/",about,name="about"),
    path("delete/<int:id>",delete_data,name='delete'),
    path("edit/<int:id>",update_data,name='edit'),
    path("deleted/",deleted,name='deleted_data'),
    path("restore/<int:id>/",restore,name="restore_data")
]