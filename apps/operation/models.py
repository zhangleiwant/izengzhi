from django.db import models
from apps.user.models import UserProfile
from apps.course.models import Course
from datetime import datetime


# Create your models here.
class UserAsk(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11, verbose_name=u'用户电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name=u'用户评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '教师'), (3, '授课机构')),
                                   default=1, verbose_name=u'收藏类型')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收id')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户学习的课程'
        verbose_name_plural = verbose_name
