from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "vinyl_lovers/list_albums.html", {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='album-entries')
    return render(request, 'vinyl_lovers/add_album.html', {"form": form})
