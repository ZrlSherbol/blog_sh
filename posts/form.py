from django import forms


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    rate = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title == "puthon":
            raise forms.ValidationError("title is required")
        return cleaned_data

        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("title is required")
        return cleaned_data
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'puthon' in title.lower():
            raise forms.ValidationError("title is required")
        return title
