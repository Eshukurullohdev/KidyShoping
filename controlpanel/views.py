# controlpanel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import Main_Kiyim
from .forms import ProductForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('controlpanel:dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('controlpanel:dashboard')
        else:
            messages.error(request, 'Noto‘g‘ri login yoki parol')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('controlpanel:login')

@login_required
def dashboard(request):
    kiyimlar = Main_Kiyim.objects.all()
    return render(request, 'dashboard.html', {'products': kiyimlar})

@login_required
def product_add(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('controlpanel:dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Main_Kiyim, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('controlpanel:dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Main_Kiyim, pk=pk)
    product.delete()
    return redirect('controlpanel:dashboard')


@login_required
def analytics_view(request):
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