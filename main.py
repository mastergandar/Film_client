import requests
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt, QUrl
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide2.QtWidgets import QTableWidgetItem

from GUI_Film import Ui_MainWindow
import sys


# Главный класс
class MakeCurse(QtWidgets.QMainWindow, Ui_MainWindow):

    # Атрибуты данных класса
    lvl_out = []
    dic_chop = []

    # Конструктор класса
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.BASE_URL = 'http://127.0.0.1:8000/films/'
        self.TOKEN = 'Token 8aba548ab94bbaa47b0c9a4cd9423ecaacb696e4'
        self.HEADERS = {'Authorization': self.TOKEN}

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['#', 'Название'])

        no_image = QtGui.QPixmap('no_image.png')
        self.label_pic.setPixmap(no_image)
        self.label_pic.setScaledContents(True)

        self.get_films()

        self.pushButton_Create.clicked.connect(self.create_pressed)
        self.pushButton_Delete.clicked.connect(self.delete_pressed)
        self.pushButton_Change.clicked.connect(self.update_pressed)
        self.pushButton_Search.clicked.connect(self.search_pressed)
        self.pushButton_Image.clicked.connect(self.image_pressed)

        category_list = ['UNCATEGORIZED', 'BLOCKBUSTER']
        country_list = ['NOCOUNTRY', 'USA', 'RUSSIA']

        self.comboBox_category.addItems(category_list)
        self.comboBox_country.addItems(country_list)

    def create_pressed(self):
        self.create_film()

    def delete_pressed(self):
        self.delete_film()

    def update_pressed(self):
        self.patch_film()

    def search_pressed(self):
        self.search_film()

    def image_pressed(self):
        self.get_image()

    def get_films(self):
        response = requests.get(self.BASE_URL, headers=self.HEADERS)
        i = 0
        json_response = response.json()
        rows_count = len(json_response)
        self.tableWidget.setRowCount(rows_count)
        for film in json_response:
            pk = str(film['pk'])
            name = film['name']
            self.tableWidget.setItem(i, 0, QTableWidgetItem(pk))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(name))
            i += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.update()

    def create_film(self):
        payload = {
            'provider': 1,
            'name': self.textEdit_Name.toPlainText(),
            'actor': self.textEdit_actor.toPlainText(),
            'description': self.textEdit_coments.toPlainText(),
            'country': self.comboBox_country.currentIndex(),
            'category': self.comboBox_category.currentIndex(),
            'image': self.imagus,
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, data=payload)
        if response.status_code == 201:
            self.get_films()

    def delete_film(self):
        payload = {'provider': 1, 'id': int(self.textEdit_Number.toPlainText())}
        film_id = self.textEdit_Number.toPlainText()
        response = requests.delete(self.BASE_URL + film_id, headers=self.HEADERS)
        if response.status_code == 204:
            self.get_films()

    def patch_film(self):
        payload = {
            'provider': 1,
            'name': self.textEdit_Name.toPlainText(),
            'actor': self.textEdit_actor.toPlainText(),
            'description': self.textEdit_coments.toPlainText(),
            'country': self.comboBox_country.currentIndex(),
            'category': self.comboBox_category.currentIndex(),
            'image': self.imagus,
        }
        film_id = self.textEdit_Number.toPlainText()
        response = requests.patch(self.BASE_URL + film_id, headers=self.HEADERS, data=payload)
        if response.status_code == 200:
            self.get_films()

    def search_film(self):
        film_id = self.textEdit_Number.toPlainText()
        response = requests.get(self.BASE_URL + film_id, headers=self.HEADERS)
        if response.status_code == 200:
            json_response = response.json()
            nam = QNetworkAccessManager(self)
            nam.finished.connect(self.get_image_from_url)
            nam.get(QNetworkRequest(QUrl(json_response['file'])))
            self.textEdit_Name.setText(json_response['name'])
            self.textEdit_actor.setText(json_response['actor'])
            self.textEdit_coments.setText(json_response['description'])
            self.comboBox_country.setCurrentIndex(json_response['country'])
            self.comboBox_category.setCurrentIndex(json_response['category'])

    def get_image_from_url(self, reply):
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(reply.readAll())
        self.label_pic.setPixmap(pixmap)

    def get_image(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*')
        try:
            self.imagus = QtGui.QPixmap(filename)
            self.label_pic.setPixmap(filename)
            self.label_pic.setScaledContents(True)
        except:
            pass


if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    quest = MakeCurse()
    # Запуск
    sys.exit(app.exec_())
