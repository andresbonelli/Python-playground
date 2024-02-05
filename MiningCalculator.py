import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def calculate_roi(monthlyKas: float, kas_price: float, retailPrice: int) -> tuple:
    if retailPrice <= 0 or monthlyKas <= 0 or kas_price <= 0:
        raise ValueError("Values must be positive.")

    totalKas = 0
    months_to_ROI = 1

    while True:
        totalKas += monthlyKas
        monthlyKas = monthlyKas * ((1 / 2) ** (1 / 12))

        if totalKas * kas_price >= retailPrice:
            return months_to_ROI, totalKas

        months_to_ROI += 1

class ROIApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ROI Calculator")
        self.setGeometry(100, 100, 400, 250)

        self.kas_price_edit = QLineEdit(self)
        self.retail_price_edit = QLineEdit(self)
        self.monthly_yield_edit = QLineEdit(self)

        self.result_label = QLabel(self)

        self.create_widgets()

    def create_widgets(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Current KAS Price:"))
        layout.addWidget(self.kas_price_edit)

        layout.addWidget(QLabel("Retail Price of Miner:"))
        layout.addWidget(self.retail_price_edit)

        layout.addWidget(QLabel("Monthly Yield in KAS:"))
        layout.addWidget(self.monthly_yield_edit)

        calculate_button = QPushButton("Calculate ROI", self)
        calculate_button.clicked.connect(self.calculate_roi)
        layout.addWidget(calculate_button)

        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_roi(self):
        try:
            kas_price = float(self.kas_price_edit.text())
            retail_price = float(self.retail_price_edit.text())
            monthly_yield = float(self.monthly_yield_edit.text())
        except ValueError:
            self.result_label.setText("Invalid input. Please enter valid numeric values.")
            return
        try:
            months_to_roi, roi_kas = calculate_roi(monthly_yield, kas_price, retail_price)
        except ValueError as e:
            self.result_label.setText(e)

        result_text = f'Months needed to ROI: {months_to_roi}\n' \
                      f'Total KAS yield in {months_to_roi} months: {round(roi_kas)}\n' \
                      f'Return: U$S {round(roi_kas * kas_price)}'
        self.result_label.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    roi_app = ROIApp()
    roi_app.show()
    sys.exit(app.exec_())