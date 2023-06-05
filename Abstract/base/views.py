from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import DetailView, ListView
from .models import Home

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'base/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('house')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('house')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('house')
        return super(RegisterPage, self).get(*args, **kwargs)




class HomeView(LoginRequiredMixin, ListView):
    model = Home
    template_name = 'base/home.html'
    context_object_name = 'houses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = context['houses'].filter(user=self.request.user)
        return context


    

class Create(LoginRequiredMixin, CreateView):
    model = Home
    fields = ['name', 'email']
    success_url = reverse_lazy('house')
    template_name = 'base/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create, self).form_valid(form)


class Read(LoginRequiredMixin, DetailView):
    model = Home
    template_name = 'base/read.html'
    context_object_name = 'reader'

class Update(LoginRequiredMixin, UpdateView):
    model = Home
    fields = ['name', 'email']
    template_name = 'base/update.html'
    success_url = reverse_lazy('house')

class Delete(LoginRequiredMixin, DeleteView):
    model = Home
    fields = '__all__'
    template_name = 'base/delete.html'
    success_url = reverse_lazy('house')

