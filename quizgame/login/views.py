from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Questions, Answers, User
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
# Create your views here.

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
        # return redirect('listing')
    else:
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username = uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')
    

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password = pwd)
        if check_user:
            request.session['user'] = uname
            return redirect ('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')
    
    return render (request, 'login.html')

def logout(request):
    try :
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')



def listing(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        try:
            question_list = caches['question_list']
            print(f'getdataformcache{question_list}')
        except InvalidCacheBackendError :
            question_list = Questions.objects.filter(id<=quantity)
            caches['question_list'] = question_list
            print(f"getdatabase{question_list}")

        paginator = Paginator(question_list,5)

        pageNumber = request.GET.get('page')
        try:
            questions = paginator.page(pageNumber)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)

        return render(request, 'pagination_1.html', {'questions': questions})
    else:
        return redirect('home')