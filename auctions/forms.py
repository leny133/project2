from django import forms

class NewItemForm(forms.Form):
    title = forms.CharField(label='Item Name', max_length=100, required=True)
    description = forms.CharField(label='Item Description', max_length=250, required=True)
    CATEGORY_CHOICES=[
        ('nocat',''),
        ('home','Home'),
        ('electronics','Electronics')
    ]
    category = forms.CharField(label="Category ",widget= forms.Select(choices=CATEGORY_CHOICES))
    imgUrl = forms.CharField(label='Image URL', max_length=100, required=False)
    price = forms.DecimalField(decimal_places=2, max_digits=8, label="Initial Price", required=True)
