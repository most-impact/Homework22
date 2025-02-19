from django.db import models


class Blog(models.Model):
    """заголовок,содержимое, превью (изображение), дата создания, признак публикации (булевое поле), количество просмотров."""
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок блога",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое блога",
    )
    image = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрзите фото продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    publication = models.BooleanField(
        default=True,
        verbose_name='Публикация')
    number_views = models.PositiveIntegerField(
        verbose_name="Кол-во просмотров",
        help_text="Укажите кол-во просмотров",
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'