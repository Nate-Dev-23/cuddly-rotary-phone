from django.urls import path
from . import views
from .views import HomeView, Create, Read, Update, Delete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='house'),
    path('create/', Create.as_view(), name='create'),
    path('read/<int:pk>/', Read.as_view(), name='read'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]