from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	# author-models.ForeignKey('user.User')
	author = models.CharField(default='author', max_length=60)
	slug = models.CharField(default='author', max_length=60)

	# def approve_comments(self):
	#         return self.comments.filer(approved_comment=True)
	# from django.core.urlresolvers import reverse
	#
	# def get_absolute_url(self):
	#        return reverse("post_detail",kwargs={'pk':self.pk})

	def __unicode__(self):
		return self.title

	def __str__(self):  # this needed for display in foreign fields like comment
		return self.title


class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	# author=models.CharField(default='author',max_length=60)
	author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
	body = models.TextField()
	# post=models.ForeignKey(Post)
	# post=models.ForeignKey(Post, related_name='comments')
	post = models.ForeignKey('blog.post', related_name='comments', on_delete=models.DO_NOTHING)
	approved_comment = models.BooleanField(default=False)

	# def approve(self):
	#         self.approved_comment=True
	#         self.save()
	# def get_absolute_url(self):
	#        return reverse('postcomment',kwargs={'pk':self.pk})
	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))
