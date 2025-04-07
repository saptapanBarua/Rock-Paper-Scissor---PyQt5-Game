'''Rock | Paper | Scissor
Author: Saptapan Barua
'''

from sys import argv, exit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class Window(QWidget):
    '''Main App window'''
    def _init_(self):
        super()._init_()
        # varialbles for app window
        self.window_width=500
        self.window_height=315

        # open in center
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2

        # load icon
        self.game_icon_path = 'assets/game.png'
        self.rock_icon_path = 'assets/rock.png'
        self.paper_icon_path = 'assets/paper.png'
        self.scissor_icon_path = 'assets/scissor.png'
        self.bot_icon_path = 'assets/bot.png'
        self.gamer_icon_path = 'assets/gamer.png'

        self.game_icon = QIcon(self.game_icon_path)
        self.rock_icon = QIcon(self.rock_icon_path)
        self.paper_icon = QIcon(self.paper_icon_path)
        self.scissor_icon = QIcon(self.scissor_icon_path)
        self.bot_icon = QIcon(self.bot_icon_path)
        self.gamer_icon = QIcon(self.gamer_icon_path)

        # setup the window
        self.setWindowTitle('Rock | Paper | Scissor')
        self.setWindowIcon(self.game_icon)
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        # score
        self.gamer_score = 0
        self.bot_score = 0

        self.ui(x, y)

    def ui(self, x, y):
        '''contain all UI things'''
        # layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.move(x, y)

        # bot-choice
        self.botChoiceLabel = QLabel(self)
        self.botChoiceLabel.setFrameStyle(QFrame.Sunken)
        self.botChoiceLabel.setText('Computer\'s choice :')
        self.botChoiceLabel.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        font=QFont()
        font.setFamily('arial')
        font.setPointSize(16)
        self.botChoiceLabel.setFont(font)
        self.botChoiceLabel.setFixedSize(185, 40)

        # display-bot-choice
        self.botChoice = QLabel(self)
        self.botChoice.setFrameStyle(QFrame.Sunken)
        self.botChoice.setText('None')
        self.botChoice.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        font=QFont()
        font.setFamily('arial')
        font.setPointSize(16)
        self.botChoice.setFont(font)
        self.botChoice.setFixedSize(70, 40)

        # rock-button
        self.rockButton = QPushButton(self)
        self.rockButton.setIcon(self.rock_icon)
        self.rockButton.setIconSize(QSize(95, 95))
        self.rockButton.setFixedSize(100, 100)
        self.rockButton.setObjectName('rock')
        self.rockButton.clicked.connect(self.updateScore)
        
        # paper-button
        self.paperButton = QPushButton(self)
        self.paperButton.setIcon(self.paper_icon)
        self.paperButton.setIconSize(QSize(95, 95))
        self.paperButton.setFixedSize(100, 100)
        self.paperButton.setObjectName('paper')
        self.paperButton.clicked.connect(self.updateScore)

        # scissor-button
        self.scissorButton = QPushButton(self)
        self.scissorButton.setIcon(self.scissor_icon)
        self.scissorButton.setIconSize(QSize(95, 95))
        self.scissorButton.setFixedSize(100, 100)
        self.scissorButton.setObjectName('scissor')
        self.scissorButton.clicked.connect(self.updateScore)

        # bot-image
        self.botImage = QLabel(self)
        bot_pixmap = QPixmap(self.bot_icon_path)
        self.botImage.setPixmap(bot_pixmap)
        self.botImage.setFixedSize(60, 60)
        self.botImage.setScaledContents(True)        
        self.botImage.setAlignment(Qt.AlignCenter)

        # bot-score
        self.botScore = QLabel(self)
        self.botScore.setFrameStyle(QFrame.Sunken)
        self.botScore.setText(f'{self.bot_score}')
        self.botScore.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        font=QFont()
        font.setFamily('arial')
        font.setPointSize(16)
        self.botScore.setFont(font)
        self.botScore.setFixedSize(50, 40)        
        self.botScore.setAlignment(Qt.AlignCenter)

        # gamer-image
        self.gamerScore = QLabel(self)
        self.gamerScore.setFrameStyle(QFrame.Sunken)
        self.gamerScore.setText(f'{self.gamer_score}')
        self.gamerScore.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        font=QFont()
        font.setFamily('arial')
        font.setPointSize(16)
        self.gamerScore.setFont(font)
        self.gamerScore.setFixedSize(50, 40)        
        self.gamerScore.setAlignment(Qt.AlignCenter)

        # gamer-score
        self.gamerLabel = QLabel(self)
        gamer_pixmap = QPixmap(self.gamer_icon_path)
        self.gamerLabel.setPixmap(gamer_pixmap)
        self.gamerLabel.setFixedSize(60, 60)
        self.gamerLabel.setScaledContents(True)        
        self.gamerLabel.setAlignment(Qt.AlignCenter)

        # first row
        layout1 = QHBoxLayout()
        layout1.addStretch(1)
        layout1.addWidget(self.botChoiceLabel)
        layout1.addWidget(self.botChoice)
        layout1.addStretch(1)        
        grid.addLayout(layout1, 0, 0, 1, 3)

        # second row
        grid.addWidget(self.rockButton, 1, 0)
        grid.addWidget(self.paperButton, 1, 1)
        grid.addWidget(self.scissorButton, 1, 2)

        # third row
        layout2 = QHBoxLayout()
        layout2.addStretch(1)
        layout2.addWidget(self.botImage)
        layout2.addWidget(self.botScore)
        layout2.addStretch(1)
        layout2.addWidget(self.gamerLabel)
        layout2.addWidget(self.gamerScore)
        layout2.addStretch(1)
        grid.addLayout(layout2, 2, 0, 1, 3)

        self.show()

    def updateScore(self):
        sender = self.sender()
        choices = ['rock', 'paper', 'scissor']
        bot_choice = random.choice(choices)
        self.botChoice.setText(bot_choice)

        if (sender.objectName() == bot_choice):
            pass

        elif (sender.objectName() == 'rock' and bot_choice == 'scissor') or (sender.objectName() == 'paper' and bot_choice == 'rock') or (sender.objectName() == 'scissor' and bot_choice == 'paper'):
            self.gamer_score+=1
            
        else:
            self.bot_score+=1

        self.gamerScore.setText(f'{self.gamer_score}')
        self.botScore.setText(f'{self.bot_score}')
            
        if self.gamer_score == 5 or self.bot_score == 5:
            self.showDialogBox()

    def showDialogBox(self):
        dialog=QMessageBox()
        if self.gamer_score > self.bot_score:
            dialog.setText('You win.')

        else:
            dialog.setText('Computer wins.')

        dialog.setWindowTitle('Rock | Paper | Scissor')
        dialog.setIcon(QMessageBox.NoIcon)
        dialog.setWindowIcon(self.game_icon)
        dialog.addButton('Play again', QMessageBox.AcceptRole)
        dialog.addButton('Exit', QMessageBox.RejectRole)
        dialog.buttonClicked.connect(self.dialog_clicked)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setMinimumWidth(320)
        dialog.exec_()
        
    def dialog_clicked(self, dialog_button):
        if dialog_button.text() == 'Exit':
            QApplication.quit()
        
        else:
            self.gamer_score=0
            self.bot_score=0
            self.gamerScore.setText(f'{self.gamer_score}')
            self.botScore.setText(f'{self.bot_score}')
            self.botChoice.setText("None")

if __name__=='__main__':
    app = QApplication(argv)
    win = Window()
    exit(app.exec_())
