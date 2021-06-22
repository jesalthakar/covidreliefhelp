from django.shortcuts import render
from .models import Counsellor
from .filters import Counsellorfilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.






# Create your views here.
def counsellor_view(request):
    counsellor_qs=Counsellor.objects.filter(is_verified=True).order_by('-created')
    page = request.GET.get('page',1)
    paginator = Paginator(counsellor_qs, 1)
    try:
        counsellors = paginator.page(page)
    except PageNotAnInteger:
        counsellors = paginator.page(1)
    except EmptyPage:
        counsellors = paginator.page(paginator.num_pages)
    myfilter = Counsellorfilter(request.GET, queryset = counsellor_qs)
    counsellor_qs= myfilter.qs

    context={
    'paginator':paginator,
    'myfilter': myfilter,
    'counsellors':counsellors,
    }
    return render(request,'counsellor/counsellor_info.html',context)
