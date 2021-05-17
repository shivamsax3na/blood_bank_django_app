from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.


# def home(request):
#     return render(request, 'index.html')

class HomeListView(ListView):
	model = Post
	template_name = 'index.html'
	# ordering = ['-id'] 
	ordering = ['-postDate']


class DonerDetailView(DetailView):
	model = Post
	template_name = 'donerDetail.html'


class DonerRequest(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'donateReq.html'
	# fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'updatePost.html'
	# fields = ['title', 'bloodgroup', 'situation'] 

class DeletePostView(DeleteView):
	model = Post
	template_name = 'deletePost.html'
	success_url = reverse_lazy('home')

