from django.urls import path
from . import views

urlpatterns = [

path('',views.Post_list.as_view(), name = 'post_list'),
path('about',views.About.as_view(), name= 'about'),
path('post/<int:pk>',views.Post_detail.as_view(), name = 'post_detail'),
path('post/new',views.Create_post.as_view(), name='create_post'),
path('post/<int:pk>/edit',views.UpdatePost.as_view(), name= 'post_edit'),
path('post/<int:pk>/delete', views.DeletePost.as_view(), name= 'post_remove'),
path('post/drafts',views.post_drafts.as_view(), name = 'post_drafts_list'),
path('post/<int:pk>/comment',views.add_comment_to_post,name = 'add_comment_to_post'),
path('comment/<int:pk>/approve',views.comment_approve, name = 'comment_approve'),
path('comment/<int:pk>/remove',views.comment_remove, name='comment_remove'),
path('post/<int:pk>/publish',views.post_publish, name = 'post_publish'),
path('like/<int:pk>/',views.like, name='like'),

]