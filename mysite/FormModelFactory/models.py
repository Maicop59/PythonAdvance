from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, modelform_factory

# Create your models here.
TITLE_CHOICE = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms')
)
class Author(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=3, choices=TITLE_CHOICE)
    birth_date = models.DateField()

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         widgets ={'birth_date': forms.DateInput(format=('%m/%d/%y'), \
#                                                 attrs={'class':'form-control', 'placeholder':'select a date', 'type': 'date'}
#                                                 ),
#                     'name' : Textarea(attrs={'cols': 80, 'rows': 20})
#                   }
#         label = {'name' : ('Writer')
#         }
        
# class BookForm(ModelForm):
#     class Meta :
#         model = Book
#         fields = ('name', 'author')

BookForm = modelform_factory(Book, fields=("name", "author"))
AuthorForm = modelform_factory(Author, fields=("name", "title","birth_date"))

