##############################################################################
- @Code:    205 Project / C
- @Purpose: 登记并提供上海IT运营中心IT系统所有责任人关系。
- @Author:  Kévin
- @Update:  17 Oct. 2018
##############################################################################

##################
I. 项目文件
##################
- /relation                 项目文件夹。
- relation.db               数据库，记录系统和责任人信息。
- CommonConfigProcessor.py  公共类，读取配置文件config.txt。
- CommonDBProcessor.py      公共类，数据库操作。
- relation.py               使能程序，提供API接口，登记和查询信息。
- config_relation.txt       配置文件，包括端口、认证等。
- start_relation.sh         启动脚本。
- readme_relation.txt       本说明文档。

##################
II. 项目部署条件
##################
- 推荐CentOS 6.9或更高
- 推荐python 2.7.14或更高
- 不需要root账号
- #visudo，增加一句：wangwei ALL=(jtitsm)   ALL
- 正确设置文件和文件夹权限，如db文件及其全路径文件夹必须可写
- requests库：wangwei$pip install --user requests
- flask库：wangwei$pip install --user flask
- flask-httpauth库：wangwei$pip install --user flask-httpauth
- pyOpenSSL库：wangwei$pip install --user pyOpenSSL

##################
III. 项目运行
##################
- 应用账号：jtitsm，部署/运维账号：wangwei
- 修改配置文件：设置正确location
- 启动脚本赋可执行权限：wangwei$chmod +x start_relation.sh
- wangwei$sudo -u jtitsm ./start_relation.sh

##################
IV. 数据库元信息
##################
- 数据库：SQLite3
- 数据库编码：utf-8
CREATE TABLE "asset" (
"ip"  TEXT NOT NULL,
"admin"  TEXT,
"description"  TEXT,
PRIMARY KEY ("ip")
);


