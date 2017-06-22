from django.db import models
from django.utils import timezone

First_a = ['Рахмонов Хайём', 'Абдулоев Мухаммад',
           'Сирочов Ахмад', 'Сидоров Валентин',
           'Алиев Саид', 'Вахобов Кариб',
           'Сангиев Ахмад', 'Валуев Сашка',
           'Каримов Алишер', ]


pupils = ((pupil, pupil) for pupil in First_a)
ratings = (('2', '2'),
           ('3', '3'),
           ('4', '4'),
           ('5', '5'),
           ('нб', 'нб'),)


class Pupil(models.Model):
    pupil = models.CharField('Ученик', choices=pupils, max_length=50)
    rating = models.CharField('Оценка', choices=ratings, max_length=50)
    data_add = models.DateField('Дата', default=timezone.now)

    def __str__(self):
        return str(self.data_add) + " | " + self.pupil + " | " + self.rating