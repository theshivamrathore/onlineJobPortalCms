from django.db import models
from cms.models.fields import PlaceholderField  #added

# Create your models here.


def my_placeholder_slotname(instance): #added
    return 'placeholder_name'
class BankModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    bank_name = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)
    my_placeholder = PlaceholderField(my_placeholder_slotname)  #added

    def __str__(self):
        return self.bank_name
