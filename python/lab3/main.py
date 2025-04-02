from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from design import Ui_wndw

from functions import encodeImage, decodeImage
from os import path


class Window(QMainWindow, Ui_wndw):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.encode_button.clicked.connect(self.encode_text_handler)

        self.encode_open.clicked.connect(self.open_encode_file_handler)
        self.encode_save.clicked.connect(self.save_encode_file_handler)

        self.decode_open.clicked.connect(self.open_decode_file_handler)

        self.encode_text.textChanged.connect(self.text_changed_handler)

        self.cur_img = ""
        self.encoded_img = None

    def encode_text_handler(self):
        text = self.encode_text.toPlainText()

        if self.cur_img == "":
            QMessageBox.critical(self, "Ошибка!", "Не выбрано изображение!")
            return

        try:
            self.encoded_img = encodeImage(self.cur_img, text).toqpixmap()
        except Exception as ex:
            print(ex)
            QMessageBox.critical(self, "Ошибка!", "Слишком длинное сообщение!")
            return

        img = self.encoded_img.scaled(
            self.encode_img.geometry().width() - 50,
            self.encode_img.geometry().height() - 50,
            Qt.KeepAspectRatio,
        )

        self.encode_img.setPixmap(img)

    def open_encode_file_handler(self):
        self.encoded_img = None

        self.cur_img, _ = QFileDialog.getOpenFileName(
            self, "Выберите *.bmp изображение:", "", "BMP Files (*.bmp)"
        )

        if not path.exists(self.cur_img):
            self.cur_img = ""
            QMessageBox.critical(self, "Ошибка!", "Изображение не выбрано!")
            return

        img = QPixmap(self.cur_img)
        self.max_len_label.setNum((img.size().width() * img.size().height()) // 3)
        
        img = img.scaled(
            self.encode_img.geometry().width() - 50,
            self.encode_img.geometry().height() - 50,
            Qt.KeepAspectRatio,
        )

        self.encode_img.setPixmap(img)

    def save_encode_file_handler(self):
        if not self.encoded_img:
            QMessageBox.critical(self, "Ошибка!", "Изображение не закодировано!")
            return

        img_path, _ = QFileDialog.getSaveFileName(
            self, "Сохраните закодированное изображение:", "encoded.bmp", "BMP Files (*.bmp)"
        )

        self.encoded_img.save(img_path)


    def open_decode_file_handler(self):
        img_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите *.bmp изображение:", "", "BMP Files (*.bmp)"
        )

        if not path.exists(img_path):
            QMessageBox.critical(self, "Ошибка!", "Изображение не выбрано!")
            return

        img = QPixmap(img_path)
        img = img.scaled(
            self.encode_img.geometry().width() - 50,
            self.encode_img.geometry().height() - 50,
            Qt.KeepAspectRatio,
        )

        self.decode_text.setPlainText(decodeImage(img_path))
        self.decode_img.setPixmap(img)

    def text_changed_handler(self):
        self.cur_len_label.setNum(len(self.encode_text.toPlainText()))


if __name__ == "__main__":
    app = QApplication()

    window = Window()
    window.show()

    app.exec()
