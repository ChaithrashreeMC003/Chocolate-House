from django.db import models
from django.forms import ModelForm


# Create your models here.

class SeasonalFlavor(models.Model): 
    id = models.AutoField(primary_key=True)  # Automatically increments IDs
    name = models.CharField(max_length=80, null=False)
    discription = models.CharField(max_length=200, null=True, blank=True)  # Allow empty values

    def __str__(self):
        return self.name  # String representation of the model
class FlavorForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model = SeasonalFlavor
        fields = ['name', 'discription']


class IngredientInventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    quantity = models.IntegerField(null=False)


    def __str__(self):
        return self.name
class InventoryForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model = IngredientInventory
        fields = ['name', 'quantity']


class CustomerSuggestion(models.Model):
    id = models.AutoField(primary_key=True)
    flavor_suggestion = models.CharField(max_length=200, null=False)
    allergy_concern = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.flavor_suggestion
class CustomerForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model =CustomerSuggestion
        fields = ['flavor_suggestion', 'allergy_concern']