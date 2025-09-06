from atut_serv import start_serv
from util.svlog import logs

ver = "2025-09-06 21:53:12"
ts = 1757166792
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
