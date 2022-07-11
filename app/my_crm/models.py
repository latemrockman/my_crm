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



class MatStatus(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Статус по коврам'
        verbose_name_plural = 'Статусы по коврам'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(text2translit(self.title))
        super(MatStatus, self).save(*args, **kwargs)









class Clients(models.Model):
    client_id = models.IntegerField()
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    stage_status = models.ForeignKey(Stages, on_delete=models.PROTECT, null=True)
    mat_status = models.ForeignKey(MatStatus, on_delete=models.PROTECT, null=True)
    additionally = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


