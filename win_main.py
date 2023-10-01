from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QApplication, QWidget, QRadioButton, QGroupBox,
    QButtonGroup, QSpinBox
)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Тестування")
main_win.resize(400, 400)

qtext = QLabel('Питання')
v_line = QVBoxLayout()

rdtn_1 = QRadioButton('')
rdtn_2 = QRadioButton('')
rdtn_3 = QRadioButton('')
rdtn_4 = QRadioButton('')

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()

RadioGroup.addButton(rdtn_1)
RadioGroup.addButton(rdtn_2)
RadioGroup.addButton(rdtn_3)
RadioGroup.addButton(rdtn_4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rdtn_1)
layout_ans2.addWidget(rdtn_2)
layout_ans3.addWidget(rdtn_3)
layout_ans3.addWidget(rdtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

btn_Menu = QPushButton('Menu')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok = QPushButton('Відповісти')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)

layout_line2.addWidget(qtext, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line4.addWidget(btn_Ok, alignment=Qt.AlignCenter)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)

main_win.setLayout(layout_card)

main_win.show()
app.exec_()