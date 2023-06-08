import datetime
from django.shortcuts import render
from .models import User

def user_input(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_year = request.POST['birth_year']
        
        current_year = datetime.date.today().year
        years_passed = current_year - int(birth_year)
        
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'years_passed': years_passed,
        }
        return render(request, 'user_output.html', context) 
    else:
        return render(request, 'user_input.html')