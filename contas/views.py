from django.shortcuts import render, redirect
from .models import User
import urllib.parse
from django.conf import settings
from .forms import UserAdminCreationForm
from django.views.generic import (
    CreateView, FormView, TemplateView
)
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import LoginForm
from django.http import HttpResponseRedirect
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
    

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'index.html'

class LoginView(FormView):
    template_name = 'contas/login.html'
    form_class = LoginForm

    def form_valid(self, form):

        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.REQUEST.get(self.redirect_field_name, '')

        netloc = urllib.parse.urlparse(redirect_to)[1]
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        # Security check -- don't allow redirection to a different host.
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL
        return redirect_to
