from django.db import models
#from django.contrib.auth.models import User
from django.utils.timezone import now
from courses.models import Batch,Course
from users.models import User
# Create your models here.

class discussion_Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13]
