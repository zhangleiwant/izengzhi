__author__ = '张磊'
__date__ = '2018/8/2 14:50'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'
__discription__ = '<---->'

import xadmin
from .models import UserProfile, Banner, EmailVerifyCode
from xadmin import views


class EmailVerifyCodeAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    list_filter = ('code', 'email')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'add_time', 'index')
    list_filter = ('title', 'image', 'url', 'index')


# 允许xadmin修改配置
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


# 修改标题和foot
class GlobalSettings(object):
    site_title = u'爱增值后台管理系统'
    site_footer = u'爱增值公司'
    menu_style = 'accordion'#收缩栏目


# xadmin.site.register(UserProfile)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
