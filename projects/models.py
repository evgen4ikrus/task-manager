from django.db import models
from django.urls import reverse


class Position(models.Model):
    title = models.CharField('Должность', max_length=50)

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    position = models.ForeignKey('Position', verbose_name='Должность', on_delete=models.CASCADE, related_name='employees')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class Project(models.Model):
    STATUSES = [
        ('active', 'Активный'),
        ('inactive', 'Неактивный')
    ]
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    manager = models.ForeignKey('Employee', verbose_name='Руководитель', on_delete=models.CASCADE,
                                related_name='projects')
    status = models.CharField('Статус', max_length=10, choices=STATUSES)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    STATUSES = [
        ('new', 'Новая'),
        ('active', 'В работе'),
        ('completed', 'Завершена')
    ]
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    project = models.ForeignKey('Project', verbose_name='Проект', on_delete=models.CASCADE, related_name='tasks')
    deadline = models.DateTimeField('Выполнить до')
    status = models.CharField('Статус', max_length=10, choices=STATUSES, default='new')
    performers = models.ManyToManyField('Employee', verbose_name='Исполнители', related_name='tasks', blank=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
