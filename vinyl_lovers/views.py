from django.shortcuts import render
from .models import Album

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "vinyl_lovers/list_albums.html", {"albums": albums})
