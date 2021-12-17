from types import NoneType
from django.shortcuts import render, redirect
from .models import room, room_number, reservation
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
import datetime , json
import pytz
c=[] #Temporary to save filter query.
c_in =''
c_out=''

#utc=pytz.UTC 
#utc.localize(datetime_data)

class home(View):
    
    def get(self, request):
            return render(request,'home.html')
    def post(self, request ):
       
        city=request.POST['destenition']
        checkin=datetime.datetime.strptime(request.POST['check_in'], '%Y-%m-%d').date()
        checkout=datetime.datetime.strptime(request.POST['check_out'], '%Y-%m-%d').date()
        global c_in
        global c_out
        c_in = request.POST['check_in']
        c_out = request.POST['check_out']
        #adults=request.POST['adults']
        #children=request.POST['children']

        
        

        a=[]
        available_rooms = room_number.objects.filter(room__destination=city)
        for i in available_rooms:
            a.append(i.id)

       
        b=[]
        not_available_reservations = reservation.objects.filter(room__id__in=a)
        for i in not_available_reservations:
            if i.check_out > checkin or i.check_in < checkout: 
                b.append(i.room.id)
            if i.check_out > checkin:
                messages.info(request,'suggestion check in: {}'.format(i.check_out))
            if i.check_in < checkout:
                messages.info(request,'suggestion check out: {}'.format(i.check_in))
       
            
        global c 
        c=[]
        for i in a:
            if i not in b:
                c.append(i)

        return redirect('/results')


class results(View):
        def get(self, request):
            global c
            rm=room.objects.all().filter(id__in=c)
            c = []
            return render(request,'result.html',{'rm':rm})
        def post(self, request):
            global c_in
            global c_out
            res_room = room.objects.get(pk=request.POST['room_id'])
            current_user = request.user
            res = reservation ( customer = current_user , room =  res_room , check_in = datetime.datetime.strptime(c_in, '%Y-%m-%d').date() , check_out = datetime.datetime.strptime(c_out, '%Y-%m-%d').date() )
            res.save()
            return redirect('/')
            

