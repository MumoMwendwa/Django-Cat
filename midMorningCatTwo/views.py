from django.shortcuts import render
from .forms import EmployeeRegistrationForm
from .forms import EmployeeHrForm


def employee_register(request):
    submit_button = request.POST.get('btn-reg')
    name = ''
    email = ''
    password = ''
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

    context = {'form': form, 'submit_button': submit_button, 'name': name, 'email': email, 'password': password}

    return render(request, 'register.html', context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def client(request):
    return render(request, 'client.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def employee_hr(request):
    submit_button = request.POST.get('btn-reg')
    name = ''
    email = ''
    password = ''
    age = ''
    gender = ''
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        age = form.cleaned_data.get('age')
        gender = form.cleaned_data.get('gender')
    context = {'form': form, 'submit_button': submit_button, 'name': name, 'email': email, 'password': password, 'age': age, 'gender': gender,}

    return render(request, 'employee hr.html', context)
