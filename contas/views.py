from django.shortcuts import render, redirect
from .models import User
import urllib.parse
from django.conf import settings
from .forms import UserAdminCreationForm
from django.views.generic import (
    CreateView, FormView, TemplateView, RedirectView
)
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
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

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class LoginView(FormView):
    template_name = 'contas/login.html'
    form_class = LoginForm

    def form_valid(self, form):

        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())



class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    next_page = 'contas/logout'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)