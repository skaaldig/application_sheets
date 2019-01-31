
from django import forms


class ContactInfoForm(forms.Form):
    name = forms.CharField(max_length=150)
    company = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    state = forms.CharField(max_length=2)
    city = forms.CharField(max_length=150)
    zip_code = forms.CharField(max_length=5)


class GeneralInfoForm(forms.Form):
    MEASURING_PRINCIPAL = (
        ('FMCW', 'FMCW Radar'),
        ('TDR', 'TDR Radar'),
        ('MBLI', 'Magnetic Bypass Level Indicator'),
        ('PRESSURE', 'Pressure')
    )

    MEASUREMENT_TYPE = (
        ('NC', 'Non-Contacting Level'),
        ('C', 'Contacting Level'),
        ('LI', 'Level & Interface Measurement')
    )

    UNITS = (
        ('FT', 'FT'),
        ('IN', 'IN')
    )

    tag_number = forms.CharField(max_length=255)
    measurement_principal = forms.ChoiceField(widget=forms.Select, choices=MEASURING_PRINCIPAL)
    measurement_type = forms.ChoiceField(widget=forms.Select, choices=MEASUREMENT_TYPE)
    chamber_height = forms.IntegerField()
    chamber_width = forms.IntegerField()
    width_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    height_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    chamber_material = forms.CharField(max_length=255)


class ProcessConditionsForm(forms.Form):
    UNITS = (
        ('FT', 'FT'),
        ('IN', 'IN')
    )

    vessel_height = forms.IntegerField()
    vessel_height_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    vessel_width = forms.IntegerField()
    vessel_width_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    max_fluid = forms.IntegerField()
    max_fluid_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    min_fluid = forms.IntegerField()
    min_fluid_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    process_connection = forms.CharField(max_length=255)
    nozzel_diameter = forms.IntegerField()
    nozzel_diameter_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    nozzel_height = forms.IntegerField()
    nozzel_height_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    nozzel_center_to_wall = forms.IntegerField()
    nozzel_center_to_wall_unit = forms.ChoiceField(widget=forms.Select, choices=UNITS)
    alt_process_connection = forms.CharField(max_length=255)

class InstrumentSpecsForm(forms.Form):
    pass
