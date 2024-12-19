from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Product
from django.db.models import Sum, Avg

#update 
def update_product(request,id):

#ambil data dari form edit-expenses.html
    tanggal = request.POST.get('date')
    kategori = request.POST.get('category')
    deskripsi = request.POST.get('description')
    jumlah = request.POST.get('amount')

    #update data
    update=Product.objects.get(id=id)
    update.date=tanggal
    update.category=kategori
    update.description=deskripsi
    update.amount=jumlah
    update.save()

    return redirect('product')


#buat fungsi untuk form update
def form_update_product(request, id):

    #panggil data id yg akan di update
    data_edit=Product.objects.get(id=id)

    context = {
        'data_edit':data_edit
    }

    return render(request, 'edit-product.html', context)


#buat fungsi untuk delete data
#id=id data pada modelyang akan di hapus
def delete_product(request, id):
    print(id)

    #panggilid yang akan dihapus
    #perintah ini ='select * from pengeluaran_expenses where id=id'
    id_hapus = Product.objects.get(id=id)

    #lakukan hapus berdasarkan id hapus
    id_hapus.delete()

    return redirect('product')


def save_product(request): #
    #ambil data dari form add expenses html
    tanggal = request.POST.get('date')
    kategori = request.POST.get('category')
    deskripsi = request.POST.get('description')
    jumlah = request.POST.get('amount')

    #proses simpan kedlm database (model expenses => tabel pengeluaran_expenses)
    simpan=Product(
        date=tanggal,
        category=kategori,
        description=deskripsi,
        amount=jumlah
    )
    simpan.save()

    return redirect('product')


def index(request):
    data= Product.objects.aggregate(total=Sum('amount'),rata2=Avg('amount'))

    context = {
        'data':data
    }
    return render(request, 'index.html', context)


def product(request):
    data=Product.objects.all()
    print(data.query)
    context={
        'data':data
    }

    return render(request, 'product.html', context)


def add_product(request):

    return render(request, 'add-product.html')


def reports_product(request):
    
    return render(request, 'reports-product.html') 

