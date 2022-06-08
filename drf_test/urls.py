import news_viewset
from news_viewset import views
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

# Automatic routes
router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registering automatic routes
    path('api/view-sets/', include(router.urls)),

    # Custom routes (same models)
    path('api/func-based/', include('news.urls')),

    # ClassBased style
    path('api/class-based/', include('news_classbased.urls')),

    # GenericBased style
    path('api/generic-based/', include('news_genericbased.urls')),

    # MixinBased style
    path('api/mixin-based/', include('news_mixinbased.urls')),

    # Authentication (built-in)
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

