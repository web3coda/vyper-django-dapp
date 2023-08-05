from django.urls import path

from . import views

urlpatterns = [
    path('server/',views.server,name="server"),
    path('client/',views.server,name="client"),
    path('',views.home,name="home")
]