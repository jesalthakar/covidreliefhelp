from django.shortcuts import render
from .models import Bed
from .filters import Bedfilter
from django.core.paginator import Paginator,Paginator,EmptyPage,PageNotAnInteger



# Create your views here.


def bed_view(request):
    bed_qs=Bed.objects.filter(is_verified=True).order_by('-created')
    print(bed_qs)
    page = request.GET.get('page',1)
    paginator = Paginator(bed_qs, 1)
    try:
        beds = paginator.page(page)
    except PageNotAnInteger:
        beds=paginator.page(1)
    except EmptyPage:
        beds= paginator.page(paginator.num_pages)



    myfilter = Bedfilter(request.GET, queryset = bed_qs)
    bed_qs= myfilter.qs


    context={
    'paginator':paginator,
    'myfilter': myfilter,
    'beds': beds,
    }
    return render(request,'beds/beds_info.html',context)
