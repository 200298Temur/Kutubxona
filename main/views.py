from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import FileResponse, Http404
import os
from .models import *
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .forms import *


def menufunc(user):
   if(user.is_authenticated and user.groups.filter(name="Kutubxona").exists()):
      return [
         {"title":"Home",'url_name':'home'},
         {"title":"Muarrirlar",'url_name':'avtor'},
         {"title":"Add Muhharir",'url_name':'addavtor'},
         {"title":"Add Kitob",'url_name':'addkitob'},
      ]
   else:
      return [
         {"title":"Home",'url_name':'home'},
         {"title":"Muarrirlar",'url_name':'avtor'},
      ]
   



class HomeView(ListView):
    model=Kitob
    paginate_by=2
    template_name="core/home.html"
    context_object_name="posts"
    title_page="Asosiy Oyna"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['menu']=menufunc(self.request.user)
        return context
    class Meta:
        fields=['name','author','photo','file']




def showavtorDef(request, avtor_slug):
    post = get_object_or_404(Author, slug=avtor_slug)
    
    data = {
        'post': post,
        'menu': menufunc(request.user),
        'title': f"{post.name} haqida"
    }
    return render(request, "core/showavtor.html", data)

class AddAvtor(CreateView):
   form_class=AddAvtorForm
   template_name="core/addavtor.html"
   context_object_name="posts"
   success_url=reverse_lazy("home")
   
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menufunc(self.request.user)
        return context

class Muharirlar(ListView):
    model=Author
    template_name="core/avtor.html"
    paginate_by=7
    context_object_name="posts"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menufunc(self.request.user)
        return context

class AddKitob(CreateView):
   form_class=AddKitobForm
   template_name="core/addkitob.html"
   context_object_name='posts'
   success_url=reverse_lazy("home")

   def get_context_data(self, **kwargs):
       context=super().get_context_data(**kwargs) 
       context['title']="Mualliflar"
       context['menu']=menufunc(self.request.user)
       return context

class Showcaregory(ListView):
    model=Kitob
    template_name="core/home.html"
    paginate_by=2
    context_object_name="posts"
    
    def  get_queryset(self):
       author_id = self.kwargs.get('author_id')
       user = self.request.user
       if author_id is not None:
            return Kitob.objects.filter(author__id=author_id, is_published=True)
       else:
            return Kitob.objects.none()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        author_id = self.kwargs.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        context['title'] = f"{author.name} maqolalari"
        context['menu'] = menufunc(self.request.user)
        context['cat_selected'] = author_id  
        return context
