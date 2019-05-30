
from django import forms
from blog.models import Comment


class PostComment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body', ]
