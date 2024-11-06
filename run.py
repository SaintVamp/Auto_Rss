from atut_serv import start_serv
from util.svlog import logs

ver = "2024-11-07 00:03:24"
ts = 1730909004
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
