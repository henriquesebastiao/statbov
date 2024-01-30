from django.test import TestCase
from django.urls import resolve, reverse


class IndexTest(TestCase):
    def test_if_url_index_is_correct(self):
        self.assertEqual(reverse('index'), '/')

    def test_if_url_index_render_correct_view(self):
        self.assertEqual(resolve('/').view_name, 'index')

    def test_if_url_index_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('index')).status_code, 200)

    def test_if_view_index_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('index')), 'index.html'
        )
