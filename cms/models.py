from django.db import models


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, default=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name