from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import home

class HomeTests(TestCase):

    def test_home_view_status_code(self):

        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_resolve(self):
        view=resolve("/")
        self.assertEquals(view.func,home)
    
    def url_status_code(self):
        url=reverse('board_topics',kwargs={'id':1})
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def url_status_code_not_found(self):
        url=reverse('board_topics',kwargs={'id':99})
        response=self.client.get(url)
        self.assertEquals(response.status_code,400)