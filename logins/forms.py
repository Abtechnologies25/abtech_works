from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,SetPasswordForm
from .models import *

class UserRegisterForm(UserCreationForm):
    department = forms.ChoiceField(choices=User.DEPARTMENT_CHOICES, label="Department")
    branch = forms.ChoiceField(choices=User.BRANCH_CHOICES, label="Branch")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department', 'branch']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'department', 'branch']

class UserPasswordEditForm(SetPasswordForm):
    class Meta:
        model = User

class AbstractPhdRegistrationForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'reg_code', 'name', 'department', 'phd_type', 
                  'college_university', 'mobile_no', 'email_id','total_amount', 
                  'amount_paid', 'amount_balance','status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'email_id': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }

# Forms for each branch
class NagercoilPhdRegistrationForm(AbstractPhdRegistrationForm):
    class Meta(AbstractPhdRegistrationForm.Meta):
        model = NagercoilPhdRegistration

class TirunelveliPhdRegistrationForm(AbstractPhdRegistrationForm):
    class Meta(AbstractPhdRegistrationForm.Meta):
        model = TirunelveliPhdRegistration

class PudukottaiPhdRegistrationForm(AbstractPhdRegistrationForm):
    class Meta(AbstractPhdRegistrationForm.Meta):
        model = PudukottaiPhdRegistration

class ChennaiPhdRegistrationForm(AbstractPhdRegistrationForm):
    class Meta(AbstractPhdRegistrationForm.Meta):
        model = ChennaiPhdRegistration

class AbstractProjectRegistrationForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'reg_code', 'name', 'department', 'project_type', 
                  'college_university', 'mobile_no', 'email_id','total_amount',  
                  'amount_paid', 'amount_balance','status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'email_id': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'project_type': forms.TextInput(attrs={'placeholder': 'Enter project title'}),
        }

# Forms for each branch
class NagercoilProjectRegistrationForm(AbstractProjectRegistrationForm):
    class Meta(AbstractProjectRegistrationForm.Meta):
        model = NagercoilProjectRegistration

class TirunelveliProjectRegistrationForm(AbstractProjectRegistrationForm):
    class Meta(AbstractProjectRegistrationForm.Meta):
        model = TirunelveliProjectRegistration

class PudukottaiProjectRegistrationForm(AbstractProjectRegistrationForm):
    class Meta(AbstractProjectRegistrationForm.Meta):
        model = PudukottaiProjectRegistration

class ChennaiProjectRegistrationForm(AbstractProjectRegistrationForm):
    class Meta(AbstractProjectRegistrationForm.Meta):
        model = ChennaiProjectRegistration

class AbstractInternshipRegistrationForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'reg_code', 'name', 'department', 'internship_type', 
                  'college_university', 'mobile_no', 'email_id', 
                  'amount_paid', 'amount_balance']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'email_id': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }

class NagercoilInternshipRegistrationForm(AbstractInternshipRegistrationForm):
    class Meta(AbstractInternshipRegistrationForm.Meta):
        model = NagercoilInternshipRegistration

class TirunelveliInternshipRegistrationForm(AbstractInternshipRegistrationForm):
    class Meta(AbstractInternshipRegistrationForm.Meta):
        model = TirunelveliInternshipRegistration

class PudukottaiInternshipRegistrationForm(AbstractInternshipRegistrationForm):
    class Meta(AbstractInternshipRegistrationForm.Meta):
        model = PudukottaiInternshipRegistration

class ChennaiInternshipRegistrationForm(AbstractInternshipRegistrationForm):
    class Meta(AbstractInternshipRegistrationForm.Meta):
        model = ChennaiInternshipRegistration

class AbstractPublicationRegistrationForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'reg_code', 'name', 'department', 'publication_type', 
                  'college_university', 'mobile_no', 'email_id', 'amount_paid', 'amount_balance']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'email_id': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }

class NagercoilPublicationRegistrationForm(AbstractPublicationRegistrationForm):
    class Meta(AbstractPublicationRegistrationForm.Meta):
        model = NagercoilPublicationRegistration

class TirunelveliPublicationRegistrationForm(AbstractPublicationRegistrationForm):
    class Meta(AbstractPublicationRegistrationForm.Meta):
        model = TirunelveliPublicationRegistration

class PudukottaiPublicationRegistrationForm(AbstractPublicationRegistrationForm):
    class Meta(AbstractPublicationRegistrationForm.Meta):
        model = PudukottaiPublicationRegistration

