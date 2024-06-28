from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from playground.models import Contact

# Create your views here.
# request -> rsponse
# request handler
# action

def home(request):
    try:
        template = get_template('playground/base.html')
    except Exception as e:
        print(e)  # This will print the error to the console
    return render(request, 'playground/base.html')

def about(request):
    return render(request, 'playground/about.html')

def services(request):
    return render(request, 'playground/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        query = request.POST.get("query")
        contact = Contact(name=name, email=email, phone=phone, city=city, query=query)
        contact.save()

    return render(request, 'playground/contact.html')