import sys ,os
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("*Adsız - Not Defteri")
        self.setGeometry(700,500,500,500)

        
        bar=self.menuBar()
        file=bar.addMenu("File")
        new_file=QAction("New File",self)
        new_file.setShortcut("Ctrl+N")
        new_file.triggered.connect(self.newfile)
        file.addAction(new_file)

        open_file=QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(self.openfile)
        file.addAction(open_file)
        file.addSeparator()

        save=QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.triggered.connect(self.save)
        file.addAction(save)

        save_as=QAction("Save As",self)
        save_as.setShortcut("Ctrl+Shift+S")
        file.addAction(save_as)

        edit=bar.addMenu("Edit")

        undo=QAction("Undo",self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.undo)
        edit.addAction(undo)

        redo=QAction("Redo",self)
        redo.setShortcut("Ctrl+Y")
        redo.triggered.connect(self.redo)
        edit.addAction(redo)

        edit.addSeparator()

        cut=QAction("Cut",self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.cut)
        edit.addAction(cut)

        copy=QAction("Copy",self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.copy)
        edit.addAction(copy)

        paste=QAction("Paste",self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.paste)
        edit.addAction(paste)
        
        appearance=bar.addMenu("Appearance")
        dark_mode=QAction("Set Dark Mode",self)
        dark_mode.triggered.connect(self.dark_mode)
        appearance.addAction(dark_mode)
        light_mode=QAction("Set Light Mode",self)
        light_mode.triggered.connect(self.light_mode)
        appearance.addAction(light_mode)
        appearance.addSeparator()

        increase_fontsize=QAction("Increase Font Size",self)
        increase_fontsize.triggered.connect(self.increase_font_size)
        appearance.addAction(increase_fontsize)

        decrease_fontsize=QAction("Decrease Font Size",self)
        decrease_fontsize.triggered.connect(self.decrease_font_size)
        appearance.addAction(decrease_fontsize)

        self.current_path=None
        self.text_font_size=9
        
        layout=QVBoxLayout()

        self.text_edit=QTextEdit()
        layout.addWidget(self.text_edit)

        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def newfile(self):
        self.text_edit.clear()
        self.current_path=None

    def openfile(self):
        fname=QFileDialog.getOpenFileName(self,'Open File','c:/Users/user/Desktop','Text Files (*.txt)')
        dosya_adi=os.path.basename(fname[0])
        self.setWindowTitle(dosya_adi+' - Not Defteri')
        with open(fname[0],'r') as file:
            self.text_edit.setText(file.read())
        self.current_path=fname[0]
    def save(self):
        if self.current_path is not None:
            filetext=self.text_edit.toPlainText()
            with open(self.current_path,'w') as file:
                file.write(filetext)
        else:
            self.save_as()

    def save_as(self):
        fname=QFileDialog.getSaveFileName(self,'Save As','c:/Users/user/Desktop','Text Files (*.txt)')
        self.current_path=fname[0]
        text=self.text_edit.toPlainText()
        with open(self.current_path,'w') as file:
            file.write(text)
        dosya_adi=os.path.basename(self.current_path)
        self.setWindowTitle(dosya_adi+' - Not Defteri')

    def undo(self):
        self.text_edit.undo()
    def redo(self):
        self.text_edit.redo()
    def cut(self):
        self.text_edit.cut()
    def copy(self):
        self.text_edit.copy()
    def paste(self):
        self.text_edit.paste()
    def dark_mode(self):
        self.setStyleSheet('''QWidget{
                    background-color: rgb(33, 33, 33);
                    color: #FFFFFF;
                }
                QTextEdit{
                    background-color: rgb(46, 46, 46);

                }
                QMenu::item{
                    background-color:  #000000;
                }
                QMenuBar::item:selected{
                    color: #000000;
                }
                QMenu::item:selected{
                    background-color: #ffffff;
                    color: #000000;
                }
        ''')
    def light_mode(self):
        self.setStyleSheet('')

    def increase_font_size(self):
        self.text_font_size+=1
        self.text_edit.setFontPointSize(self.text_font_size)

    def decrease_font_size(self):
        self.text_font_size-=1
        print(self.text_font_size)
        self.text_edit.setFontPointSize(self.text_font_size)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())