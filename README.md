# HCGuardian
=========


### 欢迎使用 HCGuardian ！ 

它一个进程监控管理小程序，用于监控守护正在运行的进程，可以方便的增加、修改、删除项目。

当发现监控中进程被意外关闭时可以自动开启。同时也可以启动，结束，重启进程。 

### 当前版本：1.0 

### 开发语言： python、wxpython 

### 运行平台：windows

### 安装包制作：

**使用cx_Freeze**

cx_Freeze是另一个用于将Python程序转换为可执行文件的库。以下是使用cx_Freeze的基本步骤：

1. 安装cx_Freeze：使用pip安装cx_Freeze：
    pip install cx_Freeze
2. 创建setup.py文件：在你的Python脚本所在的目录中，创建一个名为setup.py的新文件，并添加以下内容：
    from cx_Freeze import setup, Executable
    setup(
        name="Your Program",
        version="1.0",
        description="Description of your program",
        executables = [Executable("PMManager.py", base="win32gui", target_name="HCGuardian.exe", icon="icons\logo.ico")]
    )
    确保将“Your Program”和“Description of your program”替换为你的程序的名称和描述，并将“your_script.py”替换为你的Python脚本的文件名。

3. 构建可执行文件：在命令行中，导航到你的Python脚本所在的目录，然后运行以下命令：
    python setup.py build
    这将生成一个build文件夹，里面包含了可执行文件和其他依赖文件。

4. 运行可执行文件：找到build文件夹中的.exe文件，双击运行它。

### 注意事项
1. 确保你的Python脚本是可执行的，并且没有任何语法错误。
2. 在打包之前，最好在一个干净的虚拟环境中安装所有必要的依赖项，以避免潜在的依赖冲突。
3. 测试生成的可执行文件在不同的计算机和操作系统上是否能够正常运行。


