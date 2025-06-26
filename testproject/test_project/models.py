from django.db import models

class ProjectMaster(models.Model):
    project_name = models.CharField(max_length=255)
    sub_project = models.CharField(max_length=255)

    # def __str__(self):
    #     return f"{self.project_name} - {self.sub_project}"

    class Meta:
        db_table = 'projectmaster'

class ActivityMaster(models.Model):
    project_name = models.CharField(max_length=255)
    sub_project = models.CharField(max_length=255)
    activity_code = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    # def __str__(self):
    #     return f"{self.project_name} - {self.activity_code} - {self.activity_name}"

    class Meta:
        db_table = 'activitymaster'

class DailyProgress(models.Model):
    activity_code = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=255)
    progress_qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)


    # def __str__(self):
    #     return f"{self.activity_code} - {self.progress_qty}"


    class Meta:
        db_table = 'dailyprogress'