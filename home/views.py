from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Parking_data
from django.contrib import messages
from django.utils import timezone
from .forms import ParkingDataSearchForm

# Create your from django.shortcuts import render
def home(request):
    return render(request, 'pages/index.html')
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "pages/register.html", {'form':form})
def logout_view(request):
    logout(request)
    return redirect('home')
def add_parkingdata(request):
    if (request.method == "POST"):
        id = int(request.POST["id"])
        name = request.POST["name"]
        biensoxe = request.POST["biensoxe"]
        mobile = request.POST["mobile"]
        ngaygui = timezone.now()
        tinhtrang = request.POST["tinhtrang"]
        thanhtoan = request.POST["thanhtoan"]
        if Parking_data.objects.filter(id=id).exists():
            error = "ID người gửi đã tồn tại bạn hãy nhập một id khác."
            return render(request, 'pages/add_parkingdata.html', {'error': error})
        item_Parking = Parking_data(id=id, name=name, biensoxe=biensoxe, mobile=mobile, ngaygui=ngaygui,tinhtrang=tinhtrang, thanhtoan=thanhtoan)
        item_Parking.save()
        messages.success(request, "Đã thêm thành công dữ liệu người gửi xe")
        return redirect('/')
    
    return render(request, "pages/add_parkingdata.html")
def show_parkingdata(request):
    item_Parkingdatas = Parking_data.objects.all()
    return render(request, 'pages/show_parkingdata.html', {
        "item_Parkingdatas" : item_Parkingdatas
    })
def update_parkingdata(request, parkingdata_id):
        item_Parking = Parking_data.objects.get(id = parkingdata_id)
        if (request.method == "POST"):
            item_Parking.id = int(request.POST["id"])
            item_Parking.name = request.POST["name"]
            item_Parking.biensoxe = request.POST["biensoxe"]
            item_Parking.mobile = request.POST["mobile"]
            item_Parking.tinhtrang = request.POST["tinhtrang"]
            item_Parking.thanhtoan = request.POST["thanhtoan"]
            item_Parking.save()
            messages.success(request, "Đã cập nhập thành công dữ liệu người gửi xe")
            return redirect('/')
        return render(request, 'pages/update_parkingdata.html', {"item_Parking" : item_Parking})
def show_update(request):
    item_Parkingdatas = Parking_data.objects.all()
    return render(request, 'pages/show_update.html', {
        "item_Parkingdatas" : item_Parkingdatas
    })
def delete_product(request,parkingdata_id):
    item_Parking = Parking_data.objects.get(id = parkingdata_id)
    item_Parking.delete()
    messages.success(request, "Sản phẩm đã được xoá thành công")
    return redirect('/')
# views.py
def search_parking_data(request):
    form = ParkingDataSearchForm(request.POST or None)
    results = None

    if request.method == 'POST' and form.is_valid():
        id = form.cleaned_data.get('id')
        name = form.cleaned_data.get('name')
        biensoxe = form.cleaned_data.get('biensoxe')
        mobile = form.cleaned_data.get('mobile')
        tinhtrang = form.cleaned_data.get('tinhtrang')
        thanhtoan = form.cleaned_data.get('thanhtoan')

        if id:
            results = Parking_data.objects.filter(id__icontains=id)
        elif name:
            results = Parking_data.objects.filter(name__icontains=name)
        elif biensoxe:
            results = Parking_data.objects.filter(biensoxe__icontains=biensoxe)
        elif mobile:
            results = Parking_data.objects.filter(mobile__icontains=mobile)
        elif tinhtrang:
            results = Parking_data.objects.filter(tinhtrang__icontains=tinhtrang)
        elif thanhtoan:
            results = Parking_data.objects.filter(thanhtoan__icontains=thanhtoan)
        messages.success(request, "Đây là danh sách bạn cần tìm")
    return render(request, 'pages/search_results.html', {'form': form, 'results': results})

        
