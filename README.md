# Django-Blog [![Test status](https://github.com/DanielZhui/Django-Blog/workflows/test/badge.svg)](https://github.com/DanielZhui/Django-Blog/actions)
Use Django to build a personal Blog

## Django 开发个人 blog 系统

技术栈

- django
- bootstrapt



## 表结构

### 文章分类 - Category

| 字段 | 类型        | 说明         |
| ---- | ----------- | ------------ |
| Id   | int         | 文章分类主键 |
| name | varchar(32) | 分类名称     |



### 文章标签 - Tag

| 字段 | 类型        | 说明     |
| ---- | ----------- | -------- |
| Id   | int         | 标签主键 |
| name | varchar(32) | 标签名   |



### 文章 - Article

| 字段      | 类型         | 说明         |
| --------- | ------------ | ------------ |
| Id        | int          | 文章主键     |
| title     | varchar(200) | 文章标题     |
| content   | text         | 文章内容     |
| excerpt   | varchar(200) | 文章摘要     |
| catagory  | int          | 所属文章分类 |
| tags      | int          | 文章标签     |
| author    | int          | 文章作者     |
| views     | int          | 文章浏览量   |
| createdAt | DateTime     | 创建时间     |
| updatedAt | DateTime     | 更新时间     |



### 评论 - Comments

| 字段      | 类型         | 说明       |
| --------- | ------------ | ---------- |
| Id        | int          | 评论主键   |
| name      | varchar(64)  | 评论人名称 |
| email     | varchar(100) | 评论人邮箱 |
| url       | varchar(100) | 评论人 url |
| text      | text         | 评论内容   |
| article   | int          | 文章主键   |
| createdAt | DateTime     | 创建时间   |



## API 接口

### 一、获取所有文章
> /blog/articles

### 二、获取某篇文章详情
> /blog/articles/:id

### 三、获取具体某个时间段所有文章
> /blog/archives/:year/:month

### 四、获取某个分类下所有文章
> /articles/categories/:id

### 五、获取某个标签下所有文章
> articles/tags/:id

### 六、 获取某篇文章评论
> articles/comment/:id

## 项目相关命令
```
- 采用 make 命令配置项目相关命令
**启动项目**
make create-network
make start-service

**停止项目**
make stop-service

**重启项目**
make restart-service

**创建超级管理员**
make create-superuser
```