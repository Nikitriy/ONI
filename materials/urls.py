from django.urls import path, register_converter
from materials import views
from materials.converters import TwoDigitYearConverter


register_converter(TwoDigitYearConverter, 'year2')

urlpatterns = [
    path('', views.index, name='main'),
    path('material/<slug:material_slug>/', views.show_materials, name='material'),
    path('categories/<slug:category>/', views.categories, name='categories'),
    path('usage/<year2:year>/', views.usage, name='usage'),
]
