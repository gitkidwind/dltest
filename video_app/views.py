from django.shortcuts import render

# Create your views here.

def video_top_page(request):
    #obj = Event_Application.objects.first()


    return render(request,'video_app/video_top_page.html',)

def video_play_page(request):
    #obj = Event_Application.objects.first()


    return render(request,'video_app/video_play_page.html',)