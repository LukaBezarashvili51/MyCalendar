from django.shortcuts import render
import datetime

def current_date(request):
    current_date = datetime.date.today()
    context = {
        'current_date': current_date
    }
    return render(request, 'current_date.html', context)