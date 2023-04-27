from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , ChildUser
# Register your models here.
class ChildUserInline(admin.TabularInline):
    list_display = ('name', 'parent', 'birth_date', 'age')
    list_filter = ('parent',)
    search_fields = ('name', 'parent__email')

    model = ChildUser

class CustomUserAdmin(UserAdmin):
    inlines = [ChildUserInline]
    list_display = ('email', 'first_name', 'last_name','is_movie_subscription', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_movie_subscription','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        #('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


