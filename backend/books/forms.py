from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(label='책 제목', max_length=100)

    def clean_title(self):
        title = self.cleaned_data['title']
        return title.strip()