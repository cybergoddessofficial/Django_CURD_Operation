from django.contrib import messages
from django.shortcuts import render, redirect


from myapp.models import Student, Admin, Category
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    return render(request,"index.html")

def addstudent(request):
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Gender = request.POST.get("gender")
        Image = request.FILES["pic"]
        City = request.POST.get("city")
        Address = request.POST.get("address")
        obj=Student(Name=Name,Email=Email,Gender=Gender,Image=Image,City=City,Address=Address)
        obj.save()
        return redirect(displaystudent)
    return render(request,"addstudent.html")

def displaystudent(request):
    data=Student.objects.all()
    return render(request,"displaystudent.html",{'data':data})

def editstudent(request,dataid):
    data = Student.objects.get(id=dataid)
    print(data)
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Gender = request.POST.get("gender")

        City = request.POST.get("city")
        Address = request.POST.get("address")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Student.objects.get(id=dataid).Image
        Student.objects.filter(id=dataid).update(Name=Name,Email=Email,Gender=Gender,Image=file,City=City,Address=Address)
        return redirect(displaystudent)
    return render(request,"editstudent.html",{'data':data})

def deletestudent(request,dataid):
    data = Student.objects.get(id=dataid)
    data.delete()
    return redirect(displaystudent)

def addadmin(request):
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Mobile = request.POST.get("mob")
        Image = request.FILES["pic"]
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        CPassword = request.POST.get("cpassword")
        if Password==CPassword:
            obj = Admin(Name=Name, Email=Email, Mobile=Mobile, Image=Image, Username=Username, Password=Password,CPassword=CPassword)
            obj.save()
            return redirect(addadmin)
        else:
            messages.warning(request, 'Your password is mismatched.')



    return render(request,"addadmin.html")

def displayadmin(request):
    data=Admin.objects.all()
    return render(request,"displayadmin.html",{'data':data})

def editadmin(request,dataid):
    data = Admin.objects.get(id=dataid)
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Mobile = request.POST.get("mob")
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        CPassword = request.POST.get("cpassword")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Admin.objects.get(id=dataid).Image
        if Password == CPassword:
            Admin.objects.filter(id=dataid).update(Name=Name, Email=Email, Mobile=Mobile, Image=file, Username=Username, Password=Password,
                        CPassword=CPassword)
            return redirect(displayadmin)
        else:
            messages.warning(request, 'Your password is mismatched.')
    return render(request,"editadmin.html",{'data':data})

def deleteadmin(request,dataid):
    data = Admin.objects.get(id=dataid)
    data.delete()
    return redirect(displayadmin)

def addcategory(request):
    if request.method=="POST":
        CName=request.POST.get("cname")
        CDesc=request.POST.get("cdesc")
        CImage=request.FILES["pic"]
        obj=Category(CName=CName,CDesc=CDesc,CImage=CImage)
        obj.save()
        return redirect(displaycategory)
    return render(request,"addcategory.html")

def displaycategory(request):
    data=Category.objects.all()
    return render(request,"displaycategory.html",{'data':data})

def editcategory(request,dataid):
    data = Category.objects.get(id=dataid)
    if request.method=="POST":
        CName = request.POST.get("cname")
        CDesc = request.POST.get("cdesc")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Category.objects.get(id=dataid).CImage
        Category.objects.filter(id=dataid).update(CName=CName,CDesc=CDesc,CImage=file)
        return redirect(displaycategory)
    return render(request,"editcategory.html",{'data':data})

def deletecategory(request,dataid):
    data = Category.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)













