from  django.forms import *
class ProductForm(forms.Form):
    id = forms.CharField(max_length=13, label='รหัสสินค้า',
                         required=True, widget=forms.TextInput(attrs={'size':'15'}))
    name = forms.CharField(max_length=50, label='ชื่อสินค้า',
                         required=True, widget=forms.TextInput(attrs={'size': '55'}))
    brand = forms.CharField(max_length=30, label='ยี่ห้อ',
                         required=True, widget=forms.TextInput(attrs={'size': '35'}))
    price = forms.FloatField(min_value=1.00,  max_value=5000.00, label='ราคาต่อหน่วย',
                           required=True, widget=forms.NumberInput(attrs={'size': '10'}))
    net = forms.IntegerField(min_value=0, max_value=1000, label='คงเหลือ',
                            required=True, widget=forms.NumberInput(attrs={'size': '10'}))

