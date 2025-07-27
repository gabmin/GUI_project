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
        # self.init_db()

    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 570)
        MainWindow.setStyleSheet("background-color: #fff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(40, 30, 300, 40))
        self.main_title.setStyleSheet("font-size: 24px")
        self.main_title.setObjectName("label_2")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(40, 70, 300, 40))
        self.description.setObjectName("label_3")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(40, 120, 300, 300))
        self.image_label.setStyleSheet("border: 1px solid #b2b2b2; border-radius: 3px; background-color: #f0f0f0")
        self.image_label.setText("사진을 등록해주세요.")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("label")

        self.image_upload_button = QtWidgets.QPushButton(self.centralwidget)
        self.image_upload_button.setGeometry(QtCore.QRect(40, 440, 300, 40))
        self.image_upload_button.setObjectName("pushButton_2")
        self.image_upload_button.setStyleSheet("border-radius: 3px; border: 1px solid rgb(178, 177, 179)")
        self.image_upload_button.clicked.connect(lambda: load_image(self))

        self.request_button = QtWidgets.QPushButton(self.centralwidget)
        self.request_button.setGeometry(QtCore.QRect(40, 500, 300, 40))
        self.request_button.setObjectName("pushButton")
        self.request_button.setStyleSheet("border-radius: 3px; border: 1px solid rgb(178, 177, 179)")
        self.request_button.clicked.connect(lambda: generate_description(self))

        self.money_title = QtWidgets.QLabel(self.centralwidget)
        self.money_title.setGeometry(QtCore.QRect(380, 80, 100, 20))
        self.money_title.setStyleSheet("font-size: 16px")
        self.money_title.setObjectName("label_4")

        self.money_contents = QtWidgets.QLabel(self.centralwidget)
        self.money_contents.setGeometry(QtCore.QRect(380, 110, 290, 70))
        self.money_contents.setStyleSheet("background-color: #f0f0f0; border: 1px solid #b2b2b2; border-radius: 3px")
        self.money_contents.setWordWrap(True)
        self.money_contents.setAlignment(QtCore.Qt.AlignTop)
        self.money_contents.setObjectName("textEdit")

        self.love_title = QtWidgets.QLabel(self.centralwidget)
        self.love_title.setGeometry(QtCore.QRect(380, 200, 100, 20))
        self.love_title.setStyleSheet("font-size: 16px")
        self.love_title.setObjectName("label_5")

        self.love_contents = QtWidgets.QLabel(self.centralwidget)
        self.love_contents.setGeometry(QtCore.QRect(380, 230, 290, 70))
        self.love_contents.setStyleSheet("background-color: #f0f0f0; border: 1px solid #b2b2b2; border-radius: 3px")
        self.love_contents.setWordWrap(True)
        self.love_contents.setAlignment(QtCore.Qt.AlignTop)
        self.love_contents.setObjectName("textEdit_2")

        self.health_title = QtWidgets.QLabel(self.centralwidget)
        self.health_title.setGeometry(QtCore.QRect(380, 320, 100, 20))
        self.health_title.setStyleSheet("font-size: 16px")
        self.health_title.setObjectName("label_6")

        self.health_contents = QtWidgets.QLabel(self.centralwidget)
        self.health_contents.setGeometry(QtCore.QRect(380, 350, 290, 70))
        self.health_contents.setStyleSheet("background-color: #f0f0f0; border: 1px solid #b2b2b2; border-radius: 3px")
        self.health_contents.setWordWrap(True)
        self.health_contents.setAlignment(QtCore.Qt.AlignTop)
        self.health_contents.setObjectName("textEdit_3")

        self.summary_title = QtWidgets.QLabel(self.centralwidget)
        self.summary_title.setGeometry(QtCore.QRect(380, 440, 100, 20))
        self.summary_title.setStyleSheet("font-size: 16px")
        self.summary_title.setObjectName("label_7")

        self.summary_contents = QtWidgets.QLabel(self.centralwidget)
        self.summary_contents.setGeometry(QtCore.QRect(380, 470, 290, 70))
        self.summary_contents.setStyleSheet("background-color: #f0f0f0; border: 1px solid #b2b2b2; border-radius: 3px")
        self.summary_contents.setWordWrap(True)
        self.summary_contents.setAlignment(QtCore.Qt.AlignTop)
        self.summary_contents.setObjectName("textEdit_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "재미로 보는 관상 테스트"))
        self.request_button.setText(_translate("MainWindow", "결과 보기"))
        self.main_title.setText(_translate("MainWindow", "재미로 보는 관상 테스트"))
        self.image_upload_button.setText(_translate("MainWindow", "이미지 등록하기"))
        self.description.setText(_translate("MainWindow", "이미지를 등록해서 AI에게 관상 테스트를 받아보세요."))
        self.money_title.setText(_translate("MainWindow", "재물운"))
        self.love_title.setText(_translate("MainWindow", "연애운"))
        self.health_title.setText(_translate("MainWindow", "건강운"))
        self.summary_title.setText(_translate("MainWindow", "해석 요약"))


