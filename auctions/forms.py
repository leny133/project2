from django import forms

class NewItemForm(forms.Form):
    title = forms.CharField(label='Item Name', max_length=100)
    description = forms.CharField(label='Item Description', max_length=250)
    category = forms.CharField(label='Your name', max_length=100)
    imgUrl = forms.URLInput()