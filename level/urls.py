from django.urls import path
from . import views

from . import forms

urlpatterns = [
    path("level-application/", views.LevelWizard.as_view(
        [
            forms.ContactInfoForm,
            forms.GeneralInfoForm,
            forms.TankInformationForm,
            forms.ProcessConditionsForm,
            forms.InstrumentSpecificsForm
        ]
    )),
]