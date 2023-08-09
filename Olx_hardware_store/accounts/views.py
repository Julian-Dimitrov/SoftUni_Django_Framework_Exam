from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import RegisterUserForm, EditProfileForm, PhoneNumbersUserForm
from .models import HwStoreUser


class ForbiddenView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'perm_denied.html', status=403)


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class DetailsProfileView(views.DetailView):
    model = HwStoreUser
    template_name = 'accounts/profile/details_profile.html'

    def get_context_data(self, **kwargs):  # tova ni dava da imame dadenite tools za user-a
        context = super().get_context_data(**kwargs)

        context['tools'] = self.request.user.tool_set.all()
        return context


class EditProfileView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    model = HwStoreUser
    form_class = EditProfileForm
    template_name = 'accounts/profile/edit_profile.html'

    def get_success_url(self):
        profileid = self.kwargs['pk']
        return reverse_lazy('details_profile', kwargs={'pk': profileid})

    def get_object(self, queryset=None):
        return self.request.user

    def has_permission(self):
        return self.kwargs['pk'] == self.request.user.pk

    def handle_no_permission(self):
        return redirect('forbidden')


class DeleteProfileView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    model = HwStoreUser
    template_name = 'accounts/profile/delete_profile.html'
    success_url = reverse_lazy('register_user')

    def has_permission(self):
        return self.kwargs['pk'] == self.request.user.pk

    def handle_no_permission(self):
        return redirect('forbidden')


@login_required
def add_phone_numbers(request, pk):
    form = PhoneNumbersUserForm()

    if request.method == 'POST':
        form = PhoneNumbersUserForm(request.POST)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.user = request.user
            phone.save()

            return redirect('details_profile', pk=request.user.pk)

    context = {
        "form": form,
    }

    return render(request, 'accounts/profile/contacts_profile.html', context=context)
