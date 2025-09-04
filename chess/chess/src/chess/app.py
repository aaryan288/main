from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial
from toga.constants import RED, WHITE, ORANGE, BROWN, GREEN, WHITE, BLACK
import toga
from PIL import Image



class Chess(toga.App):
    count_for_promotion = 4
    black_king_position = '0,4'
    white_king_position = '7,4'
    wpawn1 = True
    wpawn2 = True
    wpawn3 = True
    wpawn4 = True
    wpawn5 = True
    wpawn6 = True
    wpawn7 = True
    wpawn8 = True
    bpawn1 = True
    bpawn2 = True
    bpawn3 = True
    bpawn4 = True
    bpawn5 = True
    bpawn6 = True
    bpawn7 = True
    bpawn8 = True
    white_checks = []
    black_checks = []
    all_avaliable_moves_B = []
    all_avaliable_moves_W = []
    Pieces_locations = {'BR1':'0,0', 'BN1':'0,1', 'BB1':'0,2', 'BQ':'0,3', 'BK':'0,4', 'BB2':'0,5', 'BN2':'0,6', 'BR2':'0,7', 'BP1':'1,0', 'BP2':'1,1', 'BP3':'1,2', 'BP4':'1,3', 'BP5':'1,4', 'BP6':'1,5', 'BP7':'1,6', 'BP8':'1,7', 'WP8': '6,0', 'WP7':'6,1', 'WP6':'6,2', 'WP5': '6,3', 'WP4':'6,4', 'WP3': '6,5', 'WP2': '6,6', 'WP1':'6,7', 'WR2': '7,0', 'WN2': '7,1', 'WB2': '7,2', 'WQ': '7,3', 'WK': '7,4', 'WB1': '7,5', 'WN1': '7,6', 'WR1': '7,7'}
    check = ['True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True',]
    pieces_left_B = ['BR1', 'BN1', 'BB1', 'BQ', 'BK', 'BB2', 'BN2', 'BR2','BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8']
    pieces_left_W = ['WP8', 'WP7', 'WP6', 'WP5', 'WP4', 'WP3', 'WP2', 'WP1','WR2', 'WN2', 'WB2', 'WQ', 'WK', 'WB1', 'WN1', 'WR1']
    count = 0
    value1 = ""
    value2 = ""
    piece = ""
    pieces_list = [['BR1', 'BN1', 'BB1', 'BQ', 'BK', 'BB2', 'BN2', 'BR2'], ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8'], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['WP8', 'WP7', 'WP6', 'WP5', 'WP4', 'WP3', 'WP2', 'WP1'], ['WR2', 'WN2', 'WB2', 'WQ', 'WK', 'WB1', 'WN1', 'WR1']]
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        box1 = toga.Box()
        box2 = toga.Box()
        box3 = toga.Box()
        box4 = toga.Box()
        box5 = toga.Box()
        box6 = toga.Box()
        box7 = toga.Box()
        box8 = toga.Box()
        box9 = toga.Box()
        

        self.button1 = toga.Button('BR1',on_press=partial(self.replace1, number='0,0'), style=Pack(width=80, height=80,font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button2 = toga.Button('BN1', on_press=partial(self.replace1, number='0,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button3 = toga.Button('BB1', on_press=partial(self.replace1, number='0,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button4 = toga.Button('BQ', on_press=partial(self.replace1, number='0,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button5 = toga.Button('BK', on_press=partial(self.replace1, number='0,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button6 = toga.Button('BB2', on_press=partial(self.replace1, number='0,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button7 = toga.Button('BN2', on_press=partial(self.replace1, number='0,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button8 = toga.Button('BR2', on_press=partial(self.replace1, number='0,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button9 = toga.Button('BP1', on_press=partial(self.replace1, number='1,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button10 = toga.Button('BP2', on_press=partial(self.replace1, number='1,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button11 = toga.Button('BP3', on_press=partial(self.replace1, number='1,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button12 = toga.Button('BP4', on_press=partial(self.replace1, number='1,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button13 = toga.Button('BP5', on_press=partial(self.replace1, number='1,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button14 = toga.Button('BP6', on_press=partial(self.replace1, number='1,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button15 = toga.Button('BP7', on_press=partial(self.replace1, number='1,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button16 = toga.Button('BP8', on_press=partial(self.replace1, number='1,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button17 = toga.Button('  ', on_press=partial(self.replace1, number='2,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button18 = toga.Button('  ', on_press=partial(self.replace1, number='2,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button19 = toga.Button('  ', on_press=partial(self.replace1, number='2,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button20 = toga.Button('  ', on_press=partial(self.replace1, number='2,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button21 = toga.Button('  ', on_press=partial(self.replace1, number='2,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button22 = toga.Button('  ', on_press=partial(self.replace1, number='2,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button23 = toga.Button('  ', on_press=partial(self.replace1, number='2,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button24 = toga.Button('  ', on_press=partial(self.replace1, number='2,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button25 = toga.Button('  ', on_press=partial(self.replace1, number='3,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button26 = toga.Button('  ', on_press=partial(self.replace1, number='3,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button27 = toga.Button('  ', on_press=partial(self.replace1, number='3,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button28 = toga.Button('  ', on_press=partial(self.replace1, number='3,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button29 = toga.Button('  ', on_press=partial(self.replace1, number='3,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button30 = toga.Button('  ', on_press=partial(self.replace1, number='3,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button31 = toga.Button('  ', on_press=partial(self.replace1, number='3,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button32 = toga.Button('  ', on_press=partial(self.replace1, number='3,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button33 = toga.Button('  ', on_press=partial(self.replace1, number='4,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button34 = toga.Button('  ', on_press=partial(self.replace1, number='4,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button35 = toga.Button('  ', on_press=partial(self.replace1, number='4,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button36 = toga.Button('  ', on_press=partial(self.replace1, number='4,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button37 = toga.Button('  ', on_press=partial(self.replace1, number='4,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button38 = toga.Button('  ', on_press=partial(self.replace1, number='4,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button39 = toga.Button('  ', on_press=partial(self.replace1, number='4,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button40 = toga.Button('  ', on_press=partial(self.replace1, number='4,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button41 = toga.Button('  ', on_press=partial(self.replace1, number='5,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button42 = toga.Button('  ', on_press=partial(self.replace1, number='5,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button43 = toga.Button('  ', on_press=partial(self.replace1, number='5,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button44 = toga.Button('  ', on_press=partial(self.replace1, number='5,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button45 = toga.Button('  ', on_press=partial(self.replace1, number='5,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button46 = toga.Button('  ', on_press=partial(self.replace1, number='5,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button47 = toga.Button('  ', on_press=partial(self.replace1, number='5,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button48 = toga.Button('  ', on_press=partial(self.replace1, number='5,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button49 = toga.Button('WP8', on_press=partial(self.replace1, number='6,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button50 = toga.Button('WP7', on_press=partial(self.replace1, number='6,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button51 = toga.Button('WP6', on_press=partial(self.replace1, number='6,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button52 = toga.Button('WP5', on_press=partial(self.replace1, number='6,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button53 = toga.Button('WP4', on_press=partial(self.replace1, number='6,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button54 = toga.Button('WP3', on_press=partial(self.replace1, number='6,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button55 = toga.Button('WP2', on_press=partial(self.replace1, number='6,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button56 = toga.Button('WP1', on_press=partial(self.replace1, number='6,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button57 = toga.Button('WR2', on_press=partial(self.replace1, number='7,0'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button58 = toga.Button('WN2', on_press=partial(self.replace1, number='7,1'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button59 = toga.Button('WB2', on_press=partial(self.replace1, number='7,2'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button60 = toga.Button('WQ', on_press=partial(self.replace1, number='7,3'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button61 = toga.Button('WK', on_press=partial(self.replace1, number='7,4'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button62 = toga.Button('WB1', on_press=partial(self.replace1, number='7,5'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.button63 = toga.Button('WN1', on_press=partial(self.replace1, number='7,6'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=BLACK, flex=1))
        self.button64 = toga.Button('WR1', on_press=partial(self.replace1, number='7,7'), style=Pack(width=80, height=80, font_size=20, color=("#f2f2f2"), background_color=WHITE, flex=1))
        self.texts = toga.Label('White Move')


        box1.add(self.button1)
        box1.add(self.button2)
        box1.add(self.button3)
        box1.add(self.button4)
        box1.add(self.button5)
        box1.add(self.button6)
        box1.add(self.button7)
        box1.add(self.button8)

        box2.add(self.button9)
        box2.add(self.button10)
        box2.add(self.button11)
        box2.add(self.button12)
        box2.add(self.button13)
        box2.add(self.button14)
        box2.add(self.button15)
        box2.add(self.button16)
        box3.add(self.button17)
        box3.add(self.button18)
        box3.add(self.button19)
        box3.add(self.button20)
        box3.add(self.button21)
        box3.add(self.button22)
        box3.add(self.button23)
        box3.add(self.button24)

        box4.add(self.button25)
        box4.add(self.button26)
        box4.add(self.button27)
        box4.add(self.button28)
        box4.add(self.button29)
        box4.add(self.button30)
        box4.add(self.button31)
        box4.add(self.button32)

        box5.add(self.button33)
        box5.add(self.button34)
        box5.add(self.button35)
        box5.add(self.button36)
        box5.add(self.button37)
        box5.add(self.button38)
        box5.add(self.button39)
        box5.add(self.button40)

        box6.add(self.button41)
        box6.add(self.button42)
        box6.add(self.button43)
        box6.add(self.button44)
        box6.add(self.button45)
        box6.add(self.button46)
        box6.add(self.button47)
        box6.add(self.button48)

        box7.add(self.button49)
        box7.add(self.button50)
        box7.add(self.button51)
        box7.add(self.button52)
        box7.add(self.button53)
        box7.add(self.button54)
        box7.add(self.button55)
        box7.add(self.button56)

        box8.add(self.button57)
        box8.add(self.button58)
        box8.add(self.button59)
        box8.add(self.button60)
        box8.add(self.button61)
        box8.add(self.button62)
        box8.add(self.button63)
        box8.add(self.button64)

        box9.add(self.texts)

        main_box.add(box1)
        main_box.add(box2)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5)
        main_box.add(box6)
        main_box.add(box7)
        main_box.add(box8)
        main_box.add(box9)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def pawn_jump(self,piece):
        if piece == 'WP1' and self.wpawn1 == True:
            self.wpawn1 = False
            return True
        elif piece == 'WP1' and self.wpawn1 == False:
            return False
        if piece == 'WP2' and self.wpawn2 == True:
            self.wpawn2 = False
            return True
        elif piece == 'WP2' and self.wpawn2 == False:
            return False
        if piece == 'WP3' and self.wpawn3 == True:
            self.wpawn3 = False
            return True
        elif piece == 'WP3' and self.wpawn3 == False:
            return False
        if piece == 'WP4' and self.wpawn4 == True:
            self.wpawn4 = False
            return True
        elif piece == 'WP4' and self.wpawn4 == False:
            return False
        if piece == 'WP5' and self.wpawn5 == True:
            self.wpawn5 = False
            return True
        elif piece == 'WP5' and self.wpawn5 == False:
            return False
        if piece == 'WP6' and self.wpawn6 == True:
            self.wpawn6 = False
            return True
        elif piece == 'WP6' and self.wpawn6 == False:
            return False
        if piece == 'WP7' and self.wpawn7 == True:
            self.wpawn7 = False
            return True
        elif piece == 'WP7' and self.wpawn7 == False:
            return False
        if piece == 'WP8' and self.wpawn8 == True:
            self.wpawn8 = False
            return True
        elif piece == 'WP8' and self.wpawn8 == False:
            return False
        if piece == 'BP1' and self.bpawn1 == True:
            self.bpawn1 = False
            return True
        elif piece == 'BP1' and self.bpawn1 == False:
            return False
        if piece == 'BP2' and self.bpawn2 == True:
            self.bpawn2 = False
            return True
        elif piece == 'BP2' and self.bpawn2 == False:
            return False
        if piece == 'BP3' and self.bpawn3 == True:
            self.bpawn3 = False
            return True
        elif piece == 'BP3' and self.bpawn3 == False:
            return False
        if piece == 'BP4' and self.bpawn4 == True:
            self.bpawn4 = False
            return True
        elif piece == 'BP4' and self.bpawn4 == False:
            return False
        if piece == 'BP5' and self.bpawn5 == True:
            self.bpawn5 = False
            return True
        elif piece == 'BP5' and self.bpawn5 == False:
            return False
        if piece == 'BP6' and self.bpawn6 == True:
            self.bpawn6 = False
            return True
        elif piece == 'BP6' and self.bpawn6 == False:
            return False
        if piece == 'BP7' and self.bpawn7 == True:
            self.bpawn7 = False
            return True
        elif piece == 'BP7' and self.bpawn7 == False:
            return False
        if piece == 'BP8' and self.bpawn8 == True:
            self.bpawn8 = False
            return True
        elif piece == 'BP8' and self.bpawn8 == False:
            return False


    def pawn_check(self, widget, piece):
        if piece[0] == "W":
            if self.check[(int(piece[2])-1)] != "True":
                return False
            else:
                self.check[(int(piece[2])-1)] = "False"
                return True
        elif piece[0] == 'B':
            if self.check[(int(piece[2])+7)] != "True":
                return False
            else:
                self.check[(int(piece[2])+7)] = "False"
                return True

    def replace1(self, widget, number):
        #  
        if self.value1 == "":
            self.value1 = number
            self.value1 = self.value1.split(',')
            if self.pieces_list[int(self.value1[0])][int(self.value1[1])] == "" or self.count % 2 == 0 and self.pieces_list[int(self.value1[0])][int(self.value1[1])][0] != "W" or self.count % 2 == 1 and self.pieces_list[int(self.value1[0])][int(self.value1[1])][0] != "B":
                self.value1 = ""
                return
            self.piece = self.pieces_list[int(self.value1[0])][int(self.value1[1])]


        elif self.value2 == "":
            self.value2 = number
            self.value2 = self.value2.split(',')
            if self.pieces_list[int(self.value2[0])][int(self.value2[1])][0] == "B" and self.count%2 == 1 or self.pieces_list[int(self.value2[0])][int(self.value2[1])][0] == "W" and self.count%2 == 0:
                self.value1 = ""
                self.value2 = ""
                return

            elif self.value2 != "" and self.piece[1] == "P" and abs(int(self.value1[0])-(int(self.value2[0]))) < 3 and abs(int(self.value1[1])-(int(self.value2[1]))) <= 1:
                # '''nice'''
                if abs(int(self.value2[1])-int(self.value1[1])) == 1 and abs(int(self.value2[0])-int(self.value1[0])) == 2 or abs(int(self.value2[1])-int(self.value1[1])) == 1 and self.pieces_list[int(self.value2[0])][int(self.value2[1])] == '  ' or abs(int(self.value2[1])-int(self.value1[1])) != 1 and self.pieces_list[(int(self.value2[0]))][int(self.value2[1])] != '  ' or abs(int(self.value2[0])-int(self.value1[0])) == 2 and self.pawn_check(1,self.piece) == False or abs(int(self.value2[0])-int(self.value1[0])) == 2 and self.pieces_list[(int(self.value1[0])+1)][int(self.value1[1])] != '  ' and self.piece[0] == 'B' or int(self.value2[0]) > int(self.value1[0]) and self.piece[0] == "W" or int(self.value1[0]) > int(self.value2[0]) and self.piece[0] == "B" or abs(int(self.value2[0])-int(self.value1[0])) == 2 and self.pieces_list[(int(self.value1[0])-1)][int(self.value1[1])] != '  ' and self.piece[0] == "W" or abs(int(self.value1[0]) - int(self.value2[0])) == 2 and self.pawn_jump(self.piece) == False:
                    self.value1 = ""
                    self.value2 = ''
                    return
                else: 
                    self.pawn_jump(self.piece)
                    if self.count%2 == 0 and int(self.value2[0]) == 0:
                        self.promote('WQ{}'.format(self.count_for_promotion), 'WB{}'.format(self.count_for_promotion), 'WR{}'.format(self.count_for_promotion), 'WN{}'.format(self.count_for_promotion))
                        self.pieces_left_W.remove(self.piece)
                        self.count_for_promotion+=1
                    elif self.count%2 == 1 and int(self.value2[0]) == 7:
                        self.promote('BQ{}'.format(self.count_for_promotion), 'BB{}'.format(self.count_for_promotion), 'BR{}'.format(self.count_for_promotion), 'BN{}'.format(self.count_for_promotion))
                        self.pieces_left_B.remove(self.piece)
                        self.count_for_promotion+=1
                    self.replace()

            elif abs(int(self.value2[0]) - int(self.value1[0])) == 2 and abs(int(self.value2[1]) - int(self.value1[1])) == 1 and self.piece[1] == 'N' or abs(int(self.value2[0]) - int(self.value1[0])) == 1 and abs(int(self.value2[1]) - int(self.value1[1])) == 2 and self.piece[1] == 'N':
                self.replace()
            elif abs(int(self.value1[0]) - int(self.value2[0])) == abs(int(self.value1[1]) - int(self.value2[1])) and self.bishop_jump(1,self.value1,self.value2) and self.piece[1] == 'B' or abs(int(self.value1[0]) - int(self.value2[0])) == abs(int(self.value1[1]) - int(self.value2[1])) and self.bishop_jump(1,self.value1,self.value2) and self.piece[1] == 'Q':
                self.replace()
            elif int(self.value1[0]) - int(self.value2[0]) == 0 and self.rook_jump(1,self.value1, self.value2) and self.piece[1] == 'R' or int(self.value1[1]) - int(self.value2[1]) == 0 and self.rook_jump(1,self.value1, self.value2) and self.piece[1] == 'R' or int(self.value1[0]) - int(self.value2[0]) == 0 and self.rook_jump(1,self.value1, self.value2) and self.piece[1] == 'Q' or int(self.value1[1]) - int(self.value2[1]) == 0 and self.rook_jump(1,self.value1, self.value2) and self.piece[1] == 'Q':
                self.replace()
            elif self.piece[1] == 'K' and abs(int(self.value2[0]) - int(self.value1[0])) <= 1 and abs(int(self.value2[1]) - int(self.value1[1])) <= 1: 

                if self.count%2 == 0:
                    self.white_king_position = ','.join(self.value2)
                    self.replace()

                elif self.count%2 == 1:
                    self.black_king_position = ','.join(self.value2)
                    self.replace()
                    
            else:
                self.value1 = ''
                self.value2 = ''


        if self.count % 2 == 0: 
            self.texts.refresh()
            self.texts.text = 'White Move'
        elif self.count %2 == 1:
            self.texts.refresh()
            self.texts.text = 'Black Move'


    def replace(self):
        answer = self.piece
        answer1 = self.piece
        if self.pieces_list[int(self.value2[0])][int(self.value2[1])] != '  ':
            self.check_check()
        capture = '  '
        if self.pieces_list[int(self.value2[0])][int(self.value2[1])] != '  ':
            capture = self.pieces_list[int(self.value2[0])][int(self.value2[1])]
        self.pieces_list[int(self.value1[0])][int(self.value1[1])] = '  '
        self.pieces_list[int(self.value2[0])][int(self.value2[1])] = self.piece
        self.finding_all_checks(self.pieces_left_W)
        self.finding_all_checks(self.pieces_left_B)
        self.Pieces_locations[self.piece] = ','.join(self.value2)
        if capture != '  ':
            del self.Pieces_locations[capture]
        if self.count%2 == 0:
            checker = self.piece_vision_W(self.black_king_position)
            for key,value in checker.items():
                if self.black_king_position in value:
                    answer = key
            if answer != self.piece:
                self.value2 = self.Pieces_locations[answer]
                self.value2 = list(self.value2)
                self.value2.remove(',')
        elif self.count%2 == 0:
            checker = self.piece_vision_B(self.black_king_position)
            for key,value in checker.items():
                if self.white_king_position in value:
                    answer1 = key
            if answer1 != self.piece:
                self.value2 = self.Pieces_locations[answer1]
                self.value2 = list(self.value2)
                self.value2.remove(',')

        if self.count %2 == 0 and self.black_king_position in self.white_checks and self.checkmate_white_pieces(answer):
            self.changeing_value('1', ','.join(self.value2),self.piece)
            self.changeing_value('1', ','.join(self.value1), '  ')
            print('White Pieces Win the Game')
            return 

        elif self.count %2 == 1 and self.white_king_position in self.black_checks and self.checkmate_white_pieces(answer1):
            self.changeing_value('1', ','.join(self.value2),self.piece)
            self.changeing_value('1', ','.join(self.value1), '  ')
            print('Black Pieces Win the Game')
            return 

        if answer != self.piece and self.count%2 == 0:
            self.value2 = self.Pieces_locations[self.piece]
            self.value2 = list(self.value2)
            self.value2.remove(',')
        elif answer1 != self.piece and self.count%2 == 1:
            self.value2 = self.Pieces_locations[self.piece]
            self.value2 = list(self.value2)
            self.value2.remove(',')

        if self.count %2 == 1 and self.black_king_position in self.white_checks:
            if self.black_king_position in self.white_checks:
                self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
                self.pieces_list[int(self.value2[0])][int(self.value2[1])] = capture
                self.Pieces_locations[self.piece] = ','.join(self.value1)
                if capture != '  ':
                    self.Pieces_locations[capture] = ','.join(self.value2)
                    if capture[0] == 'B':
                        self.pieces_left_B.append(capture)
                    else:
                        self.pieces_left_W.append(capture)
                self.value1 = ''
                self.value2 = ''
                return
            else:
                self.changeing_value('1', ','.join(self.value2),self.piece)
                self.changeing_value('1', ','.join(self.value1), '  ')
                self.finding_all_checks(self.pieces_left_W)
                self.finding_all_checks(self.pieces_left_B)
                self.Pieces_locations[self.piece] = ','.join(self.value2)
                self.value1 = ''
                self.value2 = ''
                self.count += 1

        elif self.count %2 == 0 and self.white_king_position in self.black_checks:
            if self.white_king_position in self.black_checks:
                self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
                self.pieces_list[int(self.value2[0])][int(self.value2[1])] = capture
                self.Pieces_locations[self.piece] = ','.join(self.value1)
                if capture != '  ':
                    self.Pieces_locations[capture] = ','.join(self.value2)
                    if capture[0] == 'B':
                        self.pieces_left_B.append(capture)
                    else:
                        self.pieces_left_W.append(capture)
                self.value1 = ''
                self.value2 = ''
                return
            else:
                self.changeing_value('1', ','.join(self.value2),self.piece)
                self.changeing_value('1', ','.join(self.value1), '  ')
                self.finding_all_checks(self.pieces_left_W)
                self.finding_all_checks(self.pieces_left_B)
                self.Pieces_locations[self.piece] = ','.join(self.value2)
                self.value1 = ''
                self.value2 = ''
                self.count += 1

        self.finding_all_checks(self.pieces_left_W)
        self.finding_all_checks(self.pieces_left_B)
        if self.count%2 == 1 and self.black_king_position in self.white_checks:
            self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
            self.pieces_list[int(self.value2[0])][int(self.value2[1])] = capture 
            self.value1 = ''
            self.value2 = ''
            return
        elif self.count%2 == 0 and self.white_king_position in self.black_checks:
            self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
            self.pieces_list[int(self.value2[0])][int(self.value2[1])] = capture
            self.value1 = ''
            self.value2 = ''
            return
        #  
        self.changeing_value('1', ','.join(self.value2),self.piece)
        self.changeing_value('1', ','.join(self.value1), '  ')
        self.finding_all_checks(self.pieces_left_W)
        self.finding_all_checks(self.pieces_left_B)

        self.value1 = ''
        self.value2 = ''
        self.count += 1
        # print(self.Pieces_locations)


    def queen1(self, widget, piece):
        self.changeing_value(1,','.join(self.value4), piece)
        del self.Pieces_locations[self.pieces_list[int(self.value4[0])][int(self.value4[1])]]
        self.pieces_list[int(self.value4[0])][int(self.value4[1])] = piece
        if self.count%2 == 1: 
            self.pieces_left_W.append(piece)

        else:
            self.pieces_left_B.append(piece)

        self.Pieces_locations[piece] = ','.join(self.value4)

        self.image_window.close()


    def changeing_value(self, widget, number, piece):
        if number == '0,0':
            self.button1.refresh()
            self.button1.text = piece

        elif number == '0,1':
            self.button2.refresh()
            self.button2.text = piece

        elif number == '0,2':
            self.button3.refresh()
            self.button3.text = piece

        elif number == '0,3':
            self.button4.refresh()
            self.button4.text = piece

        elif number == '0,4':
            self.button5.refresh()
            self.button5.text = piece

        elif number == '0,5':
            self.button6.refresh()
            self.button6.text = piece

        elif number == '0,6':
            self.button7.refresh()
            self.button7.text = piece

        elif number == '0,7':
            self.button8.refresh()
            self.button8.text = piece

        elif number == '1,0':
            self.button9.refresh()
            self.button9.text = piece
        elif number == '1,1':
            self.button10.refresh()
            self.button10.text = piece

        elif number == '1,2':
            self.button11.refresh()
            self.button11.text = piece

        elif number == '1,3':
            self.button12.refresh()
            self.button12.text = piece

        elif number == '1,4':
            self.button13.refresh()
            self.button13.text = piece

        elif number == '1,5':
            self.button14.refresh()
            self.button14.text = piece

        elif number == '1,6':
            self.button15.refresh()
            self.button15.text = piece

        elif number == '1,7':
            self.button16.refresh()
            self.button16.text = piece

        elif number == '2,0':
            self.button17.refresh()
            self.button17.text = piece

        elif number == '2,1':
            self.button18.refresh()
            self.button18.text = piece

        elif number == '2,2':
            self.button19.refresh()
            self.button19.text = piece

        elif number == '2,3':
            self.button20.refresh()
            self.button20.text = piece

        elif number == '2,4':
            self.button21.refresh()
            self.button21.text = piece

        elif number == '2,5':
            self.button22.refresh()
            self.button22.text = piece

        elif number == '2,6':
            self.button23.refresh()
            self.button23.text = piece

        elif number == '2,7':
            self.button24.refresh()
            self.button24.text = piece

        elif number == '3,0':
            self.button25.refresh()
            self.button25.text = piece

        elif number == '3,1':
            self.button26.refresh()
            self.button26.text = piece

        elif number == '3,2':
            self.button27.refresh()
            self.button27.text = piece

        elif number == '3,3':
            self.button28.refresh()
            self.button28.text = piece

        elif number == '3,4':
            self.button29.refresh()
            self.button29.text = piece

        elif number == '3,5':
            self.button30.refresh()
            self.button30.text = piece

        elif number == '3,6':
            self.button31.refresh()
            self.button31.text = piece

        elif number == '3,7':
            self.button32.refresh()
            self.button32.text = piece

        elif number == '4,0':
            self.button33.refresh()
            self.button33.text = piece

        elif number == '4,1':
            self.button34.refresh()
            self.button34.text = piece

        elif number == '4,2':
            self.button35.refresh()
            self.button35.text = piece

        elif number == '4,3':
            self.button36.refresh()
            self.button36.text = piece

        elif number == '4,4':
            self.button37.refresh()
            self.button37.text = piece

        elif number == '4,5':
            self.button38.refresh()
            self.button38.text = piece

        elif number == '4,6':
            self.button39.refresh()
            self.button39.text = piece

        elif number == '4,7':
            self.button40.refresh()
            self.button40.text = piece

        elif number == '5,0':
            self.button41.refresh()
            self.button41.text = piece

        elif number == '5,1':
            self.button42.refresh()
            self.button42.text = piece

        elif number == '5,2':
            self.button43.refresh()
            self.button43.text = piece

        elif number == '5,3':
            self.button44.refresh()
            self.button44.text = piece

        elif number == '5,4':
            self.button45.refresh()
            self.button45.text = piece

        elif number == '5,5':
            self.button46.refresh()
            self.button46.text = piece

        elif number == '5,6':
            self.button47.refresh()
            self.button47.text = piece

        elif number == '5,7':
            self.button48.refresh()
            self.button48.text = piece

        elif number == '6,0':
            self.button49.refresh()
            self.button49.text = piece

        elif number == '6,1':
            self.button50.refresh()
            self.button50.text = piece

        elif number == '6,2':
            self.button51.refresh()
            self.button51.text = piece

        elif number == '6,3':
            self.button52.refresh()
            self.button52.text = piece

        elif number == '6,4':
            self.button53.refresh()
            self.button53.text = piece

        elif number == '6,5':
            self.button54.refresh()
            self.button54.text = piece

        elif number == '6,6':
            self.button55.refresh()
            self.button55.text = piece

        elif number == '6,7':
            self.button56.refresh()
            self.button56.text = piece

        elif number == '7,0':
            self.button57.refresh()
            self.button57.text = piece

        elif number == '7,1':
            self.button58.refresh()
            self.button58.text = piece

        elif number == '7,2':
            self.button59.refresh()
            self.button59.text = piece

        elif number == '7,3':
            self.button60.refresh()
            self.button60.text = piece

        elif number == '7,4':
            self.button61.refresh()
            self.button61.text = piece

        elif number == '7,5':
            self.button62.refresh()
            self.button62.text = piece

        elif number == '7,6':
            self.button63.refresh()
            self.button63.text = piece

        elif number == '7,7':
            self.button64.refresh()
            self.button64.text = piece

    def bishop_jump(self,widget,value1,value2):
        number = 0
        number1 = 0
        if value1[0] > value2[0] and value1[1] > value2[1]:
            number = -1
            number1 = -1
        elif value1[0] > value2[0] and value1[1] < value2[1]:
            number = -1
            number1 = 1
        elif value1[0] < value2[0] and value1[1] > value2[1]:
            number = 1
            number1 = -1
        elif value1[0] < value2[0] and value1[1] < value2[1]:
            number = 1
            number1 = 1

        for i in range(0,(abs(int(value1[0])-int(value2[0]))-1)):
            value3 = int(value1[0]) + (int(number) * (i+1))
            value4 = int(value1[1]) + (int(number1) * (i+1))
            if value3 == (int(value2[0])-1) and value4 == (int(value2[1])-1):
                return True
            elif self.pieces_list[value3][value4] != '  ':
                return False
        return True


    def rook_jump(self, widget, value1, value2): 
        number = 0
        number1 = 0
        if abs(int(value1[0]) - int(value2[0])) == 1 or abs(int(value1[1]) - int(value2[1])) == 1: 
            return True     
        if value1[0] > value2[0] and int(value1[1]) - int(value2[1]) == 0:
            number = -1
            number1 = 0
        elif value1[0] < value2[0] and int(value1[1]) - int(value2[1]) == 0:
            number = 1
            number1 = 0
        elif int(value1[0]) - int(value2[0]) == 0 and value1[1] > value2[1]:
            number = 0
            number1 = -1
        elif int(value1[0]) - int(value2[0]) == 0 and value1[1] < value2[1]:
            number = 0
            number1 = 1

        for i in range(0,(abs(int(value1[0])-int(value2[0]))-1)):
            value3 = int(value1[0]) + (int(number) * (i+1))
            value4 = int(value1[1]) + (int(number1) * (i+1))
            if value3 == (int(value2[0])-1) and value4 == (int(value2[1])-1):
                return True
            elif self.pieces_list[value3][value4] != '  ':
                return False
        return True

    

    def promote(self, Q, B, R, K):
        self.image_window = toga.Window()
        self.value4 = self.value2
        self.queen = toga.Button('Queen', on_press=partial(self.queen1, piece=Q))
        self.rook = toga.Button('Rook', on_press=partial(self.queen1, piece=R))
        self.bishop = toga.Button('Bishop', on_press=partial(self.queen1,piece=B))
        self.knight = toga.Button('Knight', on_press=partial(self.queen1,piece=K))
        self.image_window.content = toga.Box(children=[self.queen, self.rook, self.bishop,self.knight], style=Pack(direction=ROW))
        self.image_window.show()

    def finding_all_checks(self, color): 
        #  
        rook_list = []
        rook_places = []
        bishop_list = []
        bishop_places = []
        Queen_list = []
        Queen_places = []
        Knight_list = []
        Knight_places = []
        pawn_list = []
        pawn_places = []
        check_locations = []
        status1 = False
        status2 = False
        status3 = False
        status4 = False
        status5 = False
        status6 = False 
        status7 = False
        status8 = False 
        for i in color:
            if i[1] == 'R':
                rook_list.append(i)
            elif i[1] == 'N':
                Knight_list.append(i)
            elif i[1] == 'B':
                bishop_list.append(i)
            elif i[1] == 'Q':
                Queen_list.append(i)
            elif i[1] == 'K':
                pass
            else:
                pawn_list.append(i)


        for j in rook_list: 
            for i in range(0,8):
                if j in self.pieces_list[i]:
                    for k in range(0,8):
                        if j == self.pieces_list[i][k]: 
                            rook_places.append('{},{}'.format(i,k))
        for i in range(0,len(rook_list)):
            piece_location = rook_places[i]
            for j in range(1,8):
                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ':
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j][1] == 'K' and status1 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                        status1 = True
                except:
                    status1 = True 
                if status1 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j][1] == 'K' and int(piece_location[2])-j > -1 and status2 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                        status2 = True
                except: 
                    status2 = True 
                if status2 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  ':
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])][1] == 'K' and status3 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                        status3 = True
                except:
                    status3 = True 

                if status3 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  ' or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])][1] == 'K' and int(piece_location[0])-j > -1 and status4 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                        status4 = True
                except: 
                    status4 = True 
                if status4 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))

                if status1 == True and status2 == True and status3 == True and status4 == True:
                    status1 = False
                    status2 = False
                    status3 = False 
                    status4 = False
                    break

        for j in bishop_list: 
            for i in range(0,8):
                if j in self.pieces_list[i]:
                    for k in range(0,8):
                        if j == self.pieces_list[i][k]: 
                            bishop_places.append('{},{}'.format(i,k))
        for i in range(0,len(bishop_list)):
            #  
            piece_location = bishop_places[i]
            for j in range(1,8):
                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ':
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j][1] == 'K' and status5 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                        status5 = True
                except:
                    status5 = True 
                if status5 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                try:
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0 or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j][1] == 'K' and  int(piece_location[2])-j > -1 and int(piece_location[0])-j > -1 and status6 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                        status6 = True
                except: 
                    status6 = True 
                if status6 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j][1] == 'K' and int(piece_location[2])-j > -1 and status7 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                        status7 = True
                except:
                    status7 = True 
                if status7 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  ' or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j][1] == 'K' and int(piece_location[0])-j > -1 and status8 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                        status8 = True
                except: 
                    status8 = True 
                if status8 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))

                if status8 == True and status5 == True and status6 == True and status7 == True:
                    status5 = False
                    status6 = False
                    status7 = False 
                    status8 = False
                    break

        for j in Queen_list: 
            for i in range(0,8):
                if j in self.pieces_list[i]:
                    for k in range(0,8):
                        if j == self.pieces_list[i][k]: 
                            Queen_places.append('{},{}'.format(i,k))
        #  
        for i in range(0,len(Queen_list)):
            piece_location = Queen_places[i]
            for j in range(1,8):
                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ':
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j][1] == 'K' and status1 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                        status1 = True
                except:
                    status1 = True 
                if status1 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j][1] == 'K' and int(piece_location[2])-j > -1 and status2 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                        status2 = True
                except: 
                    status2 = True 
                if status2 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  ':
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])][1] == 'K' and status3 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                        status3 = True
                except:
                    status3 = True 

                if status3 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  ' or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])][1] == 'K' and int(piece_location[0])-j > -1 and status4 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                        status4 = True
                except: 
                    status4 = True 
                if status4 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))


                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ':
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j][1] == 'K' and status5 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                        status5 = True
                except:
                    status5 = True 
                if status5 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                try:
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0 or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j][1] == 'K' and  int(piece_location[2])-j > -1 and int(piece_location[0])-j > -1 and status6 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                        status6 = True
                except: 
                    status6 = True 
                if status6 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  ' or int(piece_location[2])-j < 0:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j][1] == 'K' and int(piece_location[2])-j > -1 and status7 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                        status7 = True
                except:
                    status7 = True 
                if status7 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  ' or int(piece_location[0])-j < 0:
                        if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j][1] == 'K' and int(piece_location[0])-j > -1 and status8 == False:
                            check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                        status8 = True
                except: 
                    status8 = True 
                if status8 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))



                if status1 == True and status2 == True and status3 == True and status4 == True and status8 == True and status5 == True and status6 == True and status7 == True:
                    status1 = False
                    status2 = False
                    status3 = False 
                    status4 = False
                    status5 = False
                    status6 = False
                    status7 = False 
                    status8 = False
                    break

        for j in Knight_list: 
            for i in range(0,8):
                if j in self.pieces_list[i]:
                    for k in range(0,8):
                        if j == self.pieces_list[i][k]: 
                            Knight_places.append('{},{}'.format(i,k))

        for i in range(0,len(Knight_list)):
            piece_location = Knight_places[i]
            try:
                if self.pieces_list[int(piece_location[0])-2][int(piece_location[2])+1] == '  ' and int(piece_location[0])-2 > -1 or self.pieces_list[int(piece_location[0])-2][int(piece_location[2])+1][1] == 'K' and int(piece_location[0])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])+1))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-2][int(piece_location[2])-1] == '  ' and int(piece_location[0])-2 > -1 and int(piece_location[2])-1 > -1 or self.pieces_list[int(piece_location[0])-2][int(piece_location[2])-1][1] == 'K' and int(piece_location[0])-2 > -1 and int(piece_location[2])-1 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])-1))
            except:
                pass

            try:
                if self.pieces_list[int(piece_location[0])+2][int(piece_location[2])+1] == '  ' or self.pieces_list[int(piece_location[0])+2][int(piece_location[2])+1][1] == 'K':
                    check_locations.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])+1))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])+2][int(piece_location[2])-1] == '  ' and int(piece_location[2])-1 > -1 or self.pieces_list[int(piece_location[0])+2][int(piece_location[2])-1][1] == 'K' and int(piece_location[2])-1 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])-1))
            except:
                pass 




            try:
                if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+2] == '  ' or self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+2][1] == 'K':
                    check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+2))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-2] == '  ' and int(piece_location[0])-1 > -1 and int(piece_location[2])-2 > -1 or self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-2][1] == 'K' and int(piece_location[0])-1 > -1 and int(piece_location[2])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-2))
            except:
                pass

            try:
                if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-2] == '  ' and int(piece_location[2])-2 > -1 or self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-2][1] == 'K' and int(piece_location[2])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-2))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+2] == '  ' and int(piece_location[0])-1 > -1 or self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+2][1] == 'K' and int(piece_location[0])-1 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])+2))
            except:
                pass

        for j in pawn_list: 
            for i in range(0,8):
                if j in self.pieces_list[i]:
                    for k in range(0,8):
                        if j == self.pieces_list[i][k]: 
                            pawn_places.append('{},{}'.format(i,k))
        if color == self.pieces_left_W:
            for i in range(0,len(pawn_list)):
                piece_location = pawn_places[i]
                try:
                    if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+1] == '  ' and int(piece_location[0])-1 > -1 or self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+1][1] == 'K' and int(piece_location[0])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])+1))
                except:
                    pass
                try:
                    if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-1] == '  ' and int(piece_location[2])-1 > -1 and int(piece_location[0])-1 > -1 or self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-1][1] == 'K' and int(piece_location[2])-1 > -1 and int(piece_location[0])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-1))
                except:
                    pass
        elif color == self.pieces_left_B:
            for i in range(0,len(pawn_list)):
                piece_location = pawn_places[i]
                try:
                    if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+1] == '  ' or self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+1][1] == 'K':
                        check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+1))
                except:
                    pass
                try:
                    if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-1] == '  ' and int(piece_location[2])-1 > -1 or self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-1][1] == 'K' and int(piece_location[2])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-1))
                except:
                    pass


        check_locations = sorted(list(set(check_locations)))
        if color == self.pieces_left_W:
            if self.white_king_position in check_locations:
                check_locations.remove(self.white_king_position)
            self.white_checks = check_locations
        elif color == self.pieces_left_B:
            if self.black_king_position in check_locations:
                check_locations.remove(self.black_king_position)
            self.black_checks = check_locations

        # print(self.black_checks)
        # print('\n')
        # print(self.white_checks)
        # print('\n')
    def checkmate_white_pieces(self, attacker): 
        # '''nice'''
        if self.count > 1 and self.black_king_position in self.white_checks: 
            try: 
                if self.pieces_list[int(self.black_king_position[0])+1][int(self.black_king_position[2])] == '  ' and '{},{}'.format(int(self.black_king_position[0])+1,int(self.black_king_position[2])) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if self.pieces_list[int(self.black_king_position[0])+1][int(self.black_king_position[2])+1] == '  ' and '{},{}'.format(int(self.black_king_position[0])+1,int(self.black_king_position[2])+1) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.black_king_position[0])-1 > -1 and self.pieces_list[int(self.black_king_position[0])-1][int(self.black_king_position[2])] == '  ' and '{},{}'.format(int(self.black_king_position[0])-1,int(self.black_king_position[2])) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.black_king_position[0])-1 > -1 and int(self.black_king_position[2])-1 > -1 and self.pieces_list[int(self.black_king_position[0])-1][int(self.black_king_position[2])-1] == '  ' and '{},{}'.format(int(self.black_king_position[0])-1,int(self.black_king_position[2])-1) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if self.pieces_list[int(self.black_king_position[0])][int(self.black_king_position[2])+1] == '  ' and '{},{}'.format(int(self.black_king_position[0]),int(self.black_king_position[2])+1) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if  int(self.black_king_position[2])-1 > -1 and self.pieces_list[int(self.black_king_position[0])+1][int(self.black_king_position[2])-1] == '  ' and '{},{}'.format(int(self.black_king_position[0])+1,int(self.black_king_position[2])-1) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.black_king_position[2])-1 > -1 and self.pieces_list[int(self.black_king_position[0])][int(self.black_king_position[2])-1] ==  '  ' and '{},{}'.format(int(self.black_king_position[0]),int(self.black_king_position[2])-1) not in self.white_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.black_king_position[2])-1 > -1 and self.pieces_list[int(self.black_king_position[0])+1][int(self.black_king_position[2])-1] == '  ' and '{},{}'.format(int(self.black_king_position[0])+1,int(self.black_king_position[2])-1) not in self.white_checks:
                    return False
            except: 
                pass

            checking_spots = []
            checking_spots.append(self.Pieces_locations[attacker])
            avaliable_moves = self.piece_vision_B(attacker)
            # import pdb;pdb.set_trace()


            if abs(int(self.black_king_position[0]) - int(self.value2[0])) == abs(int(self.black_king_position[2]) - int(self.value2[1])) and int(self.black_king_position[0]) < int(self.value2[0]) and int(self.black_king_position[2]) < int(self.value2[1]) :
                for i in range(1,8):
                    if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][0]) - i > -1 and int(self.Pieces_locations[attacker][2]) - i > -1:
                        checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2]) - i ))
                    else:
                        break    

            elif abs(int(self.black_king_position[0]) - int(self.value2[0])) == abs(int(self.black_king_position[2]) - int(self.value2[1])) and int(self.black_king_position[0]) > int(self.value2[0]) and int(self.black_king_position[2]) > int(self.value2[1]) :
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2]) + i] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break

            elif abs(int(self.black_king_position[0]) - int(self.value2[0])) == abs(int(self.black_king_position[2]) - int(self.value2[1])) and int(self.black_king_position[0]) > int(self.value2[0]) and int(self.black_king_position[2]) < int(self.value2[1]) :
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2]) - i ))
                        else:
                            break   
                    except:
                        break

            elif abs(int(self.black_king_position[0]) - int(self.value2[0])) == abs(int(self.black_king_position[2]) - int(self.value2[1])) and int(self.black_king_position[0]) < int(self.value2[0]) and int(self.black_king_position[2]) > int(self.value2[1]) : 
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2]) + i] == '  ' and int(self.Pieces_locations[attacker][0]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break 




            elif abs(int(self.black_king_position[0]) - int(self.value2[0])) == 0 and int(self.black_king_position[2]) > int(self.value2[1]):
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0])][int(self.Pieces_locations[attacker][2]) + i] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]), int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break   

            elif abs(int(self.black_king_position[0]) - int(self.value2[0])) == 0 and int(self.black_king_position[2]) < int(self.value2[1]):
                for i in range(1,8):
                    if self.pieces_list[int(self.Pieces_locations[attacker][0])][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                        checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]),int(self.Pieces_locations[attacker][2]) - i ))
                    else:
                        break 


            elif abs(int(self.black_king_position[2]) - int(self.value2[1])) == 0 and int(self.black_king_position[2]) > int(self.value2[1]):
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2])] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2])))
                        else:
                            break   
                    except:
                        break

            elif abs(int(self.black_king_position[2]) - int(self.value2[1])) == 0 and int(self.black_king_position[2]) < int(self.value2[1]): 
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2])] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2])))
                        else:
                            break 
                    except:
                        break 


            for i in checking_spots:
                for j in self.all_avaliable_moves_B:
                    if i in j:
                        return False

        elif self.count > 1 and self.white_king_position in self.black_checks: 
            try: 
                if self.pieces_list[int(self.white_king_position[0])+1][int(self.white_king_position[2])] == '  ' and '{},{}'.format(int(self.white_king_position[0])+1,int(self.white_king_position[2])) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if self.pieces_list[int(self.white_king_position[0])+1][int(self.white_king_position[2])+1] == '  ' and '{},{}'.format(int(self.white_king_position[0])+1,int(self.white_king_position[2])+1) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.white_king_position[0])-1 > -1 and self.pieces_list[int(self.white_king_position[0])-1][int(self.white_king_position[2])] == '  ' and '{},{}'.format(int(self.white_king_position[0])-1,int(self.white_king_position[2])) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.white_king_position[0])-1 > -1 and int(self.white_king_position[2])-1 > -1 and self.pieces_list[int(self.white_king_position[0])-1][int(self.white_king_position[2])-1] == '  ' and '{},{}'.format(int(self.white_king_position[0])-1,int(self.white_king_position[2])-1) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if self.pieces_list[int(self.white_king_position[0])][int(self.white_king_position[2])+1] == '  ' and '{},{}'.format(int(self.white_king_position[0]),int(self.white_king_position[2])+1) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if  int(self.white_king_position[2])-1 > -1 and self.pieces_list[int(self.white_king_position[0])+1][int(self.white_king_position[2])-1] == '  ' and '{},{}'.format(int(self.white_king_position[0])+1,int(self.white_king_position[2])-1) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.white_king_position[2])-1 > -1 and self.pieces_list[int(self.white_king_position[0])][int(self.white_king_position[2])-1] ==  '  ' and '{},{}'.format(int(self.white_king_position[0]),int(self.white_king_position[2])-1) not in self.black_checks:
                    return False
            except: 
                pass

            try: 
                if int(self.white_king_position[2])-1 > -1 and self.pieces_list[int(self.white_king_position[0])+1][int(self.white_king_position[2])-1] == '  ' and '{},{}'.format(int(self.white_king_position[0])+1,int(self.white_king_position[2])-1) not in self.black_checks:
                    return False
            except: 
                pass

            checking_spots = []
            checking_spots.append(self.Pieces_locations[attacker])
            avaliable_moves = self.piece_vision_W(attacker)
            # print(self.all_avaliable_moves_W)

            if abs(int(self.white_king_position[0]) - int(self.value2[0])) == abs(int(self.white_king_position[2]) - int(self.value2[1])) and int(self.white_king_position[0]) < int(self.value2[0]) and int(self.white_king_position[2]) < int(self.value2[1]) :
                for i in range(1,8):
                    if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][0]) - i > -1 and int(self.Pieces_locations[attacker][2]) - i > -1:
                        checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2]) - i ))
                    else:
                        break    

            elif abs(int(self.white_king_position[0]) - int(self.value2[0])) == abs(int(self.white_king_position[2]) - int(self.value2[1])) and int(self.white_king_position[0]) > int(self.value2[0]) and int(self.white_king_position[2]) > int(self.value2[1]) :
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2]) + i] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break

            elif abs(int(self.white_king_position[0]) - int(self.value2[0])) == abs(int(self.white_king_position[2]) - int(self.value2[1])) and int(self.white_king_position[0]) > int(self.value2[0]) and int(self.white_king_position[2]) < int(self.value2[1]) :
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2]) - i ))
                        else:
                            break   
                    except:
                        break

            elif abs(int(self.white_king_position[0]) - int(self.value2[0])) == abs(int(self.white_king_position[2]) - int(self.value2[1])) and int(self.white_king_position[0]) < int(self.value2[0]) and int(self.white_king_position[2]) > int(self.value2[1]) : 
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2]) + i] == '  ' and int(self.Pieces_locations[attacker][0]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break 




            elif abs(int(self.white_king_position[0]) - int(self.value2[0])) == 0 and int(self.white_king_position[2]) > int(self.value2[1]):
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0])][int(self.Pieces_locations[attacker][2]) + i] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]), int(self.Pieces_locations[attacker][2]) + i ))
                        else:
                            break 
                    except:
                        break   

            elif abs(int(self.white_king_position[0]) - int(self.value2[0])) == 0 and int(self.white_king_position[2]) < int(self.value2[1]):
                for i in range(1,8):
                    if self.pieces_list[int(self.Pieces_locations[attacker][0])][int(self.Pieces_locations[attacker][2]) - i] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                        checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]),int(self.Pieces_locations[attacker][2]) - i ))
                    else:
                        break 


            elif abs(int(self.white_king_position[2]) - int(self.value2[1])) == 0 and int(self.white_king_position[2]) > int(self.value2[1]):
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) + i][int(self.Pieces_locations[attacker][2])] == '  ':
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) + i,int(self.Pieces_locations[attacker][2])))
                        else:
                            break   
                    except:
                        break

            elif abs(int(self.white_king_position[2]) - int(self.value2[1])) == 0 and int(self.white_king_position[2]) < int(self.value2[1]): 
                for i in range(1,8):
                    try:
                        if self.pieces_list[int(self.Pieces_locations[attacker][0]) - i][int(self.Pieces_locations[attacker][2])] == '  ' and int(self.Pieces_locations[attacker][2]) - i > -1:
                            checking_spots.append('{},{}'.format(int(self.Pieces_locations[attacker][0]) - i,int(self.Pieces_locations[attacker][2])))
                        else:
                            break 
                    except:
                        break 


            for i in checking_spots:
                for j in self.all_avaliable_moves_W:
                    if i in j:
                        return False




        return True





    def piece_vision_B(self, checker):
        # import pdb;pdb.set_trace()
        self.all_avaliable_moves_B = []
        piece_visions = {}
        if 'BP1' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP1'][0])+1][int(self.Pieces_locations['BP1'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP1'][0])+1,int(self.Pieces_locations['BP1'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP1'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP1'][0])+1][int(self.Pieces_locations['BP1'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP1'][0])+1,int(self.Pieces_locations['BP1'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP1'][0])+1,int(self.Pieces_locations['BP1'][2])))
                    
            except:
                pass

            try:
                if self.bpawn1 == True and self.pieces_list[int(self.Pieces_locations['BP1'][0])+2][int(self.Pieces_locations['BP1'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP1'][0])+2,int(self.Pieces_locations['BP1'][2])))
                    
            except:
                pass

            piece_visions['BP1'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)

        if 'BP2' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP2'][0])+1][int(self.Pieces_locations['BP2'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP2'][0])+1,int(self.Pieces_locations['BP2'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP2'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP2'][0])+1][int(self.Pieces_locations['BP2'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP2'][0])+1,int(self.Pieces_locations['BP2'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP2'][0])+1,int(self.Pieces_locations['BP2'][2])))
                    
            except:
                pass

            try:
                if self.bpawn2 == True and self.pieces_list[int(self.Pieces_locations['BP2'][0])+2][int(self.Pieces_locations['BP2'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP2'][0])+2,int(self.Pieces_locations['BP2'][2])))
                    
            except:
                pass

            piece_visions['BP2'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)

        if 'BP3' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP3'][0])+1][int(self.Pieces_locations['BP3'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP3'][0])+1,int(self.Pieces_locations['BP3'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP3'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP3'][0])+1][int(self.Pieces_locations['BP3'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP3'][0])+1,int(self.Pieces_locations['BP3'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP3'][0])+1,int(self.Pieces_locations['BP3'][2])))
                    
            except:
                pass

            try:
                if self.bpawn3 == True  and self.pieces_list[int(self.Pieces_locations['BP3'][0])+2][int(self.Pieces_locations['BP3'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP3'][0])+2,int(self.Pieces_locations['BP3'][2])))
                    
            except:
                pass

            piece_visions['BP3'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        if 'BP4' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP4'][0])+1][int(self.Pieces_locations['BP4'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP4'][0])+1,int(self.Pieces_locations['BP4'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP4'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP4'][0])+1][int(self.Pieces_locations['BP4'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP4'][0])+1,int(self.Pieces_locations['BP4'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP4'][0])+1,int(self.Pieces_locations['BP4'][2])))
                    
            except:
                pass

            try:
                if self.bpawn4 == True and self.pieces_list[int(self.Pieces_locations['BP4'][0])+2][int(self.Pieces_locations['BP4'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP4'][0])+2,int(self.Pieces_locations['BP4'][2])))
                    
            except:
                pass

            piece_visions['BP4'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        if 'BP5' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP5'][0])+1][int(self.Pieces_locations['BP5'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP5'][0])+1,int(self.Pieces_locations['BP5'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP5'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP5'][0])+1][int(self.Pieces_locations['BP5'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP5'][0])+1,int(self.Pieces_locations['BP5'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP5'][0])+1,int(self.Pieces_locations['BP5'][2])))
                    
            except:
                pass

            try:
                if self.bpawn5 == True and self.pieces_list[int(self.Pieces_locations['BP5'][0])+2][int(self.Pieces_locations['BP5'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP5'][0])+2,int(self.Pieces_locations['BP5'][2])))
                    
            except:
                pass

            piece_visions['BP5'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        if 'BP6' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP6'][0])+1][int(self.Pieces_locations['BP6'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP6'][0])+1,int(self.Pieces_locations['BP6'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP6'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP6'][0])+1][int(self.Pieces_locations['BP6'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP6'][0])+1,int(self.Pieces_locations['BP6'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP6'][0])+1,int(self.Pieces_locations['BP6'][2])))
                    
            except:
                pass

            try:
                if self.bpawn6 == True and self.pieces_list[int(self.Pieces_locations['BP6'][0])+2][int(self.Pieces_locations['BP6'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP6'][0])+2,int(self.Pieces_locations['BP6'][2])))
                    
            except:
                pass

            piece_visions['BP6'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        if 'BP7' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP7'][0])+1][int(self.Pieces_locations['BP7'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP7'][0])+1,int(self.Pieces_locations['BP7'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP7'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP7'][0])+1][int(self.Pieces_locations['BP7'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP7'][0])+1,int(self.Pieces_locations['BP7'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP7'][0])+1,int(self.Pieces_locations['BP7'][2])))
                    
            except:
                pass

            try:
                if self.bpawn7 == True and self.pieces_list[int(self.Pieces_locations['BP7'][0])+2][int(self.Pieces_locations['BP7'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP7'][0])+2,int(self.Pieces_locations['BP7'][2])))
                    
            except:
                pass

            piece_visions['BP7'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        if 'BP8' in self.pieces_left_B:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['BP8'][0])+1][int(self.Pieces_locations['BP8'][2])+1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP8'][0])+1,int(self.Pieces_locations['BP8'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['BP8'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['BP8'][0])+1][int(self.Pieces_locations['BP8'][2])-1][0] == 'W':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP8'][0])+1,int(self.Pieces_locations['BP8'][2])-1))
                    
            except:
                pass

            try:
                total_spots.append('{},{}'.format(int(self.Pieces_locations['BP8'][0])+1,int(self.Pieces_locations['BP8'][2])))
                    
            except:
                pass

            try:
                if self.bpawn8 == True and self.pieces_list[int(self.Pieces_locations['BP8'][0])+2][int(self.Pieces_locations['BP8'][2])] == '  ':
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['BP8'][0])+2,int(self.Pieces_locations['BP8'][2])))
                    
            except:
                pass

            piece_visions['BP8'] = total_spots
            self.all_avaliable_moves_B.append(total_spots)


        queen = []
        rook = []
        bishop = []
        knight = []
        status1 = False
        status2 = False
        status3 = False
        status4 = False
        status5 = False
        status6 = False 
        status7 = False
        status8 = False
        total_spots = []

        for key in self.Pieces_locations:
            if key[1] == 'Q' and key[0] == 'B':
                queen.append(self.Pieces_locations[key])
        if queen != []:
            for i in range(0,len(queen)):
                piece_location = queen[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ' and status1 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                            status1 = True
                    except:
                        status1 = True 

                    if status1 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                    try:
                        if int(piece_location[2])-j < 0:
                            status2 = True 
                        elif self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' and status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                            status2 = True
                        elif status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                    except: 
                        status2 = True 

                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  ' and status3 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                            status3 = True
                    except:
                        status3 = True 

                    if status3 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                    try: 
                        if int(piece_location[0])-j < 0:
                            status4 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  '  and status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                            status4 = True
                        elif status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                    except: 
                        status4 = True 


                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ' and status5 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                            status5 = True
                    except:
                        status5 = True 
                    if status5 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                    try:
                        if int(piece_location[2])-j <0 or int(piece_location[0])-j <0:
                            status6 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  '  and status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                            status6 = True
                        elif status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                    except: 
                        status6 = True 

                    try:
                        if int(piece_location[2])-j <0:
                            status7 = True
                        elif self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  '  and status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                            status7 = True
                        elif status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                    except:
                        status7 = True 

                    try: 
                        if int(piece_location[0])-j < 0:
                            status8 = True
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  '  and status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                            status8 = True
                        elif status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                    except: 
                        status8 = True 



                    if status1 == True and status2 == True and status3 == True and status4 == True and status8 == True and status5 == True and status6 == True and status7 == True or j == 7:
                        status1 = False
                        status2 = False
                        status3 = False 
                        status4 = False
                        status5 = False
                        status6 = False
                        status7 = False 
                        status8 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_B.append(total_spots)
                        total_spots = []
                        break

        for key in self.Pieces_locations:
            if key[1] == 'R' and key[0] == 'B':
                rook.append(self.Pieces_locations[key])
        #  
        if rook != []:
            for i in range(0,len(rook)):
                piece_location = rook[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ' and status1 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                            status1 = True
                    except:
                        status1 = True 

                    if status1 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                    try:
                        if int(piece_location[2])-j < 0:
                            status2 = True 
                        elif self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' and status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                            status2 = True
                        elif status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                    except: 
                        status2 = True 

                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  ' and status3 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                            status3 = True
                    except:
                        status3 = True 

                    if status3 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                    try: 
                        if int(piece_location[0])-j < 0:
                            status4 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  '  and status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                            status4 = True
                        elif status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                    except: 
                        status4 = True 

                    if status1 == True and status2 == True and status3 == True and status4 == True or j == 7:
                        status1 = False
                        status2 = False
                        status3 = False 
                        status4 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_B.append(total_spots)
                        total_spots = []
                        break 

        for key in self.Pieces_locations:
            if key[1] == 'B' and key[0] == 'B':
                bishop.append(self.Pieces_locations[key])
        if bishop != []:
            for i in range(0,len(bishop)):
                piece_location = bishop[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ' and status5 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                            status5 = True
                    except:
                        status5 = True 
                    if status5 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                    try:
                        if int(piece_location[2])-j <0 or int(piece_location[0])-j <0:
                            status6 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  '  and status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                            status6 = True
                        elif status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                    except: 
                        status6 = True 

                    try:
                        if int(piece_location[2])-j <0:
                            status7 = True
                        elif self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  '  and status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                            status7 = True
                        elif status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                    except:
                        status7 = True 

                    try: 
                        if int(piece_location[0])-j < 0:
                            status8 = True
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  '  and status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                            status8 = True
                        elif status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                    except: 
                        status8 = True 



                    if status8 == True and status5 == True and status6 == True and status7 == True or j == 7:
                        status5 = False
                        status6 = False
                        status7 = False 
                        status8 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_B.append(total_spots)
                        total_spots = []
                        break

        for key in self.Pieces_locations:
            if key[1] == 'N' and key[0] == 'B':
                knight.append(self.Pieces_locations[key])
        if knight != []:
            for i in range(0,len(knight)):
                piece_location = knight[i]
                try:
                    if int(piece_location[0])-2 > -1 and int(piece_location[2])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])+1))
                except:
                    pass 

                try:
                    if int(piece_location[0])-2 > -1 and int(piece_location[2])-1 > -1:
                        total_spots.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])-1))
                except:
                    pass

                try:
                    if int(piece_location[0])+2 <= 7 and int(piece_location[2])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])+1))
                except:
                    pass 

                try:
                    if int(piece_location[2])-1 > -1 and int(piece_location[0])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])-1))
                except:
                    pass 


                try:
                    if int(piece_location[0])+1 <= 7 and int(piece_location[2])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+2))
                except:
                    pass 

                try:
                    if int(piece_location[0])-1 > -1 and int(piece_location[2])-2 > -1:
                        total_spots.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-2))
                except:
                    pass

                try:
                    if int(piece_location[2])-2 > -1 and int(piece_location[0])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-2))
                except:
                    pass 

                try:
                    if int(piece_location[0])-1 > -1 and int(piece_location[2])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])+2))
                except:
                    pass

                piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                self.all_avaliable_moves_B.append(total_spots)
                total_spots = []

        return piece_visions


    def piece_vision_W(self, checker):
        self.all_avaliable_moves_W = []
        # '''nice'''
        piece_visions = {}
        if 'WP1' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP1'][0])-1][int(self.Pieces_locations['WP1'][2])+1][0] == 'B' and int(self.Pieces_locations['WP1'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP1'][0])-1,int(self.Pieces_locations['WP1'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP1'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP1'][0])-1][int(self.Pieces_locations['WP1'][2])-1][0] == 'B' and int(self.Pieces_locations['WP1'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP1'][0])-1,int(self.Pieces_locations['WP1'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP1'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP1'][0])-1,int(self.Pieces_locations['WP1'][2])))
                    
            except:
                pass

            try:
                if self.wpawn1 == True and self.pieces_list[int(self.Pieces_locations['WP1'][0])-2][int(self.Pieces_locations['WP1'][2])] == '  ' and int(self.Pieces_locations['WP1'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP1'][0])-2,int(self.Pieces_locations['WP1'][2])))
                    
            except:
                pass

            piece_visions['WP1'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP2' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP2'][0])-1][int(self.Pieces_locations['WP2'][2])+1][0] == 'B' and int(self.Pieces_locations['WP2'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP2'][0])-1,int(self.Pieces_locations['WP2'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP2'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP2'][0])-1][int(self.Pieces_locations['WP2'][2])-1][0] == 'B' and int(self.Pieces_locations['WP2'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP2'][0])-1,int(self.Pieces_locations['WP2'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP2'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP2'][0])-1,int(self.Pieces_locations['WP2'][2])))
                    
            except:
                pass

            try:
                if self.wpawn2 == True and self.pieces_list[int(self.Pieces_locations['WP2'][0])-2][int(self.Pieces_locations['WP2'][2])] == '  ' and int(self.Pieces_locations['WP2'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP2'][0])-2,int(self.Pieces_locations['WP2'][2])))
                    
            except:
                pass

            piece_visions['WP2'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP3' in self.pieces_left_W:

            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP3'][0])-1][int(self.Pieces_locations['WP3'][2])+1][0] == 'B' and int(self.Pieces_locations['WP3'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP3'][0])-1,int(self.Pieces_locations['WP3'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP3'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP3'][0])-1][int(self.Pieces_locations['WP3'][2])-1][0] == 'B' and int(self.Pieces_locations['WP3'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP3'][0])-1,int(self.Pieces_locations['WP3'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP3'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP3'][0])-1,int(self.Pieces_locations['WP3'][2])))
                    
            except:
                pass

            try:
                if self.wpawn3 == True and self.pieces_list[int(self.Pieces_locations['WP3'][0])-2][int(self.Pieces_locations['WP3'][2])] == '  ' and int(self.Pieces_locations['WP3'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP3'][0])-2,int(self.Pieces_locations['WP3'][2])))
                    
            except:
                pass

            piece_visions['WP3'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP4' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP4'][0])-1][int(self.Pieces_locations['WP4'][2])+1][0] == 'B' and int(self.Pieces_locations['WP4'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP4'][0])-1,int(self.Pieces_locations['WP4'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP4'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP4'][0])-1][int(self.Pieces_locations['WP4'][2])-1][0] == 'B' and int(self.Pieces_locations['WP4'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP4'][0])-1,int(self.Pieces_locations['WP4'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP4'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP4'][0])-1,int(self.Pieces_locations['WP4'][2])))
                    
            except:
                pass

            try:
                if self.wpawn4 == True and self.pieces_list[int(self.Pieces_locations['WP4'][0])-2][int(self.Pieces_locations['WP4'][2])] == '  ' and int(self.Pieces_locations['WP4'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP4'][0])-2,int(self.Pieces_locations['WP4'][2])))
                    
            except:
                pass

            piece_visions['WP4'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP5' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP5'][0])-1][int(self.Pieces_locations['WP5'][2])+1][0] == 'B' and int(self.Pieces_locations['WP5'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP5'][0])-1,int(self.Pieces_locations['WP5'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP5'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP5'][0])-1][int(self.Pieces_locations['WP5'][2])-1][0] == 'B' and int(self.Pieces_locations['WP5'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP5'][0])-1,int(self.Pieces_locations['WP5'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP5'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP5'][0])-1,int(self.Pieces_locations['WP5'][2])))
                    
            except:
                pass

            try:
                if self.wpawn5 == True and self.pieces_list[int(self.Pieces_locations['WP5'][0])-2][int(self.Pieces_locations['WP5'][2])] == '  ' and int(self.Pieces_locations['WP5'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP5'][0])-2,int(self.Pieces_locations['WP5'][2])))
                    
            except:
                pass

            piece_visions['WP5'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP6' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP6'][0])-1][int(self.Pieces_locations['WP6'][2])+1][0] == 'B' and int(self.Pieces_locations['WP6'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP6'][0])-1,int(self.Pieces_locations['WP6'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP6'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP6'][0])-1][int(self.Pieces_locations['WP6'][2])-1][0] == 'B' and int(self.Pieces_locations['WP6'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP6'][0])-1,int(self.Pieces_locations['WP6'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP6'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP6'][0])-1,int(self.Pieces_locations['WP6'][2])))
                    
            except:
                pass

            try:
                if self.wpawn6 == True and self.pieces_list[int(self.Pieces_locations['WP6'][0])-2][int(self.Pieces_locations['WP6'][2])] == '  ' and int(self.Pieces_locations['WP6'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP6'][0])-2,int(self.Pieces_locations['WP6'][2])))
                    
            except:
                pass

            piece_visions['WP6'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP7' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP7'][0])-1][int(self.Pieces_locations['WP7'][2])+1][0] == 'B' and int(self.Pieces_locations['WP7'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP7'][0])-1,int(self.Pieces_locations['WP7'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP7'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP7'][0])-1][int(self.Pieces_locations['WP7'][2])-1][0] == 'B' and int(self.Pieces_locations['WP7'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP7'][0])-1,int(self.Pieces_locations['WP7'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP7'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP7'][0])-1,int(self.Pieces_locations['WP7'][2])))
                    
            except:
                pass

            try:
                if self.wpawn7 == True and self.pieces_list[int(self.Pieces_locations['WP7'][0])-2][int(self.Pieces_locations['WP7'][2])] == '  ' and int(self.Pieces_locations['WP7'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP7'][0])-2,int(self.Pieces_locations['WP7'][2])))
                    
            except:
                pass

            piece_visions['WP7'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        if 'WP8' in self.pieces_left_W:
            total_spots = []
            try:
                if self.pieces_list[int(self.Pieces_locations['WP8'][0])-1][int(self.Pieces_locations['WP8'][2])+1][0] == 'B' and int(self.Pieces_locations['WP8'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP8'][0])-1,int(self.Pieces_locations['WP8'][2])+1))
            except:
                pass

            try:
                if int(self.Pieces_locations['WP8'][2])-1 > -1 and self.pieces_list[int(self.Pieces_locations['WP8'][0])-1][int(self.Pieces_locations['WP8'][2])-1][0] == 'B' and int(self.Pieces_locations['WP8'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP8'][0])-1,int(self.Pieces_locations['WP8'][2])-1))
                    
            except:
                pass

            try:
                if int(self.Pieces_locations['WP8'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP8'][0])-1,int(self.Pieces_locations['WP8'][2])))
                    
            except:
                pass

            try:
                if self.wpawn8 == True and self.pieces_list[int(self.Pieces_locations['WP8'][0])-2][int(self.Pieces_locations['WP8'][2])] == '  ' and int(self.Pieces_locations['WP8'][0])-1 > -1:
                    total_spots.append('{},{}'.format(int(self.Pieces_locations['WP8'][0])-2,int(self.Pieces_locations['WP8'][2])))
                    
            except:
                pass

            piece_visions['WP8'] = total_spots
            self.all_avaliable_moves_W.append(total_spots)

        queen = []
        rook = []
        bishop = []
        knight = []
        status1 = False
        status2 = False
        status3 = False
        status4 = False
        status5 = False
        status6 = False 
        status7 = False
        status8 = False
        total_spots = []

        for key in self.Pieces_locations:
            if key[1] == 'Q' and key[0] == 'W':
                queen.append(self.Pieces_locations[key])
        if queen != []:
            for i in range(0,len(queen)):
                piece_location = queen[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ' and status1 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                            status1 = True
                    except:
                        status1 = True 

                    if status1 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                    try:
                        if int(piece_location[2])-j < 0:
                            status2 = True 
                        elif self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' and status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                            status2 = True
                        elif status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                    except: 
                        status2 = True 

                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  '  and status3 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                            status3 = True
                    except:
                        status3 = True 

                    if status3 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                    try: 
                        if int(piece_location[0])-j < 0:
                            status4 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  '  and status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                            status4 = True
                        elif status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                    except: 
                        status4 = True 


                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ' and status5 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                            status5 = True
                    except:
                        status5 = True 
                    if status5 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                    try:
                        if int(piece_location[2])-j <0 or int(piece_location[0])-j <0:
                            status6 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  '  and status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                            status6 = True
                        elif status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                    except: 
                        status6 = True 

                    try:
                        if int(piece_location[2])-j <0:
                            status7 = True
                        elif self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  '  and status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                            status7 = True
                        elif status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                    except:
                        status7 = True 

                    try: 
                        if int(piece_location[0])-j < 0:
                            status8 = True
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  '  and status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                            status8 = True
                        elif status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                    except: 
                        status8 = True 



                    if status1 == True and status2 == True and status3 == True and status4 == True and status8 == True and status5 == True and status6 == True and status7 == True or j == 7:
                        status1 = False
                        status2 = False
                        status3 = False 
                        status4 = False
                        status5 = False
                        status6 = False
                        status7 = False 
                        status8 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_W.append(total_spots)
                        total_spots = []
                        break

        for key in self.Pieces_locations:
            if key[1] == 'R' and key[0] == 'W':
                rook.append(self.Pieces_locations[key])
        #  
        if rook != []:
            for i in range(0,len(rook)):
                piece_location = rook[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != '  ' and status1 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))
                            status1 = True
                    except:
                        status1 = True 

                    if status1 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                    try:
                        if int(piece_location[2])-j < 0:
                            status2 = True 
                        elif self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != '  ' and status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                            status2 = True
                        elif status2 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))
                    except: 
                        status2 = True 

                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != '  ' and status3 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))
                            status3 = True
                    except:
                        status3 = True 

                    if status3 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                    try: 
                        if int(piece_location[0])-j < 0:
                            status4 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != '  '  and status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                            status4 = True
                        elif status4 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                    except: 
                        status4 = True 

                    if status1 == True and status2 == True and status3 == True and status4 == True or j == 7:
                        status1 = False
                        status2 = False
                        status3 = False 
                        status4 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_W.append(total_spots)
                        total_spots = []
                        break 

        for key in self.Pieces_locations:
            if key[1] == 'B' and key[0] == 'W':
                bishop.append(self.Pieces_locations[key])
        if bishop != []:
            for i in range(0,len(bishop)):
                piece_location = bishop[i]
                for j in range(1,8):
                    try:
                        if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != '  ' and status5 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))
                            status5 = True
                    except:
                        status5 = True 
                    if status5 == False:
                        total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                    try:
                        if int(piece_location[2])-j <0 or int(piece_location[0])-j <0:
                            status6 = True 
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != '  '  and status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                            status6 = True
                        elif status6 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))
                    except: 
                        status6 = True 

                    try:
                        if int(piece_location[2])-j <0:
                            status7 = True
                        elif self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != '  '  and status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                            status7 = True
                        elif status7 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))
                    except:
                        status7 = True 

                    try: 
                        if int(piece_location[0])-j < 0:
                            status8 = True
                        elif self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != '  '  and status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                            status8 = True
                        elif status8 == False:
                            total_spots.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])+j))
                    except: 
                        status8 = True 



                    if status8 == True and status5 == True and status6 == True and status7 == True or j == 7:
                        status5 = False
                        status6 = False
                        status7 = False 
                        status8 = False
                        piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                        self.all_avaliable_moves_W.append(total_spots)
                        total_spots = []
                        break

        for key in self.Pieces_locations:
            if key[1] == 'N' and key[0] == 'W':
                knight.append(self.Pieces_locations[key])
        if knight != []:
            for i in range(0,len(knight)):
                piece_location = knight[i]
                try:
                    if int(piece_location[0])-2 > -1 and int(piece_location[2])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])+1))
                except:
                    pass 

                try:
                    if int(piece_location[0])-2 > -1 and int(piece_location[2])-1 > -1:
                        total_spots.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])-1))
                except:
                    pass

                try:
                    if int(piece_location[0])+2 <= 7 and int(piece_location[2])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])+1))
                except:
                    pass 

                try:
                    if int(piece_location[2])-1 > -1 and int(piece_location[0])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])-1))
                except:
                    pass 


                try:
                    if int(piece_location[0])+1 <= 7 and int(piece_location[2])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+2))
                except:
                    pass 

                try:
                    if int(piece_location[0])-1 > -1 and int(piece_location[2])-2 > -1:
                        total_spots.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-2))
                except:
                    pass

                try:
                    if int(piece_location[2])-2 > -1 and int(piece_location[0])+1 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-2))
                except:
                    pass 

                try:
                    if int(piece_location[0])-1 > -1 and int(piece_location[2])+2 <= 7:
                        total_spots.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])+2))
                except:
                    pass

                piece_visions[self.pieces_list[int(piece_location[0])][int(piece_location[2])]] = total_spots
                self.all_avaliable_moves_W.append(total_spots)
                total_spots = []

        return piece_visions


    def check_check(self):
        try: 
            self.pieces_left_B.remove(self.pieces_list[int(self.value2[0])][int(self.value2[1])])
        except ValueError: 
            self.pieces_left_W.remove(self.pieces_list[int(self.value2[0])][int(self.value2[1])])


def main():
    return Chess()

