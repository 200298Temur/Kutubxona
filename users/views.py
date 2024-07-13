from typing import Any
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout,login
from .forms import *
from main.views import menufunc
from django.http import  HttpResponseRedirect

class LoginUser(LoginView):
    form_class=LoginForm
    template_name="core/login.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['menu']=menufunc(self.request.user)
        context['title']="LogIn"
        return  context
    
    def get_success_url(self):
        return reverse_lazy("home")

def logoutDef(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))

class Register(CreateView):
    form_class=RegisterForm
    template_name="core/register.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['menu']=menufunc(self.request.user)
        context['title']='Registratsiya'
        return  context
    
    def get_success_url(self):
        return reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)