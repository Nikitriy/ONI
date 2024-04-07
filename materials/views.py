from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime


db = [
    {'id': 1, 'name': 'Бетон', 'text': 'Вот такой вот бетон'},
    {'id': 2, 'name': 'Стекло', 'text': 'Ага, очень уиное стекло'},
    {'id': 3, 'name': 'Черепицца', 'text': 'Пицца с черри'},
]

menu = ['Первое', 'Второе', 'Войти']


def index(request):
    data = {
        'title': 'Главная страница',
        'materials': db,
        'menu': menu,
    }
    return render(request, 'women/index.html', context=data)


def show_materials(request, material_slug):
    data = {
        'title': 'Материал',
        'materials': db,
        'menu': menu,
    }
    return render(request, 'women/material.html', context=data)


def categories(request, category):
    return render(request, 'women/categories.html', context={'category': category})


def usage(request, year):
    current_year = datetime.now().year
    if year > current_year:
        save_path = reverse('categories', args=(current_year, ))
        return redirect(save_path)
    return render(request, 'women/usage.html', context={'year': year})


def custom_404(request, exception):
    return render(request, 'women/custom_404.html', status=404)
