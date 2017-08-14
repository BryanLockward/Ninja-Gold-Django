from django.shortcuts import render,redirect
from time import gmtime, strftime
import random

def index(request):
    return render(request,"ninjagold/index.html")

def process_money(request):
    new_gold={}
    try:
        request.session['gold_total']
    except KeyError:
        request.session['gold_total']=0


    if request.POST['location']=="1":
        new_gold['location']="cave"
        new_gold['gold']=random.randint(10,20)
    elif request.POST['location']=="2":
        new_gold['location']="farm"
        new_gold['gold']=random.randint(5,10)
    elif request.POST['location']=="3":
        new_gold['location']="house"
        new_gold['gold']=random.randint(2,5)
    else:
        new_gold['location']="casino"
        new_gold['gold']=random.randint(-50,50)

    if new_gold['gold'] < 0:
        new_gold["positive"]=new_gold['gold']*-1
        total=request.session['gold_total'] + new_gold['gold']
        if total < 0:
            print "help"
            new_gold['gold']= 0 - request.session['gold_total']
            new_gold['positive']=new_gold['gold']*-1

    new_gold['created_at']=strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['gold_total']+=new_gold['gold']
    print new_gold
    try:
        request.session['ninja']
    except KeyError:
        request.session['ninja']=[]
    holder = request.session['ninja']
    holder.append(new_gold)
    request.session['ninja'] = holder

    return redirect('/')
