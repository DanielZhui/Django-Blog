# -*- coding:utf-8 -*-
import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dblog.settings")
    django.setup()

    from blog.models import Article, Category, Tag
    from comments.models import Comments
    from django.contrib.auth.models import User

    print('start clean database >>>')
    Article.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comments.objects.all().delete()
    User.objects.all().delete()

    print('create a blog user...')
    user =User.objects.create_superuser('admin', 'admin@test.com', 'admin')
    category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Docker', 'Nginx', 'Elasticsearch', 'Gunicorn', 'Supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)

    print('create categories and tag...')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    print('create a markdown sample post...')
    Article.objects.create(
        title='Markdown 高亮测试',
        content=pathlib.Path(BASE_DIR).joinpath('scripts', 'test.md').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown 测试'),
        author=user,
    )

    print('create some faked posts published within the past year')
    fake = faker.Faker('zh_CN')
    for _ in range(20):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        createdAt = fake.date_time_between(
            start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()
        )
        body = '\n\n'.join(fake.paragraphs(10))
        article = Article.objects.create(
            title=fake.sentence().rstrip('.'),
            content=body,
            category=cate,
            excerpt=body[:60],
            createdAt=createdAt,
            author=user
        )
        article.tags.add(tag1, tag2)
        article.save()

    print('create some comments...')
    for article in Article.objects.all():
        article_createdAt = Article.createdAt
        for _ in range(random.randrange(3, 10)):
            Comments.objects.create(
                name=fake.name(),
                email=fake.email(),
                url=fake.url(),
                text=fake.paragraph(),
                createdAt=fake.date_time_between(
                    start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()
                ),
                article=article
            )
    print('insert fake data success...')
