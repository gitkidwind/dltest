from django.urls import path
from . import views


app_name = 'video_app'
urlpatterns = [
    path('', views.video_top_page, name='video_top_page'),
    # path('detail/', views.home_page, name='home_page'),
    path('play/', views.video_play_page, name='video_play_page'),

]