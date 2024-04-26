from django.test import TestCase
from django.urls import resolve, reverse


class PlansTest(TestCase):
    def test_if_url_plans_is_correct(self):
        self.assertEqual(reverse('plans'), '/plans/')

    def test_if_url_plans_render_correct_view(self):
        self.assertEqual(resolve('/plans/').view_name, 'plans')

    def test_if_url_plans_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('plans')).status_code, 200)

    def test_if_view_plans_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('plans')), 'landing/plans.html'
        )
