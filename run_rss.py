from atut_serv import start_serv
from util.svlog import logs

ver = "2025-04-06 22:14:41"
ts = 1743948881
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
