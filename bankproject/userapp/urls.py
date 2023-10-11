from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('button/',views.button, name='button'),
    path('customer_forms/', views.Customer_forms, name='Customer_forms'),
    path('branches', views.branches, name = 'branches'),

]
