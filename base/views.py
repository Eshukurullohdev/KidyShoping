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


def yosh_boyicha(request, yosh):
    yoshlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    yosh = request.GET.get('yosh')

    if yosh:
        kiyimlar = Main_Kiyim.objects.filter(yoshi=yosh)
    else:
        kiyimlar = Main_Kiyim.objects.all()

    return render(request, 'index.html', {
        'kiyimlar': kiyimlar,
        'yoshlar': yoshlar,
    })
    
    
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        phone = request.POST.get('phone')

        if password != confirm:
            messages.error(request, "Parollar mos emas.")
            return redirect('register')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Bu foydalanuvchi allaqachon mavjud.")
            return redirect('register')

        user = User.objects.create_user(
            username=name,
            password=password
        )
        user.first_name = phone  # phone ma'lumotni vaqtincha shu yerga yozamiz
        user.save()

        messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli!")
        return redirect('/')

    return render(request, 'register.html')