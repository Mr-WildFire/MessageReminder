from django.db import models
import datetime

# Create your models here.


class Message(models.Model):
    message_info = models.CharField(max_length=80)
    # TODO:时间+8问题
    setup_time = models.DateTimeField(auto_now_add=True)  # 创建对象时自动添加时间
    # TODO:后期添加提交者、目标邮件等类
