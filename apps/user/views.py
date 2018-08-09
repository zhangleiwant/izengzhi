from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyCode
from django.db.models import Q
from django.views.generic.base import View
from .froms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_email_to_user


# 自定义authentication
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))  # 获取用户
            if user.check_password(password):  # 检测密码
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    # active_code 传递过来的
    def get(self, request, active_code):
        # 根据code查找数据库所有匹配的code
        all_user_code = EmailVerifyCode.objects.filter(code=active_code)
        if all_user_code:
            for random_code in all_user_code:
                email = random_code.email  # 根据邮箱查看用户
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return render(request, 'login.html')


# 注册
class RegisterView(View):
    def get(self, request):
        register_from = RegisterForm()
        return render(request, 'register.html', {'register_form': register_from})

    def post(self, request):
        register_from = RegisterForm(request.POST)
        if register_from.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.email = email
            user_profile.username = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()
            #     发送邮件
            send_email_to_user(email, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_from})


# 使用django里面自带的view里面又封装好的方法  不用判断请求类型
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        # 如果验证通过 在进数据库
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户还未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'error': login_form.errors})


# 前期的方法需要判断请求方法。(不建议该方法)
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    elif request.method == 'GET':
        return render(request, 'login.html', {})
