from django.urls import path
from .views import (
    oxygen_view,
    home_view,

)
app_name = 'oxygen'

urlpatterns = [
    path('oxygen/', oxygen_view, name='oxygen_info'),
    path('',home_view, name = 'index')

]
