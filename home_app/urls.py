from django.urls import path
from . import views


app_name = 'home_app'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('price/', views.price_page, name='price_page'),
    path('schedule/', views.lesson_schedule_page, name='schedule_page'),
    path('instructor/', views.instructor_page, name='instructor_page'),
]