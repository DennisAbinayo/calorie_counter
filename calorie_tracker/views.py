from django.shortcuts import render

# Create your views here.
food_items = {}
total_calories = 0

def base(request):
    global food_items, total_calories
    
    if request.method == 'POST':
        if 'add' in request.POST:
            food_name = request.POST.get('food_name').strip().title()
            calorie_count = int(request.POST.get('calorie_count'))
            if food_name and calorie_count >= 0:
                food_items[food_name] = calorie_count
                total_calories += calorie_count
        elif 'remove' in request.POST:
            food_name = request.POST.get('food_name').strip()
            if food_name in food_items:
                total_calories -= food_items[food_name]
                del food_items[food_name]
        elif 'reset' in request.POST:
            total_calories = 0
            food_items.clear()
    
    return render(request, 'tracker/index.html', {'food_items': food_items, 'total_calories': total_calories})