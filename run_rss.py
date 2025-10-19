from atut_serv import start_serv
from util.svlog import logs

ver = "2025-10-19 18:12:35"
ts = 1760868755
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
