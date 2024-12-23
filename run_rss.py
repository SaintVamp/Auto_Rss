from atut_serv import start_serv
from util.svlog import logs

ver = "2024-12-23 22:25:43"
ts = 1734963943
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
