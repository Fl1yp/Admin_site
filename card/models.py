from django.db import models
from django.utils import timezone

NULLABLE = {
    'blank': True,
    'null': True
}


class Card(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Фото")
    address = models.URLField(verbose_name="Ссылка на сайт", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"


class WhyLook(Card):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Что посмотреть"


class WhyStop(Card):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Где остановиться"


class WhyEat(Card):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Где поесть"


class MyHistory(Card):
    img_2 = models.ImageField(verbose_name="Второе фото", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"


class ZoneRelax(Card):
    img_2 = models.ImageField(verbose_name="Второе фото", **NULLABLE)
    img_3 = models.ImageField(verbose_name="Третье фото", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Зона отдыха"
        verbose_name_plural = "Зоны отдыха"


class Proiz(Card):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Наши производители"


class Question(models.Model):
    question = models.CharField(max_length=150, verbose_name="Вопрос", )
    answer = models.CharField(max_length=400, verbose_name="Ответ", )

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Contact(models.Model):
    name = models.CharField(max_length=12, verbose_name="Имя", )
    number = models.CharField(verbose_name="Номер", max_length=15)
    message = models.TextField(verbose_name="Сообщение", max_length=100,**NULLABLE)
    date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.date = self.date.replace(microsecond=0)  # обрезаем миллисекунды
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f"\n Время:{self.date} \n id:{self.id}\n Имя:{self.name}\n Номер:{self.number}\n\n"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"