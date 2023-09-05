from django.urls import path

from . import views

urlpatterns = [
    path('server/',views.server,name="server"),
    path('client/',views.client,name="client"),
    path('',views.home,name="home")
]
