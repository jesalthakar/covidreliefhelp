from django.urls import path
from .views import (
    bed_view,
    

)
app_name = 'beds'

urlpatterns = [
    path('', bed_view, name='beds_info')


]
