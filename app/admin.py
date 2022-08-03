from django.contrib import admin
from app.models.timetable import Subject, Group, Day, Pair, Teacher, Lessons

admin.site.register(Day)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Lessons)
admin.site.register(Pair)