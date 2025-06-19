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


admin.site.register(NAGERCOILPHDBILL)
admin.site.register(TIRUNELVELIPHDBILL)
admin.site.register(PUDUKOTTAIPHDBILL)
admin.site.register(CHENNAIPHDBILL)

admin.site.register(NAGERCOILINTERNSHIPBILL)
admin.site.register(TIRUNELVELIINTERNSHIPBILL)
admin.site.register(PUDUKOTTAIINTERNSHIPBILL)
admin.site.register(CHENNAIINTERNSHIPBILL)

admin.site.register(NAGERCOILPROJECTBILL)
admin.site.register(TIRUNELVELIPROJECTBILL)
admin.site.register(PUDUKOTTAIPROJECTBILL)
admin.site.register(CHENNAIPROJECTBILL)

admin.site.register(NAGERCOILJOURNALBILL)
admin.site.register(TIRUNELVELIJOURNALBILL)
admin.site.register(PUDUKOTTAIJOURNALBILL)
admin.site.register(CHENNAIJOURNALBILL)

admin.site.register(NAGERCOILSHARINGBILL)
admin.site.register(TIRUNELVELISHARINGBILL)
admin.site.register(PUDUKOTTAISHARINGBILL)
admin.site.register(CHENNAISHARINGBILL)

admin.site.register(NAGERCOILPATENTBILL)
admin.site.register(TIRUNELVELIPATENTBILL)
admin.site.register(PUDUKOTTAIPATENTBILL)
admin.site.register(CHENNAIPATENTBILL)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'department', 'branch', 'is_active')  # ✅ Replaced 'role' with 'department'
    list_filter = ('department', 'branch', 'is_active')  # ✅ Replaced 'role' with 'department'
    search_fields = ('username', 'email')
    ordering = ('username',)



# Register User model in the Django Admin panel
admin.site.register(User, CustomUserAdmin)