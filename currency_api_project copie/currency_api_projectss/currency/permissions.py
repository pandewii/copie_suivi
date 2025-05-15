from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsTNDu(BasePermission):
    """
    Permission pour les utilisateurs du groupe TNDu.
    """
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='TNDu').exists():
            return True
        raise PermissionDenied(detail="Accès refusé : vous n'êtes pas autorisé à consulter les taux TND.")

class IsDZDu(BasePermission):
    """
    Permission pour les utilisateurs du groupe DZDu.
    """
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='DZDu').exists():
            return True
        raise PermissionDenied(detail="Accès refusé : vous n'êtes pas autorisé à consulter les taux DZD.")
