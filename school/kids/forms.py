from django import forms

class StudentFrom(forms.Form):
	name=forms.CharField(label='name', max_length=100)
	standard=forms.CharField(label='standard', max_length=100)
	section=forms.CharField(label='section', max_length=100)
	status=forms.CharField(label='status', max_length=100)
	age=forms.CharField(label='age', max_length=100)
	rollnumber=forms.CharField(label='Roll Number', max_length=100)
	dateofbirth=forms.CharField(label='Date Of Birth', max_length=100)
	address = forms.CharField(label='Address', max_length=100)

