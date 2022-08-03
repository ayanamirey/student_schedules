from django.db import models

DAY_OF_THE_WEEK = (
    ('понедельник', 'понедельник'),
    ('вторник', 'вторник'),
    ('среда', 'среда'),
    ('четверг', 'четверг'),
    ('пятница', 'пятница'),
)


class Day(models.Model):
    name = models.CharField('День недели',
                            max_length=100,
                            choices=DAY_OF_THE_WEEK,
                            default='1'
                            )

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Номер группы', max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField('Предмет', max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField('Имя учителя', max_length=100)

    def __str__(self):
        return self.name


class Lessons(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Имя учителя', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.subject} - {self.teacher}'


class Pair(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True)
    cabinet = models.CharField(max_length=5)
    lessons = models.ManyToManyField(Lessons)

    def __str__(self):
        return f'{self.day} - {self.group} группа'
