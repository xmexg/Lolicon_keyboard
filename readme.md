# Lolicon keyboard
+ 萝莉键盘  
+ 监听 `/dev/input/eventX` 键盘当用户触发关键词时会弹出萝莉摇  
+ 只适用于(kali)`linux`

# 现状
我只写完了键盘检测功能,输入`luoli`和`lly`会触发, 但播放视频功能没写完  
我希望输入`luoli`时会右下角播放背景透明的绿幕视频,输入`lly`时全屏无法停止地播放一遍爆萌视频  

# 混乱的桌面环境
gtk -> tk -> qt

# 不要看这份安装步骤
+ GTK  
  `sudo apt install libgtk-4-dev` 

+ libgtk-4-media-gstreamer  
  `sudo apt install libgtk-4-media-gstreamer`
 
+ <b>[PyGObject, pycairo](https://pygobject.readthedocs.io/en/latest/getting_started.html)</b>  
  1. 首先安装 `sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config gir1.2-gtk-4.0`  
  2. 然后安装 `pip3 install PyGObject` 和 `pip3 install pycairo`  

+ python3-tk  
  `sudo apt-get install python3-tk`
