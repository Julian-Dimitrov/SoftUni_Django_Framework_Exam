from django import forms


class SearchForm(forms.Form):
    SEARCH_CHOICES = (
        ('name', 'Name'),
        ('tool_country', 'Country'),
        ('tool_city', 'City')
    )

    search = forms.CharField(
        required=False
    )

    filter_field = forms.ChoiceField(
        choices=SEARCH_CHOICES
    )
