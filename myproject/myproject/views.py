from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from myproject import settings
# import stripe

def home(request):
      return render(request,"index.html")
@login_required(login_url='login')
def bmi(request):
      return render(request,"bmi.html")

def about(request):
      return render(request,"about.html")
def services(request):
      return render(request,"services.html")
def blog(request):
      return render(request,"blog.html")
@login_required(login_url='login')
def blogdetails(request):
      return render(request,"blogdetails.html")
def gallery(request):
      return render(request,"gallery.html")
def contact(request):
      return render(request,"contact.html")
def chatbot(request):
      return render(request,"chatbot.html")
@login_required(login_url='login')
def HomeAFP(request):
      return render(request,"HomeAFP.html")



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

      

