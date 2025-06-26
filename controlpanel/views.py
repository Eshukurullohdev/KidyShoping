# controlpanel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import Main_Kiyim
from .forms import ProductForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    kiyimlar = Main_Kiyim.objects.all()
    return render(request, 'dashboard.html', {'products': kiyimlar})

@login_required
def product_add(request):
    form = MainKiyimForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Main_Kiyim, pk=pk)
    form = MainKiyimForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Main_Kiyim, pk=pk)
    product.delete()
    return redirect('dashboard.html')

# controlpanel/forms.py
from django import forms
from base.models import Main_Kiyim

class MainKiyimForm(forms.ModelForm):
    class Meta:
        model = Main_Kiyim
        fields = '__all__'
