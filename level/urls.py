from django.urls import path
from . import views

from . import forms
from django.conf.urls import url

level_forms = (
    ('contact', forms.ContactInfoForm),
    ('general', forms.GeneralInfoForm),
    ('tank', forms.TankInformationForm),
    ('nozzel', forms.NozzelInformationForm),
    ('process', forms.ProcessConditionsForm),
    ('medium', forms.MediumCharacteristicsForm),
    ('instrument', forms.InstrumentSpecificsForm)
)

level_wizard = views.LevelWizard.as_view(level_forms, url_name='level_step', done_step_name='finished')

urlpatterns = [
    path("<str:step>", level_wizard, name="level_step"),
    path("", level_wizard, name="level_form"),
]
