from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class IntegerRangeField(models.PositiveSmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.PositiveSmallIntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Enrollment(models.Model):
    enrollment = IntegerRangeField(min_value=2018, max_value=2099, primary_key=True)
    class Meta:
        db_table = 'app_enrollment'

    def __str__(self):
        return str(self.enrollment)

class Student(models.Model):
    GENDER = [("male", "男"), ("female", "女"), ("na", "NA")]
    STATUS = [("active", "在学"), ("leave", "休学"), ("graduate", "卒業")]

    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    kana = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER, default="na")
    email = models.EmailField(max_length = 254)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    current_status = models.CharField(
        max_length=10, choices=STATUS, default="active"
    )
    others = models.TextField(blank=True)
    class Meta:
        db_table = 'app_student'

    def __str__(self):
        return self.name


class Instructor(models.Model):
    FACULTY = [
    ("permanent", "専任"), ("adjunct", "科目担当"), ("na", "その他")
    ]

    name = models.CharField(max_length=30, unique=True)
    kana = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    faculty = models.CharField(
        max_length=10, choices=FACULTY, default="na"
    )
    others = models.TextField(blank=True)
    class Meta:
        db_table = 'app_instructor'

    def __str__(self):
        return self.name

class Course(models.Model):
    QUARTER = [
    ("Q1", "春"), ("Q2", "夏"), ("Q3", "秋"), ("Q4", "冬")
    ]
    DAY = [
    ("Mon", "月"), ("Tue", "火"), ("Wed", "水"), 
    ("Thu", "木"), ("Fri", "金")
    ]
    SLOT = [   
    ("P1", "１限"), ("P2", "２限"),
    ("P3", "３限"), ("P4", "４限"), ("P5", "５限")
    ]

    course_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    title_short = models.CharField(max_length=20)
    acad_year = IntegerRangeField(min_value=2018, max_value=2099)
    quarter = models.CharField(max_length=10, choices=QUARTER)
    day_of_week = models.CharField(
        max_length=3, choices=DAY, default="Tue"
    )
    slot = models.CharField(max_length=10, choices=SLOT)
    instructor1 = models.ForeignKey(
        Instructor, null=True, on_delete=models.SET_NULL,
        related_name="instr_1"
    )
    instructor2 = models.ForeignKey(
        Instructor, null=True, on_delete=models.SET_NULL,
        related_name="instr_2"
    )
    others = models.TextField(blank=True)
    class Meta:
        db_table = 'app_course'

    def __str__(self):
        return self.course_id

class Course_student(models.Model):
    STATUS = [
        ("registered", "登録済"), ("attending", "履修中"),
        ("pass", "合格"), ("fail", "不合格")
    ]

    student = models.ForeignKey(
        Student, null=True, on_delete=models.SET_NULL, to_field="student_id"
    )
    course = models.ForeignKey(
        Course, null=True, on_delete=models.SET_NULL, to_field="course_id"
    )
    current_status = models.CharField(
        max_length=10, choices=STATUS, default="inactive"
    )
    others = models.TextField(blank=True)
    class Meta:
        db_table = 'app_course_student'