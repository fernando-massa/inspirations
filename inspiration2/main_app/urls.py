from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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

# ------------------Gallery-------------------------------------------------
    # http://localhost:8000/galleries/
    path('galleries/', views.GalleryList.as_view(), name='galleries_index'),
    # http://localhost:8000/galleries/1/
    path('galleries/<int:pk>/', views.GalleryDetail.as_view(), name='galleries_detail'),
    # http://localhost:8000/galleries/create/
    path('galleries/create/', views.GalleryCreate.as_view(), name='galleries_create'),
    # http://localhost:8000/galleries/1/update/
    path('galleries/<int:pk>/update/', views.GalleryUpdate.as_view(), name='galleries_update'),
    # http://localhost:8000/galleries/1/delete/
    path('galleries/<int:pk>/delete/', views.GalleryDelete.as_view(), name='galleries_delete'),


# ------------------Sign up-------------------------------------------------

    path('accounts/signup/', views.signup, name='signup'),

]