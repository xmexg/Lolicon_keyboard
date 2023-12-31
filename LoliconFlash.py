import sys
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout


def Flash():
    app = QApplication(sys.argv)
    win = QMainWindow()
    widget = QWidget()
    layout = QVBoxLayout(widget)

    # 创建QMediaPlayer和QVideoWidget
    media_player = QMediaPlayer()
    video_widget = QVideoWidget()

    layout.addWidget(video_widget)

    # 设置QMediaPlayer的输出到QVideoWidget
    media_player.setVideoOutput(video_widget)

    # 加载视频文件
    file_path = os.getcwd()+"/media/flash.mp4"
    media_content = QMediaContent(QUrl.fromLocalFile(file_path))
    media_player.setMedia(media_content)

    # 播放视频
    media_player.play()

    widget.show()
    sys.exit(app.exec_())


class LoliconFlash:
    pass
