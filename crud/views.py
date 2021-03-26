from django.shortcuts import render,HttpResponseRedirect
from .models import USER
from .forms import StudentRegistration

# Add user function
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            reg=USER(name=nm, email=em)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=USER.objects.all()
    return render(request, 'crud/addandshow.html', {'form':fm, 'stu':stud})    



# Update User

def update_user(request,id):
    if request.method == 'POST':
     pi=USER.objects.get(pk=id)
     fm=StudentRegistration(request.POST, instance=pi)  
     if fm.is_valid():
         fm.save() 
    else:
     pi=USER.objects.get(pk=id)
     fm=StudentRegistration(instance=pi)    
    return render(request, 'crud/update.html', {'form':fm})



# Deleting User Function
def delete_user(request, id):
    if request.method == 'POST':
        pi=USER.objects.get(pk=id)   
        pi.delete()
        return HttpResponseRedirect('/')

