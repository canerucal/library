from django.shortcuts import render, redirect
from .models import table_inventory
from django.db.models import Max

# Create your views here.
def loginUser(request):
    return render(request, 'index.html')

def reservation(request):
    allList = table_inventory.objects.all()
    return render(request, 'reservation.html', {
        'allList': allList,

    })

def delete(request, table_id):
    deleteRecord = table_inventory.objects.filter(table_id = table_id)
    deleteRecord.delete()
    max_rating = table_inventory.objects.aggregate(Max('table_number')).get('table_number__max')
    print(max_rating)
    context = {
        'deleteRecord': deleteRecord,
        'max_rating': max_rating
    }
    return redirect('reservation', context)