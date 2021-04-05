from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IcwXfFMAqtZpW0NDjv4C5v0rFfy2iPgNfhgWmQPRxd9bSA3f0toTnQ4F907HK3BMz3Cae3YvHIr1YlDKOykEDlc00SAMmRuA1',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)