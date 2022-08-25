from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from PyQt5 import QtGui
import sys
from dokusan import generators
import numpy as np


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("sudoku.ui", self)
        
        self.setWindowTitle("Sudoku 3X3")
        self.setWindowIcon(QtGui.QIcon('image/logo.ico'))
        # tagging items
        self.s = [self.findChild(QLineEdit, "lineEdit"),
                  self.findChild(QLineEdit, "lineEdit_2"),
                  self.findChild(QLineEdit, "lineEdit_3"),
                  self.findChild(QLineEdit, "lineEdit_10"),
                  self.findChild(QLineEdit, "lineEdit_16"),
                  self.findChild(QLineEdit, "lineEdit_12"),
                  self.findChild(QLineEdit, "lineEdit_19"),
                  self.findChild(QLineEdit, "lineEdit_24"),
                  self.findChild(QLineEdit, "lineEdit_26"),
                  self.findChild(QLineEdit, "lineEdit_4"),
                  self.findChild(QLineEdit, "lineEdit_6"),
                  self.findChild(QLineEdit, "lineEdit_5"),
                  self.findChild(QLineEdit, "lineEdit_14"),
                  self.findChild(QLineEdit, "lineEdit_15"),
                  self.findChild(QLineEdit, "lineEdit_11"),
                  self.findChild(QLineEdit, "lineEdit_23"),
                  self.findChild(QLineEdit, "lineEdit_27"),
                  self.findChild(QLineEdit, "lineEdit_22"),
                  self.findChild(QLineEdit, "lineEdit_8"),
                  self.findChild(QLineEdit, "lineEdit_9"),
                  self.findChild(QLineEdit, "lineEdit_7"),
                  self.findChild(QLineEdit, "lineEdit_18"),
                  self.findChild(QLineEdit, "lineEdit_17"),
                  self.findChild(QLineEdit, "lineEdit_13"),
                  self.findChild(QLineEdit, "lineEdit_20"),
                  self.findChild(QLineEdit, "lineEdit_21"),
                  self.findChild(QLineEdit, "lineEdit_25"),
                  self.findChild(QLineEdit, "lineEdit_40"),
                  self.findChild(QLineEdit, "lineEdit_38"),
                  self.findChild(QLineEdit, "lineEdit_39"),
                  self.findChild(QLineEdit, "lineEdit_53"),
                  self.findChild(QLineEdit, "lineEdit_30"),
                  self.findChild(QLineEdit, "lineEdit_35"),
                  self.findChild(QLineEdit, "lineEdit_50"),
                  self.findChild(QLineEdit, "lineEdit_48"),
                  self.findChild(QLineEdit, "lineEdit_42"),
                  self.findChild(QLineEdit, "lineEdit_29"),
                  self.findChild(QLineEdit, "lineEdit_49"),
                  self.findChild(QLineEdit, "lineEdit_37"),
                  self.findChild(QLineEdit, "lineEdit_31"),
                  self.findChild(QLineEdit, "lineEdit_44"),
                  self.findChild(QLineEdit, "lineEdit_34"),
                  self.findChild(QLineEdit, "lineEdit_36"),
                  self.findChild(QLineEdit, "lineEdit_28"),
                  self.findChild(QLineEdit, "lineEdit_43"),
                  self.findChild(QLineEdit, "lineEdit_51"),
                  self.findChild(QLineEdit, "lineEdit_54"),
                  self.findChild(QLineEdit, "lineEdit_41"),
                  self.findChild(QLineEdit, "lineEdit_47"),
                  self.findChild(QLineEdit, "lineEdit_33"),
                  self.findChild(QLineEdit, "lineEdit_45"),
                  self.findChild(QLineEdit, "lineEdit_46"),
                  self.findChild(QLineEdit, "lineEdit_52"),
                  self.findChild(QLineEdit, "lineEdit_32"),
                  self.findChild(QLineEdit, "lineEdit_80"),
                  self.findChild(QLineEdit, "lineEdit_78"),
                  self.findChild(QLineEdit, "lineEdit_57"),
                  self.findChild(QLineEdit, "lineEdit_61"),
                  self.findChild(QLineEdit, "lineEdit_81"),
                  self.findChild(QLineEdit, "lineEdit_73"),
                  self.findChild(QLineEdit, "lineEdit_79"),
                  self.findChild(QLineEdit, "lineEdit_60"),
                  self.findChild(QLineEdit, "lineEdit_62"),
                  self.findChild(QLineEdit, "lineEdit_77"),
                  self.findChild(QLineEdit, "lineEdit_67"),
                  self.findChild(QLineEdit, "lineEdit_71"),
                  self.findChild(QLineEdit, "lineEdit_56"),
                  self.findChild(QLineEdit, "lineEdit_68"),
                  self.findChild(QLineEdit, "lineEdit_70"),
                  self.findChild(QLineEdit, "lineEdit_58"),
                  self.findChild(QLineEdit, "lineEdit_74"),
                  self.findChild(QLineEdit, "lineEdit_76"),
                  self.findChild(QLineEdit, "lineEdit_75"),
                  self.findChild(QLineEdit, "lineEdit_55"),
                  self.findChild(QLineEdit, "lineEdit_59"),
                  self.findChild(QLineEdit, "lineEdit_63"),
                  self.findChild(QLineEdit, "lineEdit_66"),
                  self.findChild(QLineEdit, "lineEdit_65"),
                  self.findChild(QLineEdit, "lineEdit_64"),
                  self.findChild(QLineEdit, "lineEdit_72"),
                  self.findChild(QLineEdit, "lineEdit_69")]
        self.s2 = [[self.findChild(QLineEdit, "lineEdit"),
                    self.findChild(QLineEdit, "lineEdit_2"),
                    self.findChild(QLineEdit, "lineEdit_3"),
                    self.findChild(QLineEdit, "lineEdit_10"),
                    self.findChild(QLineEdit, "lineEdit_16"),
                    self.findChild(QLineEdit, "lineEdit_12"),
                    self.findChild(QLineEdit, "lineEdit_19"),
                    self.findChild(QLineEdit, "lineEdit_24"),
                    self.findChild(QLineEdit, "lineEdit_26"), ],

                   [self.findChild(QLineEdit, "lineEdit_4"),
                   self.findChild(QLineEdit, "lineEdit_6"),
                   self.findChild(QLineEdit, "lineEdit_5"),
                   self.findChild(QLineEdit, "lineEdit_14"),
                   self.findChild(QLineEdit, "lineEdit_15"),
                   self.findChild(QLineEdit, "lineEdit_11"),
                   self.findChild(QLineEdit, "lineEdit_23"),
                   self.findChild(QLineEdit, "lineEdit_27"),
                   self.findChild(QLineEdit, "lineEdit_22"), ],

                   [self.findChild(QLineEdit, "lineEdit_8"),
                   self.findChild(QLineEdit, "lineEdit_9"),
                   self.findChild(QLineEdit, "lineEdit_7"),
                   self.findChild(QLineEdit, "lineEdit_18"),
                   self.findChild(QLineEdit, "lineEdit_17"),
                   self.findChild(QLineEdit, "lineEdit_13"),
                   self.findChild(QLineEdit, "lineEdit_20"),
                   self.findChild(QLineEdit, "lineEdit_21"),
                   self.findChild(QLineEdit, "lineEdit_25"),
                    ],

                   [self.findChild(QLineEdit, "lineEdit_40"),
                   self.findChild(QLineEdit, "lineEdit_38"),
                   self.findChild(QLineEdit, "lineEdit_39"),
                   self.findChild(QLineEdit, "lineEdit_53"),
                   self.findChild(QLineEdit, "lineEdit_30"),
                   self.findChild(QLineEdit, "lineEdit_35"),
                   self.findChild(QLineEdit, "lineEdit_50"),
                   self.findChild(QLineEdit, "lineEdit_48"),
                   self.findChild(QLineEdit, "lineEdit_42"),
                    ],
                   [self.findChild(QLineEdit, "lineEdit_29"),
                   self.findChild(QLineEdit, "lineEdit_49"),
                   self.findChild(QLineEdit, "lineEdit_37"),
                   self.findChild(QLineEdit, "lineEdit_31"),
                   self.findChild(QLineEdit, "lineEdit_44"),
                   self.findChild(QLineEdit, "lineEdit_34"),
                   self.findChild(QLineEdit, "lineEdit_36"),
                   self.findChild(QLineEdit, "lineEdit_28"),
                   self.findChild(QLineEdit, "lineEdit_43"),
                    ],
                   [self.findChild(QLineEdit, "lineEdit_51"),
                   self.findChild(QLineEdit, "lineEdit_54"),
                   self.findChild(QLineEdit, "lineEdit_41"),
                   self.findChild(QLineEdit, "lineEdit_47"),
                   self.findChild(QLineEdit, "lineEdit_33"),
                   self.findChild(QLineEdit, "lineEdit_45"),
                   self.findChild(QLineEdit, "lineEdit_46"),
                   self.findChild(QLineEdit, "lineEdit_52"),
                   self.findChild(QLineEdit, "lineEdit_32"),
                    ],
                   [self.findChild(QLineEdit, "lineEdit_80"),
                   self.findChild(QLineEdit, "lineEdit_78"),
                   self.findChild(QLineEdit, "lineEdit_57"),
                   self.findChild(QLineEdit, "lineEdit_61"),
                   self.findChild(QLineEdit, "lineEdit_81"),
                   self.findChild(QLineEdit, "lineEdit_73"),
                   self.findChild(QLineEdit, "lineEdit_79"),
                   self.findChild(QLineEdit, "lineEdit_60"),
                   self.findChild(QLineEdit, "lineEdit_62"), ],
                   [self.findChild(QLineEdit, "lineEdit_77"),
                   self.findChild(QLineEdit, "lineEdit_67"),
                   self.findChild(QLineEdit, "lineEdit_71"),
                   self.findChild(QLineEdit, "lineEdit_56"),
                   self.findChild(QLineEdit, "lineEdit_68"),
                   self.findChild(QLineEdit, "lineEdit_70"),
                   self.findChild(QLineEdit, "lineEdit_58"),
                   self.findChild(QLineEdit, "lineEdit_74"),
                   self.findChild(QLineEdit, "lineEdit_76"), ],
                   [self.findChild(QLineEdit, "lineEdit_75"),
                   self.findChild(QLineEdit, "lineEdit_55"),
                   self.findChild(QLineEdit, "lineEdit_59"),
                   self.findChild(QLineEdit, "lineEdit_63"),
                   self.findChild(QLineEdit, "lineEdit_66"),
                   self.findChild(QLineEdit, "lineEdit_65"),
                   self.findChild(QLineEdit, "lineEdit_64"),
                   self.findChild(QLineEdit, "lineEdit_72"),
                   self.findChild(QLineEdit, "lineEdit_69")]]

        self.newGame = self.findChild(QPushButton, "pushButton")
        self.solveButton = self.findChild(QPushButton, "pushButton_2")

        # button event handle
        self.newGame.clicked.connect(lambda: self.displaySudoku())
        # self.newGame.clicked.connect(lambda:self.newGame)
        self.solveButton.clicked.connect(lambda: self.solve())
        self.arr = np.array(list(str(generators.random_sudoku(avg_rank=100))))
        self.counter = 0
        self.arrTosolve = self.arr.reshape(9, 9)
        self.arrTosolve2 = self.arr.reshape(9, 9)

        self.displaySudoku()

        # show the app
        self.show()

    def possible(self, y, x, n):
        for i in range(0, 9):
            if self.arrTosolve[y][i] == str(n):
                return False
        for i in range(0, 9):
            if self.arrTosolve[i][x] == str(n):
                return False
        box_y = (y//3)*3
        box_x = (x//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.arrTosolve[box_y+i][box_x+j] == str(n):
                    return False
        return True

    def displaySudoku(self):
        self.arr = np.array(list(str(generators.random_sudoku(avg_rank=100))))
        self.counter = 0
        self.arrTosolve = self.arr.reshape(9, 9)
        for x in self.arr:
            if(x != '0'):
                self.s[self.counter].setEnabled(False)

            self.s[self.counter].setText(f'{x}')
            self.counter += 1

    def solve(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.arrTosolve[y][x] == '0':
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.arrTosolve[y][x] = str(n)
                            self.arrTosolve2[y][x] = str(n)
                            self.solve()
                            self.arrTosolve[y][x] = '0'
                    return
        self.printSolve(self.arrTosolve, True)

    def printSolve(self, d, k):
        if k == True:
            for y in range(0, 9):
                for x in range(0, 9):
                    print(self.arrTosolve)
                    self.s2[y][x].setText(f'{d[y][x]}')


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
