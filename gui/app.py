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
        MainWindow.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(40, 50, 300, 300))
        self.image_label.setStyleSheet("border: 1px solid black;")
        self.image_label.setText("매장 이미지를 등록해주세요.")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("label")

        self.image_upload_button = QtWidgets.QPushButton(self.centralwidget)
        self.image_upload_button.setGeometry(QtCore.QRect(35, 370, 310, 41))
        self.image_upload_button.setObjectName("pushButton_2")
        self.image_upload_button.clicked.connect(lambda: load_image(self))

        self.link_address_text = QtWidgets.QTextEdit(self.centralwidget)
        self.link_address_text.setGeometry(QtCore.QRect(40, 470, 300, 30))
        self.link_address_text.setObjectName("plainTextEdit")

        self.serch_button = QtWidgets.QPushButton(self.centralwidget)
        self.serch_button.setGeometry(QtCore.QRect(35, 520, 310, 41))
        self.serch_button.setObjectName("pushButton")
        self.serch_button.clicked.connect(lambda: generate_description(self))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 440, 101, 16))
        self.label_3.setObjectName("label_3")

        self.result_output = QtWidgets.QTextEdit(self.centralwidget)
        self.result_output.setGeometry(QtCore.QRect(370, 50, 500, 700))
        self.result_output.setStyleSheet("border: 1px solid black")
        self.result_output.setText("")
        self.result_output.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "여기 어때??"))
        self.serch_button.setText(_translate("MainWindow", "검색하기"))
        self.label_2.setText(_translate("MainWindow", "매장 사진"))
        self.label_3.setText(_translate("MainWindow", "식당 검색 링크"))
        self.image_upload_button.setText(_translate("MainWindow", "이미지 등록하기"))


