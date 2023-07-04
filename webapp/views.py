import email
from django.urls import reverse
from django.shortcuts import render
from .forms import ApplicationForm, CustomUserForm,LoginForm,ApplicationForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import ApplicationModel, CustomUser
from django.contrib import messages
from django.views.decorators.cache import never_cache




def index(request):

    if request.session.has_key('email'):
        email=request.session['email']
        c=CustomUser.objects.get(email=email)
        if(c.role=='student'):
            return HttpResponseRedirect(reverse('webapp:student',args=[c.id]))
        if(c.role=='faculty'):
            return HttpResponseRedirect(reverse('webapp:fac',args=[c.id]))

    else:
        return render(request,'webapp/home.html') 
   
    return render(request,'webapp/home.html')    



@never_cache
def CustomUserView(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password']
            # cpassword=request.POST['cpassword']
            role=form.cleaned_data['role']

            
            user=CustomUser.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,role=role)
            user.save()
               
            messages.success(request,'registration successfull')
            return HttpResponseRedirect('login')

    else:
        form=CustomUserForm()
    
    return render(request,'webapp/reg.html',{'form':form})



@never_cache
def LoginView(request):

    if request.session.has_key('email'):
        email=request.session['email']
        c=CustomUser.objects.get(email=email)
        if(c.role=='student'):
            return HttpResponseRedirect(reverse('webapp:student',args=[c.id]))
        if(c.role=='faculty'):
            return HttpResponseRedirect(reverse('webapp:fac',args=[c.id]))

    else:

        if(request.method=='POST'):
            form=LoginForm(request.POST)
            if(form.is_valid()):
                
                email=request.POST['email']
                password=request.POST['password']
        
                try:
                   
                    request.session.set_expiry(3600)
                    c=CustomUser.objects.get(email=email)
                    
                    if(email==c.email and password==c.password):
                        request.session['email']=email

                        if(c.role=='faculty'):
                            
                            response=HttpResponseRedirect(reverse('webapp:fac',args=[c.id]))
                            return response

                        elif(c.role=='student'):
                        
                            response=HttpResponseRedirect(reverse('webapp:student',args=[c.id]))
                            return response

                        else:
                            
                            messages.error(request,'invalid email or password')
                            return HttpResponseRedirect('login')
                        
                    else:
                        messages.error(request,'invalid email or password')
                        return HttpResponseRedirect('login')
        
                except:
                    messages.error(request,'invalid email or password except')
                    return HttpResponseRedirect('login')
                
        else:
            form=LoginForm()
        return render(request,'webapp/login.html',{'form':form})



@never_cache
def Faculty_dashView(request,id):
    student_user=CustomUser.objects.filter(role='student')
    name=CustomUser.objects.get(pk=id)
    applications=ApplicationModel.objects.all()

    return render(request,'webapp/faculty_dash.html',{'student':student_user,'name':name,'applications':applications})


@never_cache
def Student_dashView(request,id):
    name=CustomUser.objects.get(pk=id)
    applications=ApplicationModel.objects.filter(customer__pk=id)
    return render(request,'webapp/student_dash.html',{'applications':applications,'name':name})



@never_cache
def ApplicationView(request,id):
    name=CustomUser.objects.get(pk=id)
    if(request.method=='POST'):
        form=ApplicationForm(request.POST)
        if(form.is_valid()):
            uni_name=request.POST['uni_name']
            program_name=request.POST['program_name']
            study_mode=request.POST['study_mode']
            ap=ApplicationModel(uni_name=uni_name,program_name=program_name,study_mode=study_mode,customer=name)
            ap.save()

            messages.success(request,'application sent successfull')
            return HttpResponseRedirect(reverse('webapp:student',args=[name.id]))
            
    else:
        form=ApplicationForm()

    return render(request,'webapp/application.html',{'name':name,'form':form})



@never_cache
def UpdateView(request,id,app_id):
    
    application=ApplicationModel.objects.get(pk=app_id)
    return render(request,'webapp/changestatus.html',{'application':application,'id':id})



@never_cache
def ChangeStatus(request,id,app_id):
    cstatus=request.POST['cstatus']
    obj=ApplicationModel.objects.get(pk=app_id)
    obj.status=cstatus  
    obj.save()    
    return HttpResponseRedirect(reverse('webapp:fac',args=[id]))



@never_cache
def LogoutView(request):
    try:
        del request.session['email']
    except:
        pass
    # return HttpResponseRedirect('/webapp')

    return render(request,'webapp/logout.html')
  


