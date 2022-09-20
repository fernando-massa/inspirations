from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('galleries/', views.gallery_index, name='index'),


# ------------------Inspiration----------------------------------------------
    
    # show all the inspirations added
    # http://localhost:8000/inspirations/
    path('inspirations/', views.inspiration_index, name='inspirations_index'),

    # click in to see the details of selected inspiration
    # http://localhost:8000/inspirations/1/
    path('inspirations/<int:inspiration_id>/', views.inspirations_detail, name='detail'),

    # new route used to show a form and create a inspiration.
    # http://localhost:8000/inspirations/create/
    path('inspirations/create/', views.InspirationCreate.as_view(), name='inspirations_create'),

    # update the inspiration 
    # http://localhost:8000/inspirations/1/update/
    path('inspirations/<int:pk>/update/',
        views.InspirationUpdate.as_view(), name='inspirations_update'),

    # delete the inspiration
    # http://localhost:8000/inspirations/1/delete/
    path('inspirations/<int:pk>/delete/',
        views.InspirationDelete.as_view(), name='inspirations_delete'),

# ------------------Sign up-------------------------------------------------

path('accounts/signup/', views.signup, name='signup'),

]