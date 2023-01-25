from django.shortcuts import render,redirect
from .models import Bio
from .forms import Bio_form,Edu_form,Exp_form
# Create your views here.

def home_view(request):
    return render(request,"Home.html")
"""
def read_view(request):
    bio = Bio.objects.get(id=1)

    cotext = {
        'name' : bio.Nama,
        'alamat' : bio.Alamat,

    }
    return render(request,"Read.html",context)
"""




def create_view(request):
    bio_form = Bio_form()
    if request.method == 'POST':
        bio_data = Bio_form(request.POST)
        print(bio_data)
        if bio_data.is_valid():
            bio_data.save()

        else:
            bio_data = Bio_form()

    myform = {
        'bio' : bio_form

    }
    return render(request, "Create.html",myform)

def extra_create(request):
    num1 = int(request.POST.get('loop1',None)) #none can be use if it dont get any feedback after request the data
    num2 = int(request.POST.get('loop2',None))
#    nama = request.POST.get('Nama')
#    print(nama)
    
    dummy1 = []
    dummy2 = []

    for a in range(num1):
        dummy1.append(a)
    
    for a in range(num2):
        dummy2.append(a)

    edu_form = Edu_form()
    if request.method == "POST":
        edu_form = Edu_form(request.POST)
        if edu_form.is_valid():
            Edu_form.save()
            Edu_form.object.create(request.POST)
        else:
            edu_form = Edu_form()

    exp_form = Exp_form()
    if request.method == "POST":
        exp_form = Exp_form(request.POST)
        if exp_form.is_valid():
            Exp_form.save()
            Exp_form.object.create(request.POST)
        else:
            exp_form = Exp_form()

    context = {
        'num1' : dummy1,
        'num2' : dummy2,
        'edu' : edu_form,
        'exp' : exp_form
    }
    return render(request,"ExtraCreate.html",context)

"""
def pos_delete_view(request):
    obj = request.POST.get('target',None)
    obj.delete()
    return redirect('home.html')

def delete_view(redirect):
    return render(request,"Delete.html",{})

def update_view(redirect):
    return render(request, "Update.html,{})