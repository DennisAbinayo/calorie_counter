from django.shortcuts import redirect, render
from .models import FoodItem
from django.db.models import Sum


# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST.get('food_name').strip().title()
            calories = int(request.POST.get('calorie_count'))
            FoodItem.objects.create(name=name, calories=calories)
        elif 'remove' in request.POST:
            food_name = request.POST.get('food_name').strip()
            FoodItem.objects.filter(name=food_name).delete()
        elif 'reset' in request.POST:
            FoodItem.objects.all().delete()
        return redirect('index')



    foods = FoodItem.objects.all()
    total_calories = foods.aggregate(Sum('calories'))['calories__sum'] or 0
    context = {
        'food_items': {food.name: food.calories for food in foods},
        'total_calories': total_calories,
    }
    
    return render(request, "tracker/index.html", context)
