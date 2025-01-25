from atut_serv import start_serv
from util.svlog import logs

ver = "2025-01-25 17:05:47"
ts = 1737795947
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
