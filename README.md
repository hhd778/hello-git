# hello-git

一个用来验证 Git / GitHub 工作流的练手仓库。

它的作用不是提供什么功能，而是让你完整走一遍「改文件 → 提交 → 推送 → 在 GitHub 网页上看到」的流程。跑通之后，这个仓库可以删掉，或者直接改造成你的第一个真实项目。

## 效果

```bash
$ python hello.py
你好，hhd778
当前时间：2026-11-20 22:50:09
```

## 安装

只需要 Python 3.8 以上，没有第三方依赖。

```bash
git clone git@github.com:hhd778/hello-git.git
cd hello-git
```

## 使用

```bash
python hello.py
```

## 目录结构

```
hello-git/
├── hello.py        # 入口脚本
├── README.md       # 本文件
├── LICENSE         # MIT 许可证
└── .gitignore      # 告诉 Git 哪些文件不要提交
```

## 许可证

本项目使用 [MIT 许可证](LICENSE)。
