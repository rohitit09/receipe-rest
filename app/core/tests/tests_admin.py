from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse



class AdminTest(TestCase):

    def setUp(self):
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(
                email='rohit@gmail.com',
                password="rohit123")
        self.client.force_login(self.admin_user)

        self.user=get_user_model().objects.create_user(
                email='rohit1@gmail.com',
                password="odsfdsrhit123",
                name="rohitkumar"
                )

    def test_user_listed(self):
        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)
        self.assertContains(res,self.user.email)
        self.assertContains(res,self.user.name)

    def test_change_user_page(self):
        url=reverse('admin:core_user_change',args=[self.user.id])
        res=self.client.get(url)
        self.assertTrue(res.status_code,200)

    def test_add_user(self):
        url=reverse('admin:core_user_add')
        res=self.client.get(url)
        self.assertTrue(res.status_code,200)


