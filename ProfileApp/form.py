from django import forms
from .models import *

#งาน11
class ProductForm(forms.Form):

    optionbrand = (("LEVI'S","LEVI'S"),("JASPAL", "JASPAL"), ("LACOSTE","LACOSTE"),("H&M", "H&M"),("ZARA","ZARA"),("A||Z","A||Z"))
    optionsize = (("xs","xs"),("s","s"),("m","m"),("l","l"),("xl","xl"))
    optiontype = (("Jacket","Jacket"),("Jeans","Jeans"),("t-shirt","t-shirt"),("long-sleeved shirt","long-sleeved shirt"),
                  ("shirt","shirt"))
    optionmember = (('y', 'y'),('n', "n"))
    id = forms.CharField()
    brand = forms.ChoiceField(widget=forms.Select, choices= optionbrand)
    type = forms.ChoiceField(widget=forms.Select, choices= optiontype)
    size = forms.ChoiceField(widget=forms.Select, choices= optionsize)
    price = forms.IntegerField(min_value=0)
    amount = forms.IntegerField(min_value=0)
    member = forms.ChoiceField(widget=forms.RadioSelect,choices=optionmember)


class ProductMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid','name','brand','price','net','category')
        widgets = {
            'pid':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control','required':'required',
                                          'max_length':35}),
            'brand':forms.TextInput (attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'net':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
             }
        labels = {
            'pid':'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี่ห้อ',
            'price': 'ราคาต่อหน่วย',
            'net':'คงเหลือ',
            'category': 'ประเภทสินค้า'

        }