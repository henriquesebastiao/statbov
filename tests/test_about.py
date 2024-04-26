from django.test import TestCase
from django.urls import resolve, reverse


class AboutTest(TestCase):
    def test_if_url_about_is_correct(self):
        self.assertEqual(reverse('about'), '/about/')

    def test_if_url_about_render_correct_view(self):
        self.assertEqual(resolve('/about/').view_name, 'about')

    def test_if_url_about_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('about')).status_code, 200)

    def test_if_view_about_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('about')), 'landing/about.html'
        )
