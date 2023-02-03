from django.db import models


class Link(models.Model):
    original_url = models.URLField(max_length=500, default='')
    url_hash = models.CharField(max_length=10, default='')

    def __str__(self):
        return f'{self.original_url} - {self.url_hash}'
