from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import AddToolForm
from .models import Tool
from Olx_hardware_store.permissions import AuthUserPermissions


@login_required
def add_tool(request):
    form = AddToolForm()

    if request.method == 'POST':
        form = AddToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.user = request.user
            tool.save()

            return redirect('details_profile', pk=request.user.pk)

    context = {
        "form": form,
    }

    return render(request, 'tools/add_tool.html', context=context)


class DetailsToolView(views.DetailView):
    model = Tool
    template_name = 'tools/details_tool.html'


class EditToolView(AuthUserPermissions, views.UpdateView):
    model = Tool
    form_class = AddToolForm
    template_name = 'tools/edit_tool.html'

    def get_success_url(self):
        profileid = self.request.user.id
        return reverse_lazy('details_profile', kwargs={'pk': profileid})

    def has_permission(self):
        return self.get_object().user == self.request.user


class DeleteToolView(AuthUserPermissions, views.DeleteView):
    model = Tool
    template_name = 'tools/delete_tool.html'

    def get_success_url(self):
        profileid = self.request.user.pk
        return reverse_lazy('details_profile', kwargs={'pk': profileid})

    def has_permission(self):
        return self.get_object().user == self.request.user
