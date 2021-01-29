from django.shortcuts import render
from .models import Pizza , Pie , Sandwich


def list_pizza(request):
    # list_pizz = Pizza.objects.values_list("name")
    list_pizz = Pizza.objects.all()
    list_pie_price = Pie.objects.values_list("price")
    list_pie = Pie.objects.all()
    list_sandwich = Sandwich.objects.all()
    
    
    return render(request,'Meals/list_pizza.html',{
        'pizza':list_pizz ,
        'pie':list_pie ,
        'sandwich': list_sandwich

        })

