from django.shortcuts import render, redirect
from booking.models import register
from django.http import HttpResponse


# Create your views here.


def sign_up(request):
    Register = register.objects.all()
    print(Register)
    return render(request, 'booking/register.html')


def dashboard(request):
    return render(request, 'bookong/dashboard.html')


def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        nem_password = request.POST.get('nem_password')
        confirm_password = request.POST.get('confirm_password')
        if username and email and nem_password and confirm_password:
            register.objects.create(
                username=username,
                email=email,
                nem_password=nem_password,
                confirm_password=confirm_password
            )
            return redirect('dashboard')
        else:
            # Handle missing data, e.g., return to form with error
            return render(request, 'booking/register.html', {'error': 'All fields are required'})
    return redirect('register')  # Or handle GET requests appropriately


# def submit(request):
#     create_email = request.POST['email']
#     register.objects.create(username=create_email)


# def submit(request):
#     create_password = request.POST['password']
#     register.objects.create(username=create_password)
