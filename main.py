import nmf
from PyQt4 import QtGui, uic
import scraper
import sys


# Little WebScraper for testing text analysis with python
class WebScraper(QtGui.QDialog):
    def __init__(self):
        super(WebScraper, self).__init__()
        uic.loadUi("ui/webscraper.ui", self)
        self.save_btn.clicked.connect(self.save)
        self.analyze_btn.clicked.connect(self.analyze)
        self.topics_area.setReadOnly(True)

        self.show()

    @staticmethod
    def path():
        save_file = QtGui.QFileDialog()
        path = QtGui.QFileDialog.getSaveFileName(save_file, "Save File")
        return path

    # Save the data in a file
    def save(self):
        file_url = self.path()
        page_url = self.url_edit.text()

        try:
            scraper.url_text(page_url, file_url)
        except:
            print("no file saved")

    # Open a file and analyze the data in it with NMF
    def analyze(self):
        self.topics_area.clear()
        file = QtGui.QFileDialog()
        path = ""
        file.setFileMode(QtGui.QFileDialog.AnyFile)
        file.setFilter("Text files (*.txt)")
        if file.exec_():
            file_name = file.selectedFiles()
            path = "".join(file_name)

        n_topics = int(self.topics_edit.text())
        n_top_words = int(self.words_edit.text())

        text = open(path, "r")
        text = text.read()

        top_words = nmf.top_words(text.split(" "), n_topics, n_top_words)
        for key, value in top_words.items():
            inserted_text = key + ": " + value + "\n"
            self.topics_area.append(inserted_text)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = WebScraper()
    app.setStyle("plastique")
    app.exec_()
