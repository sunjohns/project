from django.db import models


class Student(models.Model):
    Username=models.CharField(max_length=10,help_text='bu yao du bo')
    Nid=models.AutoField(primary_key=True)
    Password=models.CharField(max_length=10)
    def __unicode__(self):
        return self.Username




