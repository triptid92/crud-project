from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import StudentRegistrtion
from .models import User

def add_show(request):
    stud = User.objects.all()  # Initialize stud here
    if request.method == 'POST':
        fm = StudentRegistrtion(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, email=em, password=ps, address=ad)
            reg.save()
            fm = StudentRegistrtion()
    else:
        fm = StudentRegistrtion()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stud': stud})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistrtion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistrtion(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')
    


