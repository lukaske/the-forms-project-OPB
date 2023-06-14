from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=100)
    form = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.form_name
    
class Submit(models.Model):
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
    submit_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)