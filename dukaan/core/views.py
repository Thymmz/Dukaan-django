from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False) [0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)


        if form.is_valid():
            form.save()
            print("Reached past valid")
            return redirect('/login/')
    
    else:
        form = SignupForm()


    return render(request, 'core/signup.html',{
        'form': form
    })