from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Article, Tag, Category
from django.shortcuts import reverse

class BlogDateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin'
        )

        self.cate = Category.objects.create(name='category one')
        self.cate_other = Category.objects.create(name='category two')

        self.article = Article.objects.create(
            title='test title',
            content='test content',
            category=self.cate,
            author=self.user
        )
        self.article_other = Article.objects.create(
            title='other test title',
            content='test other content',
            category=self.cate_other,
            author=self.user
        )


class CategoryViewTestCase(BlogDateTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('blog:category', kwargs={'pk': self.cate.pk})
        self.url_other = reverse('blog:category', kwargs={'pk': self.cate_other.pk})

    def test_visit_nonexistent(self):
        url = reverse('blog:category', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_without_article(self):
        Article.objects.all().delete()
        response = self.client.get(self.url_other)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('blog/index.html')
        self.assertContains(response, '暂时还没有发布的文章！')

    def test_with_article(self):
        response = self.client.get(self.url_other)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('blog/index.html')
        self.assertContains(response, self.article.title)
        self.assertIn('articles', response.context)
        self.assertIn('is_paginated', response.context)
        self.assertIn('page_obj', response.context)
        self.assertEqual(response.context['articles'].count(), 1)


class ArticleDetailViewTestCase(BlogDateTestCase):
    def setUp(self):
        super().setUp()
        self.md_article = Article.objects.create(
            title = 'test article',
            content = '# test content',
            category = self.cate_other,
            author=self.user
        )
        self.url = reverse('blog:detail', kwargs={'pk': self.md_article.pk})

    def test_exits_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('blog/detail.html')
        self.assertContains(response, self.md_article.title)
        self.assertIn('article', response.context)

    def test_increase_view(self):
        self.client.get(self.url)
        self.md_article.refresh_from_db()
        self.assertEqual(self.md_article.views, 1)

        self.client.get(self.url)
        self.md_article.refresh_from_db()
        self.assertEqual(self.md_article.views, 2)

    def test_markdown_article_and_set_toc(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'article')
        self.assertContains(response, self.md_article.title)

        article_template = response.context['article']
        self.assertHTMLEqual(article_template.body_html, '<h1 id="test-content">test content</h1>')