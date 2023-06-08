from django.contrib import admin
from django.urls import path, include 
from user_app.views import user_input  
from django.views.generic import TemplateView   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('user/', include('user_app.urls')),  
    path('calendar/', include('Calendar.urls')), 
]
