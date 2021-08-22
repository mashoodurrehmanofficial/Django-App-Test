
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('', calculator_page, name='calculator_page'),
    path('calculator_page', calculator_page, name='calculator_page'),

    path('perform_calculation', perform_calculation, name='perform_calculation'),   
    path('history_page', history_page, name='history_page'),   
    path('profile_page', profile_page, name='profile_page'),   
      
    path('signup', signup_page, name='signup'), 

    path('login', login_page, name='login_page'),      
    path('logout', logout_page, name='logout_page'),    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

