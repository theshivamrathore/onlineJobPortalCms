from django.shortcuts import render
from latestnotification.models import BankModel

# Create your views here.

def latestnotificationview(request):
    bank_data = BankModel.objects.all()

    context = {'bank_data':bank_data}

    return render(request,'latestnotification.html',context=context)
