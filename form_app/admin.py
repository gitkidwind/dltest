from django.contrib import admin
from .models import Contact ,DanceLessonContact , DanceWork ,DanceEvent ,DanceEventRegistration
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'telphone_number', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email', 'telphone_number', 'content')

admin.site.register(Contact, ContactAdmin)


class DanceLessonContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'desired_date', 'desired_class', 'telphone_number', 'email', 'created_at')
    list_filter = ('gender', 'desired_class', 'created_at')
    search_fields = ('name', 'parent_name', 'telphone_number', 'email', 'content')
    date_hierarchy = 'created_at'

admin.site.register(DanceLessonContact, DanceLessonContactAdmin)


class DanceWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'rehearsal_time', 'rehearsal_cost')

admin.site.register(DanceWork, DanceWorkAdmin)


class DanceEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_day', 'start_time', 'place')

admin.site.register(DanceEvent, DanceEventAdmin)



class DanceEventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'get_child_users', 'get_dance_works')

    def get_child_users(self, obj):
        return "\n".join([c.name for c in obj.child_users.all()])

    def get_dance_works(self, obj):
        return "\n".join([w.name for w in obj.dance_works.all()])

    get_child_users.short_description = '参加者'
    get_dance_works.short_description = '出演曲'

admin.site.register(DanceEventRegistration, DanceEventRegistrationAdmin)