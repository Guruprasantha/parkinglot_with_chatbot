from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.http import JsonResponse
import google.generativeai as genai
import os
import nltk
os.getenv('AIzaSyDt1TMqr33BAknZCKEIIFxMzCRGkuLkEVc')



def homepage(request):
    s=request.session['username']
    context={'session':s}
    return render(request,'app/homepage.html',context)




def login(request):
        if request.method == 'POST':
            user = request.POST.get('username')
            pwrd = request.POST.get('password')
            try:
                User = Register.objects.get(name=user)

                if User.password == pwrd:
                    request.session['username']=user
                    data={'session':user}
                    return redirect('homepage')
                else:
                    data = {'status':"Incorrect Password!!!"}
                    return render(request,'app/login.html',context=data)
            except:
                data = {'status':"NO user found !!!"}
                return render(request,'app/login.html',context=data)
                
        return render(request,'app/login.html')


def logout(request):
    if 'username' in request.session:
        del request.session['username']

    return redirect('login')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('Username')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        repassword = request.POST.get('password')
                
        if password==repassword:
            reg=Register(name=name,email=email,phonenumber=phonenumber,password=password,repassword=repassword)
            reg.save()
            return render(request,'app/login.html')
        else:
            data='Password and confirm password has not match'
            return render(request,'app/register.html',context=data)
    return render(request,'app/register.html')


def booking(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        car = request.POST.get('car')
        license = request.POST.get('license')
        intime = request.POST.get('intime')
        outtime = request.POST.get('outtime')
        indate = request.POST.get('indate')
        outdate = request.POST.get('outdate')
        oname=request.session['username']

        obj=Booking(oname=oname,name=name,car=car,carnumber=license,intime=intime,outtime=outtime,indate=indate,outdate=outdate)
        obj.save()
        user=request.session['username']
        if 'username' in  request.session:
          user=request.session['username']
          data={'session':user}
          return render(request,'app/logout.html',context=data)

    return render(request,'app/booking.html')

def history(request):
        if 'username' in request.session:
            event = Booking.objects.all()
            data = {'event':event}
            return render(request,'app/history.html',context=data)
        else:
            data = {'status':'You need to login first'}
            return render(request,'login.html',context=data)




def bot(request):
    if request.method == 'POST':
        text=request.POST.get('text')
        result=sent_message(text)
        return render(request, 'bot.html',{'result':result,'usertext':text})
    return render(request,'app/bot.html',{'result':None})


def sent_message(txt):
        b=nltk.word_tokenize(txt)
        print(b)
        genai.configure(api_key='AIzaSyDt1TMqr33BAknZCKEIIFxMzCRGkuLkEVc')
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(txt)
        res = response.text
        print(res)
        return res
     


      


