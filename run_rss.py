from atut_serv import start_serv
from util.svlog import logs

ver = "2024-12-27 10:25:21"
ts = 1735266321
if __name__ == '__main__':
    logs.logger.info(f'RSS总控主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
