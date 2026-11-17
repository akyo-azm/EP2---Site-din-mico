from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/novo/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/editar/', views.post_update, name='post_update'),
    path('post/<int:pk>/remover/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comentar/', views.comment_create, name='comment_create'),
    path('categorias/', views.category_list, name='category_list'),
    path('categorias/<int:pk>/', views.category_detail, name='category_detail'),
]