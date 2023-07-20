from django.db import models

# Create your models here.


class Message(models.Model):
    message_title = models.CharField(max_length=80)
    message_info = models.CharField(max_length=80)
    setup_time = models.DateTimeField
    #TODO:后期添加提交者、目标邮件等类
