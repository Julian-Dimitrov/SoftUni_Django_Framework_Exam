from django import forms
from .models import Tool


class AddToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = (
            'tool_photo',
            'name',
            'description',
            'tool_country',
            'tool_city',
            'tool_price'
        )
