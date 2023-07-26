# 用于一键启动django和celery
import argparse
import os

DEPLOY_DEBUG = 'debug'
DEPLOY_PRODUCT = 'product'



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
    # 参考博客:https://blog.csdn.net/Mr_Li1/article/details/89353276
    if os.path.exists('./celerybeat-schedule'):
        os.remove('./celerybeat-schedule')

    cmd0 = "python3 manage.py runserver &"
    os.system(cmd0)

    cmd1 = "celery -A backend worker -l info &"
    os.system(cmd1)

    cmd2 = "celery -A backend beat &"
    os.system(cmd2)

    # TODO:每次执行完都得去杀进程,需要改进


def deploy_product():
    pass


def main_process():
    # deploy_type = getTerminalInput()
    deploy_type = 'debug'
    if deploy_type == DEPLOY_DEBUG:
        deploy_debug()
    else:
        deploy_product()


if __name__ == "__main__":
    main_process()
