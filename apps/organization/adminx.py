__author__ = '张磊'
__date__ = '2018/8/2 15:35'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'
__discription__ = '<---->'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ('name', 'desc', 'add_time')
    list_filter = ('name', 'desc')
    search_fields = ('name', 'desc')


class CourseOrgAdmin(object):
    list_display = ('name', 'desc', 'address', 'image', 'favorites_num', 'click_num', 'city', 'add_time')
    list_filter = ('name', 'desc', 'address', 'image', 'favorites_num', 'click_num', 'city')
    search_fields = ('name', 'desc', 'address', 'image', 'favorites_num', 'click_num', 'city')


class TeacherAdmin(object):
    list_display = (
    'org', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num', 'click_num',
    'add_time')
    list_filter = (
    'org', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num', 'click_num')
    search_fields = (
    'org', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num', 'click_num')


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
