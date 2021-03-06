"""izengzhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import xadmin
from django.views.generic import TemplateView
from apps.user.views import user_login, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView,ModifyPwdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 以前使用includ 在app里面url进行render
    # 现在用更简单的方式 templateview 模板文件
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    # 拿到链接中的验证码 和数据库保存的验证码进行匹配验证
    path('active/<active_code>', ActiveUserView.as_view(), name='activeuser'),
    #     忘记密码
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    #     邮箱重置密码
    path('reset/<reset_code>', ResetPwdView.as_view(), name='reset_pwd'),
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),
]
