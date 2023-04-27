from django.urls import path
from . import views



app_name = 'form_app'
urlpatterns = [
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/confirm/', views.contact_confirm_view, name='contact_confirm_view'),
    path('complete/', views.contact_complete_view, name='contact_complete_view'),
    path('contact/lesssen', views.dance_lesson_contact_view, name='dance_lesson_contact_view'),
    path('contact/lesssen/confirm', views.dance_lesson_contact_confirm_view, name='dance_lesson_contact_confirm_view'),
    path('contact/lesssen/complete', views.dance_lesson_contact_complete_view, name='dance_lesson_contact_complete_view'),
    path('danceworks/', views.dancework_list, name='dancework_list'),
    path('danceworks/new', views.dancework_new, name='dancework_new'),
    path('danceevent/', views.danceevent_list, name='danceevent_list'),
    path('danceevent/new', views.danceevent_new, name='danceevent_new'),
    path('danceevent/register/', views.register_dance_event, name='register_dance_event'),
    path('danceevent/register/home', views.dance_event_registration_home, name='dance_event_registration_home'),
    path('danceevent/register/<int:registration_id>/edit/', views.edit_dance_event_registration, name='register_dance_event_edit'),
    path('danceevent/register/confirm/', views.confirm_dance_event_registration, name='register_dance_event_confirm'),
    path('danceevent/register/complete/', views.complete_dance_event_registration, name='register_dance_event_complete'),
    path('danceevent/register/delete/<int:registration_id>/', views.delete_dance_event_registration, name='register_dance_event_delete'),
]