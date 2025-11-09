from atut_serv import start_serv
from util.svlog import logs

ver = "2025-11-09 22:03:09"
ts = 1762696989
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
