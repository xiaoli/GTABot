from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.TextField(default="")

    class Meta:
        app_label = 'research'

class Paper(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    short_id = models.CharField(max_length=255, unique=True)
    rating = models.SmallIntegerField(default=0)
    title = models.CharField(max_length=255, default="")
    authors = models.CharField(max_length=255, default="")
    summary = models.TextField(default="")
    is_read = models.BooleanField(default=False)
    published_date = models.DateTimeField("date published", blank=True, null=True)
    updated_date = models.DateTimeField("date updated", blank=True, null=True)

    class Meta:
        app_label = 'research'
