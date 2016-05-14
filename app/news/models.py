from django.db import models

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager

# Create your models here.
class NewsEntry(TimeStampedModel):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)

    pub_date = models.DateField(null=False)

    NEWSCHOICES = Choices('news', 'membernews')
    newstype = StatusField(choices_name='NEWSCHOICES')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News Entries"
