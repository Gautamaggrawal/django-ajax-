from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	age=models.IntegerField()
	college_name=models.CharField(max_length=50)
	summary = models.CharField(max_length=200)
	def __str__(self):
		return self.summary