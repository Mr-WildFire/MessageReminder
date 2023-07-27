from django.db import models
import datetime

MESSAGE_LEVEL = {
    'high': 2,
    'middle': 1,
    'low': 0,
}

# Create your models here.


class Message(models.Model):
    MESSAGE_LEVEL = (  # 消息级别的二元组，第一个值会存储在数据库，第二个值会显示在表单
        (2, 'high'),
        (1, 'middle'),
        (0, 'low')
    )
    message_info = models.CharField(max_length=80)
    setup_time = models.DateTimeField(auto_now_add=True)  # 创建对象时自动添加时间
    message_level = models.IntegerField(default=0, choices=MESSAGE_LEVEL)
    user_id = models.IntegerField(default=0)
    # TODO:后期添加目标邮件

    class Meta:
        ordering = ["setup_time"]
