from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post
from django.shortcuts import get_object_or_404, redirect
from blog.forms import PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from signup.models import Profile


class PostListView(ListView):
	model = Post
	paginate_by = 3
	queryset = Post.objects.order_by('-created')
	# if you don't want queryset you ca add the following to model.
	# and it only works on date field
	# nested: class Meta:
	#                ordering = ['-created']


class PostDetailView(DetailView):
	model = Post


@login_required()
def PostCommentView(request, pk):
	user = User.objects.get(pk=pk)
	myedit = Profile.objects.get(user=user)
	# print myedit.editor
	# print myedit.user_id
	# print user.last_name
	# print user.approved_comment
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostComment(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = user
			comment.save()
			return redirect('/thanks/')
			# return redirect('asdf.html',pk=post.pk)
	else:
		form = PostComment()
	return render(request, 'postcomment.html', {'form': form})

# def comment_approve(request,pk):
#    comment = get_object_or_404(Comment,pk=pk)
#    #comment.approve()
#    return redirect('post_detail', pk=post.pk)

