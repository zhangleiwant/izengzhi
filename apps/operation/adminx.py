__author__ = '张磊'
__date__ = '2018/8/2 15:25'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'
__discription__ = '<---->'

import xadmin
from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ('user', 'course', 'mobile', 'add_time')
    list_filter = ('user', 'course', 'mobile')
    search_fields = ('user', 'course', 'mobile')


class CourseCommentAdmin(object):
    list_display = ('user', 'course', 'comments', 'add_time')
    list_filter = ('user', 'course', 'comments')
    search_fields = ('user', 'course', 'comments')


class UserFavoriteAdmin(object):
    list_display = ('user', 'fav_type', 'fav_id', 'add_time')
    list_filter = ('user', 'fav_type', 'fav_id')
    search_fields = ('user', 'fav_type', 'fav_id')


class UserMessageAdmin(object):
    list_display = ('user', 'message', 'has_read', 'add_time')
    list_filter = ('user', 'message', 'has_read')
    search_fields = ('user', 'message', 'has_read')


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time')
    list_filter = ('user', 'course')
    search_fields = ('user', 'message')


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
