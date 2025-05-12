from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(NagercoilPhdRegistration)
admin.site.register(TirunelveliPhdRegistration)
admin.site.register(PudukottaiPhdRegistration)
admin.site.register(ChennaiPhdRegistration)

admin.site.register(NagercoilProjectRegistration)
admin.site.register(TirunelveliProjectRegistration)
admin.site.register(PudukottaiProjectRegistration)
admin.site.register(ChennaiProjectRegistration)

admin.site.register(NagercoilInternshipRegistration)
admin.site.register(TirunelveliInternshipRegistration)
admin.site.register(PudukottaiInternshipRegistration)
admin.site.register(ChennaiInternshipRegistration)

admin.site.register(NagercoilPublicationRegistration)
admin.site.register(TirunelveliPublicationRegistration)
admin.site.register(PudukottaiPublicationRegistration)
admin.site.register(ChennaiPublicationRegistration)

admin.site.register(NagercoilPaymentVoucher)
admin.site.register(TirunelveliPaymentVoucher)
admin.site.register(PudukottaiPaymentVoucher)
admin.site.register(ChennaiPaymentVoucher)


admin.site.register(NagercoilPhdBill)
admin.site.register(TirunelveliPhdBill)
admin.site.register(PudukottaiPhdBill)
admin.site.register(ChennaiPhdBill)

admin.site.register(NagercoilInternshipBill)
admin.site.register(TirunelveliInternshipBill)
admin.site.register(PudukottaiInternshipBill)
admin.site.register(ChennaiInternshipBill)

admin.site.register(NagercoilProjectBill)
admin.site.register(TirunelveliProjectBill)
admin.site.register(PudukottaiProjectBill)
admin.site.register(ChennaiProjectBill)

admin.site.register(NagercoilJournalBill)
admin.site.register(TirunelveliJournalBill)
admin.site.register(PudukottaiJournalBill)
admin.site.register(ChennaiJournalBill)

admin.site.register(NagercoilSharingBill)
admin.site.register(TirunelveliSharingBill)
admin.site.register(PudukottaiSharingBill)
admin.site.register(ChennaiSharingBill)

admin.site.register(NagercoilPatentBill)
admin.site.register(TirunelveliPatentBill)
admin.site.register(PudukottaiPatentBill)
admin.site.register(ChennaiPatentBill)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'department', 'branch', 'is_active')  # ✅ Replaced 'role' with 'department'
    list_filter = ('department', 'branch', 'is_active')  # ✅ Replaced 'role' with 'department'
    search_fields = ('username', 'email')
    ordering = ('username',)



# Register User model in the Django Admin panel
admin.site.register(User, CustomUserAdmin)