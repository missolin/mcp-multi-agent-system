#!/usr/bin/env python3
"""
MCP 客户端测试脚本
用于测试 MCP 服务器的功能

版本: v1.1.0
更新: 添加详细的测试输出和错误处理
"""
import asyncio
import sys
import time
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def test_mcp_server():
    """测试 MCP 服务器"""
    print("=" * 60)
    print("🚀 MCP 客户端测试套件")
    print("=" * 60)
    print(f"⏰ 开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    test_results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "errors": []
    }
    
    try:
        # 连接到服务器（使用虚拟环境中的 Python）
        print("📡 连接到 MCP 服务器...")
        server_params = StdioServerParameters(
            command="./mcp-venv/bin/python3",
            args=["mcp-demo-server.py"]
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # 初始化会话
                print("🔌 初始化会话...")
                await session.initialize()
                print("✅ 会话初始化成功\n")
                print("-" * 60)
            
                # 测试 1: 列出所有工具
                test_results["total"] += 1
                print("\n📋 测试 1: 列出可用工具")
                try:
                    tools = await session.list_tools()
                    print(f"   发现 {len(tools.tools)} 个工具:")
                    for i, tool in enumerate(tools.tools, 1):
                        print(f"   {i}. {tool.name}")
                        print(f"      描述: {tool.description}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"列出工具失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
                
                # 测试 2: echo 工具
                test_results["total"] += 1
                print("\n🔧 测试 2: echo 工具")
                try:
                    test_message = "Hello MCP!"
                    print(f"   输入: {test_message}")
                    result = await session.call_tool("echo", {"message": test_message})
                    for content in result.content:
                        print(f"   输出: {content.text}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"echo 工具失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
                
                # 测试 3: calculate 工具
                test_results["total"] += 1
                print("\n🔧 测试 3: calculate 工具")
                try:
                    expression = "10 + 20 * 3"
                    print(f"   表达式: {expression}")
                    result = await session.call_tool("calculate", {"expression": expression})
                    for content in result.content:
                        print(f"   {content.text}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"calculate 工具失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
                
                # 测试 4: 错误处理 - 无效表达式
                test_results["total"] += 1
                print("\n🔧 测试 4: 错误处理（无效表达式）")
                try:
                    invalid_expression = "1 / 0"
                    print(f"   表达式: {invalid_expression}")
                    result = await session.call_tool("calculate", {"expression": invalid_expression})
                    for content in result.content:
                        print(f"   {content.text}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过（正确处理了错误）")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"错误处理测试失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
                
                # 测试 5: 列出资源
                test_results["total"] += 1
                print("\n📦 测试 5: 列出可用资源")
                try:
                    resources = await session.list_resources()
                    print(f"   发现 {len(resources.resources)} 个资源:")
                    for i, resource in enumerate(resources.resources, 1):
                        print(f"   {i}. {resource.uri}")
                        print(f"      名称: {resource.name}")
                        # mimeType 可能不存在，使用 getattr 安全访问
                        mime_type = getattr(resource, 'mimeType', 'N/A')
                        print(f"      类型: {mime_type}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"列出资源失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
                
                # 测试 6: 读取资源
                test_results["total"] += 1
                print("\n📖 测试 6: 读取资源内容")
                try:
                    resource_uri = "demo://info"
                    print(f"   资源 URI: {resource_uri}")
                    resource_content = await session.read_resource(resource_uri)
                    print("   内容:")
                    for content in resource_content.contents:
                        # 只显示前 200 个字符
                        text = content.text
                        if len(text) > 200:
                            print(f"   {text[:200]}...")
                        else:
                            print(f"   {text}")
                    test_results["passed"] += 1
                    print("   ✅ 测试通过")
                except Exception as e:
                    test_results["failed"] += 1
                    test_results["errors"].append(f"读取资源失败: {str(e)}")
                    print(f"   ❌ 测试失败: {str(e)}")
                
                print("-" * 60)
    
    except Exception as e:
        print(f"\n❌ 连接失败: {str(e)}")
        test_results["errors"].append(f"连接失败: {str(e)}")
        return 1
    
    # 打印测试摘要
    print("\n" + "=" * 60)
    print("📊 测试摘要")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"✅ 通过: {test_results['passed']}")
    print(f"❌ 失败: {test_results['failed']}")
    
    if test_results['failed'] > 0:
        print("\n❌ 失败的测试:")
        for i, error in enumerate(test_results['errors'], 1):
            print(f"   {i}. {error}")
    
    success_rate = (test_results['passed'] / test_results['total'] * 100) if test_results['total'] > 0 else 0
    print(f"\n成功率: {success_rate:.1f}%")
    print(f"⏰ 结束时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    if test_results['failed'] > 0:
        print("\n⚠️  部分测试失败")
        return 1
    else:
        print("\n✅ 所有测试通过!")
        return 0


if __name__ == "__main__":
    exit_code = asyncio.run(test_mcp_server())
    sys.exit(exit_code)
