# Generated by Django 2.0.7 on 2018-08-01 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片地址')),
                ('url', models.CharField(max_length=200, verbose_name='跳转地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('index', models.IntegerField(default=100, verbose_name='排列顺序')),
            ],
            options={
                'verbose_name': '用户banner',
                'verbose_name_plural': '用户banner',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.CharField(max_length=50, verbose_name='邮件地址')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '忘记密码')], max_length=10, verbose_name='发送类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
    ]