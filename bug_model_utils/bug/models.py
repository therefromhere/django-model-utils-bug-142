from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

class Foo(models.Model):
    
    STATUS = Choices('', 'NEW','INACTIVE', 'ACTIVE')
    status = StatusField(default="NEW")

