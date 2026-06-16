from django.shortcuts import render
from shop.models import Mevalar
# Create your views here.

def index_page(request):
    matn = "Goodbye world"
    mevalar = Mevalar.objects.all()
    ism = ['Abduraxim','vali','bali']
    context = {
        'title':matn,
        'ism':ism,
        'mevalar':mevalar

    }
    return render(request,'index.html', context=context)


