from atut_serv import start_serv
from util.svlog import logs

ver = "2025-04-18 09:14:39"
ts = 1744938879
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
