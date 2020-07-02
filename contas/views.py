from django.shortcuts import render, redirect
from .models import User
from .forms import UserAdminCreationForm
from django.views.generic import (
    CreateView
)
from django.urls import reverse
# Create your views here.

class CadastroView(CreateView):

    model = User
    template_name = 'contas/cadastro.html'
    form_class = UserAdminCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
    