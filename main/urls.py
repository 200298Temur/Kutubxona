from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("avtor/",Muharirlar.as_view(),name="avtor"),
    path("addavtor/",AddAvtor.as_view(),name="addavtor"),
    path("showavtor/<slug:avtor_slug>/", showavtorDef, name="showavtor"),
    path("addkitob/",AddKitob.as_view(),name="addkitob"),
    path("authorlar/<int:author_id>",Showcaregory.as_view(),name="authorlar"),
]