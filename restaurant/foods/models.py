from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = (
        ('breakefast','صبحانه'),
        ('drinks','نوشیدنی'), 
        ('dinner','شام'),
        ('lunch','ناهار')
    )
    name = models.CharField(max_length=100)
    description = models.CharField(_('توضیحات'), max_length=50)
    rate = models.IntegerField(_('امتیاز'), default=0)
    price = models.CharField(max_length=50)
    time = models.IntegerField(_('زمان لازم'))
    put_date = models.DateField(_('تاریخ انتشار'), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='foods/')
    slug = models.SlugField(unique=True)
    type_food = models.CharField(_('نوع غذا'), max_length=10,choices=FOOD_TYPE,default="drinks")


    def __str__(self):
        return self.name
    