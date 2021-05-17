from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'bloodgroup', 'doner', 'situation')

		widgets = {
			'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
			'doner' : forms.Select(attrs={'class' : 'form-control'}),
			'bloodgroup' : forms.Select(attrs={'class' : 'form-control'}),
			'situation' : forms.Textarea(attrs={'class' : 'form-control'}),
			
			}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'bloodgroup', 'situation')

		widgets = {
			'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
			'doner' : forms.Select(attrs={'class' : 'form-control', 'value' : 'user.firstname'}),
			'bloodgroup' : forms.Select(attrs={'class' : 'form-control'}),
			'situation' : forms.Textarea(attrs={'class' : 'form-control'}),
			
			}			