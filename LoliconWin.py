import sys

import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *

height = 400
width = 300


class LoliconWin:
    def __init__(self):
        # 初始化Qt应用
        self.app = QApplication(sys.argv)
        self.win = QMainWindow()

        # 创建QWidget和布局
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)

        # 创建QMediaPlayer和QVideoWidget
        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()

        # 将 QMediaPlayer 和 QVideoWidget 移动到当前线程
        self.media_player.moveToThread(self.app.thread())
        self.video_widget.moveToThread(self.app.thread())

        self.layout.addWidget(self.video_widget)

        # 设置QMediaPlayer的输出到QVideoWidget
        self.media_player.setVideoOutput(self.video_widget)

        # 加载视频文件
        file_path = "/home/vina/PycharmProjects/Lolicon/media/dance.mp4"
        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media_content)

    def green_screen_to_transparent(self, frame):
        # 定义绿色的HSV范围
        lower_green = np.array([40, 40, 40])
        upper_green = np.array([80, 255, 255])

        # 将图像转换为HSV颜色空间
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 创建掩码
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # 将掩码取反，得到绿幕区域以外的区域
        result = cv2.bitwise_and(frame, frame, mask=~mask)

        return result

    def convert_cvimage_to_qpixmap(self, cvimage):
        height, width, channel = cvimage.shape
        bytes_per_line = 3 * width
        q_image = QImage(cvimage.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image.rgbSwapped())
        return q_pixmap

    def run(self):
        # 播放视频
        self.media_player.play()

        self.widget.show()

        while not self.media_player.isVideoAvailable():
            self.app.processEvents()

        cap = cv2.VideoCapture("/home/vina/PycharmProjects/Lolicon/media/dance.mp4")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 将绿幕转换为透明
            processed_frame = self.green_screen_to_transparent(frame)

            # 将OpenCV图像转换为QPixmap
            q_pixmap = self.convert_cvimage_to_qpixmap(processed_frame)

            # 更新 QLabel 的 pixmap
            self.video_widget.videoOutput().widget().setPixmap(q_pixmap)

            # 处理 Qt 事件
            self.app.processEvents()

        sys.exit(self.app.exec_())


