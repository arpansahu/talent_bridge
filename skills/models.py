from django.db import models

# Create your models here.
from talent_bridge.models import AbstractBaseModel


class Skills(AbstractBaseModel):
    name = models.CharField(max_length=100, null=False)
