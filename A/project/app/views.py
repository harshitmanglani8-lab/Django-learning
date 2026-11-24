from django.shortcuts import render
import razorpay
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

def payment_page(request):
    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1,
    })

    context = {
        'payment': payment,
        'razorpay_key': settings.RAZORPAY_KEY_ID
    }

    return render(request, 'payment.html', context)


def payment_success(request):
    return HttpResponse("Payment Successful")