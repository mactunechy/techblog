from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.



class Post(models.Model):
	author  =models.ForeignKey('auth.User', on_delete=models.PROTECT)
	title	  =models.CharField(max_length=200)
	text 	=models.TextField()
	category= models.CharField(max_length=100,default="None",blank=True)
	create_date	 = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	likes = models.IntegerField(default = 0,blank=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def approved_comments(self):
		return self.comments.filter(approve_comment=True)
		
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk':self.pk})
		
	def like(self):
		self.likes += 1
		self.save()
		
		
		
		
		
class Comment	(models.Model):
	post = models.ForeignKey('blog.Post',related_name = 'comments', on_delete=models.PROTECT)		
	author= models.CharField(max_length=200)
	text= models.TextField()
	create_date= models.DateTimeField(default=timezone.now)
	approve_comment = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title
	def approve(self):
		self.approve_comment = True
		self.save()	
		
	def get_absolute_url(self):
		return reverse('post_list')
			