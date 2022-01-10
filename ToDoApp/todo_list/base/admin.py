from django.contrib import admin

# Register your models here.


from .models import Task
# Register model with admin panel
admin.site.register(Task)
