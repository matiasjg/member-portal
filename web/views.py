from core.models import Member
from core.models import Payment
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.db.models import Q

from .forms import PayForm, SignupForm


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return Member.objects.order_by('-joined_on')[:5]

class DetailView(generic.DetailView):
    model = Member
    template_name = 'member.html'

class ResultsView(generic.ListView):
    model = Member
    template_name = 'members.html'
    context_object_name = 'member_list'
    paginate_by = 10

    def get_queryset(self):
        try:
            search = self.request.GET.get('search')
        except:
            search = None

        if search:
            object_list = self.model.objects.filter(
                Q(email__icontains = search) |
                Q(first_name__icontains = search)
            )
        else:
            object_list = self.model.objects.all()

        return object_list

def signup(request):
    errors = ""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            # validate existing member
            member_email = form.cleaned_data['member_email']
            member_fname = form.cleaned_data['member_fname']
            member_lname = form.cleaned_data['member_lname']
            plan         = form.cleaned_data['plan']

            memberValidate = Member.objects.filter(email=member_email)

            if memberValidate:
                errors = "Email already registered."
            else:
                member = Member(
                    email      = member_email,
                    first_name = member_fname,
                    last_name  = member_lname,
                    plan       = plan,
                )
                member.save()

                return render(request, 'signup.html', {'message': 'Welcome!'})
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form, 'errors': errors})

# Register a new payment (no payment gateway implemented, it's just a simple POST)
def pay(request):
    errors = ""
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():

            # validate existing member
            member_email   = form.cleaned_data['member_email']
            payment_amount = form.cleaned_data['payment_amount']
            member         = Member.objects.filter(email=member_email)

            if not member:
                errors = "Invalid Member."
            else:
                payment = Payment(member=member[0], amount=payment_amount, )
                payment.save()

                return render(request, 'pay.html', {'message': 'Payment added!'})
    else:
        form = PayForm()

    return render(request, 'pay.html', {'form': form, 'errors': errors})
