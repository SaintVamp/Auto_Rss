from atut_serv import start_serv
from util.svlog import logs

ver = "2025-02-08 09:37:02"
ts = 1738978622
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
