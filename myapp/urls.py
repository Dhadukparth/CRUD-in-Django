from . import views
from django.urls import path

urlpatterns = [
    path('', views.empty),
    path('display', views.display),
    path('update', views.update),
    path('delete', views.delete),
    path('signupForm', views.signupForm),
    path('loginForm', views.loginForm),
    path('updateForm', views.updateForm),
    path('deleteForm', views.deleteForm),
]
