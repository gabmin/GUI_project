from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import base64

def get_image_file():
    path, _ = QFileDialog.getOpenFileName(None, '이미지 선택', '', 'Images (*.png *.jpg *.jpeg)')
    return path


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def load_image(self):
    try:
        path = get_image_file()
        if path:
            pixmap = QPixmap(path).scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
            if pixmap.isNull():
                raise ValueError("이미지를 불러올 수 없습니다.")
            self.image_label.setPixmap(pixmap)
            self.image_path = path
    except Exception as e:
        QMessageBox.warning(self, "오류", f"이미지 불러오기 실패: {e}")