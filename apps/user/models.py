from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 使用ddjango系统自带的表进行扩展
# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, default=u'', verbose_name=u'用户昵称')
    birth = models.DateField(default=u'', null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(('male', u'男'), ('femal', u'女')), default='female',
                              verbose_name=u'用户性别')
    address = models.CharField(max_length=200, default=u'', verbose_name=u'用户地址')
    mobile = models.CharField(max_length=11, default=u'', null=True, blank=True, verbose_name='手机号码')
    avater = models.ImageField(max_length=200, upload_to=u'avater/%Y/%m', default=u'avater/default.png',
                               verbose_name=u'用户头像')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.CharField(max_length=50, verbose_name=u'邮件地址')
    send_type = models.CharField(max_length=10, choices=(('register', u'注册'), ('forget', u'忘记密码')),
                                 verbose_name=u'发送类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(max_length=100, verbose_name=u'图片地址', upload_to='banner/%Y/%m')
    url = models.CharField(max_length=200, verbose_name=u'跳转地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    index = models.IntegerField(default=100, verbose_name=u'排列顺序')

    class Meta:
        verbose_name = u'用户banner'
        verbose_name_plural = verbose_name
