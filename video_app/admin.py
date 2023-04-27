
# Register your models here.
from django.contrib import admin
from .models import VideoEventlist, Video_detile
from django.utils.translation import gettext_lazy as _

class VideoDetileInline(admin.TabularInline):
    model = Video_detile

class VideoEventlistAdmin(admin.ModelAdmin):
    list_display = ('get_dance_events', 'get_dance_events_info', 'event_img_src',)
    inlines = [VideoDetileInline]

    def get_dance_events_info(self, obj):
       return ', '.join([str(d.event_day) for d in obj.dance_events.all()])
    get_dance_events_info.short_description = _("イベント日")

    def get_dance_events(self, obj):
        return ', '.join([str(dance_event) for dance_event in obj.dance_events.all()])
    get_dance_events.short_description = _("ダンスイベント名")

    

class VideoDetileAdmin(admin.ModelAdmin):
    list_display = ('get_parent_event', 'video_title', 'video_file_path', 'video_img_path')
    
    def get_parent_event(self, obj):
        return ', '.join([str(children_event) for children_event in obj.children_event.all()])
    get_parent_event.short_description = _("ダンスイベント名")

admin.site.register(VideoEventlist, VideoEventlistAdmin)
admin.site.register(Video_detile)