from apps.user.models import EmailVerifyCode
from random import Random
from django.core.mail import send_mail
from izengzhi.settings import EMAIL_FROM

__author__ = '张磊'
__date__ = '2018/8/8 17:34'
__product__ = 'PyCharm'
__filename__ = 'email_send'
__discription__ = '<---->'


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()  # 随机数
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_email_to_user(email, send_type='register'):
    email_verify_code = EmailVerifyCode()
    email_verify_code.email = email
    email_verify_code.send_type = send_type
    random_str = generate_random_str(16)
    email_verify_code.code = random_str
    email_verify_code.save()
    if send_type == 'register':
        email_title = '爱增值网络注册激活软件'
        email_content = '就差最后一步，点击链接激活你的邮箱地址，链接地址是：http://127.0.0.1:8000/active/{0}'.format(random_str)
        # 发送邮件  返回值如果是1 就是成功
        status = send_mail(email_title, email_content, EMAIL_FROM, [email])
        if status:
            return random_str
