from django.test import TestCase

from django.urls import resolve
from .views import level_page
# Create your tests here.


class LevelPageTest(TestCase):

    def test_level_url_resolves_to_level_page(self):
        found = resolve('/level/')
        self.assertEqual(found.func, level_page)

    def test_level_uses_level_form_template(self):
        response = self.client.get('/level/')
        self.assertTemplateUsed(response, 'pages/level_form.html')