from django.db import models
from authentication.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        try:
            return self.title
        except:
            return str(self.id)
