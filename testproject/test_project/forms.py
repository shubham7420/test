from django import forms
from .models import ProjectMaster, ActivityMaster, DailyProgress

class ProjectMasterForm(forms.ModelForm):
    class Meta:
        model = ProjectMaster
        fields = '__all__'

class ActivityMasterForm(forms.ModelForm):
    class Meta:
        model = ActivityMaster
        fields = '__all__'

class DailyProgressForm(forms.ModelForm):
    class Meta:
        model = DailyProgress
        fields = '__all__'
