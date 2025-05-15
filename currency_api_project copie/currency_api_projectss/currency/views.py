from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend

from .models import TNDconv, DZDconv
from .serializers import TNDconvSerializer, DZDconvSerializer
from .permissions import IsTNDu, IsDZDu  # Permissions personnalisées

# ✅ LOGIN VIEW
class CustomLoginView(APIView):
    permission_classes = []  # Pas besoin d'être authentifié pour se connecter

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Veuillez fournir un nom d'utilisateur et un mot de passe."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Identifiants incorrects."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        # Redirection selon le groupe
        if user.groups.filter(name='TNDu').exists():
            redirect_url = '/api/tnd/rates/'
        elif user.groups.filter(name='DZDu').exists():
            redirect_url = '/api/dzd/rates/'
        else:
            return Response(
                {"error": "Vous n'avez pas les permissions nécessaires."},
                status=status.HTTP_403_FORBIDDEN
            )

        return Response({
            "message": "Connexion réussie.",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "redirect_url": redirect_url
        }, status=status.HTTP_200_OK)

# ✅ VIEWSET POUR TND
class TNDconvViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TNDconv.objects.all()
    serializer_class = TNDconvSerializer
    permission_classes = [IsAuthenticated, IsTNDu]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'eur', 'usd']

# ✅ VIEWSET POUR DZD
class DZDconvViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DZDconv.objects.all()
    serializer_class = DZDconvSerializer
    permission_classes = [IsAuthenticated, IsDZDu]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'tnd', 'eur', 'usd']
