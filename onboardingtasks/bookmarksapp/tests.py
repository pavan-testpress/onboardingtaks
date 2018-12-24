from django.test import TestCase
from .models import Bookmarks, Folders
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.


class BookMarksSignupSigninTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'pavan',
            'password': 'pavankumar'
        }
        User.objects.create_user(**self.credentials)

    def testGetLoginPage(self):
        response = self.client.get('/bookmarks/login')
        self.assertEqual(response.status_code, 301)

    def testPostLoginPage(self):
        response = self.client.post('/bookmarks/login/', self.credentials, follow=True)
        self.assertRedirects(response, reverse('home:index'))
        return response

    def testGetSignupPage(self):
        response = self.client.get(reverse('home:signup'))
        self.assertEqual(response.status_code, 200)

    def testPostSignupPage(self):
        data = {
            'username': "kumar",
            'password1': "pavankumar",
            'password2': "pavankumar"
        }
        response = self.client.post(reverse('home:signup'), data, follow=True)
        self.assertRedirects(response, reverse('home:index'))


class HomeViewTestCase(BookMarksSignupSigninTestCase):
    def setUp(self):
        super().setUp()
        test_post_login_page = super().testPostLoginPage()
        f = Folders.objects.create(
            folder_name="Google",
            user=test_post_login_page.context['user']
        )
        Bookmarks.objects.create(
            folder_name=f,
            bookmark_url="http://www.google.com",
            name='Google Website',
            description='Google search engine',
            user=test_post_login_page.context['user']
        )
        f = Folders.objects.create(folder_name="Yahoo", user=test_post_login_page.context['user'])
        Bookmarks.objects.create(
            folder_name=f,
            bookmark_url="http://www.yahoo.com",
            name='yahoo Website',
            description='yahoo search engine',
            user=test_post_login_page.context['user']
        )

    def testGetIndexPage(self):
        response = self.client.get(reverse('home:index'))
        folders = Folders.objects.filter(user=response.context['user'])
        bookmarks = Bookmarks.objects.filter(user=response.context['user'])
        self.assertQuerysetEqual(response.context['folders'], folders, transform=lambda x: x, ordered=False)
        self.assertQuerysetEqual(response.context['bookmarks'], bookmarks, transform=lambda x: x, ordered=False)

    def testPostFolderInIndexPage(self):
        data = {
            'add_folder': '',
            'folder': 'New Folder'
        }
        response = self.client.post(reverse('home:index'), data, follow=True)
        self.assertRedirects(response, reverse('home:index'))
        folder_from_database = response.context['folders'].get(folder_name=data['folder']).folder_name
        self.assertEqual(folder_from_database, data['folder'])

    def testPostBookmarkInIndexPage(self):
        data = {
            'add': '',
            'folder_list': Folders.objects.last().id,
            'bookmark_url': 'http://new-url.com',
            'name': 'new url added',
            'description': 'new description'
        }
        response = self.client.post(reverse('home:index'), data, follow=True)
        url_from_database = response.context['bookmarks']\
            .get(
            name=data['name'],
            bookmark_url='http://new-url.com',
            description='new description'
        ).name
        self.assertEqual(url_from_database, data['name'])
        self.assertEqual(response.status_code, 200)

    def testPostDelInIndexPage(self):
        data = {
            'delete': '',
            'id': Bookmarks.objects.last().id,
        }
        response = self.client.post(reverse('home:index'), data, follow=True)
        print(response.context)
