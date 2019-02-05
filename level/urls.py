from django.urls import path
from . import views

from . import forms


level_forms = (
    ('contactinfo', forms.ContactInfoForm),
    ('generalinfo', forms.GeneralInfoForm),
    ('tankinfo', forms.TankInformationForm),
    ('processinfo', forms.ProcessConditionsForm),
)

urlpatterns = [
    path("", views.LevelWizard.as_view(
        [
            forms.ContactInfoForm,
            forms.GeneralInfoForm,
            forms.TankInformationForm,
            forms.ProcessConditionsForm,
            forms.InstrumentSpecificsForm
        ]
    )),
]