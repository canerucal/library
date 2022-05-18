from django.shortcuts import render, redirect
from .models import table_inventory, visitor
from django.db.models import Max

# Create your views here.
def loginUser(request):
    return render(request, 'index.html')

def reservation(request):
    allList = table_inventory.objects.all()
    max_rating = table_inventory.objects.aggregate(Max('table_number')).get('table_number__max')

    return render(request, 'reservation.html', {
        'allList': allList,
        'max_rating': max_rating
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

def session(request, visitor_id):
    addSession = visitor.objects.filter(visitor_id = visitor_id)
    addSession.create(
        visitor_id = taken_id,
        visitor_name = taken_name,
        visitor_surname = taken_surname,
        time = taken_time
    )