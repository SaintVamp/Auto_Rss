from atut_serv import start_serv
from util.svlog import logs

ver = "2025-01-25 17:18:11"
ts = 1737796691
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
