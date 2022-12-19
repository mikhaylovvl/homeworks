from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe(request):
    name_of_recipe = request.path.strip('/')
    amount_of_person = int(request.GET.get('servings', 1))

    context = {}

    if name_of_recipe in DATA.keys():
        for key, value in DATA[name_of_recipe].items():
            DATA[name_of_recipe][key] = value * amount_of_person
        context['recipe'] = DATA[name_of_recipe]
    else:
        context['recipe'] = {}

    return render(request, 'calculator/index.html', context)

