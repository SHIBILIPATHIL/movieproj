from django.shortcuts import render, redirect

# Create your views here.
from movieapp.form import MovieForm
from movieapp.models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        desc1 = request.POST.get('desc')
        year1 = request.POST.get('year')
        img1 = request.FILES['img']
        movie = Movie(name=name1, desc=desc1, year=year1, img=img1)
        movie.save()
    return render(request, 'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form= MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
