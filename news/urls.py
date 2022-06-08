from . import views
from django.urls import path

urlpatterns = [
    path('', views.api_root, name="func_based.root"),
    path('posts/', views.post_list, name="func_based.post-list"),
    path('posts/<int:pk>/', views.post_detail, name="func_based.post-detail"),
    path('categories/', views.category_list, name="func_based.category-list"),
    path('categories/<int:pk>/', views.category_detail, name="func_based.category-detail"),
]
