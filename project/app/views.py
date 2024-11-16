from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import json
from .models import SeasonalFlavor, IngredientInventory, CustomerSuggestion,CustomerForm,InventoryForm,FlavorForm
from django.views import generic
 
def index(request):
    return render(request,'index.html')

def flavors(request):
    names_and_descriptions = [
    ('Peppermint Bark', 'Minty, cool, festive'),
    ('Pumpkin Spice', 'Warm, spicy, cozy'),
    ('Salted Caramel', 'Sweet, salty, rich'),
    ('Eggnog Truffle', 'Creamy, spiced, smooth'),
    ('Hazelnut Praline', 'Nutty, sweet, crunchy')]
    return render(request,'flavors.html',{"names_and_descriptions":names_and_descriptions})
    

def inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully</h1>")
        else:
            return HttpResponse("<h1>Record not inserted. Please try again.</h1>")
    else:
        form = InventoryForm()
        inventory_records = IngredientInventory.objects.all()
    return render(request, "inventory.html", {"form": form,"inventory_records": inventory_records})


def suggestions(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully</h1>")
        else:
            return HttpResponse("<h1>Record not inserted. Please try again.</h1>")
    else:
        form = CustomerForm()
        suggestions_list = CustomerSuggestion.objects.all() 
    return render(request, "suggestions.html", {"form": form,"suggestions_list": suggestions_list})

# Create your views here.
