__author__ = '张磊'
__date__ = '2018/8/2 14:50'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'
__discription__ = '<---->'

import xadmin
from .models import UserProfile, Banner, EmailVerifyCode


class EmailVerifyCodeAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    list_filter = ('code', 'email')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'add_time', 'index')
    list_filter = ('title', 'image', 'url',  'index')


# xadmin.site.register(UserProfile)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
