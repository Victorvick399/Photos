from django.shortcuts import render
from .models import Photos,Category,Location

# Create your views here.
def home_page(request):
    all_pics = Photos.objects.all()
    return render(request, 'home.html' ,{"photos":all_pics})

def about_page(request):
    return render(request, 'test.html')

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})