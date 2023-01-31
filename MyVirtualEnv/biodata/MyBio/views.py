from django.shortcuts import render,redirect
from .models import Bio, Pendidikan, Pengalaman
from .forms import Bio_form,Edu_form,Exp_form
# Create your views here.

def home_view(request):
    return render(request,"Home.html")

def read_view(request):
    bios = Bio.objects.values_list('Nama')

    context = {
        'bios':bios
    }
    return render(request,"Read.html",context)

def create_view(request):
    bio_form = Bio_form()
    if request.method == 'POST':
        bio_form = Bio_form(request.POST)
        if bio_form.is_valid():
            num1 = request.POST.get('loop1') #none can be use if it dont get any feedback after request the data
            num2 = request.POST.get('loop2')

            bio_form.save()
            return redirect('extra',num1,num2)

    context = {
        'bio' : bio_form

    }
    return render(request, "Create.html",context)

def extra_create(request,num1,num2):
    edu_form = Edu_form()
    if request.method == "POST":
        edu_form = Edu_form(request.POST)
        if edu_form.is_valid():
            edu_form.save()
            return redirect('home')
        else:
            edu_form = Edu_form()

    exp_form = Exp_form()
    if request.method == "POST":
        exp_form = Exp_form(request.POST)
        if exp_form.is_valid():
            exp_form.save()
            return redirect('home')
        else:
            exp_form = Exp_form()

    num1 = int(num1)
    num2 = int(num2)

#    nama = request.POST.get('Nama')
#    print(nama)
    
    dummy1 = []
    dummy2 = []

    for a in range(num1):
        dummy1.append(a)
    
    for a in range(num2):
        dummy2.append(a)

    context = {
        'num1' : dummy1,
        'num2' : dummy2,
        'edu' : edu_form,
        'exp' : exp_form
    }
    return render(request,"ExtraCreate.html",context)

def update_view(request):
    bios = Bio.objects.values_list('Nama')

    context = {
        'bios':bios
    }
    return render(request, "Update.html",context)

def update_isi_view(request,pk):
    data = Bio.objects.get(Nama = pk)
    bio_form = Bio_form(instance=data)
    mydata = Bio.objects.filter(Nama=pk).values()

    if request.method == 'POST':
        bio_form = Bio_form(request.POST,instance=data)
        if bio_form.is_valid():
            bio_form.save()
            return redirect('home')
    #number = 0
    #for i in mydata:
    #    number = i['id']

    #edu = Pendidikan.objects.get(id=number)
    #exp = Pengalaman.objects.get(Nama_id=number)
    #edu_form = Edu_form(instance=edu)
    #exp_form = Exp_form(instance=exp)
    
    context={
        'bio' : bio_form,
        #'education' : edu,
        #'experience' : exp
    }
    return render(request, "Update_isi.html",context)



def delete_view(request):
    bios = Bio.objects.values_list('Nama')
    context = {
        'bios':bios
    }

    return render(request,"Delete.html",context)

def pos_delete_view(request,pk):
    data = Bio.objects.get(Nama=pk)
 
    if request.method == 'POST':
        return redirect('home')
    else:
        data.delete()
        return redirect('home')
        
    context= {
        'bio' : data
    }
    return render(request,"Confirm_Delete.html", context)

def isi_view(request,pk):
    bios = Bio.objects.values_list('Nama')
    mydata = Bio.objects.filter(Nama=pk).values()
    nama = None
    number = 0
    for i in bios:
        if i == pk:
            nama = i
    for i in mydata:
        number = i['id']
    edu = Pendidikan.objects.filter(id=number).values()
    exp = Pengalaman.objects.filter(Nama_id=number).values()
    context={
        'data' : mydata,
        'education' : edu,
        'experience' : exp
    }
    return render(request, "Isi.html",context)