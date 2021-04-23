from django import forms
from .models import UserCapture, CellphoneCapture


class UserCaptureForm(forms.ModelForm):

    class Meta:
        model = UserCapture
        fields = (
            'name',
            'email',
            'employee_number',
            'department'
        )


class CellphoneCaptureForm(forms.ModelForm):

    class Meta:
        model = CellphoneCapture
        fields = (
            'phone_manufacturer',
            'phone_model',
            'imei_number',
            'sim_number',
            'phone_number',
        )
