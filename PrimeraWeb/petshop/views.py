from django.shortcuts import render
from .models import Pet, Customer
from .forms import PetForm, CustomerForm, OrderForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'petshop/home.html')


def pet_list(request):
    pets = Pet.objects.all()
    print(pets)
    return render(request, 'petshop/pet_list.html', {'pets': pets})
    # return HttpResponse("Hola mundo")


def add_pet(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('pet_list')
    else:
        pet_form = PetForm()
    return render(request, 'petshop/add_pet.html', {'pet_form': pet_form})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or redirect somewhere else
    else:
        form = CustomerForm()
    return render(request, 'petshop/add_customer.html', {'form': form})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or redirect somewhere else
    else:
        form = OrderForm()
    return render(request, 'petshop/add_order.html', {'form': form})


def search_pets_by_customer(request):
    pets = None
    customer_id = None
    customer = None

    if request.method == 'GET':
        customer_id = request.GET.get('customer_id')
        if customer_id:
            pets = Pet.objects.filter(customer_id=customer_id)
            customer = Customer.objects.filter(id=customer_id).first()

    return render(request, 'petshop/search_pets.html', {
        'pets': pets,
        'customer_id': customer_id,
        'customer': customer
    })
