from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    is_helium = models.BooleanField(
        default=False,
        verbose_name="С гелием"
    )
    is_painted = models.BooleanField(
        default=False,
        verbose_name="С рисунком"
    )
    is_metallic = models.BooleanField(
        default=False,
        verbose_name="Металлик"
    )
    is_foil = models.BooleanField(
        default=False,
        verbose_name="Фольгированный"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['-created_at']
        

