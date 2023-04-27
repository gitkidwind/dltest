from django.urls import path
from . import views


app_name = 'login_app'
urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('password_change/', views.password_change_view, name='password_change_view'),
    path('user_profile/', views.user_profile_view, name='user_profile_view'),
    path('user_profile/edit', views.user_profile_edit_view, name='user_profile_edit_view'),



]