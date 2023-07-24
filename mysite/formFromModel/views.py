from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, AuthorForm, BookForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        # a = Author.objects.get(pk=2)
        f = AuthorForm(request.POST)
        if f.is_valid():
            # f.save()
            return HttpResponse("<h2>Save Successfully</h2>")
        else:
            return HttpResponse("<h2>Save Not Successfully</h2>")
    form = AuthorForm()
    return render(request, 'authors.html', {'form': form})