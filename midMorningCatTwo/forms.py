from django import forms


class EmployeeRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class EmployeeHrForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()
    age = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
