import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class Bedfilter(django_filters.FilterSet):
    #Name = CharFilter(field_name = 'name', lookup_expr ='icontains', label='Name')
    City = CharFilter(field_name = 'city', lookup_expr ='icontains', label='City')
    hospital = CharFilter(field_name = 'hospital', lookup_expr ='icontains', label='Hospital')
    Address = CharFilter(field_name = 'Address', lookup_expr ='icontains', label='Address')
    POC = CharFilter(field_name = 'poc', lookup_expr ='icontains', label='POC')
    Additional_info = CharFilter(field_name = 'additional_info', lookup_expr ='icontains', label='Additional_info')
    start_date = DateFilter(field_name='created',lookup_expr = 'gte',label = 'date from')
    end_date = DateFilter(field_name='created',lookup_expr = 'lte', label = 'date to' )



    class Meta:
        model = Bed
        fields = '__all__'
        exclude = ['created','name','city','Address','hospital','poc','additional_info']
