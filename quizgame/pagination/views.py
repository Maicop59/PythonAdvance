from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Questions, Answers
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
# from django.core import cache

# Create your views here.
@cache_page(60*15)
def listing(request):
    try:
        question_list = caches['question_list']
        print(f'getdataformcache{question_list}')
    except InvalidCacheBackendError :
        question_list = Questions.objects.all()
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
