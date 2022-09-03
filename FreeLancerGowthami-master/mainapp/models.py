from django.db import models

from django.db import models

class ipModel(models.Model):
    ip=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("ip", "time"),)

    def __str__(self):
        return self.ip
