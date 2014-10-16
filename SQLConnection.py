from PyQt4.QtSql import * 

class SQLConnection:
    """A class to open a database and represent a model"""

    def __init__(self,path):
        self.path= path
        self.db= None

    def open_database(self):
        if self.db:
            self.close_dataase
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok=self.db.open()
        return opened_ok
        

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("Conn")

    def closeEvent(self,event):
        self.close_database()

    def find_products(self):
        pass
