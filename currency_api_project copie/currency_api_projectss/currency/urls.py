from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TNDconvViewSet, DZDconvViewSet

# Créer un routeur pour les viewsets
router = DefaultRouter()
router.register(r'tnd', TNDconvViewSet)
router.register(r'dzd', DZDconvViewSet)

# Définir les URLs
urlpatterns = [
    path('', include(router.urls)),
]