'''from django.urls import path
from .views import current_date

app_name = 'Calendar'

urlpatterns = [
    path('calendar/', current_date, name='current_date'),
]'''
from django.urls import path
from .views import current_date

urlpatterns = [
    path('', current_date, name='current_date'),
]
