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
        'stripe_public_key': 'pk_test_51GsRxiJ9r5Fk3Kw98U3iPPOegbhm2yY61NkcQL14mmiH7rjb5x5t0WsotweH6BRfcMRYt3GOabXP5F6245z1tRFE0014FGdzcK',
        'client_secret': 'client_secret',
    }

    return render(request, template, context)