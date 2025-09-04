import sys
from PyQt5.QtWidgets import*

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800,300,600,200)
        self.setWindowTitle('Istek Listesi')
        #self.setWindowIcon()

        layaout=QGridLayout(self)

        #WlistWidget oluşturma
        self.list_widget=QListWidget()
        layaout.addWidget(self.list_widget,0,0,4,1) # 4 satırlık yer kaplasın ve 1 sütunluk yer kaplasın

        add_button=QPushButton('Add')
        add_button.clicked.connect(self.add)

        edit_button=QPushButton('Edit')
        edit_button.clicked.connect(self.edit)

        remove_button=QPushButton('Remove')
        remove_button.clicked.connect(self.remove)

        clear_button=QPushButton('Clear')
        clear_button.clicked.connect(self.clear)

        layaout.addWidget(add_button,0,1)
        layaout.addWidget(edit_button,1,1)
        layaout.addWidget(remove_button,2,1)
        layaout.addWidget(clear_button,3,1)
        

        widget=QWidget()
        widget.setLayout(layaout)
        self.setCentralWidget(widget)


    def add(self):
        text,ok=QInputDialog.getText(self,'Ekle','Yeni istek:')
        if ok and text:
            self.list_widget.addItem(text)
    def edit(self):
       current_row=self.list_widget.currentRow()
       if current_row>=0:
            item_text=self.list_widget.item(current_row).text()
            text,ok=QInputDialog.getText(self,'Duzenle','Duzenle:',QLineEdit.Normal,item_text)
            if ok and text:
                self.list_widget.item(current_row).setText(text)

    def remove(self):
        current_row=self.list_widget.currentRow()
        if current_row >=0:
            current_item = self.list_widget.takeItem(current_row)
            del current_item
    
    def clear(self):
        self.list_widget.clear()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())