from django import forms

class ProductCreateForms(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()

class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Напишите отзыв")