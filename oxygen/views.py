from django.shortcuts import render
from .models import Oxygen
from .filters import Oxygenfilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def home_view(request):
    print("hi")
    return render(request,'oxygen/index.html',{})


# Create your views here.
def oxygen_view(request):
    oxygen_qs=Oxygen.objects.filter(is_verified=True).order_by('-created')
    myfilter = Oxygenfilter(request.GET, queryset = oxygen_qs)
    oxygen_qs= myfilter.qs
    paginator = Paginator(oxygen_qs, 3)
    page = request.GET.get('page',1)

    try:
        oxygen = paginator.page(page)
    except PageNotAnInteger:
        oxygen=paginator.page(1)
    except EmptyPage:
        oxygen = paginator.page(paginator.num_pages)


    #print(myfilter)

    context={
        'paginator':paginator,
        'myfilter': myfilter,
        'oxygen':oxygen,
    }
    return render(request,'oxygen/oxygen_info.html',context)
