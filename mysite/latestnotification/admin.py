from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin  #added
from latestnotification.models import BankModel

# Register your models here.

class BankAdmin(PlaceholderAdminMixin,admin.ModelAdmin):
    list_display = ['post_date','bank_name','post_name','qualification','advt_no','last_date']

admin.site.register(BankModel,BankAdmin)
