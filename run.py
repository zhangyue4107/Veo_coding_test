import os
import shutil
import pytest
import click
from common.log import logger


def clear_last_testing_data():
    def clear_folder(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if os.path.isfile(file_path):
                os.remove(file_path)
            
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    folder_list = ['allure-report', 'logs', 'screenshots']
    try:
        for folder in folder_list:
            clear_folder(folder)
    except Exception as e:
        logger.error("清除文件夹失败{}".format(e))
        pass


@click.command()
@click.option('-e', '--env')
def run(**options):
    clear_last_testing_data()
    if not options['env']:
        env = 'dev'
    else:
        env = options['env']
    logger.info('当前运行环境为:{}'.format(env))
    pytest.main(['./test_case/test_2_homepage', '--env=' + env])


if __name__ == '__main__':
    run()
