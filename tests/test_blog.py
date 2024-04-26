from django.test import TestCase
from django.urls import resolve, reverse


class BlogTest(TestCase):
    def test_if_url_blog_is_correct(self):
        self.assertEqual(reverse('blog'), '/blog/')

    def test_if_url_blog_render_correct_view(self):
        self.assertEqual(resolve('/blog/').view_name, 'blog')

    def test_if_url_blog_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('blog')).status_code, 200)

    def test_if_view_blog_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('blog')), 'landing/blog.html'
        )
