from django.db import models
from django.utils.translation import gettext_lazy as _
from form_app.models import DanceEvent


# Create your models here.
class VideoEventlist(models.Model):
    dance_events = models.ManyToManyField(DanceEvent, verbose_name=_("ダンスイベント"), related_name="dance_events")
    event_img_src = models.TextField(max_length=200,blank=True,verbose_name = "IMG_URL")
    class Meta:
        verbose_name ="イベント"
        verbose_name_plural = _("イベント")
    
    def __str__(self):
        dance_events_info = ', '.join([f"{d.event_title} ({d.event_day})" for d in self.dance_events.all()])
        return dance_events_info

class Video_detile(models.Model):
    parent_event = models.ForeignKey(VideoEventlist, on_delete=models.CASCADE, related_name='children_event')
    video_title = models.CharField(max_length=30,verbose_name ="作品名")
    video_file_path = models.CharField(max_length=30,verbose_name ="ビデオパス")
    video_img_path = models.CharField(max_length=30,verbose_name ="イメージパス")
    class Meta:
        verbose_name ="動画"
        verbose_name_plural = _("動画")

    def __str__(self):
        return self.video_title