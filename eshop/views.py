from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime


# Create your views here.


def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def sneakers(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/sneakers.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def detailedView(request):
    productId = request.session['productId']
    product = Product.objects.get(id=productId)
    sizes = ProductSizes.objects.filter(product=product).all()
    context = {'product': product, 'sizes': sizes}
    return render(request, 'store/detailedView.html', context)


def go_to_detailed_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    request.session['productId'] = productId
    return JsonResponse("Got to detail page", safe=False)


def update_item(request):
    data = json.loads(request.body)
    productId = request.session['productId']
    size = data['size']
    action = data['action']
    request.session['size'] = data['size']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem = OrderItem.objects.create(order=order, size=size, product=product)

    if action == 'add':
        orderItem.save()
    elif action == 'remove':
        orderItem.delete()

    return JsonResponse("Sending data..", safe=False)


def delete_item(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    orderItem = OrderItem.objects.get(id=itemId)
    if action == 'remove':
        orderItem.delete()

    return JsonResponse("Deleting data..", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=str(data['shipping']['address']),
            city=data['shipping']['city'],
            postal_code=data['shipping']['postalCode'],
        )
    else:
        print('Not logged in')
    return JsonResponse('Payment submitted..', safe=False)


def order_confirmation(request):
    return render(request, 'store/orderSuccessful.html')

