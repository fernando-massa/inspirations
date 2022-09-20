from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Gallery
#from .forms import FeedingForm
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import the login_required decorator for functions
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

import os
import boto3
import uuid


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# def home(request):
#     return render(request, "home.html")

def gallery_index(request):
    # select * from table_name
    #cats = Cat.objects.all()  # this will return a list of cats
    
    #SELECT, name, age .... FROM cats WHERE user_id = id
    # cats = Cat.objects.filter(user=request.user)
    # #request.user comes from signup function: 
    # # user = form.save()
    # # login(request, user) 
    
    #return render(request, 'cats/index.html', {'cats': cats})
    #return HttpResponse('<h1>gallery test</h1>')
    return render(request, 'galleries/index.html')
  
  
def inspiration_index(request):
    return HttpResponse('<h1>inspirations test</h1>')



def add_photo(request, inspiration_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to inspiration_id or inspiration (if you have a inspiration object)
            Photo.objects.create(url=url, inspiration_id=inspiration_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', inspiration_id=inspiration_id)


def some_function(request):
    secret_key = os.environ['SECRET_KEY']
    
    
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
      
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm() # this is our html form
  context = {'form': form, 
             'error_message': error_message
            }
  return render(request, 'registration/signup.html', context)

