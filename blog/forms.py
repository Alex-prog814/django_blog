from django import forms

from .models import Category, Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image', 'user')


    # title = forms.CharField(max_length=255, required=True, strip=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    # text = forms.CharField(required=True, widget=forms.Textarea)
    # image = forms.ImageField()


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image')
