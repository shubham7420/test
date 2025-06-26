from django.contrib import admin
from .models import ProjectMaster, ActivityMaster, DailyProgress

admin.site.register(ProjectMaster)
admin.site.register(ActivityMaster)
admin.site.register(DailyProgress)
