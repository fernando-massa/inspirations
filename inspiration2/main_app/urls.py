from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('galleries/', views.gallery_index, name='index'),
    # http://localhost:8000/cats/1/
path('galleries/', views.inspiration_index, name='detail'),

path('inspirations/<int:inspiration_id>/add_photo/', views.add_photo, name='add_photo'),
path('accounts/signup/', views.signup, name='signup'),

]