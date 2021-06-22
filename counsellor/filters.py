import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class Counsellorfilter(django_filters.FilterSet):
    #Name = CharFilter(field_name = 'name', lookup_expr ='icontains', label='Name')
    Counsellor_Name = CharFilter(field_name = 'Counsellor_Name', lookup_expr ='icontains', label='Counsellor Name')
    Contact_nos = CharFilter(field_name = 'Contact_nos', lookup_expr ='icontains', label='Contact_nos')
    Location = CharFilter(field_name ='Location', lookup_expr ='icontains', label='Location')
    Additional_info = CharFilter(field_name = 'additional_info', lookup_expr ='icontains', label='Additional info')
    start_date = DateFilter(field_name='created',lookup_expr = 'gte',label = 'date from')
    end_date = DateFilter(field_name='created',lookup_expr = 'lte', label = 'date to' )



    class Meta:
        model = Counsellor
        fields = '__all__'
        exclude = ['created','Name','Counsellor_Name','Contact_nos','Location','Hospital','additional_info']
