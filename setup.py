from cx_Freeze import setup, Executable
setup(
    name="HCGuardian",
    version="1.0",
    description="汇萃进程监控管理器",
    executables = [Executable("PMManager.py", base="win32gui", target_name="HCGuardian.exe", icon="icons\logo.ico")]
)