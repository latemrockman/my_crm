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

    def get_len_clients(self):
        return 'HELLO'

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
    client_id = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    stage_status = models.ForeignKey(Stages, on_delete=models.PROTECT, null=True)
    mat_status = models.ForeignKey(MatStatus, on_delete=models.PROTECT, null=True)
    additionally = models.TextField(max_length=500)
    slug = models.SlugField(default='', null=False, db_index=True)


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        #if Clients.objects.all():
        #    self.client_id = str(Clients.objects.order_by('-id')[0].id+1)
        #    self.client_id = f'{self.client_id:0>5}'
        #else:
        #    self.client_id = '00001'
#
      # #self.slug = slugify(f'{self.client_id}_{text2translit(self.title)}')
      # #super(Clients, self).save(*args, **kwargs)
#
        self.slug = slugify(text2translit(self.title))
        super(Clients, self).save(*args, **kwargs)
