from PyQt5 import QtCore, QtGui, QtWidgets
from api.openai_api import get_image_description
from utils.file_handler import get_image_file, encode_image_to_base64
from utils.config import DB_PATH
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenAI 이미지 설명 프로그램")
        self.setGeometry(100, 100, 700, 500)
        self.image_path = None
        self.init_ui(self)
        self.init_db()

    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 300, 300))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 400, 300, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(35, 450, 310, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 370, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 50, 500, 700))
        self.label_4.setStyleSheet("border: 1px solid black")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색하기"))
        self.label_2.setText(_translate("MainWindow", "매장 사진"))
        self.label_3.setText(_translate("MainWindow", "식당 검색 링크"))

    def init_db(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS image_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image BLOB,
                prompt TEXT,
                response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def load_image(self):
        try:
            path = get_image_file()
            if path:
                pixmap = QtGui.QPixmap(path).scaled(self.image_label.width(), self.image_label.height(), QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    raise ValueError("이미지를 불러올 수 없습니다.")
                self.image_label.setPixmap(pixmap)
                self.image_path = path
        except Exception as e:
            QMessageBox.warning(self, "오류", f"이미지 불러오기 실패: {e}")


    def generate_description(self):
        if not self.image_path:
            self.result_output.setPlainText("이미지를 먼저 불러와 주세요.")
            return

        prompt = self.text_input.toPlainText()

        try:
            base64_image = encode_image_to_base64(self.image_path)
            result = get_image_description(self.image_path, prompt)
            self.result_output.setPlainText(result)

            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                with open(self.image_path, "rb") as f:
                    image_blob = f.read()
                cursor.execute('''
                    INSERT INTO image_logs (image, prompt, response) VALUES (?, ?, ?)
                ''', (image_blob, prompt, result))
                conn.commit()

        except Exception as e:
            self.result_output.setPlainText(f"응답 오류 발생: {e}")
