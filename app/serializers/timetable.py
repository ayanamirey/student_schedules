from rest_framework import serializers
from app.models.timetable import Pair, Lessons, Group, Day, Subject, Teacher
from authorization.models.users import MyUser


class DaySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ("__all__")


class GroupSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("__all__")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("__all__")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("__all__")


class LessonSerilaizer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Lessons
        fields = ("__all__")


class PairSerializer(serializers.ModelSerializer):
    day = DaySerilaizer()
    group = GroupSerilaizer()
    lessons = LessonSerilaizer(many=True)
    day = DaySerilaizer()

    class Meta:
        model = Pair
        fields = '__all__'


class PairCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'


class MyUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('group',)
