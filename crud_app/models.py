from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,validators=[MinLengthValidator(5)])
    age=models.PositiveIntegerField()
    email=models.EmailField()
    message=models.TextField()
    is_delete=models.BooleanField(default=False)
    profile=models.ImageField(upload_to="images/",null=True)
    profile_video=models.FileField(upload_to="videos/",null=True)
