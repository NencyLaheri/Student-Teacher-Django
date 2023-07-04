from django.contrib import admin
from .models import CustomUser,ApplicationModel

# admin.site.register(CustomUser)

class ApplicationInline(admin.TabularInline):
    model = ApplicationModel

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','password','is_active','role','is_staff')
    inlines=[ApplicationInline]

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ApplicationModel)