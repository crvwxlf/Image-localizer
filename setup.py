from cx_Freeze import setup, Executable
import sys
from ImageLocalizer import __version__

build_exe_options = {"packages": [
    "sys", "webbrowser", "GPSPhoto", "PySide2"], 'include_files': ["img/"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Image localizer",
      version=__version__,
      author="Kwalixx",
      description="Gui tool to extract GPS datas from image",
      options={"build_exe": build_exe_options},
      executables=[Executable("ImageLocalizer.py", base=base, icon="img/imageLocalizer-icons.ico")])
