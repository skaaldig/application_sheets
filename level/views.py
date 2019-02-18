from django.shortcuts import render

from formtools.wizard.views import SessionWizardView

from formtools.wizard.views import NamedUrlSessionWizardView


TEMPLATES = {
    "contact": "pages/level/contact_step.html",
    "general": "pages/level/general_step.html",
    "tank": "pages/level/tank_step.html",
    "nozzel": "pages/level/nozzel_step.html",
    "process": "pages/level/process_step.html",
    "medium": "pages/level/medium_step.html",
    "instrument": "pages/level/instrument_step.html"
}


class LevelWizard(NamedUrlSessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render(self.requests, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
