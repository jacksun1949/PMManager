from cx_Freeze import setup, Executable
setup(
    name="HCGuardian",
    version="1.5",
    description="汇萃进程监控管理器",
    executables = [Executable("PMManager.py", base="win32gui", target_name="HCGuardian.exe", icon="icons\logo.ico")],
    options={
        'build_exe': {
            'packages': ['os', 'sys'],  # 需要包含的包
            'excludes': ['tkinter'],    # 需要排除的包
            'include_files': ['setting.ini', 'data/', 'icons/', 'data/', 'Img/', 'logs/']  # 需要包含的额外文件
        }
    }
)