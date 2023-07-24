import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class WangYiEmail:
    # https://www.cnblogs.com/hsyi/p/13569841.html
    Email_Host = "smtp.163.com"
    Port = 25
    SSL_Port = 465

    Email_User = "m15230488845"
    Email_Password = "TAGWCIWHUQDWLUNB"
    Email_Sender = "m15230488845@163.com"

    # Email_Receivers = _settings['email']['email-receivers']

    EmailSenderName = "Mr.WildFire"
    EmailTitle = "事件提醒"
    Email_list = ["m15230488845@163.com"]


class EmailSmtp:
    """
    邮件发送
    """
    module = 'WangYiSmtp'
    # 附件列表
    atts = []

    def __init__(self):
        self.port = WangYiEmail.Port
        self.ssl_port = WangYiEmail.SSL_Port
        self.mail_host = WangYiEmail.Email_Host
        self.mail_user = WangYiEmail.Email_User
        self.mail_pass = WangYiEmail.Email_Password
        self.sender = WangYiEmail.Email_Sender
        self.__receivers = None

    def setReceivers(self, receivers):
        self.__receivers = receivers

    def getReceivers(self):
        return self.__receivers

    def send_email(self, message):
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.mail_host, self.port)
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            smtpObj.sendmail(self.sender, self.__receivers, message.as_string())
            # 退出
            smtpObj.quit()
            self.atts = []
        except smtplib.SMTPException as e:
            print(traceback.format_exc())
            print('error', e)  # 打印错误

    def make_message(self, content):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header(WangYiEmail.EmailSenderName, 'utf-8')
        message['To'] = Header(",".join(self.__receivers), 'utf-8')
        message['Subject'] = Header(WangYiEmail.EmailTitle, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText(content, 'html', 'utf-8'))
        for att in self.atts:
            message.attach(att)
        self.atts = []
        return message


def sendEmail(_message):
    email_list = WangYiEmail.Email_list
    emailSmtp = EmailSmtp()
    # 设置收件人
    emailSmtp.setReceivers(email_list)
    # 创建消息
    message = emailSmtp.make_message(_message)
    # 发送消息
    emailSmtp.send_email(message)
    print("测试结果已发送邮件！")


def setHtmlMessage(message):
    return message
