
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


class TankInformationForm(forms.Form):
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


class ProcessConditionsForm(forms.Form):
    TEMP_UNITS = (
        ('C', 'F'),
        ('F', 'F'),
        ('K', 'K')
    )

    PRESSURE_UNITS = (
        ('PSIG', 'PSIG'),
        ('BARG', 'BARG')
    )

    STATES = (
        ('LIQUID', 'Liquid'),
        ('POWDER', 'Powder'),
        ('PASTE', 'Paste'),
        ('SLUDGE', 'Sludge')
    )

    CHARACTERISTICS = (
        ('CLEAN', 'Clean'),
        ('COATS', 'Coats'),
        ('CRYSTALIZES', 'Crystalizes'),
        ('Deposits', 'Deposits'),
        ('DUSTY', 'Dusty')
    )

    SURFACES = (
        ('SMOOTH', 'Smooth'),
        ('AGITATED', 'Agitated'),
        ('FOAMS', 'Foams')
    )

    medium_min_temp = forms.IntegerField()
    medium_min_unit = forms.ChoiceField(widget=forms.Select, choices=TEMP_UNITS)
    medium_max_temp = forms.IntegerField()
    medium_max_unit = forms.ChoiceField(widget=forms.Select, choices=TEMP_UNITS)

    vessel_min_pressure = forms.IntegerField()
    vessel_min_unit = forms.ChoiceField(widget=forms.Select, choices=PRESSURE_UNITS)
    vessel_max_pressure = forms.IntegerField()
    vessel_max_unit = forms.ChoiceField(widget=forms.Select, choices=PRESSURE_UNITS)

    dielectric_top = forms.IntegerField()
    dielectric_bottom = forms.IntegerField()

    medium_name = forms.CharField(max_length=255)
    media_state = forms.ChoiceField(widget=forms.Select, choices=STATES)
    media_characteristics = forms.ChoiceField(widget=forms.Select, choices=CHARACTERISTICS)
    liquid_surface = forms.ChoiceField(widget=forms.Select, choices=SURFACES)

    foam_description = forms.TextField(required=False)


class InstrumentSpecificsForm(forms.Form):
    HOUSING = (
        ('INTEGRAL', 'Integral'),
        ('REMOTE', 'Remote')
    )

    CLASSIFICATION = (
        ('IS(C1D1)', 'IS(C1D1)'),
        ('NI(C1D2)', 'NI(C1D2)'),
        ('XP(C1D1)', 'XP(C1D1)'),
        ('SIL2', 'SIL2')
    )

    POWER = (
        ('24VDC', '24 vdc'),
        ('100VAC', '100 vac'),
        ('OTHER', 'Other')
    )

    OUTPUTS = (
        ('4-20MA HART', '4-20ma HART'),
        ('FF', 'FF'),
        ('OTHER', 'Other')
    )

    ALARM_OPTIONS = (
        ('H', 'High'),
        ('L', 'Low')
    )

    PUMP_CONTROL = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    power_available = forms.ChoiceField(widget=forms.Select, choices=POWER)
    power_outputs = forms.ChoiceField(widget=forms.Select, choices=OUTPUTS)
    alarms = forms.ChoiceField(widget=forms.Select, choices=ALARM_OPTIONS)
    alarms_description = forms.TextField(required=False)
    pump_options = forms.ChoiceField(widget=forms.Select, choices=PUMP_CONTROL)
    pump_options_description = forms.TextField(required=False)
    area_classification = forms.ChoiceField(widget=forms.Select, choices=CLASSIFICATION)
    electrical_housing = forms.ChoiceField(widget=forms.Select, choices=HOUSING)
    special_requirements = forms.TextField()
