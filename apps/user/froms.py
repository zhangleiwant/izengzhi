__author__ = '张磊'
__date__ = '2018/8/3 16:02'
__product__ = 'PyCharm'
__filename__ = 'froms'
__discription__ = '<--form表单认证-->'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, min_length=6)
