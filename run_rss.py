from atut_serv import start_serv
from util.svlog import logs

ver = "2025-09-23 10:48:05"
ts = 1758595685
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
