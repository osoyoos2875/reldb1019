from django.contrib import admin
from import_export.resources import ModelResource
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from .models import Enrollment, Student, Instructor, Course, Course_student

class StudentResource(ModelResource):
    enrollment = Field(attribute='enrollment', column_name='enrollment',
                       widget=ForeignKeyWidget(Enrollment, 'enrollment'))
    student_id = Field(attribute='student_id', column_name='student_id')
    name = Field(attribute='name', column_name='name')
    kana = Field(attribute='kana', column_name='kana')
    name_en = Field(attribute='name_en', column_name='name_en')
    gender = Field(attribute='gender', column_name='gender')
    email = Field(attribute='email', column_name='email')
    current_status = Field(attribute='current_status', column_name='current_status')
    others = Field(attribute='others', column_name='others')
    class Meta:
        model = Student
#        import_order = ('student_id', 'name', 'kana', 'name_en', 'gender',
#                        'email', 'current_status', 'others', 'enrollment')
        import_id_fields = ['student_id']


class InstructorResource(ModelResource):
    name = Field(attribute='name', column_name='name')
    kana = Field(attribute='kana', column_name='kana')
    name_en = Field(attribute='name_en', column_name='name_en')
    email = Field(attribute='email', column_name='email')
    faculty = Field(attribute='faculty', column_name='faculty')
    others = Field(attribute='others', column_name='others')
    class Meta:
        model = Instructor
        import_order = ('name', 'kana', 'name_en', 'email', 'faculty', 'others')

class InstructorAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = InstructorResource
    list_display = ('name', 'faculty')

class StudentAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('name', 'enrollment')
    resource_class = StudentResource
    list_filter = ('enrollment', 'current_status')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_short', 'title', 'instructor1')
    list_filter = ('acad_year', 'quarter')

class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')



admin.site.register(Enrollment)
admin.site.register(Student, StudentAdmin)

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Course_student, CourseStudentAdmin)