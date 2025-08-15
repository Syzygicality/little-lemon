from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_renders(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')