from django import forms
from .models import Item, Category

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': INPUT_CLASSES})  
    )
    
    name = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': 'Item name', 'class': INPUT_CLASSES})
    )
    
    description = forms.CharField(
       widget=forms.Textarea(attrs={"rows":5, 'class': INPUT_CLASSES})
    )
    
    price = forms.DecimalField(
        min_value=0, 
        widget=forms.NumberInput(attrs={'placeholder':'0.00', 'class': INPUT_CLASSES})
    )
    
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        
class EditItemForm(forms.ModelForm):

    # Fields with styling classes
    
    class Meta:  
        model = Item
        fields = ('name', 'description', 'price', 'image')