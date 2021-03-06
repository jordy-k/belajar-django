from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Customer
from app.forms import customerForm
from django import forms


def index(request):
    return render(request, 'home.html')


def text(request):
    output = '<b>This is a bold text.</b>'
    output += '<i>This is a italic text.</i>'
    output += '<u>This is a underlined text.</u>'
    output += '<p>This is a paragraph.</p>'
    return HttpResponse(output)


def temp(request):
    my_dict = {'my_name': "Jordy", 'my_age': "23"}
    return render(request, 'index.html', context=my_dict)


def customer(request):
    data = Customer.objects.all()
    customerDataDict = {'customerData': data}
    return render(request, 'customer.html', context=customerDataDict)


def addCustomer(request):
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return index(request)
            return HttpResponseRedirect('../')
        else:
            print('Validation Error')
    return render(request, 'formCustomer.html', context={'form': form})


def detailCustomer(request, key):
    customerDetail = Customer.objects.get(userName__exact=key)
    customerDetailDict = {'customer': customerDetail}
    return render(request, 'detailCustomer.html', context=customerDetailDict)


def deleteCustomer(request, key):
    customerDetail = Customer.objects.get(userName__exact=key)
    customerDetailDict = {'customer': customerDetail}
    if request.method == 'POST':
        customerDetail.delete()
        return HttpResponseRedirect('../')
    return render(request, 'deleteCustomer.html', context=customerDetailDict)


def editCustomer(request, key):
    customerDetail = Customer.objects.get(userName__exact=key)
    form = customerForm(instance=customerDetail)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=customerDetail)
        if form.is_valid():
            form.save(commit=True)
            # return index(request)
            return HttpResponseRedirect('../')
        else:
            print('Validation error!')
    return render(request, 'formCustomer.html', context={'form': form})
