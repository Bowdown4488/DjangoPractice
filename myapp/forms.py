from django import forms 
from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]

#Source: https://www.quora.com/Why-do-we-use-the-class-Meta-inside-the-ModelForm-in-Django
#The Meta class of Models and ModelForms can be thought of as something similar to a class or function decorator. The Meta class is referenced 
# during the construction of the form/object instance before the class definition itself. You could try to do the same work by 
# overriding the class __init__ function, but 1) that would be a lot of extra work to replicate something already being done for you by 
# he Meta class, and 2) any such implementation is unlikely to be as efficient or clean as the Meta class.

#In short, it’s efficient and it is useful. If you need to do something exotic that doesn’t use the Meta class knock yourself out,
# but in my experience when you start down that road you eventually realize you’re trying to make a class do something at a level 
# that another class is better suited for.