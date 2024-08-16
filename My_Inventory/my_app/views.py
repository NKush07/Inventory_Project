from django.shortcuts import render,redirect, get_object_or_404
from .models import Inventory
from .forms import InventoryForm


def create(req):
    if req.method == 'POST':
        form = InventoryForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('show')
        
    else:
        form = InventoryForm()
    
    return render(req, 'create.html', {'form':form})



def show(req):
    items = Inventory.objects.all()
    return render(req, 'show.html', {'items':items})



def update(req, pk):
    item = get_object_or_404(Inventory, pk=pk)
    
    if req.method == 'POST':
        form = InventoryForm(req.POST, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('show')
    
    else:
        form = InventoryForm()
    
    return render(req, 'update.html', {'form':form})



def delete(req, pk):
    item = get_object_or_404(Inventory, pk=pk)
    
    if req.method == 'POST':
        item.delete()
        return redirect('show')
    
    return render(req, 'delete.html', {'item':item})



def search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        items = Inventory.objects.filter(product_name__icontains=query)
    else:
        items = Inventory.objects.all()
    
    return render(request, 'show.html', {'items': items})