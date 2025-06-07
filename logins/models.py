from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('JOURNAL TEAM', 'JOURNAL TEAM'),
        ('RESEARCH WORK DEVELOPMENT TEAM', 'RESEARCH WORK DEVELOPMENT TEAM'),
        ('SOFTWARE PROJECT DEVELOPMENT TEAM', 'SOFTWARE PROJECT DEVELOPMENT TEAM'),
        ('HARDWARE PROJECT DEVELOPMENT TEAM', 'HARDWARE PROJECT DEVELOPMENT TEAM'),
        ('TECHNICAL TEAM', 'TECHNICAL TEAM'),
        ('ADMIN TEAM', 'ADMIN TEAM'),
    ]

    BRANCH_CHOICES = [
        ('NAGERCOIL', 'NAGERCOIL'),
        ('TIRUNELVELI', 'TIRUNELVELI'),
        ('CHENNAI', 'CHENNAI'),
        ('PUDUKOTTAI', 'PUDUKOTTAI'),
        
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    is_approved = models.BooleanField(default=False)  # ✅ New field for admin approval 

    def __str__(self):
        return f"{self.username} - {self.department} - {self.branch} - {'Approved' if self.is_approved else 'Pending'}"



class PurchaseOrder(models.Model):
    BRANCH_CHOICES = [
        ('NAGERCOIL', 'NAGERCOIL'),
        ('TIRUNELVELI', 'TIRUNELVELI'),
        ('CHENNAI', 'CHENNAI'),
        ('PUDUKOTTAI', 'PUDUKOTTAI'),
        
    ]

    date = models.DateField()
    po_no = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    dealer = models.CharField(max_length=100)
    material_received_on = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.po_no} - {self.branch}"

class Dealer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# models.py
class DealerPurchaseOrder(models.Model):
    BRANCH_CHOICES = [
        ('NAGERCOIL', 'NAGERCOIL'),
        ('TIRUNELVELI', 'TIRUNELVELI'),
        ('CHENNAI', 'CHENNAI'),
        ('PUDUKOTTAI', 'PUDUKOTTAI'),
        
    ]

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    date = models.DateField()
    po_no = models.CharField(max_length=50)
    abt_branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    material_received_on = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50,default='null')
    gst_bill_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.po_no} - {self.dealer.name}"



class DealerPayment(models.Model):
    order = models.ForeignKey(DealerPurchaseOrder, related_name="payments", on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.amount}"




