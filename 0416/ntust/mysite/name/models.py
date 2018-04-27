from django.db import models


# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=20)
	gender = models.CharField(max_length=5)
	birthday=models.DateTimeField()
	phone_number=models.CharField(max_length=10)

	def __str__(self):
		return self.name

# Create your models here.
