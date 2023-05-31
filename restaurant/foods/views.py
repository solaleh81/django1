from django.shortcuts import render
from .models import Food
# Create your views here.

def food_list(request):
    food_list = Food.objects.all()
    context = {"foods" : food_list}
    return render(request, "foods/list.html", context=context)


def food_detail(request, id):

    food = Food.objects.filter(id=id)
    context = {"food": food}
    return render(request, "foods/detail.html", context=context)
