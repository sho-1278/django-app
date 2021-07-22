from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class UserQuery(models.Model):
	"""docstring for UserQueryForm"""
	The_choices = (
		(1,'Anxiety'),
		(2,'Fear of performance'),
		(3,'Exam pressure'),
		(4,'low self-confidence'),
		(5,'stress'),
		(6,'None'))
	Name            = models.CharField(max_length=50)
	Class           = models.CharField(max_length=10)
	TargetExam      = models.CharField(max_length=50)
	Problem         = MultiSelectField(choices=The_choices)
	Query           = models.CharField(max_length=5000)
	Mail            = models.EmailField(max_length=200)
	date            = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.Mail
		