"""hello-git 入口脚本。

只做两件事：打印一句问候、打印当前时间。
存在的意义是让这个仓库有真实的代码可提交，方便验证 Git 工作流。
"""

import sys
from datetime import datetime


def greet(name: str) -> str:
    """返回一句中文问候。"""
    return f"你好，{name}"


def main() -> None:
    # 命令行第一个参数作为名字，不传就用默认值
    name = sys.argv[1] if len(sys.argv) > 1 else "hhd778"
    print(greet(name))
    print(f"当前时间：{datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
