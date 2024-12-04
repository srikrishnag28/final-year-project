from django.shortcuts import render, redirect
from .models import *
from .forms import Criteria_4_1_1Form
# Create your views here.


def criteria_4_1_1_form(request):
    if request.method == 'POST':
        form = Criteria_4_1_1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('criteria_4_1_1')  # Redirect to a success page after form submission
    else:
        form = Criteria_4_1_1Form()

    return render(request, 'form/criteria_4_1_1.html', {'form': form})


from .models import Criteria_4_1_1


def criteria_4_1_1(request):
    criteria_data = Criteria_4_1_1.objects.all()

    if not criteria_data:  # If the queryset is empty
        context = {'no_data': True}
    else:
        context = {'criteria_data': criteria_data[0]}
    print(context)
    return render(request, 'table/criteria_4_1_1.html', context)

