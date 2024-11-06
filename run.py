from atut_serv import start_serv
from util.svlog import logs

ver = "2024-11-06 18:26:32"
ts = 1730888792
if __name__ == '__main__':
    logs.logger.info(f'主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
