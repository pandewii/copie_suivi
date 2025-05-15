from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Routes de l'app currency
    path('api/currency/', include('currency.urls')),

    # Authentification JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
]