class AbstractPhdRegistration(models.Model):
    date = models.DateField()
    reg_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phd_type = models.CharField(max_length=100)
    college_university = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_balance = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = [
        ('REGISTERED', 'REGISTERED'),
        ('INPROGRESS', 'IN PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
    ]
    status=models.CharField(max_length=50, choices=STATUS,default=0)

    class Meta:
        abstract = True  # This makes it an abstract base model

    def __str__(self):
        return f"{self.name} - {self.reg_code}"


class NagercoilPhdRegistration(AbstractPhdRegistration):
    class Meta:
        verbose_name = "Nagercoil PHD Registration"
        verbose_name_plural = "Nagercoil PHD Registrations"

class TirunelveliPhdRegistration(AbstractPhdRegistration):
    class Meta:
        verbose_name = "Tirunelveli PHD Registration"
        verbose_name_plural = "Tirunelveli PHD Registrations"

class PudukottaiPhdRegistration(AbstractPhdRegistration):
    class Meta:
        verbose_name = "Pudukottai PHD Registration"
        verbose_name_plural = "Pudukottai PHD Registrations"

class ChennaiPhdRegistration(AbstractPhdRegistration):
    class Meta:
        verbose_name = "Chennai PHD Registration"
        verbose_name_plural = "Chennai PHD Registrations"

class AbstractProjectRegistration(models.Model):
    date = models.DateField()
    reg_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    college_university = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    STATUS = [
        ('REGISTERED', 'REGISTERED'),
        ('INPROGRESS', 'IN PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
    ]
    status=models.CharField(max_length=50, choices=STATUS,default=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True  # This makes it an abstract base model

    def __str__(self):
        return f"{self.name} - {self.reg_code} - {self.project_type}"

# Individual Models for Each Branch
class NagercoilProjectRegistration(AbstractProjectRegistration):
    class Meta:
        verbose_name = "Nagercoil Project Registration"
        verbose_name_plural = "Nagercoil Project Registrations"

class TirunelveliProjectRegistration(AbstractProjectRegistration):
    class Meta:
        verbose_name = "Tirunelveli Project Registration"
        verbose_name_plural = "Tirunelveli Project Registrations"

class PudukottaiProjectRegistration(AbstractProjectRegistration):
    class Meta:
        verbose_name = "Pudukottai Project Registration"
        verbose_name_plural = "Pudukottai Project Registrations"

class ChennaiProjectRegistration(AbstractProjectRegistration):
    class Meta:
        verbose_name = "Chennai Project Registration"
        verbose_name_plural = "Chennai Project Registrations"


class AbstractInternshipRegistration(models.Model):
    date = models.DateField()
    reg_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    internship_type = models.CharField(max_length=100)
    college_university = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.reg_code}"

class NagercoilInternshipRegistration(AbstractInternshipRegistration):
    class Meta:
        verbose_name = "Nagercoil Internship Registration"
        verbose_name_plural = "Nagercoil Internship Registrations"

class TirunelveliInternshipRegistration(AbstractInternshipRegistration):
    class Meta:
        verbose_name = "Tirunelveli Internship Registration"
        verbose_name_plural = "Tirunelveli Internship Registrations"

class PudukottaiInternshipRegistration(AbstractInternshipRegistration):
    class Meta:
        verbose_name = "Pudukottai Internship Registration"
        verbose_name_plural = "Pudukottai Internship Registrations"

class ChennaiInternshipRegistration(AbstractInternshipRegistration):
    class Meta:
        verbose_name = "Chennai Internship Registration"
        verbose_name_plural = "Chennai Internship Registrations"

class AbstractPublicationRegistration(models.Model):
    date = models.DateField()
    reg_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    publication_type = models.CharField(max_length=100)
    college_university = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.reg_code}"

class NagercoilPublicationRegistration(AbstractPublicationRegistration):
    class Meta:
        verbose_name = "Nagercoil Publication Registration"
        verbose_name_plural = "Nagercoil Publication Registrations"

class TirunelveliPublicationRegistration(AbstractPublicationRegistration):
    class Meta:
        verbose_name = "Tirunelveli Publication Registration"
        verbose_name_plural = "Tirunelveli Publication Registrations"

class PudukottaiPublicationRegistration(AbstractPublicationRegistration):
    class Meta:
        verbose_name = "Pudukottai Publication Registration"
        verbose_name_plural = "Pudukottai Publication Registrations"

class ChennaiPublicationRegistration(AbstractPublicationRegistration):
    class Meta:
        verbose_name = "Chennai Publication Registration"
        verbose_name_plural = "Chennai Publication Registrations"

class AbstractDailyIncomeExpenditure(models.Model):
    date = models.DateField()
    description = models.TextField()
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pvc_no = models.CharField(max_length=100, default="N/A")  # PVC No as manually entered text
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Allow manual entry

    class Meta:
        abstract = True  # Abstract model


class NagercoilDailyIncomeExpenditure(AbstractDailyIncomeExpenditure):
    class Meta:
        verbose_name = "Nagercoil Daily Income Expenditure"
        verbose_name_plural = "Nagercoil Daily Income Expenditures"

class TirunelveliDailyIncomeExpenditure(AbstractDailyIncomeExpenditure):
    class Meta:
        verbose_name = "Tirunelveli Daily Income Expenditure"
        verbose_name_plural = "Tirunelveli Daily Income Expenditures"

class PudukottaiDailyIncomeExpenditure(AbstractDailyIncomeExpenditure):
    class Meta:
        verbose_name = "Pudukottai Daily Income Expenditure"
        verbose_name_plural = "Pudukottai Daily Income Expenditures"

class ChennaiDailyIncomeExpenditure(AbstractDailyIncomeExpenditure):
    class Meta:
        verbose_name = "Chennai Daily Income Expenditure"
        verbose_name_plural = "Chennai Daily Income Expenditures"


class AbstractPaymentVoucher(models.Model):
    date = models.DateField()
    vc_no = models.CharField(max_length=100, unique=True)
    purpose = models.TextField()
    online_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Online (A/C)")
    cash_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cash")

    class Meta:
        abstract = True  # Abstract base model

    def __str__(self):
        return f"VC No: {self.vc_no} - {self.purpose}"


# Branch-Specific Models
class NagercoilPaymentVoucher(AbstractPaymentVoucher):
    class Meta:
        verbose_name = "Nagercoil Payment Voucher"
        verbose_name_plural = "Nagercoil Payment Vouchers"

class TirunelveliPaymentVoucher(AbstractPaymentVoucher):
    class Meta:
        verbose_name = "Tirunelveli Payment Voucher"
        verbose_name_plural = "Tirunelveli Payment Vouchers"

class PudukottaiPaymentVoucher(AbstractPaymentVoucher):
    class Meta:
        verbose_name = "Pudukottai Payment Voucher"
        verbose_name_plural = "Pudukottai Payment Vouchers"

class ChennaiPaymentVoucher(AbstractPaymentVoucher):
    class Meta:
        verbose_name = "Chennai Payment Voucher"
        verbose_name_plural = "Chennai Payment Vouchers"



class AbstractBill(models.Model):
    date = models.DateField()
    bill_number = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cash_received = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    MODE_CHOICES = [
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE'),
        # ('Completed', 'Completed'),
    ]
    modeofpayment = models.CharField(max_length=50, choices=MODE_CHOICES)
    # online_received = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # balance = models.DecimalField(max_digits=10, decimal_places=2)
    # payment_status = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.bill_number}"

class NagercoilPhdBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil PHD Bill"
        verbose_name_plural = "Nagercoil PHD Bills"

class TirunelveliPhdBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli PHD Bill"
        verbose_name_plural = "Tirunelveli PHD Bills"

class PudukottaiPhdBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai PHD Bill"
        verbose_name_plural = "Pudukottai PHD Bills"

class ChennaiPhdBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai PHD Bill"
        verbose_name_plural = "Chennai PHD Bills"

class NagercoilInternshipBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil Internship Bill"
        verbose_name_plural = "Nagercoil Internship Bills"

class TirunelveliInternshipBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli Internship Bill"
        verbose_name_plural = "Tirunelveli Internship Bills"

class PudukottaiInternshipBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai Internship Bill"
        verbose_name_plural = "Pudukottai Internship Bills"

class ChennaiInternshipBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai Internship Bill"
        verbose_name_plural = "Chennai Internship Bills"

class NagercoilProjectBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil Project Bill"
        verbose_name_plural = "Nagercoil Project Bills"

class TirunelveliProjectBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli Project Bill"
        verbose_name_plural = "Tirunelveli Project Bills"

class PudukottaiProjectBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai Project Bill"
        verbose_name_plural = "Pudukottai Project Bills"

class ChennaiProjectBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai Project Bill"
        verbose_name_plural = "Chennai Project Bills"

class NagercoilJournalBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil Journal Bill"
        verbose_name_plural = "Nagercoil Journal Bills"

class TirunelveliJournalBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli Journal Bill"
        verbose_name_plural = "Tirunelveli Journal Bills"

class PudukottaiJournalBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai Journal Bill"
        verbose_name_plural = "Pudukottai Journal Bills"

class ChennaiJournalBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai Journal Bill"
        verbose_name_plural = "Chennai Journal Bills"

class NagercoilSharingBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil Sharing Bill"
        verbose_name_plural = "Nagercoil Sharing Bills"

class TirunelveliSharingBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli Sharing Bill"
        verbose_name_plural = "Tirunelveli Sharing Bills"

class PudukottaiSharingBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai Sharing Bill"
        verbose_name_plural = "Pudukottai Sharing Bills"

class ChennaiSharingBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai Sharing Bill"
        verbose_name_plural = "Chennai Sharing Bills"

class NagercoilPatentBill(AbstractBill):
    class Meta:
        verbose_name = "Nagercoil Patent Bill"
        verbose_name_plural = "Nagercoil Patent Bills"

class TirunelveliPatentBill(AbstractBill):
    class Meta:
        verbose_name = "Tirunelveli Patent Bill"
        verbose_name_plural = "Tirunelveli Patent Bills"

class PudukottaiPatentBill(AbstractBill):
    class Meta:
        verbose_name = "Pudukottai Patent Bill"
        verbose_name_plural = "Pudukottai Patent Bills"

class ChennaiPatentBill(AbstractBill):
    class Meta:
        verbose_name = "Chennai Patent Bill"
        verbose_name_plural = "Chennai Patent Bills"

class WorkStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    date = models.DateField(auto_now_add=True)
    work_code = models.CharField(max_length=50)
    work_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    work_status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.work_code}"
