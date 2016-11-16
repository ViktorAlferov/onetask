# -*- coding: utf-8 -*-
from django.db import models



class Region(models.Model):
	region_id = models.AutoField(primary_key = True)
	region_name = models.CharField(max_length=100, verbose_name='Регион')

	class Meta:
		verbose_name=u'Регион'
		verbose_name_plural=u'Регионы'

	def __str__(self):                      # __unicode__ on Python 2
		return u'%s' % (self.region_name)


class Client(models.Model):
	client_id = models.AutoField(primary_key = True)
	client_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
	regions_client = models.ManyToManyField(Region, verbose_name='Регион заказчика')

	class Meta:
		verbose_name='Заказчик'
		verbose_name_plural='Заказчики'
 
	def __str__(self):                      # __unicode__ on Python 2
		return u'%s %s' % (self.client_id, self.client_name)

class Provider(models.Model):
	provider_id = models.AutoField(primary_key = True)
	provider_name = models.CharField(max_length=100, verbose_name='Имя поставщика')
	regions_provider = models.ManyToManyField(Region, verbose_name='Регион поставщика')

	class Meta:
		verbose_name='Поставщик'
		verbose_name_plural='Поставщики'

	def __str__(self):                      # __unicode__ on Python 2
		return u'%s %s' % (self.provider_id, self.provider_name)
