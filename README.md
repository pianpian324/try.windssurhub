# 民宿房间管理系统

新建decfenzhi
一个简单的民宿房间管理系统，用于管理房间状态、价格和基本信息。

## 功能特点

- 查看所有房间状态
- 添加新房间
- 更新房间状态（可用/已占用/维护中）
- 显示房间基本信息（房间号、类型、价格）

## 技术栈

- Python 3.x
- Flask
- SQLite
- Bootstrap 5

## 安装步骤

1. 克隆仓库：
```bash
git clone [你的仓库URL]
cd guesthouse-manager
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python app.py
```

4. 在浏览器中访问：`http://localhost:5000`

## 使用说明

1. 首页显示所有房间信息
2. 点击"添加新房间"按钮可以添加新的房间
3. 每个房间卡片都可以更新房间状态

## 开发计划

- [ ] 添加用户认证
  - 技术路径：使用 Flask-Login 进行用户会话管理，bcrypt 进行密码哈希
- [ ] 添加预订系统
  - 技术路径：设计预订模型，集成日历组件，添加预订状态管理
- [ ] 添加收入统计
  - 技术路径：使用 SQLAlchemy 进行数据聚合，集成 Chart.js 进行可视化
- [ ] 添加房间图片上传功能
  - 技术路径：使用 Flask-Uploads 处理文件上传，集成云存储（如 AWS S3）
- [ ] 添加多语言支持（中文/英文）
  - 技术路径：使用 Flask-Babel 实现国际化，创建语言资源文件
- [ ] 实现移动端优化
  - 技术路径：使用 Bootstrap 5 的响应式布局，添加 PWA 支持
- [ ] 添加房间评价系统
  - 技术路径：设计评价模型，实现星级评分和评论功能
- [ ] 集成支付网关
  - 技术路径：集成 Stripe 或支付宝 API，实现安全支付流程
- [ ] 开发API接口
  - 技术路径：使用 Flask-RESTful 构建 RESTful API，添加 JWT 认证
- [ ] 添加数据分析仪表盘
  - 技术路径：使用 SQLAlchemy 进行数据分析，集成 AdminLTE 仪表盘模板

  煮好
