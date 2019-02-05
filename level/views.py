from django.shortcuts import render

from formtools.wizard.views import SessionWizardView


class LevelWizard(SessionWizardView):

    template_name = 'pages/levelform.html'

    def done(self, form_list, **kwargs):
        return render(self.requests, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
