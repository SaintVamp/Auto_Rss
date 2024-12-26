from atut_serv import start_serv
from util.svlog import logs

ver = "2024-12-26 22:57:26"
ts = 1735225046
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
