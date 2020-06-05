from django.shortcuts import render
from .models import Destination, Message
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

destCount = Destination.objects.all().count
tesCount = Message.objects.all().count

def index(request):

    dests = Destination.objects.all()
    paginator = Paginator(dests, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    return render(request, "index.html", {'queryset': paginated_queryset, 'page_request_var': page_request_var, 'destcount': destCount, 'tescount': tesCount})


def search(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        rating = request.POST.get('rating')
        budget = request.POST.get('budget')
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