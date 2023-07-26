# 用于一键启动django和celery
import argparse
import os
import subprocess

DEPLOY_DEBUG = 'debug'
DEPLOY_PRODUCT = 'product'
CELERYBEAT_SCHEDULE = './celerybeat-schedule'
PRODUCT_PORT = 18000


def getTerminalInput():
    # 接收数据
    parser = argparse.ArgumentParser()
    parser.add_argument('deploy_type', help='How the project is deployed')

    # 后续逻辑处理
    args = parser.parse_args()
    deploy_type = args.deploy_type
    if deploy_type not in [DEPLOY_DEBUG, DEPLOY_PRODUCT]:
        raise Exception(f"位置参数请填 {DEPLOY_DEBUG} 或者 {DEPLOY_PRODUCT}")
    return deploy_type


def deploy_debug():
    if os.path.exists(CELERYBEAT_SCHEDULE):  # 在每次重启celery前删除celerybeat-schedule文件
        os.remove(CELERYBEAT_SCHEDULE)

    info1 = subprocess.getoutput("ps -ef | grep celery")  # 根据pid杀死celery进程
    lines = info1.split("\n")
    if len(lines) > 2:
        lines = lines[0:2]
        for line in lines:
            keywords = line.split()
            cmd = f"kill -9 {keywords[1]}"
            os.system(cmd)

    info2 = subprocess.getoutput(f"lsof -i:{PRODUCT_PORT}")  # 根据pid杀死django进程
    if info2 != "":
        keywords = info2.split("\n")[1]
        keywords = keywords.split()
        cmd = f"kill -9 {keywords[1]}"
        os.system(cmd)

    # 参考博客:https://blog.csdn.net/Mr_Li1/article/details/89353276
    cmd0 = "python3 manage.py runserver &"
    os.system(cmd0)

    cmd1 = "celery -A backend worker -l info &"
    os.system(cmd1)

    cmd2 = "celery -A backend beat &"
    os.system(cmd2)


def deploy_product():
    """
    部署,暂时使用nohup
    """
    if os.path.exists(CELERYBEAT_SCHEDULE):  # 在每次重启celery前删除celerybeat-schedule文件
        os.remove(CELERYBEAT_SCHEDULE)

    info1 = subprocess.getoutput("ps -ef | grep celery")  # 根据pid杀死celery进程
    lines = info1.split("\n")
    if len(lines) > 2:
        lines = lines[0:2]
        for line in lines:
            keywords = line.split()
            cmd = f"kill -9 {keywords[1]}"
            os.system(cmd)

    info2 = subprocess.getoutput(f"lsof -i:{PRODUCT_PORT}")  # 根据pid杀死django进程
    if info2 != "":
        keywords = info2.split("\n")[1]
        keywords = keywords.split()
        cmd = f"kill -9 {keywords[1]}"
        os.system(cmd)

    # 参考博客:https://blog.csdn.net/Mr_Li1/article/details/89353276
    cmd0 = "python3 manage.py runserver 18000 > ./logs/django.out &"
    os.system(cmd0)

    cmd1 = "nohup celery -A backend worker -l info > ./logs/celery.out &"
    os.system(cmd1)

    cmd2 = "nohup celery -A backend beat > ./logs/celery_beat.out &"
    os.system(cmd2)


def main_process():
    # deploy_type = getTerminalInput()
    deploy_type = 'debug'
    if deploy_type == DEPLOY_DEBUG:
        deploy_debug()
    else:
        deploy_product()


if __name__ == "__main__":
    main_process()
