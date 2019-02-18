from django.urls import path
from . import views

from . import forms


level_forms = (
    ('contact', forms.ContactInfoForm),
    ('general', forms.GeneralInfoForm),
    ('tank', forms.TankInformationForm),
    ('nozzel', forms.NozzelInformationForm),
    ('process', forms.ProcessConditionsForm),
    ('medium', forms.MediumCharacteristicsForm),
    ('instrument', forms.InstrumentSpecificsForm)
)

urlpatterns = [
    path("", views.LevelWizard.as_view(level_forms)),
]
