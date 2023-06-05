# from django.shortcuts import render
# from django.conf import settings
# import stripe
# def payment(request,amount):
#     context = {
#         'amount': amount
#     }
#     return render(request,'payment.html',context)
# stripe.api_key=settings.STRIPE_SECRET_KEY
from django.shortcuts import render
from django.conf import settings
from myproject import settings
import stripe

def payment(request, amount):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Retrieve the payment token from the request
        token = request.POST.get('stripeToken')

        try:
            # Create a charge using the Stripe API
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Amount in cents
                currency='usd',
                source=token,
                description='Payment for your purchase'
            )

            # Payment was successful
            return render(request, 'payment_success.html')

        except stripe.error.CardError as e:
            # Payment was declined or failed
            error_message = e.error.message
            context = {
                'amount': amount,
                'error_message': error_message
            }
            return render(request, 'payment.html', context)

    context = {
        'amount': amount,
        'publishable_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'payment.html', context)
