# !!!  这个文件名称必须是task!
import datetime
from celery import shared_task
# 这里必须从app名层级开始导入
from email_alert.models import Message
from email_alert.utils.email import sendEmail


@shared_task
def send_email():
    date_begin = datetime.datetime.now().date()
    date_end = (date_begin + datetime.timedelta(1))

    email_info = datetime.datetime.now().strftime("%Y年%m月%d日备忘录提示:")
    messages = Message.objects.filter(setup_time__range=[date_begin, date_end])
    if len(messages) > 0:
        email_info = "下面是今日注意事项：\n"
        for message in messages:
            email_info += f"{message.message_info}\n"

    sendEmail(email_info)

    return "消息发送成功!"


@shared_task
def print_hello():
    return "hello world!"
