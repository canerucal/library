from turtle import right
from django.shortcuts import render, redirect
from .models import table_inventory, visitor
from django.db.models import Max

# Create your views here.
def loginUser(request):
    return render(request, 'index.html')

def reservation(request):
    allList = table_inventory.objects.all()
    allSession = visitor.objects.all()
    max_rating = table_inventory.objects.aggregate(Max('table_number')).get('table_number__max')
    visitor_no = visitor.objects.aggregate(Max('visitor_id')).get('visitor_id__max')
    visitor_no +=1
    return render(request, 'reservation.html', {
        'allList': allList,
        'max_rating': max_rating,
        'visitor_no': visitor_no,
        'allSession': allSession
    })

def delete(request, table_number):
    deleteRecord = table_inventory.objects.filter(table_number = table_number)
    deleteRecord.delete()
    context = {
        'deleteRecord': deleteRecord
    }
    return redirect('reservation')

def create(request, table_number):
    addRecord = table_inventory.objects.filter(table_number = table_number)
    max_rating = table_inventory.objects.aggregate(Max('table_number')).get('table_number__max')
    max_rating +=1
    addRecord.create(
        table_number = max_rating,
        left_side = 0,
        right_side = 0
        )

    context = {
        'addRecord': addRecord
    }
    return redirect('reservation')

def createSession(request, visitor_id):
    addSession = visitor.objects.filter(visitor_id = visitor_id)
    if request.method == "POST":
        taken_name = request.POST.get('taken_name')
        taken_surname = request.POST.get('taken_surname')
        taken_time = request.POST.get('taken_time')

    addSession.create(
        visitor_name = taken_name,
        visitor_surname = taken_surname,
        res_time = taken_time
    )

    context = {
    'addSession': addSession
    }
    return redirect('reservation')

