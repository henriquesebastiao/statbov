from django.test import TestCase
from django.urls import resolve, reverse


class SupportTest(TestCase):
    def test_if_url_support_is_correct(self):
        self.assertEqual(reverse('support'), '/support/')

    def test_if_url_support_render_correct_view(self):
        self.assertEqual(resolve('/support/').view_name, 'support')

    def test_if_url_support_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('support')).status_code, 200)

    def test_if_view_support_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('support')), 'landing/support.html'
        )
