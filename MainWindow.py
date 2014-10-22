import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from SQLConnection import *
from DisplayWidget import * 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jesus is my saviour")
        #create menu and tool bar
        self.open_database=QAction("Open Database",self)
        self.close_database=QAction("Close Database", self)
        self.find_products=QAction("Find Products",self)
        self.show_products=QAction("Show Products",self)
        #add menu to menu bar 
        self.menu=QMenuBar()
        self.database_toolbar=QToolBar()
        self.database_menu=self.menu.addMenu("Database")
        self.products_toolbar=QToolBar()
        self.products_menu=self.menu.addMenu("Products")
        
        #add actions to menu
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        self.products_menu.addAction(self.find_products)
        self.products_menu.addAction(self.show_products)
        #add actions to toolbar
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        self.products_toolbar.addAction(self.find_products)
        self.products_toolbar.addAction(self.show_products)
        #add toolbar to window
        self.addToolBar(self.database_toolbar)
        self.addToolBar(self.products_toolbar)
        #add menu to toolbar 
        self.setMenuBar(self.menu)
        #making connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

        self.find_products.triggered.connect(self.find_data)
        self.show_products.triggered.connect(self.display_data)


    def open_connection(self):
        
        print("Opening Database")
        path=QFileDialog.getOpenFileName()
        self.connection=SQLConnection(path)
        ok=self.connection.open_database()
        print(ok)
        
    def close_connection(self):
        print("Closing Database")

    def display_data(self):
        if not hasattr(self,"display_widget"):
            self.display_widget=DisplayWidget()
        self.setCentralWidget(self.display_widget)
        query=self.connection.find_products((1,))
        self.display_widget.show_results(query)

    def find_data(self):
        pass
        

if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
        
