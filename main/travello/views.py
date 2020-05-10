from django.shortcuts import render
from .models import Destination, Message
from django.db.models import Q

def index(request):

    dests = Destination.objects.all()[:3]
    count = Destination.objects.all().count

    return render(request, "index.html", {'dests': dests, 'count': count})


def search(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        rating = request.POST.get('rating', 1)
        budget = request.POST.get('budget', 0)
        
        dests = Destination.objects.filter(Q(name=city) | Q(rating=rating) | Q(price=budget))

        return render(request, "search.html", {'dests': dests})

def about(request):
    return render(request, "about.html")

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Message.objects.create(name=name, email=email, subject=subject, message=message)

    return render(request, "contact.html")

def destinations(request):

    dests = Destination.objects.all()

    return render(request, "destinations.html", {'dests' : dests})