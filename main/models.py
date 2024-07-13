from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Kitob(models.Model):
    name=models.CharField(max_length=255,verbose_name='Nomi')
    author=models.ForeignKey('Author',on_delete=models.CASCADE,blank=True,verbose_name="Muallif")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    file = models.FileField(upload_to="file/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="File")
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Rasm")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilish vaqti")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update vaqti")
    is_published = models.BooleanField(default=True,verbose_name="Status")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('name', kwargs={'name_slug': self.slug})




class Author(models.Model):
    name=models.CharField(max_length=255,verbose_name='I.F.O')
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Muallif rasmi")
    content=models.TextField(verbose_name="Muallif haqida",null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return reverse('avtor', kwargs={'avtor_slug': self.slug})
