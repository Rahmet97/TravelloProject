from django.shortcuts import render
from .models import Destination

def index(request):

    dest1 = Destination()
    dest1.name = 'Bali'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Indonesia'
    dest2.desc = 'The best Country on the World'
    dest2.price = 650
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = 'The more beautifull City'
    dest3.price = 750
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})