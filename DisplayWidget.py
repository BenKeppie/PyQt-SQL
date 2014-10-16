class DisplayWidget(QWidget):
    """A class to display the model and represent a view"""

    def __init__(self):
        super().__init__()
        self.stacked_layout= QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model=None
        

    def display_results_layout(self):
        self.results_table= QTableView
        self.results_layout= QVBoxLayout

        self.results_layout.addWidget(self.results_table)

        self.results_widget=QWidget()
        self.results_widget.setLayout(self.results_layout)
        self.stacked_layout.addWidget(self.results_widget)

    def show_results(self):
        pass

    def show_table(self):
        pass
