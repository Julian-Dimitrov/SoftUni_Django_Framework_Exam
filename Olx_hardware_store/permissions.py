from django.shortcuts import redirect
from django.contrib.auth import mixins as auth_mixins


class AuthUserPermissions(auth_mixins.PermissionRequiredMixin):
    def has_permission(self):
        return self.kwargs['pk'] == self.request.user.pk

    def handle_no_permission(self):
        return redirect('forbidden')
