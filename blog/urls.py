from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', views.posts,name="posts" ),
    path('posts/<int:pk>/', views.more,name="more" ),
    path('posts/<int:pk>/delete/', views.delete,name="delete" ),
    path('posts/<int:pk>/edit/', views.edit,name="edit" ),
    path('create-post', views.form,name="form" ),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)