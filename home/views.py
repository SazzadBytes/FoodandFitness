from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import SignUp,FoodTips,Bmi,Sugar,BloodPresure,Update,FoodBlog,HealthBlog
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def fullhealthblog(request, slug):
    blog = HealthBlog.objects.get(slug=slug)
    return render(request, 'fullblog.html', {'blog': blog,})

def fullfoodblog(request,slug):
    blog=FoodBlog.objects.get(slug=slug)
    return render(request, 'fullblog.html', {'blog': blog,})


def teamview(request):
    return render(request,'ourteam.html')

def healthblogview(request):
    HealthBlogData = HealthBlog.objects.all()
    paginator = Paginator(HealthBlogData, 3) # Show 3 blogs per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'healthblog.html', {'blogs': blogs})
def foodblogview(request):
    FoodBlogData=FoodBlog.objects.all()
    paginator=Paginator(FoodBlogData,3)
    page=request.GET.get('page')
    blogs=paginator.get_page(page)
    return render(request,'foodblog.html',{'blogs':blogs})

def homeview(request):
    if request.method=="POST":
        if request.POST.get('formtype')=="checkfood":
            foodname=request.POST.get('foodname')
            foodData=FoodTips.objects.filter(foodname=foodname)
            fData={
                'foodData':foodData
            }
            return render(request,'foodtips.html',fData)
        if request.POST.get('formtype')=='bmi':
            height=eval(request.POST.get('height'))
            weight=eval(request.POST.get('weight'))
            height=height/100
            bmi=weight/(height*height)
            bmi = round(bmi, 2)
            
            if bmi>0 and bmi<17:
                bmitype='Underweight'
            elif bmi>17 and bmi<25:
                bmitype='Normalweight'
            elif bmi>25 and bmi<30:
                bmitype='Overweight'
            elif bmi>30 and bmi<100:
                bmitype='Obesity'
            else:
                print('You are dead')
            BmiData=Bmi.objects.filter(bmitype=bmitype)
            bdata={
                'BmiData':BmiData,
                'bmi':bmi
            }
            return render(request,'bmi.html',bdata)
        if request.POST.get('formtype')=='bloodpresure':
            try:
                systolic=eval(request.POST.get('systolic'))
                diastolic=eval(request.POST.get('diastolic'))
                sumpressure=systolic+diastolic
                if sumpressure>180 and sumpressure<205:
                    pressuretype='Normal Blood Pressure'
                elif sumpressure>205 and sumpressure<240:
                    pressuretype='High Blood Pressure'
                elif sumpressure>140 and sumpressure<180:
                    pressuretype='Low Blood Pressure'
                else:
                    return render(request,'error.html')
                pData=BloodPresure.objects.filter(presuretype=pressuretype)
                PressureData={
                    'pData':pData
                }
                return render(request,'bloodpresure.html',PressureData)
            except:
                return render(request,'error.html')
        
        if request.POST.get('formtype')=='sugar':
            try:
                sugar=eval(request.POST.get('sugar'))
                if sugar>1 and sugar<5.7:
                    sugartype='Normal'
                elif sugar>=5.7 and sugar<6.4:
                    sugartype='Prediabetes'
                elif sugar>=6.5 and sugar<20:
                    sugartype='Diabetes'
                elif sugar>=20 and sugar<0:
                    sugartype='Danger'
                else:
                    return render(request,'error.html')
                sugarData=Sugar.objects.filter(sugartype=sugartype)
                sgData={
                    'sugarData':sugarData
                }
                return render(request,'sugar.html',sgData)
            except:
                return render(request,'error.html')
    return render(request,'index.html')

def aboutview(request):
    return render(request,'aboutus.html')

def tipsview(request):   
    return render(request,'foodtips.html')

def signinview(request):
    if request.user.is_authenticated:
        return redirect('profile')
    try:
        if request.method=='POST':
            uname=request.POST['uname']
            pass2=request.POST['pass2']  
            user=authenticate(username=uname,password=pass2)
            if user is not None:
                login(request,user)
                # SData=SignUp.objects.filter(uname=uname)
                # SignUpData={
                #     'SData':SData
                # }
                
                return redirect('/profile')
            else:
                return render(request,'signin.html',{'signinerror':True})
    except:
        return render(request,'error.html')
    return render(request,'signin.html')

def signupview(request):
    if request.method=="POST":
        try:
            fname=request.POST.get('fname')
            uname=request.POST.get('uname')
            dob=request.POST.get('dob')
            gender=request.POST.get('inlineRadioOptions')
            umail=request.POST.get('umail')
            pnumber=request.POST.get('pnumber')
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            checkbox=request.POST.get('checkbox')
            if checkbox !='checked':
                return render(request,'signup.html',{'checkerror':True})
            if pass1 != pass2:
                return render(request,'signup.html',{'passerror':True})
                
            myuser=User.objects.create_user(username=uname,email=umail,password=pass1)
            myuser.first_name=fname
            myuser.save()
            update_signup=SignUp(fname=fname,uname=uname,dob=dob,gender=gender,umail=umail,pnumber=pnumber,pass1=pass1,pass2=pass2)
            update_signup.save()
            return redirect('/signin')
        except:
            return render(request,'signup.html',{'error':True})
    return render(request,'signup.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Update, SignUp

@login_required(login_url='/signin')
def profileview(request):
    uname = request.user.username
    SData = SignUp.objects.filter(uname=uname)
    record = Update.objects.filter(unamep=uname).order_by('-id').first()
    context = {
        'SData': SData,
        'record': record,
    }

    if request.method == 'POST':
        if request.POST.get('formtype') == 'ubmi':
            sbmi = request.POST.get('ubmi')
            ubmi=float(sbmi)
            unamep = request.user.username
            if record:
                record.bmi = ubmi
                record.save()
            else:
                Update.objects.create(bmi=ubmi, unamep=unamep)
        elif request.POST.get('formtype') == 'pressure':
            upressure = request.POST.get('pressure')
            if record:
                record.bp = upressure
                record.save()
            else:
                Update.objects.create(bp=upressure, unamep=unamep)
        elif request.POST.get('formtype') == 'sugar':
            usugar = request.POST.get('sugar')
            if record:
                record.bs = usugar
                record.save()
            else:
                Update.objects.create(bs=usugar, unamep=unamep)

    return render(request, 'profile.html', context)


def handlelogout(request):
    logout(request)
    return redirect('/')
