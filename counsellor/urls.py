from django.urls import path
from .views import (
    counsellor_view,


)
app_name = 'counsellor'

urlpatterns = [
    path('', counsellor_view, name='counsellor_info')
    ]
