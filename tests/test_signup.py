from django.test import TestCase
from django.urls import resolve, reverse


class SignupTest(TestCase):
    def test_if_url_signup_is_correct(self):
        self.assertEqual(reverse('signup'), '/signup/')

    def test_if_url_user_create_is_correct(self):
        self.assertEqual(reverse('user_create'), '/signup/user_create/')

    def test_if_url_signup_render_correct_view(self):
        self.assertEqual(resolve('/signup/').view_name, 'signup')

    def test_if_url_user_create_render_correct_view(self):
        self.assertEqual(
            resolve('/signup/user_create/').view_name, 'user_create'
        )

    def test_if_url_signup_get_method_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('signup')).status_code, 200)

    def test_if_view_signup_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('signup')), 'signup.html'
        )
