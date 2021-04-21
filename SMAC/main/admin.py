from django.contrib import admin

# Register your models here.
from .models import Members
#admin.site.register(Members)
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'contact','join_date', 'flat_no', 'paid_upto', 'date_at')

from .models import expence
admin.site.register(expence)

from .models import Invoice
admin.site.register(Invoice)

from .models import Balance
#admin.site.register(Balance)
@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
  list_display = ('id','collection','this_month_collection','expence', 'this_month_expence','balance')

from .models import FestivalFunds
admin.site.register(FestivalFunds)

from .models import EmergencyFunds
admin.site.register(EmergencyFunds)

from .models import SpecialPurposeFunds
admin.site.register(SpecialPurposeFunds)