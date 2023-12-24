from django import forms  


class Productform(forms.Form):  
    name = forms.CharField(max_length=250, blank=True, null=True)
    photo = forms.ImageField(upload_to='images/')
    price = forms.IntegerField()

    status = forms.CharField(max_length=8, choices=(
        ('active', 'active'),
        ('noactive', 'no active')
    ), default='noactive')
