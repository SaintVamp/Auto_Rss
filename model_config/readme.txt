☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆
☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆
☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆

一、拉取镜像：【docker pull saintvamp/auto_rss:latest】
二、创建容器：【docker run -d --network host \
--name=auto_rss \
-e TZ=Asia/Shanghai \
-v /{父目录地址}/atu_release/bdinfo:/auto_rss/bdinfo \
-v /{父目录地址}/atu_release/log:/auto_rss/log \
-v /{父目录地址}/atu_release/config:/auto_rss/config \
-v /{父目录地址}/atu_release/database:/auto_rss/database \
-v /{父目录地址}/atu_release/picture:/auto_rss/picture \
-v /{父目录地址}/{资源存放地址}:/downloads \
saintvamp/auto_rss:latest】
#自行修改-v中冒号前的文件夹地址后，执行一次，此时程序未运行，只是生成容器。
三、修改base_config中config.toml中的内容。
四、源站点选择RSS，直接生成，查询对应的passkey字段
五、从本地的base_config目录中复制finish.sh到qb能读取到的目录
六、在QB设置>下载>运行外部程序，完成时运行外部程序，输入【sh finish.sh "%I"】。比如QB是docker，持久化映射了config目录，finish放在config里，命令行就是【sh /config/finish.sh "%I"】
七、建议QB使用官方4.6.0版本。创建容器命令：【docker run -d --network host \
--name=qb \
-e PUID=911 \
-e PGID=911 \
-e TZ=Asia/Shanghai \
-e accept \
-v /{父目录地址}/config:/config \
-v /{父目录地址}/download:/downloads/disk1 \
--restart always \
qbittorrentofficial/qbittorrent-nox:4.6.0-1】


Q&A：
Q1：base_config里的model-config.toml是干什么的？
A1：这个是最全的配置文件模版。在第一次创建容器后，需要复制model-config.toml一份并改名为config.toml，然后配置config中的必备信息。
另外每次更新model后，重启时程序会自动更新model-config.toml，并将config.toml缺少的配置项补全，但仍需要人工配置此类配置项的值。

Q2：当前支持哪些源站，哪些目标站？
A2：源站支持【观众、季节、憨憨、家园、杜比、HDV、朋友、猫、织梦、优堡、reelflix、FL】
目标站支持【末日、象岛、优堡、麒麟、劳改所、织梦、柠檬、南工大】

Q3：QB没调用finish.sh。
A3：1、ssh进入命令行。
2、【docker exec -it {qb的容器名称或ID} /bin/sh】。
3、【sh /{finish存放路径}/finish.sh {任意字符}】。
4、查看工具日志是否有“收到种子”的打印
5、如果sh找不到文件，就在容器内找到正确的finish.sh文件的位置，输入pwd查看详细地址

Q4：是否可以手动添加资源链接发布。
A4：可以，但必须是当前工具支持的网站，通过调用"http://127.0.0.1:45678/sv/api/addTorrent?h={QB种子信息中的信息哈希值}&u={源网站的域名}&i={源网站的种子id}&hr={源网站此种子的HR标记}&sf={站点架构}"
举例源站种子页面是>>>>https://audiences.me/details.php?id=306417
源网站的域名：audiences.me
源网站的种子id：306417
源网站此种子的HR标记：有标记写1，没标记写0
站点架构：目前支持两类，选一个填写：np|u3d|fl
如果是curl命令要把url整体引号，浏览器则无影响

Q5：如何删除发种机种记录的种子信息。
A5：通过调用"http://127.0.0.1:45678/sv/api/delTorrent?h={QB种子信息中的信息哈希值}"
如果是curl命令要把url整体引号，浏览器则无影响

Q6：如何针对指定站重新发布。
A6：通过调用"http://127.0.0.1:45678/sv/api/reload?h={QB种子信息中的信息哈希值}&ts={目标站的域名}"
域名查询方式同Q4
如果是curl命令要把url整体引号，浏览器则无影响

Q7：配置中的RSS链接怎么填。
A7：从你想要发布的网站选择RSS后生成的链接中【是生成的链接中！！！不是控制面板的！！！】，只需要找到passkey对应的内容，比如原链接可能为【https://www.sv.com/rss?passkey=123321&cat=1&dl=true】那么passkey对应的就是【123321】

