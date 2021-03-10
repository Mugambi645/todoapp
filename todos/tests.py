from django.test import TestCase
# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_page(self):
        """check if index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)