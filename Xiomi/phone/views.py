from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Phone
from .forms import PhoneForm, ContactForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def phone_list(request):
    return render(request, template_name='phone_things/phone_list.html', context={'phonen':Phone.objects.all()})

def phone_detail(request, pk):
    return render(request, template_name='phone_things/phone_detail.html', context={'phonen2':Phone.objects.get(id=pk)})

# def phone_add(request):
#     if request.method == 'POST':
#         phone = Phone()
#         phone.maker = request.POST.get('maker', '')
#         phone.model = request.POST.get('model', '')
#         phone.year = request.POST.get('year', 0)
#         phone.color = request.POST.get('color', '')
#         phone.price = request.POST.get('price', 0)
#         phone.description = request.POST.get('description', '')
#         phone.image = request.FILES.get('image', '')
#         phone.created_at = request.POST.get('created_at', '')
#         phone.save()
#         return redirect('phone_list')
#     return render(request, template_name='phone_things/phone_add.html', context={'phone': 'phone'})

def phone_add_form(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('phone_list')
    return render(request, template_name='phone_things/phone_add.html', context={'form':form})



# def phone_edit(request, pk):
#     phone = Phone.objects.get(id=pk)
#     if request.method == 'POST':
#         phone.maker = request.POST.get('maker', phone.maker)
#         phone.model = request.POST.get('model', phone.model)
#         phone.year = request.POST.get('year', phone.year)
#         phone.color = request.POST.get('color', phone.color)
#         phone.price = request.POST.get('price', phone.price)
#         phone.description = request.POST.get('description', phone.description)
#         phone.image = request.FILES.get('image', phone.image)
#         phone.created_at = request.POST.get('created_at', phone.created_at)
#         phone.save()
#         return redirect('phone_detail', pk=pk)
#     return render(request, template_name='phone_things/phone_edit.html', context={'phone': phone})

def phone_edit(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_detail', pk)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'phone_things/phone_edit.html', {'form': form, 'phone':phone})


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, id=pk)

    if request.method == "POST":
        phone.delete()
        return redirect("phone_list")

    return render(request, "phone_things/phone_delete.html", {"phone": phone})


def contact_form(request):
    form = ContactForm(request.POST)
    print(1)
    if form.is_valid():
        print(2)
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        print(f"{name}, {phone_number}, {email}, {message}")
        return redirect('home')
    return render(request, template_name='contact.html', context={'form':form})