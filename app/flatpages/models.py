from django.db import models

from autoslug import AutoSlugField

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices


class FlatPage(TimeStampedModel):
    """
        a very simple static page model, with an option to be rendered as
        markdown or rST
    """
    FORMAT_CHOICES = Choices('markdown', 'raw')
    text_format = StatusField(choices_name='FORMAT_CHOICES',
                              default=FORMAT_CHOICES.raw)

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Flat Pages"
