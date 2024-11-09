from atut_serv import start_serv
from util.svlog import logs

ver = "2024-11-09 21:29:20"
ts = 1731158960
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
