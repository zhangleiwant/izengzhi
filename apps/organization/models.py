from django.db import models
from datetime import datetime


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市名字')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名字')
    desc = models.CharField(max_length=100,verbose_name=u'机构描述')
    address = models.CharField(max_length=200, verbose_name=u'机构地址')
    image = models.ImageField(max_length='200', upload_to='org/%Y/%m', verbose_name=u'封面图')
    favorites_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    city = models.ForeignKey(CityDict, verbose_name=u'所属城市',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程机构信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构',on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u'教师名字')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'工作岗位')
    work_point = models.CharField(max_length=100, verbose_name=u'教学特点')
    favorites_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
