from django.shortcuts import redirect, render, get_object_or_404
from .models import Hobby
from .models import Place
#from .models import Music
from .models import Photo
from .models import Post
from .models import Visit
from django.utils import timezone

def main(request):
    return render(request,"main.html")

def who(request):
    return render(request,"who.html")

def hobby(request):
    hobbys = Hobby.objects.all()
    return render(request,"hobby.html", {'hobbys':hobbys})

def place(request):
    places = Place.objects.all()
    return render(request,"place.html", {'places':places})

def music(request):
    posts = Post.objects.all()
    return render(request,"music.html", {'posts':posts})

def photo(request):
    photos = Photo.objects.all()
    return render(request,"photo.html",{'photos':photos})

def visit(request):
    visits = Visit.objects.all()
    return render(request,"visit.html",{'visits':visits})

def visit_detail(request, id):
    visit = get_object_or_404(Visit, pk=id)
    return render(request, 'visit_detail.html', {'visit':visit})

def new(request):
    return render(request,"visit_new.html")

def create(request):
    new_visit = Visit()
    new_visit.title = request.POST['title']
    new_visit.write_date = timezone.now()
    new_visit.body = request.POST['body']
    new_visit.save()
    return redirect(visit_detail, new_visit.id)

def edit(request, id):
    edit_visit = Visit.objects.get(id=id)
    return render(request, 'visit_edit.html', {'visit':edit_visit})

def update(request, id):
    update_visit = Visit.objects.get(id=id)
    update_visit.title = request.POST['title']
    update_visit.body = request.POST['body']
    update_visit.write_date = timezone.now()
    update_visit.save()
    return redirect('visit_detail', update_visit.id)

def delete(request, id):
    delete_visit = Visit.objects.get(id=id)
    delete_visit.delete()
    return redirect('visit')