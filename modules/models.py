from django.db import models

NULLABLE = {"blank": True, "null": True}


class Module(models.Model):
    """Модель образовательные модули"""

    number = models.IntegerField(verbose_name="Порядковый номер")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"Модуль {self.name}"

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"
