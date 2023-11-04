from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index, name='home'),
    path("index",views.index, name='home'),
    path("about",views.about, name='about'),
    path("login1",views.login1, name='login1'),
    path("signup",views.signup, name='signup'),

    path("category/<slug:val>",views.CategoryView.as_view(), name='category'),
]