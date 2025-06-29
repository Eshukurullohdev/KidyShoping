# controlpanel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from base.models import Main_Kiyim
from .forms import ProductForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

def login_view(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # ✅ Faqat staff userlar kiradi
                login(request, user)
                messages.success(request, "Xush kelibsiz, admin!")
                return redirect('controlpanel:dashboard')
            else:
                messages.error(request, "❌ Sizda admin-panelga kirish huquqi yo‘q!")
                return redirect('controlpanel:login')
        else:
            messages.error(request, "❌ Login yoki parol xato!")
            return redirect('controlpanel:login')

    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('controlpanel:login')

@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('home') 
    kiyimlar = Main_Kiyim.objects.all()
    profile = Profile.objects.all()
    return render(request, 'dashboard.html', {'products': kiyimlar, 'profile': profile})

@login_required
def product_add(request):
    if not request.user.is_staff:
        return redirect('home')
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('controlpanel:dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    product = get_object_or_404(Main_Kiyim, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('controlpanel:dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    product = get_object_or_404(Main_Kiyim, pk=pk)
    product.delete()
    return redirect('controlpanel:dashboard')


@login_required
def analytics_view(request):
    if not request.user.is_staff:
        return redirect('home')
    qiz_count = Main_Kiyim.objects.filter(jinsi='qiz').count()
    ogil_count = Main_Kiyim.objects.filter(jinsi='ogil').count()

    range_1 = Main_Kiyim.objects.filter(narhi__lte=100000).count()
    range_2 = Main_Kiyim.objects.filter(narhi__gt=100000, narhi__lte=200000).count()
    range_3 = Main_Kiyim.objects.filter(narhi__gt=200000, narhi__lte=300000).count()
    range_4 = Main_Kiyim.objects.filter(narhi__gt=300000).count()

    with_discount = Main_Kiyim.objects.filter(skidkasi__isnull=False).exclude(skidkasi=0).count()
    without_discount = (
        Main_Kiyim.objects.filter(skidkasi__isnull=True).count() +
        Main_Kiyim.objects.filter(skidkasi=0).count()
    )
    return render(request, 'analytics.html', {
        'qiz_count': qiz_count,
        'ogil_count': ogil_count,
        'range_1': range_1,
        'range_2': range_2,
        'range_3': range_3,
        'range_4': range_4,
        'with_discount': with_discount,
        'without_discount': without_discount
    })
    
@login_required
def user_list_view(request):
    if not request.user.is_staff:
        return redirect('home')
    users = User.objects.order_by('-date_joined')
    return render(request, 'user_list.html', {'users': users})


@login_required
def admin_profile_view(request):
    if not request.user.is_staff:
        return redirect('home')

    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        avatar = request.FILES.get('avatar')

        if not authenticate(username=user.username, password=old_password):
            messages.error(request, "❌ Eski parol noto‘g‘ri!")
            return redirect('controlpanel:admin_profile')

        if password and password != confirm_password:
            messages.error(request, "❌ Yangi parollar mos emas!")
            return redirect('controlpanel:admin_profile')

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.set_password(password)
            update_session_auth_hash(request, user)
        user.save()

        if avatar:
            profile.avatar = avatar
        profile.save()

        messages.success(request, "✅ Profil muvaffaqiyatli yangilandi!")
        return redirect('controlpanel:admin_profile')

    return render(request, 'admin_profile.html', {'profile': profile})