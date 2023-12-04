# syz
常用python工具

## common
```python
import syz
```
+ 时间工具
+ 文件名后缀
+ 日志工具
+ CPU物理核心数


# 打包方法
1. 修改版本 setup.py
2. 运行
```bash
python3 setup.py sdist
twine upload dist/syz-0.1.0.tar.gz
```
