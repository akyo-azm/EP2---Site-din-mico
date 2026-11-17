from django.urls import path
from . import views

# Os nomes das views são os mesmos nas 3 versões (a v3 exporta "post_list = PostListView.as_view()" etc.)
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/novo/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/editar/', views.post_update, name='post_update'),
    path('post/<int:pk>/remover/', views.post_delete, name='post_delete'),
]
