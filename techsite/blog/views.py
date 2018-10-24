from django.shortcuts import render ,  get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm , CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ( TemplateView,
															ListView,
															CreateView,
															DetailView,
															UpdateView,
															DeleteView,
															
															)
															


# Create your views here.
class About(TemplateView):
	template_name = 'blog/about.html'
	
class Post_list(ListView):
	model = 	Post
	template_name = 'blog/post_list.html'
	def get_queryset(self):
		return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
	
	
class Post_detail(DetailView):
	template_name = 'blog/post_detail.html'
	model = Post
	
	
	
class Create_post(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post


	def form_valid(self,form):
		post = form.save(commit=False)
		author = self.request.user
		post.author = author
		post.save()
		return redirect('post_detail',pk=post.pk)	
	
	
	
class DeletePost(LoginRequiredMixin,DeleteView):
	template_name="blog/post_confirm_delete.html"
	model = Post
	success_url = reverse_lazy('post_list')	
	
	
class UpdatePost(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	form_class = PostForm
	model = Post
	redirect_field_name = 'blog/post_detail.html'
	
	
class post_drafts(LoginRequiredMixin, ListView):
	template_name='blog/post_drafts_list.html'
	login_url = '/login/'
	redirect_field_name = 'blog/post_list.html'
	model =Post
	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('-create_date')
	

		

def add_comment_to_post(request,pk):
	login_url= '/login/'
	post = get_object_or_404(Post,pk=pk)
	if request.method== 'POST':
		form = CommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit = False)
			comment.post = post 
			comment.save()
			return redirect('post_detail',pk = post.pk)
	else:
		form = CommentForm()	
		return render(request,'blog/comment_form.html',{'form':form})	
	
	
@login_required	
def comment_approve(request,pk):
	comment  = get_object_or_404(Comment,pk=pk)
	comment.approve()
	return redirect( 'post_detail',pk = comment.post.pk)	
	
	
@login_required
def comment_remove(request,pk):
	comment = get_object_or_404(Comment,pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail',post_pk)	
	
@login_required
def post_publish(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.publish()
	return redirect('post_detail',pk=pk)	
	
def like(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.like()	
	return redirect('post_list')
	
	
	  	