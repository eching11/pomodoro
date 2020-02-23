from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class EditPomodoroForm(forms.Form):
    edit_minutes = forms.IntegerField(help_text="Enter a number between 25 and 50 (default 25).")
    
    def clean_edit_minutes(self):
        data = self.cleaned_data['edit_minutes']
        
        # Check if number is not less than 25
        if data < 25:
            raise ValidationError(_('Invalid number - must be be between 25 - 50'))
        elif data > 50:
            raise ValidationError(_('Invalid number - must be between 25 - 50'))    
        # Check if number is in allowed range
        else:
            return data