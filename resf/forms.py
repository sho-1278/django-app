from django.forms import ModelForm
from resf.models import *
from django import forms
from multiselectfield import MultiSelectField

class UserQueryForm(ModelForm):
	Name       = forms.CharField(label="Full Name", widget = forms.TextInput(attrs = { "placeholder":"Enter your Full name", "class": "form-control"})) 
	Class      = forms.CharField(label="Class(10th/11th/12th)", widget = forms.TextInput(attrs = { "placeholder":"Enter your Full Class", "class": "form-control"}))
	TargetExam = forms.CharField(label="Your Target Exam", widget = forms.TextInput(attrs = { "placeholder":"Enter your Target exam(JEE/Olympiads)", "class": "form-control"}))
	#Problem    = MultiSelectField(label="Full Name", widget = forms.Select(attrs = {"class": "form-control"}))
	Query      = forms.CharField(label="Queries", widget = forms.Textarea(attrs = { "placeholder":"Enter your Queries", "class": "form-control", 'rows': 3, 'cols': 100 }))
	Mail      = forms.CharField(label="Email Id", widget = forms.EmailInput(attrs = { "placeholder":"Enter your Mail(for reply)", "class": "form-control"}))
	class Meta:
		model = UserQuery 
		fields = [
		'Name', 
		'Class',
		'TargetExam',
		'Problem',
		'Query',
		'Mail']

	# widgets = {
	# 'Name'      : forms.TextInput(attrs={'class': 'form-control'}),
	# # 'Class'     : forms.TextInput(attrs={'class': 'form-control'}),
	# # 'TargetExam': forms.TextInput(attrs={'class': 'form-control'}),
	# # 'Problem'   : forms.TextInput(attrs={'class': 'form-control'}),
	# # 'Query'     : forms.TextInput(attrs={'class': 'form-control'})
	# }