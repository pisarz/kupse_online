from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .forms import CheckoutForm
from .models import Item, OrderItem, Order, BillingAddress


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add funcionality for these fields
                # same_shipping_address = form.cleaned_data.get(
                #     'same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # TODO: add redirect to the selected payment option
                return redirect('core:checkout')
            messages.warning(self.request, "Failed checkout")
            return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.info(self.request, "Nie posiadasz aktywnego zamówienia.")
            return redirect("core:order_summary")
        


class HomeView(ListView):
    model = Item
    paginate_by = 8
    ordering = ['-id']
    template_name = "home.html"


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "Nie posiadasz aktywnego zamówienia.")
            return redirect("/")


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        # if order.items.filter(item__slug=item.slug).exists():
        #     # order_item.quantity += 1
        #     order_item.save()
        #     messages.info(request, "Dodano jeszcze raz ten sam przemiot.")
        #     return redirect("core:order-summary")
        # else:
        if item.quantity > 0:
            order.items.add(order_item)
            item.quantity -= 1
            # if item.quantity < 1:
            #     item.is_visible = False
            item.save()
            messages.info(request, "Przedmiot został dodany do Twojego koszyka.")
            return redirect("core:order-summary")
        else:
            messages.warning(request, "Przedmiot nie jest obecnie dostępny.")
            return redirect("/")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        item.quantity -= 1
        item.save()
        messages.info(request, "Przedmiot został dodany do Twojego koszyka.")
        return redirect("core:order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                        item=item,
                        user=request.user,
                        ordered=False
            )[0]
            order_item.quantity = 1
            order_item.save()
            order.items.remove(order_item)
            item.quantity = 1
            # item.is_visible = True
            item.save()
            messages.info(request, "Przedmiot został usunięty z Twojego koszyka.")
            return redirect("core:order-summary")
        else:
            messages.info(request,
                          "Ten przedmiot nie znajdował się w Twoim koszyku.")
            return redirect("core:home")

    else:
        messages.info(request, "Nie posiadasz aktywnego zamówienia.")
        return redirect("core:home")


def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                        item=item,
                        user=request.user,
                        ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Ilość produktów została zaktualizowana.")
            return redirect("core:order-summary")
        else:
            messages.info(request,
                          "Ten przedmiot nie znajdował się w Twoim koszyku.")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "Nie posiadasz aktywnego zamówienia.")
        return redirect("core:product", slug=slug)
