from django.shortcuts import render

from formtools.wizard.views import SessionWizardView


def level_general(request):
    return render(request, 'pages/level_form.html')


def level_tank(request):
    return render(request, 'pages/level_tank_material.html')


class LevelWizard(SessionWizardView):

    template_name = 'pages/levelform.html'

    def done(self, form_list, **kwargs):
        return render(self.requests, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
