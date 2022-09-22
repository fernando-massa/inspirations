import os
import boto3
import uuid

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .forms import NoteForm, AddGalleriesForm
from django.shortcuts import render, redirect
from .models import Gallery, Inspiration, Note, Photo
#from .forms import FeedingForm
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import the login_required decorator for functions
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin




# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def home(request):
    return render(request, "home.html")

# -----------------Notes---------------------------------------------------
def add_note(request, inspiration_id):
    # print(request.POST['date'])
    # print(request.POST['meal'])
    # print(request.POST['csrfmiddlewaretoken'])
    form = NoteForm(request.POST)
    if form.is_valid():
        # commit=False because we need to assign a cat id
        new_note = form.save(commit=False)
        new_note.inspiration_id = inspiration_id
        print(new_note)
        new_note.save()
    return redirect('detail', inspiration_id=inspiration_id)

# -----------------Inspiration----------------------------------------------

# show all the inspirations in the index page
# http://localhost:8000/inspirations
def inspiration_index(request):
    inspirations = Inspiration.objects.filter(user=request.user)
    return render(request, 'inspirations/index.html', {'inspirations': inspirations})


# to see the inspiration detail
# http://localhost:8000/inspirations/1/
def inspirations_detail(request, inspiration_id):
    inspiration = Inspiration.objects.get(id=inspiration_id)
    note_form = NoteForm()
    return render(
        request,
        'inspirations/detail.html',
        {'inspiration': inspiration, 'note_form': note_form}
    )



# create inspiration
# http://localhost:8000/inspirations/create/
class InspirationCreate(CreateView): # to add LoginRequiredMixin later
    model = Inspiration

    def post(self,request,*args,**kwargs):
        print(":postmethod")
        form = AddGalleriesForm(request.POST)
        print(request.POST["galleries"])
        if form.is_valid():
            print(form)
            form.instance.user=self.request.user
            form.save()
        return HttpResponse("working")
    # fields = '__all__'
    # form_class = AddGalleriesForm
    fields = ['name', 'description', 'link', 'galleries']
        # fields should contain gallery later, in html we need to have if else "create gallery first, before creating inspiration"

    def form_valid(self, form):
        # self.request.user means current logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # self.object.id = 9
        # http://127.0.0.1:8000/inspirations/9
        # path('inspirations/<int:gallery_id>/', views.inspirations_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))


# # create inspiration
# # http://localhost:8000/inspirations/create/
# class InspirationCreate(CreateView): # to add LoginRequiredMixin later
#     model = Inspiration
#     # fields = '__all__'
#     fields = ['name', 'description', 'link', 'photo_file']
#         # fields should contain gallery later, in html we need to have if else "create gallery first, before creating inspiration"

#     def form_valid(self, form):
#         photo_file = self.request.FILES.get('photo_file', None)

#         if photo_file:
#             s3 = boto3.client('s3')
#             # need a unique "key" for S3 / needs image file extension too
#             key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#             # just in case something goes wrong
#             try:
#                 bucket = os.environ['S3_BUCKET']
#                 s3.upload_fileobj(photo_file, bucket, key)
#                 # build the full url string
#                 url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#                 # we can assign to inspiration_id or inspiration (if you have a inspiration object)
#             except:
#                 print('An error occurred uploading file to S3')

#         form.instance.user = self.request.user
#         form.instance.photo_file = url

#         return super().form_valid(form) 




# update inspiration 
# http://localhost:8000/inspirations/create/
class InspirationUpdate(UpdateView): # to add LoginRequiredMixin later
    model = Inspiration
    # fields = '__all__'
    fields = ['description', 'description', 'link']

    def get_success_url(self, **kwargs):
        # self.object.id = 9
        # http://127.0.0.1:8000/inspirations/9
        # path('inspirations/<int:gallery_id>/', views.inspirations_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))


class InspirationDelete(DeleteView): # to add LoginRequiredMixin later
    model = Inspiration
    success_url = '/inspirations/'

# # create inspiration's photo
# # http://localhost:8000/inspirations/create/
# class InspirationPhotoCreate(CreateView): # to add LoginRequiredMixin later
#     model = Inspiration
#     fields = "__all__"



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


# -----------------Gallery---------------------------------------------------

# http://localhost:8000/galleries/
class GalleryList(ListView):
    model = Gallery

# http://localhost:8000/galleries/1/
class GalleryDetail(DetailView):
    model = Gallery


# http://localhost:8000/galleries/create/
class GalleryCreate(CreateView):
    model = Gallery
    fields = '__all__'


# http://localhost:8000/galleries/1/update/
class GalleryUpdate(UpdateView):
    model = Gallery
    fields = fields = '__all__'


# http://localhost:8000/galleries/1/delete/
class GalleryDelete(DeleteView):
    model = Gallery
    success_url = '/galleries/'


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
      return redirect('/galleries/')
    else:
      error_message = 'Invalid sign up - try again'
      
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm() # this is our html form
  context = {'form': form, 
             'error_message': error_message
            }
  return render(request, 'registration/signup.html', context)

