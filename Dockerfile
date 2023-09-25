# 使用 Python 作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /usr/local/vomds_mit_python_archive_system

# 复制 requirements.txt 到容器中
COPY requirements.txt .

# 安装所需的依赖项
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --no-cache-dir uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple

# RUN apt-get update && apt-get install -y vim

# 将整个项目复制到容器中
# COPY __init__.py /usr/local/lib/python3.8/site-packages/flask_script/

COPY . .

COPY copy/file/__init__.py /usr/local/lib/python3.8/site-packages/flask_script/

# 暴露 Flask 应用程序的端口
EXPOSE 10405

# 在容器启动时运行的命令
CMD ["uwsgi", "--ini", "uwsgi.ini", "--enable-threads", "--thunder-lock"]



## 使用基础Python映像作为构建环境
#FROM python:3.8 as builder
#
## 设置工作目录
#WORKDIR /usr/local/vomds_mit_python_archive_system
#
## 复制项目文件到工作目录
#COPY requirements.txt .
#
#COPY . .
#
## 使用uWSGI作为运行时环境
#FROM tiangolo/uwsgi-nginx:python3.8
#
## 设置工作目录和复制项目文件
#WORKDIR /usr/local/vomds_mit_python_archive_system
#
#COPY --from=builder /usr/local/vomds_mit_python_archive_system /usr/local/vomds_mit_python_archive_system
#
## 安装所需的依赖项
#RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
#
#RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#
#RUN pip install --no-cache-dir uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
#
#COPY uwsgi.ini /app/uwsgi.ini
##
##RUN rm -rf uwsgi.ini & rm -rf /etc/uwsgi/uwsgi.ini
#
#COPY copy/file/__init__.py /usr/local/lib/python3.8/site-packages/flask_script/
#
## 开放端口（根据您的应用程序需要开放的端口进行修改）
#EXPOSE 8080
#
## 运行uWSGI服务器:
##CMD ["uwsgi", "--ini", "uwsgi.ini", "--enable-threads"]
#
## docker run -d -p 10405:8080 uwsgi-archive:v1.0
##CMD ["uwsgi", "--http", "0.0.0.0:8080", "--module", "manage:app", "--processes", "4", "--threads", "2", "--enable-threads"]