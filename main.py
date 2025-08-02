#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YOLO Badge Project - 主程序

这是一个简单的Python脚本，用于演示项目功能。
作者: chord233
"""

import datetime
import sys

def print_banner():
    """打印项目横幅"""
    banner = """
    ╔══════════════════════════════════════╗
    ║          YOLO Badge Project          ║
    ║      GitHub Achievement Hunter       ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def get_current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    """主函数"""
    print_banner()
    print(f"🚀 项目启动时间: {get_current_time()}")
    print("📋 项目状态: 运行正常")
    print("🎯 目标: 获取GitHub YOLO徽章")
    print("✅ 任务: 创建并合并Pull Request")
    
    # 简单的交互
    try:
        name = input("\n👋 请输入你的名字: ")
        print(f"\n🎉 欢迎 {name}! 祝你成功获得YOLO徽章!")
    except KeyboardInterrupt:
        print("\n\n👋 再见!")
        sys.exit(0)

if __name__ == "__main__":
    main()