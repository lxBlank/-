# 智能语音交互后端服务（eye_backend）

本项目是基于 **Django** 的后端服务，提供用户管理、消息/社区功能以及语音音频文件的上传与访问等能力，可作为智能语音应用或眼动交互系统的后端支撑。

---

## 功能概览

- **用户模块（`users`）**
  - 用户注册 / 登录 / 注销
  - 用户基本信息管理
  - Token 认证（如使用 `rest_framework.authtoken` 或自定义 token）

- **消息模块（`message`）**
  - 消息/通知的发送与接收
  - 消息的序列化与接口输出（`serializers.py`）
  - 消息记录的持久化存储（`models.py`）

- **社区模块（`community`）**
  - 社区/帖子/评论等相关数据模型
  - 对外提供社区相关的接口（`views.py`、`urls.py`）

- **语音音频处理**
  - 静态音频资源存放于 `static/audio/`
  - 用户语音/录音文件存放于 `media/audio/`
  - 音频文件的上传、访问与播放接口（视项目实际实现而定）

- **工具组件（`tools` 包）**
  - `audioex.py`：音频处理相关工具
  - `baseurl.py`：基础 URL / 常量
  - `my_token.py`：token 相关逻辑
  - `redis_pool.py`：Redis 连接池封装
  - `sms.py`：短信发送工具
  - 其他公共工具模块

---

## 技术栈

- **语言**：Python 3.x
- **框架**：Django（具体版本见 `requirements.txt`）
- **数据库**：SQLite（默认，文件 `db.sqlite3`），可扩展为 MySQL / PostgreSQL
- **缓存 / 消息**：Redis（通过 `tools/redis_pool.py` 使用）
- **依赖管理**：`pip` + `requirements.txt`

---

## 环境准备

1. **安装 Python 3**

   请确保本机已安装 Python 3.8+，并已添加到环境变量。

2. **创建虚拟环境（推荐）**

   ```bash
   # Windows PowerShell 示例
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **安装依赖**

   在项目根目录（`eye_backend0414_1`）下执行：

   ```bash
   pip install -r requirements.txt
   ```

---

## 项目结构（简要）

```text
eye_backend0414_1/
  ├─ eye_backend/         # Django 项目配置（settings、urls、wsgi、asgi 等）
  ├─ users/               # 用户模块
  ├─ message/             # 消息模块
  ├─ community/           # 社区模块
  ├─ tools/               # 公共工具（音频、短信、Redis、token 等）
  ├─ media/audio/         # 用户或业务相关音频文件
  ├─ static/audio/        # 静态音频资源
  ├─ templates/           # 模板目录（如果使用 Django 模板）
  ├─ manage.py            # Django 管理脚本
  ├─ requirements.txt     # Python 依赖
  └─ README.md            # 项目说明
```

---

## 本地运行

1. **数据库迁移**

   ```bash
   python manage.py migrate
   ```

2. **创建超级用户（可选，用于管理后台）**

   ```bash
   python manage.py createsuperuser
   ```

3. **启动开发服务器**

   ```bash
   python manage.py runserver
   ```

   默认地址为：`http://127.0.0.1:8000/`

4. **访问 Django 管理后台**

   在浏览器访问：

   `http://127.0.0.1:8000/admin/`

   使用上面创建的超级用户账号登录。

---

## 静态文件与媒体文件

- **静态文件**：位于 `static/` 目录（如 `static/audio/hello.mp3` 等），用于前端直接访问的固定资源。
- **媒体文件**：位于 `media/` 目录（如 `media/audio/20230407211411.mp3` 等），通常由用户上传或业务运行时生成。

请确保在 `settings.py` 中正确配置了：

- `STATIC_URL` / `STATIC_ROOT` 或 `STATICFILES_DIRS`
- `MEDIA_URL` / `MEDIA_ROOT`

开发环境中可以通过 `urls.py` 暴露静态和媒体文件访问。

---

## 路由说明（简要）

项目主路由位于 `eye_backend/urls.py`，各 app 自己的路由通常在：

- `users/urls.py`
- `message/urls.py`
- `community/urls.py`

如需新增接口，请在对应 app 的：

1. `views.py` 中编写视图函数或类视图；
2. `urls.py` 中添加路由配置；
3. 如有需要，配合 `serializers.py`、`models.py` 修改数据结构和序列化逻辑。

---

## 部署建议（简要）

生产环境中建议：

- 使用 **Gunicorn / uWSGI + Nginx** 或其他 WSGI/ASGI 服务器部署；
- 将静态文件收集到统一目录：

  ```bash
  python manage.py collectstatic
  ```

- 使用 **MySQL / PostgreSQL** 等生产级数据库，而不是 SQLite；
- 配置环境变量以区分开发 / 生产环境（如 `DEBUG`、数据库连接、密钥等）。

---

## 开发规范与建议

- 统一通过 `requirements.txt` 管理依赖；
- 新增/修改模型后记得执行：

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- 提交前尽量运行单元测试（如果已编写）：

  ```bash
  python manage.py test
  ```

---

## 许可证

根据实际情况补充：

- 如果是个人/内部项目，可写：**本项目仅用于学习和内部使用，禁止商业用途。**
- 如果开源，可注明使用的开源协议（如 MIT、Apache-2.0 等）。

---

## 维护者

- 维护者：*在此填写你的名字或团队名称*
- 联系方式：*邮箱 / 微信 / 其他联系方式（可选）*