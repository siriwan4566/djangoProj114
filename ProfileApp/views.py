from django.shortcuts import render,HttpResponse,redirect
import datetime
from django.contrib import messages
from  ProfileApp.form import *

# Create your views here.

def tests(request):
    return HttpResponse("<H1>Hello Word <br> This is My Word Wide Web </H1>")

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request, 'profile.html')

def education(request):
    return render(request,'education.html')

def interests(request):
    return render(request,'interests.html')

def dreamJob(request):
    return render(request,'dreamJob.html')

def idol(request):
    return render(request,'idol.html')

def hny (request):
    return render(request,'hny.html')

def product(request):
    ID = '65342310114-0'
    Name = "ศิริวรรณ แสงอุ่นอุรัย"
    Address = '303 อ.บ้านไผ่ จ.ขอนแก่น'
    Domicile = 'จังหวัดขอนแก่น'
    Gender = "หญิง"
    Weight = "54 กิโลกรัม"
    Height = "166 เซนติเมตร"
    FavoriteColor = 'สีชมพู'
    FavoriteFood = 'ก๋วยเตี๋ยว'
    Status = "นักศึกษา"
    products = [
      ['Bright Body Cologne Spray ', '175.00','images/spraybody.jpg'],
      ['Perfume 9ml', "195.00",'images/perfume.jpg'],
      ['Perfume 50ml', "895.00", 'images/perfume15.jpg'],
      ['Body Lotion',"145.00",'images/lotion.jpg'],
      ['Brightening Serum Vitamin C','250.00','images/c.jpg'],
      [' Nature Summer Soft Linen Mist ','195.00','images/cc.jpg'],
      ['Care Pure ผลิตภัณฑ์ดูแลใต้วงแขน','305.00','images/juk.jpg']  ,
      ['ครีมบำรุงผิวหน้า แก้ปัญหาฝ้ากระ','275.00','images/pech.jpg'],
      ['Nature Sunscreen','395.00','images/sun.jpg'],
      ['สเปรย์ระงับกลิ่นกาย สำหรับผู้ชาย','245.00','images/men.jpg']  ,
      ['โฟมล้างหน้าเนื้อโคลนสำหรับผู้ชาย ','250.00','images/mens.jpg']



    ]
    return render(request,'product.html',{ 'ID':ID,'Name':Name,'Address':Address,
      'Domicile':Domicile,'Gender':Gender,'Weight':Weight,'Height':Height,
      'Coler':FavoriteColor,'Food':FavoriteFood,'Status':Status,'products': products})


from .models import *
def retrieveAllProduct(request):
    products = Product.objects.all() #อ่ํานข้อมูลทุกเรคอร์ด All ในฐํานข้อมูลที่เชื่อมโดย Category
    context ={'products':products}
    return render(request, 'Product/retivevAllProduct.html',context)

def retivevOneProduct(request, pid):
    product = Product.objects.get(pid=pid) #อ่ํานข้อมูลทุกเรคอร์ด One ในฐํานข้อมูลที่เชื่อมโดย Category
    context ={'product':product}
    return render(request, 'Product/retivevOneProduct.html',context)

def createProduct(request):
    if request.method == 'POST':
        form = ProductMForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทุกสินค้าใหม่เรียบร้อย.........')
            return redirect('retrieveAllProduct')
        else:
            product = Product.objects.get(pid=request.POST['pid'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = ProductMForm()
    context = {'form':form}
    return render(request,'product/createProduct.html',context)



lstOurProduct = []
def listProduct(request):
    details = "CLOTHES"
    name = "MISS.SIRIWAN SAENGAUNURAI"
    date = datetime.datetime.now()
    return render(request, 'listProduct.html', {'lstProduct': lstOurProduct,
                                              'details': details, 'name': name,
                                              'date': date.strftime("%A %d-%m-%Y ")},)
def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['id']
            brand = form.cleaned_data['brand']
            ptype = form.cleaned_data['type']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            member = form.cleaned_data['member']

            productnew = product11(pid, brand, ptype, size, price, amount,member,)
            lstOurProduct.append(productnew)
            return redirect('listProduct')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'inputProduct.html', context)


# productList = []
# def showProduct(request):
#         products = Product('P001','Shampoo','Dove',49.00,100)
#         productList.append(products)
#         products = Product('P002', 'Lotion', 'vee', 89.00, 100)
#         productList.append(products)
#         products = Product('P00', 'Soft Drink ', 'Fanta', 25.00, 100)
#         productList.append(products)
#         context = {'products':productList}
#         return render(request,'showProduct.html',context)

# def newProduct(request):
#     if request.method =='POST': #submit ข้อมูลจากฟอร์มมา
#         id = request.POST['id']
#         name = request.POST['name']
#         brand = request.POST['brand']
#         price= request.POST['price']
#         net = request.POST['net']
#         product =Product(id,name,brand,price,net)
#         productList.append(product)
#         return redirect('showProduct')
#     else:
#         return render(request,'fromProductNormal.html')
#
#
# def frmProduct(request):
#     if request.method == 'POST':
#         return  redirect('showProduct')
#     else:
#         form = ProductForm()
#         context = {'form':form }
#         return render(request,'Products.html')