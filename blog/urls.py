from django.urls import path
from . import views_v2

# Os nomes das views são os mesmos nas 3 versões (a v3 exporta "post_list = PostListView.as_view()" etc.)
urlpatterns = [
    path('', views_v2.home, name='home'),
    path('posts/', views_v2.post_list, name='post_list'),
    path('post/novo/', views_v2.post_create, name='post_create'),
    path('post/<int:pk>/', views_v2.post_detail, name='post_detail'),
    path('post/<int:pk>/editar/', views_v2.post_update, name='post_update'),
    path('post/<int:pk>/remover/', views_v2.post_delete, name='post_delete'),
]
