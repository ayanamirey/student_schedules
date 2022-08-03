from django.db import models
from django.contrib.auth.models import User
from app.models.timetable import Group


class MyUser(User):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
