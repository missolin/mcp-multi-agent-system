# MCP 多 Agent 纠偏系统

这是一个基于 Model Context Protocol (MCP) 的多 Agent 协作系统，用于自动化需求分析、方案设计、代码构建和错误修正。

## 项目结构

```
.
├── 4/                          # ABC 纠偏系统核心代码
│   ├── agents/                 # Agent 定义文档
│   │   ├── agent-a-builder.md
│   │   ├── agent-b-bugfinder.md
│   │   ├── agent-c-checker.md
│   │   ├── agent-q-questioner.md
│   │   └── agent-s-solution-designer.md
│   ├── mcp_server.py          # MCP 服务器实现
│   ├── mcp_client.py          # MCP 客户端
│   ├── visual_verify.py       # 视觉验证工具
│   └── requirements.txt       # Python 依赖
├── mcp-demo-server.py         # MCP 演示服务器
├── test-mcp-client.py         # MCP 客户端测试
└── melody-generator.html      # 示例项目
```

## 功能特性

### ABC 纠偏系统
- **Agent Q (Questioner)**: 质疑需求，发现潜在问题
- **Agent S (Solution Designer)**: 设计多个方案并对比优缺点
- **Agent D (Decision Maker)**: 自动选择最佳方案
- **Agent A (Builder)**: 构建完整解决方案
- **Agent B (Bug Finder)**: 发现事实级错误
- **Agent C (Checker)**: 检查需求对齐

### Git Agent（新增）
- **智能询问**: 在开始时询问是否需要 Git 集成
- **自动提交**: 每次完成任务后自动提交代码
- **版本管理**: 自动生成版本号（v1.0.0, v1.1.0, ...）
- **GitHub 集成**: 自动推送到远程仓库
- **灵活配置**: 可以随时启用或禁用

### MCP 演示服务器
提供基础的 MCP 工具和资源：
- `echo`: 回显文本
- `calculate`: 简单计算器
- `demo://info`: 服务器信息资源

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
python3 -m venv mcp-venv
source mcp-venv/bin/activate  # macOS/Linux

# 安装 MCP SDK
pip install -e ./mcp-python-sdk

# 安装项目依赖
pip install -r 4/requirements.txt
```

### 2. 配置 Git Agent（可选）

如果需要自动提交到 GitHub：

1. 创建 GitHub Personal Access Token
   - 访问：https://github.com/settings/tokens
   - 选择权限：`repo`, `read:org`, `read:user`

2. 在使用时，系统会自动询问是否启用 Git 集成

详细说明请查看：[Git Agent 集成指南](./4/GIT_AGENT_GUIDE.md)

### 3. 测试 MCP 服务器

```bash
# 运行测试客户端
./mcp-venv/bin/python3 test-mcp-client.py
```

## 文档

- [ABC 纠偏架构设计](./a_b_c_多agent纠偏架构设计文档.md)
- [Git Agent 集成指南](./4/GIT_AGENT_GUIDE.md) ⭐ 新增
- [MCP 部署说明](./MCP-部署说明.md)
- [实现指南](./4/IMPLEMENTATION_GUIDE.md)
- [工作流程](./4/FLOW.md)

## 技术栈

- Python 3.14+
- MCP (Model Context Protocol)
- Selenium (浏览器自动化)
- Playwright (可选)

## License

MIT