# 民宿房间管理系统

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
- [ ] 添加预订系统
- [ ] 添加收入统计
- [ ] 添加房间图片上传功能
