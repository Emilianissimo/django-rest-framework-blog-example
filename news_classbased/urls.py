from . import views
from django.urls import path

urlpatterns = [
    path('', views.Root.as_view(), name="class_based.root"),
    path('posts/', views.PostList.as_view(), name="class_based.post-list"),
    path('posts/<int:pk>/', views.PostDetails.as_view(), name="class_based.post-detail"),
    path('categories/', views.CategoryList.as_view(), name="class_based.category-list"),
    path('categories/<int:pk>/', views.CategoryDetails.as_view(), name="class_based.category-detail"),
]
