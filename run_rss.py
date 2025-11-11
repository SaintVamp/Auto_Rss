from atut_serv import start_serv
from util.svlog import logs

ver = "2025-11-11 22:09:02"
ts = 1762870142
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
