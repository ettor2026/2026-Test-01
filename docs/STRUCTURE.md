# 项目文件结构（MVP）

```text
2026-Test-01/
├── app.py                      # Python HTTP 服务入口与API路由
├── requirements.txt            # 依赖
├── docs/
│   ├── PRD.md                  # 产品需求文档
│   └── STRUCTURE.md            # 文件结构说明
├── services/
│   ├── riddle_generator.py     # 本地化灯谜生成逻辑
│   └── poster_generator.py     # 海报提示词与文案生成逻辑
├── static/
│   ├── style.css               # 页面样式
│   └── app.js                  # 前端交互逻辑
├── templates/
│   └── index.html              # 单页UI
└── tests/
    └── test_services.py        # 核心服务测试
```
