from django.db import models
from django.utils.text import slugify
from . translit import text2translit

# Create your models here.


class Stages(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=7)
    slug = models.SlugField(default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Этап продажы'
        verbose_name_plural = 'Этапы продаж'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(text2translit(self.title))
        super(Stages, self).save(*args, **kwargs)


