from django.urls import resolve
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Ne pas appliquer cette authentification personnalisée sur l'endpoint de refresh
        current_url_name = resolve(request.path_info).url_name
        if current_url_name in ['token_refresh', 'token_obtain_pair']:  # évite aussi de gêner login
            return None

        header = self.get_header(request)
        if header is None:
            raise AuthenticationFailed("Aucun token fourni.")

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed("Format du token invalide.")

        try:
            validated_token = self.get_validated_token(raw_token)
        except InvalidToken as e:
            error = str(e)
            if "Token is expired" in error:
                raise AuthenticationFailed("Votre session a expiré : le token JWT est expiré.")
            else:
                raise AuthenticationFailed("Le token JWT est invalide.")
        except TokenError:
            raise AuthenticationFailed("Erreur dans le token JWT.")

        user = self.get_user(validated_token)
        if user is None:
            raise AuthenticationFailed("Utilisateur introuvable.")

        return (user, validated_token)
