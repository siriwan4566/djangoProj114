from django.shortcuts import render,HttpResponse

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

def product (request):
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
      ['Perfume 15ml', "895.00", 'images/perfume15.jpg'],
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
      'Coler':FavoriteColor,'Food':FavoriteFood,'Status':Status,'products': products} )

# def showMydata(request):
#     Brand ='oriental princess shop'
#
#     context =
#     return render(request, 'product.html', context)
#



# def myData (request):
#     name = "Siriwan"
#     surname = "Saengaunurai"
#     gender = "G"
#     status = "student"
#     work = "RMUTI.Khonkean"
#     education = "dgree"
#     return render(request,'myData.html',
#     {'name':name, 'surname':surname,'gender':gender,
#      'status':status,'work':work, 'education':education} )
#
#

