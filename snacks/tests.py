from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class sanakesTests(SimpleTestCase):
    def test_home_page_1(self):
        url=reverse('home')
        actual_code=self.client.get(url).status_code
        excepted_code=200
        self.assertEqual(actual_code,excepted_code)

    def test_home_page_templete_2(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response , 'home.html')
        self.assertTemplateUsed(response , 'base.html')

    def test_about_page_3(self):
        url=reverse('about')
        actual_code=self.client.get(url).status_code
        excepted_code=200
        self.assertEqual(actual_code,excepted_code)

    def test_about_page_templete_4(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertTemplateUsed(response , 'about.html')
        self.assertTemplateUsed(response , 'base.html')
