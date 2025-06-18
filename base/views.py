from django.shortcuts import render, get_object_or_404
from .models import Main_Kiyim

def navigation(request):
    return render(request, "navigation.html")
def home(request):
    kiyim = Main_Kiyim.objects.all()
    return render(request, "home.html", {"kiyim": kiyim})

def detail_clothes(request, detail_id):  # <--- BU YER TO‘G‘RILANDI
    kiyim = get_object_or_404(Main_Kiyim, id=detail_id)  
    return render(request, "detail.html", {"kiyim": kiyim})


def kiyimlar_view(request, jinsi=None):
    if jinsi in ['qiz', 'ogil']:
        kiyimlar = Main_Kiyim.objects.filter(jinsi=jinsi)
    else:
        kiyimlar = Main_Kiyim.objects.all()

    return render(request, 'kiyimlar.html', {
        'kiyimlar': kiyimlar,
        'tanlangan_jins': jinsi
    })
    
def skidkali_kiyimlar_view(request):
    kiyimlar = Main_Kiyim.objects.filter(skidkasi__isnull=False)
    return render(request, 'skidka_kiyimlar.html', {'kiyimlar': kiyimlar})