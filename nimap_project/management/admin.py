from django.contrib import admin
from .models import Client, Project

admin.site.register(Client)
admin.site.register(Project)


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')  # Customize the columns to display

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'client', 'start_date', 'end_date')  # Customize the columns to display
