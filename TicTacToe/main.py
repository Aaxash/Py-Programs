import sys,time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMessageBox
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *



class AppPlay(QWidget):

    def __init__(self,move="X"):
        super().__init__()
        self.title="Tic Tac Toe"
        self.flags= QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move=move
        self.player1=move
        self.Com1=""
        self.current_board = [[' ', ' ', ' '],
                              [' ', ' ', ' '],
                              [' ', ' ', ' ']]
        self.whose_turn = self.player1
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.button8 = QPushButton(self)
        self.button9 = QPushButton(self)
        self.turn = QLabel("1P Turn",self)
        self.msg = QLabel("",self)
        self.button11 = QPushButton("Pause",self)

        self.map={
            "button1":"00","button2":"01","button3":"02",
             "button4":"10","button5":"11","button6":"12",
             "button7":"20","button8":"21","button9":"22",
            }
        self.initUI()
        self.display()
        self.play()
        

    

    def display(self):

        self.button1.setText(self.current_board[0][0])
        self.button2.setText(self.current_board[0][1])
        self.button3.setText(self.current_board[0][2])
        self.button4.setText(self.current_board[1][0])
        self.button5.setText(self.current_board[1][1])
        self.button6.setText(self.current_board[1][2])
        self.button7.setText(self.current_board[2][0])
        self.button8.setText(self.current_board[2][1])
        self.button9.setText(self.current_board[2][2])


    def is_valid(self,px,py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_board[px][py] != " ":
            return False
        else:
            return True
        
    
    def is_end(self):

        for i in range(0, 3):
            if (self.current_board[0][i] != " " and
                    self.current_board[0][i] == self.current_board[1][i] and
                    self.current_board[1][i] == self.current_board[2][i]):
                return self.current_board[0][i]

        for i in range(0, 3):
            if self.current_board[i] == ['X', 'X', 'X']:
                return "X"
            elif self.current_board[i] == ['O', 'O', 'O']:
                return "O"

        if (self.current_board[0][0] != " " and
                self.current_board[0][0] == self.current_board[1][1] and
                self.current_board[0][0] == self.current_board[2][2]):
            return self.current_board[0][0]

        if (self.current_board[0][2] != " " and
                self.current_board[0][2] == self.current_board[1][1] and
                self.current_board[0][2] == self.current_board[2][0]):
            return self.current_board[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_board[i][j] == " ":
                    return None

        return " "

    
    def max(self):
        maxscore =-2
        x ,y =None,None
        result = self.is_end()
        if result == self.player1:
            return -1, 0, 0
        elif result == self.Com1:
            return 1, 0, 0
        elif result == ' ':
            return 0, 0, 0
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_board[i][j]==" ":
                    self.current_board[i][j]= self.Com1
                    m,p,q =self.min()
                    if m > maxscore:
                        maxscore = m
                        x = i
                        y = j
                    self.current_board[i][j]=" "
                      
        return maxscore,x,y  


    def min(self):
        minscore = 2
        x ,y =None,None
        result = self.is_end()
        if result == self.player1:
            return -1, 0, 0
        elif result == self.Com1:
            return 1, 0, 0
        elif result == ' ':
            return 0, 0, 0


       
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_board[i][j]==" ":
                    self.current_board[i][j]=self.player1
                    m,p,q = self.max()
                    if m < minscore:
                        minscore = m
                        x = i
                        y = j
                    self.current_board[i][j]=" "
                      
        return minscore,x,y  
       

    def play(self):

        if self.player1=="X":
            self.Com1="O"
        elif self.player1=="O":
            self.Com1="X"

                
                
                


    def com(self):
            (m, x, y) = self.max()
            self.current_board[x][y] = self.Com1
            self.whose_turn = self.player1
            self.turn.setText("Player Turn")
            
            
            if self.is_end() is not None:
                if self.is_end() == "X":
                    self.msg.setText('The winner is X!')
                    self.turn.setText("")
                elif self.is_end() == "O":
                    self.msg.setText('The winner is O!')
                    self.turn.setText("")
                elif self.is_end() == " ":
                    self.msg.setText("It's a tie!")
                    self.turn.setText("")
            
            self.display()

                    
                   

    def exit(self):
        msgBox = QMessageBox()
        msgBox.setText("Are You Sure ?")
        msgBox.setWindowTitle(self.title)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Yes:
            self.close()
        else:
            pass
    
    
    
    def reset(self):
        self.turn.setText("Player Turn")
        self.current_board = [[' ', ' ', ' '],
                              [' ', ' ', ' '],
                              [' ', ' ', ' ']]

        self.display()



    def pause(self):
        print(self.button11.text())

        if self.button11.text()=="Pause":
            self.button1.setEnabled(False)
            self.button2.setEnabled(False)
            self.button3.setEnabled(False)
            self.button4.setEnabled(False)
            self.button5.setEnabled(False)
            self.button6.setEnabled(False)
            self.button7.setEnabled(False)
            self.button8.setEnabled(False)
            self.button9.setEnabled(False)
            self.button11.setText("Continue")
            self.msg.setText("Pause")
        
        elif self.button11.text()=="Continue":
            self.button1.setEnabled(True)
            self.button2.setEnabled(True)
            self.button3.setEnabled(True)
            self.button4.setEnabled(True)
            self.button5.setEnabled(True)
            self.button6.setEnabled(True)
            self.button7.setEnabled(True)
            self.button8.setEnabled(True)
            self.button9.setEnabled(True)
            self.button11.setText("Pause")
            self.msg.setText("")

        


        



    
    

    def backtomenu(self):
        msgBox = QMessageBox()
        msgBox.setText("Go Back to Menu ?")
        msgBox.setWindowTitle(self.title)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Yes:
            self.w =  Appmain()
            self.w.show()
            self.hide()
        else:
            pass




       


    def click(self,i):
        c=self.map.get("button"+str(i))
        x=int(c[0])
        y=int(c[1])
        if self.is_valid(int(x),int(y)):
            self.current_board[int(x)][int(y)]=self.player1
            self.whose_turn = self.Com1
            if self.is_end() is not None:
                if self.is_end() == "X":
                    self.msg.setText('The winner is X!')
                    self.turn.setText("")
                elif self.is_end() == "O":
                    self.msg.setText('The winner is O!')
                    self.turn.setText("")
                elif self.is_end() == " ":
                    self.msg.setText("It's a tie!")
                    self.turn.setText("")
            self.turn.setText("Com1 Turn")
            self.display()
        else:
            self.msg.setText("Invalid Move")
        
        self.com()

    
    
    
    def initUI(self):
        self.setFixedSize(800,500)
        self.setWindowFlags(self.flags)
        self.setStyleSheet("Background-color:#0f4d92;")
        style="border: 1px solid white;"

        
      
        self.button1.resize(120,120)
        self.button1.move(80,80)
        self.button1.setStyleSheet("border-bottom:1px solid white;border-right:1px solid white;border-left:hidden;border-top:hidden;")
        self.button1.setFont(QFont('Times', 50))
        self.button1.clicked.connect(lambda:self.click(1))


        
        self.button2.resize(120,120)
        self.button2.move(200,80)
        self.button2.setStyleSheet("border-bottom:1px solid white;border-right:1px solid white;border-left:1px solid white;border-top:hidden;")
        self.button2.setFont(QFont('Times', 50))
        self.button2.clicked.connect(lambda:self.click(2))

        self.button3.resize(120,120)
        self.button3.move(320,80)
        self.button3.setStyleSheet("border-bottom:1px solid white;border-right:hidden;border-left:1px solid white;border-top:hidden;")
        self.button3.setFont(QFont('Times', 50))
        self.button3.clicked.connect(lambda:self.click(3))



        self.button4.resize(120,120)
        self.button4.move(80,200)
        self.button4.setStyleSheet("border-top:1px solid white;border-right:1px solid white;border-bottom:1px solid white;border-left:hidden;")
        self.button4.setFont(QFont('Times', 50))
        self.button4.clicked.connect(lambda:self.click(4))


      
        self.button5.resize(120,120)
        self.button5.move(200,200)
        self.button5.setStyleSheet("border:1px solid white")
        self.button5.setFont(QFont('Times', 50))
        self.button5.clicked.connect(lambda:self.click(5))
        

       
        self.button6.resize(120,120)
        self.button6.move(320,200)
        self.button6.setStyleSheet("border-top:1px solid white;border-right:hidden;border-bottom:1px solid white;border-left:1px solid white;")
        self.button6.setFont(QFont('Times', 50))
        self.button6.clicked.connect(lambda:self.click(6))



        self.button7.resize(120,120)
        self.button7.move(80,320)
        self.button7.setStyleSheet("border-top:1px solid white;border-right:1px solid white;border-bottom:hidden;border-left:hidden;")
        self.button7.setFont(QFont('Times', 50))
        self.button7.clicked.connect(lambda:self.click(7))


        self.button8.resize(120,120)
        self.button8.move(200,320)
        self.button8.setStyleSheet("border-bottom:hidden;border-right:1px solid white;border-left:1px solid white;border-top:1px solid white;")
        self.button8.setFont(QFont('Times', 50))
        self.button8.clicked.connect(lambda:self.click(8))

       
        self.button9.resize(120,120)
        self.button9.move(320,320)
        self.button9.setStyleSheet("border-bottom:hidden;border-right:hidden;border-left:1px solid white;border-top:1px solid white;")
        self.button9.setFont(QFont('Times', 50))
        self.button9.clicked.connect(lambda:self.click(9))

        btn="background-color : #2e5090;color: white;border-radius: 15px;border-style: outset;border-width: 1px;"
        button = QPushButton("Back to Menu",self)
        button.resize(150,40)
        button.move(550,150)
        button.setStyleSheet(btn)
        button.setFont(QFont('Times', 14))
        button.clicked.connect(self.backtomenu)
        

       
        self.button11.resize(150,40)
        self.button11.move(550,200)
        self.button11.setStyleSheet(btn)
        self.button11.setFont(QFont('Times', 14))
        self.button11.clicked.connect(self.pause)
        



        button12 = QPushButton("Exit",self)
        button12.resize(150,40)
        button12.move(550,250)
        button12.setStyleSheet(btn)
        button12.setFont(QFont('Times', 14))
        button12.clicked.connect(self.exit)
        


        button13 = QPushButton("Restart",self)
        button13.resize(150,40)
        button13.move(550,300)
        button13.setStyleSheet(btn)
        button13.setFont(QFont('Times', 14))
        button13.clicked.connect(self.reset)


        
        
        self.turn.resize(150,40)
        self.turn.move(550,350)
        self.turn.setStyleSheet("color:white;text-align:center;")
        self.turn.setFont(QFont('Times', 14))
        self.turn.setAlignment(QtCore.Qt.AlignCenter)


        self.msg.resize(300,40)
        self.msg.move(120,20)
        self.msg.setStyleSheet("color:white;text-align:center;")
        self.msg.setFont(QFont('Times', 25))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)

  
        self.show()






class AppSetting(QWidget):

    def __init__(self,difficulty):
        super().__init__()
        self.flags= QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.difficulty=difficulty
        self.initUI()
    

    def back(self):
        self.w =  Appmain()
        self.w.show()
        self.hide()


    def click(self,i):
        if i==0:
            self.difficulty=i
            self.diff.setChecked(False)
        elif i==1:
            self.difficulty=i
            self.easy.setChecked(False)

    

    def initUI(self):

        self.setFixedSize(800,500)
        label = QLabel(self)
        pixmap = QPixmap('bg.png')
        label.setPixmap(pixmap)
        self.resize(800,pixmap.height())

        self.setWindowFlags(self.flags)

        lab = QPushButton("<- Back",self)
        lab.setStyleSheet("border:hidden;color:white")
        lab.resize(100,45)
        lab.move(100,40)
        lab.setFont(QFont('Times', 18))
        lab.clicked.connect(self.back)

        

        
        label = QLabel(self)
        label.setText("Difficulty Level")
        label.move(100,130)
        label.setStyleSheet("color: white;")
        label.setFont(QFont('Times', 20))


        s="color: white;background-color : #2e5090; border-bottom: 1px solid white;border-radius: 15px;padding:15px;"
        easy=QCheckBox(self)
        diff=QCheckBox(self)
        easy.setText("Easy")
        diff.setText("Hard")

        def onCickedeasy(self):
            self.difficulty=0
            easy.setChecked(True)
            diff.setChecked(False)


        def onCickedhard(self):
            self.difficulty=1
            diff.setChecked(True)
            easy.setChecked(False)
            


        def apply(self):
            if self.difficulty==0:
                 easy.setChecked(True)
                 diff.setChecked(False)
            elif self.difficulty==1:
                diff.setChecked(True)
                easy.setChecked(False)

        easy.move(100,180)
        easy.resize(150,50)
        easy.setFont(QFont('Times', 15))
        easy.setStyleSheet(s)
        easy.toggled.connect(lambda:onCickedeasy(self))
        

       
        
        diff.move(100,250)
        diff.resize(150,50)
        diff.setFont(QFont('Times', 15))
        diff.setStyleSheet(s)
        diff.toggled.connect(lambda:onCickedhard(self))


        


        

    
        self.show()



class Appmain(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tic Tac Toe'
        self.dificulty=0
        self.flags= QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.initUI()
    
    def initUI(self):
        
        self.setFixedSize(800,500)
        label = QLabel(self)
        pixmap = QPixmap('bg.png')
        label.setPixmap(pixmap)
        self.resize(800,pixmap.height())
        self.setWindowFlags(self.flags)
        self.set_btn()
        self.show()

    
    
    def start(self):
        self.w =  Appsubmenu()
        self.w.show()
        self.hide()

        


 
    def exit(self):
        buttonReply = QMessageBox.question(self,self.title, "Are You Sure ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()
        else:
            pass
    

    def set_btn(self):
        
        style="background-color : #2e5090;color: white;border-radius: 15px;border-style: outset;border-width: 2px;"

        button1 = QPushButton('Start', self)
        button1.resize(150,60)
        button1.move(100,120)
        button1.setStyleSheet(style)
        button1.setFont(QFont('Times', 14))
        button1.clicked.connect(self.start)

        self.button3 = QPushButton('Exit', self)
        self.button3.move(100,220)
        self.button3.resize(150,60)
        self.button3.setStyleSheet(style)
        self.button3.setFont(QFont('Times', 14))
        self.button3.clicked.connect(self.exit)









class Appsubmenu(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tic Tac Toe'
        self.move="X"
        self.button1=QPushButton("X")
        self.button2=QPushButton("O")
        self.button3=QPushButton("Easy")
        self.button4=QPushButton("Hard")
        self.button5=QPushButton("Start")
        self.flags= QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.initUI()
    
    def initUI(self):
        
        self.setFixedSize(800,500)
        label = QLabel(self)
        pixmap = QPixmap('bg.png')
        label.setPixmap(pixmap)
        self.resize(800,pixmap.height())
        self.setWindowFlags(self.flags)
        self.set_main_btn()
        self.show()

    
    
    def back(self):
        self.w =  Appmain()
        self.w.show()
        self.hide()
    
    
    def start(self,move):
        self.w =  AppPlay(move)
        self.w.show()
        self.hide()
        


 
    def exit(self):
        buttonReply = QMessageBox.question(self,self.title, "Are You Sure ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.close()
        else:
            pass
    

   
    
    def set_main_btn(self):
        style="background-color : #2e5090;color: white;border-style: outset;border-width: 1px;"
        style1="background-color : #2e5090;color: white;border-radius: 15px;border-style: outset;border-width: 2px;"
        label="color:white;"
        lab = QPushButton("<- Back",self)
        lab.setStyleSheet("border:hidden;color:white")
        lab.resize(100,45)
        lab.move(100,40)
        lab.setFont(QFont('Times', 18))
        lab.clicked.connect(self.back)
        

        label1=QLabel("Choose Move",self)
        label1.move(110,120)
        label1.setFont(QFont('Times', 14))
        label1.setStyleSheet(label)
        default="background-color:#2e5090;"
        press="background-color:#6495ed;"

        def onclickx():
            self.move="X"
            button1.setStyleSheet(press)
            button2.setStyleSheet(default)

        def onclicko():
            self.move="O"
            button2.setStyleSheet(press)
            button1.setStyleSheet(default)


       

        
        button1 = QPushButton('X', self)
        button1.resize(100,60)
        button1.move(100,150)
        button1.setStyleSheet(style)
        button1.setFont(QFont('Times', 14))
        button1.clicked.connect(onclickx)

        button2 = QPushButton('O', self)
        button2.move(250,150)
        button2.resize(100,60)
        button2.setStyleSheet(style)
        button2.setFont(QFont('Times', 14))
        button2.clicked.connect(onclicko)



        button5 = QPushButton('Start', self)
        button5.move(170,400)
        button5.resize(100,60)
        button5.setStyleSheet(style1)
        button5.setFont(QFont('Times', 14))
        button5.clicked.connect(lambda:self.start(self.move))

        
       

      
        self.show()

        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Appmain()
    sys.exit(app.exec_())
