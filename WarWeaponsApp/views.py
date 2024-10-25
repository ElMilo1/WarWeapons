from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from WarWeaponsApp.models import Weapon
from WarWeaponsApp.forms import WeaponForm

# Create your views here.

def Home(request):
    return render(request,'Index.html')

def Registro(request):
    form = WeaponForm
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
        return Home(request)
    data = {'form':form}
    return render(request,'RegistrarArma.html',data)

def Listar(request):
    x = Weapon.objects.all()
    data = {'Weapon':x}
    return render(request,'Lista.html',data)

def Borrar(request,id):
    x = Weapon.objects.get(id=id)
    x.delete()
    return redirect('../listar/')

def Editar(request,id):
    EWeapon = Weapon.objects.get(id=id)
    form = WeaponForm
    if request.method == 'POST':
        form = WeaponForm(request.POST, instance=EWeapon)
        if form.is_valid():
            form.save()
        return Home(request)
    else:
        form = WeaponForm(instance=EWeapon)
    data = {'form':form}
    return render(request,'RegistrarArma.html',data)