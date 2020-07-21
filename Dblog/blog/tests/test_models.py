from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Article, Category, Tag
from django.shortcuts import reverse

# Create your tests here.

# models test
class ArticleModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin'
        )
        cate = Category.objects.create(name='test')
        self.article = Article.objects.create(
            title='test title',
            content='test content',
            category=cate,
            author=user
        )

    def test_str_representation(self):
        self.assertEqual(self.article.__str__(), self.article.title)

    def test_get_absolute_url(self):
        expected_url = reverse('blog:detail', kwargs={'pk': self.article.pk})
        self.assertEqual(self.article.get_absolute_url(), expected_url)

    def test_auto_populate_excerpt(self):
        self.assertIsNotNone(self.article.excerpt)
        self.assertTrue(0 < len(self.article.excerpt) <= 60)
