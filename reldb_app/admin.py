from django.contrib import admin
from .models import Enrollment, Student, Instructor, Course, Course_student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment')
    list_filter = ('enrollment', 'current_status')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_short', 'title', 'instructor1')
    list_filter = ('acad_year', 'quarter')

class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')



admin.site.register(Enrollment)
admin.site.register(Student, StudentAdmin)
#admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(Course_student, CourseStudentAdmin)