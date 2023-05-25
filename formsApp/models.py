from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HTML_storing_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=100)
    form_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)