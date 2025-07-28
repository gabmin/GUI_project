from PyQt5 import QtCore, QtWidgets
from api.openai_api import generate_description
from utils.file_handler import load_image
from utils.db_handler import init_db


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 700, 500)
        self.image_path = None
        self.init_ui(self)
        init_db(self)

    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 630)
        MainWindow.setStyleSheet("background-color: #fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(60, 40, 300, 30))
        self.main_title.setStyleSheet("font-size: 32px;")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(60, 90, 300, 50))
        self.description.setStyleSheet("font-size: 13px;")
        self.description.setWordWrap(True)

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(60, 150, 300, 300))
        self.image_label.setStyleSheet("border: 1px solid #b2b2b2; border-radius: 3px; background-color: #f0f0f0")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.upload_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_button.setGeometry(QtCore.QRect(60, 470, 300, 40))
        self.upload_button.setStyleSheet("border-radius: 3px; border: 1px solid rgb(178, 177, 179)")
        self.upload_button.clicked.connect(lambda: load_image(self))

        self.request_button = QtWidgets.QPushButton(self.centralwidget)
        self.request_button.setGeometry(QtCore.QRect(60, 530, 300, 40))
        self.request_button.setStyleSheet("border-radius: 3px; border: 1px solid rgb(178, 177, 179)")
        self.request_button.clicked.connect(lambda: generate_description(self))

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(390, 90, 460, 480))
        self.result_label.setStyleSheet("font-size: 14px; padding: 10px; border: 1px solid #b2b2b2; border-radius: 3px; background-color: #f0f0f0")
        self.result_label.setText("")
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(QtCore.Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "오늘은 뭐 먹지?"))
        self.main_title.setText(_translate("MainWindow", "오늘은 뭐 먹지?"))
        self.description.setText(_translate("MainWindow", "냉장고에 있는 재료로 뭘 만들어 먹을 수 있을지 레시피를 확인해보세요!"))
        self.image_label.setText(_translate("MainWindow", "사진을 등록해주세요."))
        self.upload_button.setText(_translate("MainWindow", "이미지 등록하기"))
        self.request_button.setText(_translate("MainWindow", "레시피 보기"))


