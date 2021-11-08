from django.shortcuts import get_object_or_404, render, redirect
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


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to="album-entries")
    return render(
        request,
        'vinyl_lovers/edit_album.html',
        {"form": form, "album": album}
    )


def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'vinyl_lovers/view_album.html', {"album": album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='album-entries')
    return render(request, 'vinyl_lovers/delete_album.html', {"album": album})
