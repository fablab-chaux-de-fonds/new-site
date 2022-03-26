import stripe
import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView


from accounts.models import Profile

class SubscriptionUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "payments/subscription_update.html"

class SubscriptionUpdateSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "payments/subscription_update_success.html"

class SubscriptionUpdateCancelView(LoginRequiredMixin, TemplateView):
    template_name = "payments/subscription_update_cancel.html"

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)

class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        YOUR_DOMAIN =  request.scheme + '://' + Site.objects.get_current().domain + '/'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                    'price_data': {
                        'currency': settings.STRIPE_CURRENCY,
                        'unit_amount': request.user.profile.subscription.subscription_category.price * 100, # stripe use cents
                        'product_data': {
                            'name': request.user.profile.subscription.subscription_category.title,
                            'images': [
                                "https://www.fablab-chaux-de-fonds.ch/assets/fablab-logo-officiel-ddbeac0f8738a60507bd2441b7bc3bc9.svg"
                            ]
                        },
                    },
                    'quantity': 1,
                    },
                ],
                metadata = {
                    'profile_id': request.user.profile.id
                },
                payment_method_types=['card'],
                mode='payment',
                success_url=YOUR_DOMAIN + 'payments/subscription-update-success/',
                cancel_url=YOUR_DOMAIN + 'payments/subscription-update-cancel/',
                customer_email=request.user.email,
            )
        except Exception as e:
            return str(e)
        return redirect(checkout_session.url, code=303)


# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    fulfill_order(session, request)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(session, request):
    customer_email = session['customer_details']['email']
    profile = Profile.objects.get(pk=session['metadata']["profile_id"])
    end_updated = max(datetime.date.today(), profile.subscription.end) + datetime.timedelta(days=profile.subscription.subscription_category.duration)
    profile.subscription.end = end_updated
    profile.save()

    context = {
        'profile': profile
    }

    html_message = render_to_string('accounts/email/subscription_updated.html', context)
    send_mail(
        subject=_("Your subsription has been updated successfully"),
        message="Your subsription has been updated successfully",
        from_email = None,
        recipient_list=[customer_email],
        html_message=html_message
    )