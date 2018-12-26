from django.test import TestCase
from django.urls import reverse
from .models import Pages
from .forms import PagesForm

# Create your tests here.


class PagesTests(TestCase):
    def setUp(self):
        Pages.objects.create(
            title="Google Page",
            content_html="<h1>Hi Google</h1>",
            ordering=1
        )

    def testGetHomePage(self):
        response = self.client.get(reverse('pagesapp:home'))
        form = PagesForm()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data'], Pages.objects.all(), transform=lambda x: x)
        self.assertHTMLEqual(str(response.context['form']), str(form))

    def testPostPage(self):
        data = {
            'title': "Yahoo Page",
            'content_html': "<h1>Hi Yahoo<h1>",
            'ordering': 1
        }
        response = self.client.post(reverse('pagesapp:home'), data, follow=True)
        form = PagesForm()
        exists = Pages.objects.filter(
            title="Yahoo Page",
            content_html="<h1>Hi Yahoo<h1>",
            ordering=1
        ).exists()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(exists, True)
        self.assertQuerysetEqual(response.context['data'], Pages.objects.all(), transform=lambda x: x, ordered=False)
        self.assertHTMLEqual(str(response.context['form']), str(form))

    def testNavPage(self):
        response = self.client.get('/pages/google-page/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data'], Pages.objects.all(), transform=lambda x: x, ordered=False)
        self.assertEqual(response.context['title'], "Google Page")
        self.assertHTMLEqual(response.context['html'], "<h1>Hi Google</h1>")
