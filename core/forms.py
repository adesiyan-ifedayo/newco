from django import forms
from django.contrib.auth.models import User
from .models import Profile, Journal, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class JournalForm(forms.Form):
    slug = forms.SlugField()
    image = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea)



class JournalModelForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = [ 'image', 'slug', 'content']







class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
#    image = forms.ImageField()
    country = forms.CharField(max_length = 30)
    


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1', 'password2', )
    
    def save(self, commit=True):
    	user = super(SignUpForm, self).save(commit=False)
    	user.first_name = self.cleaned_data['first_name']
    	user.last_name = self.cleaned_data['last_name']
    	user.email = self.cleaned_data['email']
    	
    	if commit:
    		user.save()
    	return user




class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'about_me', 'location', 'passion', 'plan']


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='',widget=forms.Textarea)


