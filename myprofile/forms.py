from django import forms
from .models import Career
from .models import License
from .models import Portfolio
from .models import Profile

# 날짜 입력받는 포맷
class DateInput(forms.DateInput):
    input_type = 'date'

# 경력사항 폼
class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('start','end','office','position','text')
        widgets = {
            'start' : DateInput(),
            'end' : DateInput(),
        }

# 자격사항 폼    
class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ('date','license_name','license_organ')
        widgets = {
            'date' : DateInput(),
        }