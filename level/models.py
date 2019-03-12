from django.db import models
from customers.models import CustomerInfo


LENGTH_UNITS = (
    ('FT', 'FT'),
    ('IN', 'IN')
)

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

TEMP_UNITS = (
    ('C', 'C'),
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


class GeneralInfo(models.Model):
    tag_number = models.CharField(max_length=75)
    measurement_principal = models.CharField(max_length=25)
    measurement_type = models.CharField(max_length=3, choices=MEASUREMENT_TYPE)
    bypass_chamber_height = models.IntegerField()
    height_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    bypass_chamber_width = models.IntegerField()
    width_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    chamber_material = models.CharField(max_length=255)


class TankInfo(models.Model):
    vessel_height = models.IntegerField()
    vessel_height_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    vessel_width = models.IntegerField()
    vessel_width_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    max_fluid = models.IntegerField()
    max_fluid_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    min_fluid = models.IntegerField()
    min_fluid_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    process_connection = models.CharField(max_length=255)
    alt_process_connection = models.CharField(max_length=255)


class NozzelInfo(models.Model):
    nozzel_diameter = models.IntegerField()
    nozzel_diameter_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    nozzel_height = models.IntegerField()
    nozzel_height_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)
    nozzel_center_to_wall = models.IntegerField()
    nozzel_center_to_wall_unit = models.CharField(max_length=2, choices=LENGTH_UNITS)


class ProcessConditions(models.Model):
    medium_min_temp = models.IntegerField()
    medium_min_unit = models.CharField(max_length=1, choices=TEMP_UNITS)
    medium_max_temp = models.IntegerField()
    medium_max_unit = models.CharField(max_length=1, choices=TEMP_UNITS)
    vessel_min_pressure = models.IntegerField()
    vessel_min_unit = models.CharField(max_length=4, choices=PRESSURE_UNITS)
    vessel_max_pressure = models.IntegerField()
    vessel_max_unit = models.CharField(max_length=4, choices=PRESSURE_UNITS)
    dielectric_top = models.IntegerField()
    dielectric_bottom = models.IntegerField()


class MediumCharacteristics(models.Model):
    medium_name = models.CharField(max_length=255)
    media_state = models.CharField(max_length=10, choices=STATES)
    media_characteristics = models.CharField(max_length=12, choices=CHARACTERISTICS)
    liquid_surface = models.CharField(max_length=12, choices=SURFACES)
    foam_description = models.TextField()


class InstrumentSpecifics(models.Model):
    power_available = models.CharField(max_length=12, choices=POWER)
    power_outputs = models.CharField(max_length=25, choices=OUTPUTS)
    alarms = models.CharField(max_length=2, choices=ALARM_OPTIONS)
    alarms_description = models.TextField()
    pump_options = models.BooleanField(choices=PUMP_CONTROL)
    pump_options_description = models.TextField()
    area_classification = models.CharField(max_length=12, choices=CLASSIFICATION)
    electrical_housing = models.CharField(max_length=25, choices=HOUSING)
    special_requirements = models.TextField()


class LevelApplicationData(models.Model):
    contact_info = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    general_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE)
    tank_info = models.ForeignKey(TankInfo, on_delete=models.CASCADE)
    nozzel_info = models.ForeignKey(NozzelInfo, on_delete=models.CASCADE)
    process_conditions = models.ForeignKey(ProcessConditions, on_delete=models.CASCADE)
    medium_characteristics = models.ForeignKey(MediumCharacteristics, on_delete=models.CASCADE)
    instrument_specifics = models.ForeignKey(InstrumentSpecifics, on_delete=models.CASCADE)