class ChennaiPublicationRegistrationForm(AbstractPublicationRegistrationForm):
    class Meta(AbstractPublicationRegistrationForm.Meta):
        model = ChennaiPublicationRegistration


class AbstractDailyIncomeExpenditureForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'description', 'income', 'expense', 'pvc_no', 'balance']  # Include balance
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description', 'rows': 2}),
            'income': forms.NumberInput(attrs={'placeholder': 'Enter income'}),
            'expense': forms.NumberInput(attrs={'placeholder': 'Enter expense'}),
            'pvc_no': forms.TextInput(attrs={'placeholder': 'Enter PVC No'}),
            'balance': forms.NumberInput(attrs={'placeholder': 'Enter balance manually'}),  # Manual input enabled
        }


# Forms for each branch
class NagercoilDailyIncomeExpenditureForm(AbstractDailyIncomeExpenditureForm):
    class Meta(AbstractDailyIncomeExpenditureForm.Meta):
        model = NagercoilDailyIncomeExpenditure

class TirunelveliDailyIncomeExpenditureForm(AbstractDailyIncomeExpenditureForm):
    class Meta(AbstractDailyIncomeExpenditureForm.Meta):
        model = TirunelveliDailyIncomeExpenditure

class PudukottaiDailyIncomeExpenditureForm(AbstractDailyIncomeExpenditureForm):
    class Meta(AbstractDailyIncomeExpenditureForm.Meta):
        model = PudukottaiDailyIncomeExpenditure

class ChennaiDailyIncomeExpenditureForm(AbstractDailyIncomeExpenditureForm):
    class Meta(AbstractDailyIncomeExpenditureForm.Meta):
        model = ChennaiDailyIncomeExpenditure



class AbstractPaymentVoucherForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'vc_no', 'purpose', 'online_payment', 'cash_payment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'purpose': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter purpose'}),
            'online_payment': forms.NumberInput(attrs={'placeholder': 'Enter Online Payment'}),
            'cash_payment': forms.NumberInput(attrs={'placeholder': 'Enter Cash Payment'}),
        }

# Forms for each branch
class NagercoilPaymentVoucherForm(AbstractPaymentVoucherForm):
    class Meta(AbstractPaymentVoucherForm.Meta):
        model = NagercoilPaymentVoucher

class TirunelveliPaymentVoucherForm(AbstractPaymentVoucherForm):
    class Meta(AbstractPaymentVoucherForm.Meta):
        model = TirunelveliPaymentVoucher

class PudukottaiPaymentVoucherForm(AbstractPaymentVoucherForm):
    class Meta(AbstractPaymentVoucherForm.Meta):
        model = PudukottaiPaymentVoucher

class ChennaiPaymentVoucherForm(AbstractPaymentVoucherForm):
    class Meta(AbstractPaymentVoucherForm.Meta):
        model = ChennaiPaymentVoucher


DATE_WIDGET = forms.DateInput(attrs={'type': 'date'})

class BaseBillForm(forms.ModelForm):
    class Meta:
        fields = [
            'date', 'bill_number', 'registration_number', 'name', 
            'cash_received', 'modeofpayment'
        ]
        widgets = {
            'date': DATE_WIDGET
        }

# Dynamically generate forms
for model in [NagercoilPhdBill, NagercoilInternshipBill, NagercoilProjectBill, NagercoilJournalBill, NagercoilSharingBill, NagercoilPatentBill,
              TirunelveliPhdBill, TirunelveliInternshipBill, TirunelveliProjectBill, TirunelveliJournalBill, TirunelveliSharingBill, TirunelveliPatentBill,
              PudukottaiPhdBill, PudukottaiInternshipBill, PudukottaiProjectBill, PudukottaiJournalBill, PudukottaiSharingBill, PudukottaiPatentBill,
              ChennaiPhdBill, ChennaiInternshipBill, ChennaiProjectBill, ChennaiJournalBill, ChennaiSharingBill, ChennaiPatentBill]:
    
    form_class = type(f"{model.__name__}Form", (BaseBillForm,), {'Meta': type('Meta', (), {'model': model, **BaseBillForm.Meta.__dict__})})
    globals()[form_class.__name__] = form_class

class WorkStatusForm(forms.ModelForm):
    class Meta:
        model = WorkStatus
        exclude = ['user', 'branch', 'department', 'date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }