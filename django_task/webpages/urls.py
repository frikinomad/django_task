from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>', views.delete_user, name="delete_user"),
    path('webpages/<int:pk>', views.edit_user, name="edit_user"),
]
