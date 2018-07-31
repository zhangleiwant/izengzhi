from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=24, default='zl', verbose_name=u'用户名')
    age = models.IntegerField(verbose_name=u'用户年龄')
    email = models.EmailField(verbose_name=u'邮件地址')

    #     创建数据表的说明  前面加u意思是unicode编码
    class Meta:
        verbose_name = u'用户数据表'
        verbose_name_plural = verbose_name
        # 设置数据表名称，如果不设置就会默认appname_类名
        db_table = 'user_table'
