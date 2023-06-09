from django.shortcuts import render
from .models import Food
# Create your views here.

def food_list(request):
    food_list = Food.objects.all()
    context = {"foods" : food_list}
    return render(request, "foods/list.html", context=context)


def food_detail(request, slug):

    food = Food.objects.filter(slug = slug)
    context = {"foods": food}
    return render(request, "foods/detail.html", context=context)

