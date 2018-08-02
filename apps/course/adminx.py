__author__ = '张磊'
__date__ = '2018/8/2 15:06'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'
__discription__ = '<---->'

import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = (
        'name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image', 'click_num',
        'add_time')
    list_filter = (
        'name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image', 'click_num')
    search_fields = (
        'name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image', 'click_num')


class LessonAdmin(object):
    list_display = {'course', 'name', 'add_time'}
    list_filter = {'course', 'name', 'add_time'}
    search_fields = {'course', 'name'}


class VideoAdmin(object):
    list_display = {'lesson', 'name', 'add_time'}
    list_filter = {'lesson', 'name', 'add_time'}
    search_fields = {'lesson', 'name'}


class CourseResourceAdmin(object):
    list_display = {'course', 'name', 'add_time', 'download'}
    list_filter = {'course', 'name', 'add_time', 'download'}
    search_fields = {'course', 'name'}


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
