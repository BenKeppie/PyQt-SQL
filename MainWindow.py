import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jesus is my saviour")
        #create menu and tool bar
        self.open_database=QAction("Open Database",self)
        self.close_database=QAction("Close Database", self)
        #add menu to menu bar 
        self.menu=QMenuBar()
        self.database_toolbar=QToolBar()
        self.database_menu=self.menu.addMenu("Database")
        #add actions to menu
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)
        #add actions to toolbar
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)
        #add toolbar to window
        self.addToolBar(self.database_toolbar)
        #add menu to toolbar 
        self.setMenuBar(self.menu)
        #making connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

    def open_connection(self):
        print("Opening Database")
        path=QFileDialog.getOpenFileName()
    def close_connection(self):
        print("Closing Database")
        

if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
        
