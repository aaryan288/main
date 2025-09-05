"""
God
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,CENTER
from random import shuffle
from random import randint
from copy import deepcopy
from functools import partial
from toga.constants import RED, WHITE, ORANGE, BROWN, GREEN, WHITE, BLACK,BLUE


class Sudoku(toga.App):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    row10 = []
    value1 = []
    main_frame = []
    showing_frame = []
    color_button = ''
    strike = 0
    def sudoku_code(self):
        # import pdb;pdb.set_trace()
        row1 = [1,2,3,4,5,6,7,8,9]
        row2 = [5,9,7,1,3,8,2,4,6]
        f = [1,2,3,4,5,6,7,8,9]
        row3 = []
        row4 = []
        row5 = [1,2,3,4,4,5,6,7,8,9]
        row6 = []
        row7 = []
        row8 = []
        row9 = []
        column1 = []
        column2 = []
        column3 = []
        column4 = []
        column5 = []
        column6 = []
        column7 = []
        column8 = []
        column9 = []
        boz1 = []
        boz2 = []
        boz3 = []
        boz4 = []
        boz5 = []
        boz6 = []
        boz7 = []
        boz8 = []   
        boz9 = []
        status = True

        shuffle(row1)
        self.check1(row1,boz1,boz2,boz3)
        shuffle(row2)
        self.rows(row2,boz1,boz2,boz3)
        shuffle(row3)
        self.last_row(f,boz1,boz2,boz3,row3)
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

        column1.append(row1[0])
        column2.append(row1[1])
        column3.append(row1[2])
        column4.append(row1[3])
        column5.append(row1[4])
        column6.append(row1[5])
        column7.append(row1[6])
        column8.append(row1[7])
        column9.append(row1[8])

        column1.append(row2[0])
        column2.append(row2[1])
        column3.append(row2[2])
        column4.append(row2[3])
        column5.append(row2[4])
        column6.append(row2[5])
        column7.append(row2[6])
        column8.append(row2[7])
        column9.append(row2[8])

        column1.append(row3[0])
        column2.append(row3[1])
        column3.append(row3[2])
        column4.append(row3[3])
        column5.append(row3[4])
        column6.append(row3[5])
        column7.append(row3[6])
        column8.append(row3[7])
        column9.append(row3[8])

        # print(self.row1)
        self.row4 = self.creating_rows7to9(row4,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz4,boz5,boz6)
        self.check1(self.row4,boz4,boz5,boz6)
        self.row5 = self.creating_rows7to9(row5,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz4,boz5,boz6)
        self.check1(self.row5,boz4,boz5,boz6)
        self.row10 = self.creating_rows7to9(row6,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz4,boz5,boz6)
        if type(self.row10) == list and self.row10 != []:
            self.row6 = self.row10
        try:
            self.check1(self.row10,boz4,boz5,boz6)
            self.row7 = self.creating_rows7to9(row7,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz7,boz8,boz9)
            self.check1(self.row7,boz7,boz8,boz9)
            self.row8 = self.creating_rows7to9(row8,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz7,boz8,boz9)
            self.check1(self.row8,boz7,boz8,boz9)
            self.row9 = self.creating_rows7to9(row9,column1,column2,column3,column4,column5,column6,column7,column8,column9,boz7,boz8,boz9)
            self.check1(self.row9,boz7,boz8,boz9)
        except:
            self.check1(self.row6,boz4,boz5,boz6)
            pass

        self.main_frame = deepcopy([self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8,self.row9])



    def creating_rows7to9(self,r7,c1,c2,c3,c4,c5,c6,c7,c8,c9,boz1,boz2,boz3):
        # if len(boz1) == 6:
            # import pdb;pdb.set_trace()
        basic = [1,2,3,4,5,6,7,8,9]
        shuffle(basic)

        c1_values_left = []
        c2_values_left = []
        c3_values_left = []
        c4_values_left = []
        c5_values_left = []
        c6_values_left = []
        c7_values_left = []
        c8_values_left = []
        c9_values_left = []
        remainder = []
        for i in basic:
            if i not in c1 and i not in boz1:
                c1_values_left.append(i)
            if i not in c2 and i not in boz1:
                c2_values_left.append(i)
            if i not in c3 and i not in boz1:
                c3_values_left.append(i)
            if i not in c4 and i not in boz2:
                c4_values_left.append(i)
            if i not in c5 and i not in boz2:
                c5_values_left.append(i)
            if i not in c6 and i not in boz2:
                c6_values_left.append(i)
            if i not in c7 and i not in boz3:
                c7_values_left.append(i)
            if i not in c8 and i not in boz3:
                c8_values_left.append(i)
            if i not in c9 and i not in boz3:
                c9_values_left.append(i)

        if c1_values_left == [] or c2_values_left == [] or c3_values_left == [] or c4_values_left == [] or c5_values_left == [] or c7_values_left == [] or c6_values_left == [] or c8_values_left == [] or c9_values_left == []:
            self.sudoku_code()
            return

        r7 = [c1_values_left[0],c2_values_left[0],c3_values_left[0],c4_values_left[0],c5_values_left[0],c6_values_left[0],c7_values_left[0],c8_values_left[0],c9_values_left[0]]
        if len(set(r7)) != 9:
            r7 = self.finding_missing_values(r7,c1_values_left,c2_values_left,c3_values_left,c4_values_left,c5_values_left,c6_values_left,c7_values_left,c8_values_left,c9_values_left,0)
        c1.append(r7[0])
        c2.append(r7[1])
        c3.append(r7[2])
        c4.append(r7[3])
        c5.append(r7[4])
        c6.append(r7[5])
        c7.append(r7[6])
        c8.append(r7[7])
        c9.append(r7[8])
        return r7


    def finding_missing_values(self,row,c1,c2,c3,c4,c5,c6,c7,c8,c9,num):
        row = []
        for a in range(0,len(c1)):
            for b in range(0,len(c2)):
                for c in range(0,len(c3)):
                    for d in range(0,len(c4)):
                        for e in range(0,len(c5)):
                            for f in range(0,len(c6)):
                                for g in range(0,len(c7)):
                                    for h in range(0,len(c8)):
                                        for i in range(0,len(c9)):
                                            row = [c1[a],c2[b],c3[c],c4[d],c5[e],c6[f],c7[g],c8[h],c9[i]]
                                            if len(set(row)) == 9:
                                                return row




    def check1(self,e,b,c,d):
        for i in range(0,len(e)):
            if i >= 0 and i <=2:
                b.append(e[i])
            elif i > 2 and i <= 5:
                c.append(e[i])
            else:
                d.append(e[i])

    def loopsss(self,a,c,length,num):
        j = 0
        while length+num != len(c):
            if a[j] not in c:
                c.append(a[j])
                a.pop(j)
            else:
                j+=1
        j = 0

    def rows(self,a,b,c,d):
        # import pdb;pdb.set_trace()
        j = 0
        lengthb = len(b)
        lengthc = len(c)
        lengthd = len(d)
        self.loopsss(a,b,lengthb,3)
        self.loopsss(a,c,lengthc,3)
        while lengthd+3 != len(d):
            try:
                if a[j] not in d:
                    d.append(a[j])
                    a.pop(j)
                else:
                    j+=1
            except IndexError:
                # import pdb;pdb.set_trace()
                i = 0
                while len(a) != 0:
                    for j in range(3,5):
                        if b[j] not in d:
                            d.insert(j,b[j])
                            b.remove(b[j])
                            b.insert(j,a[i])
                            a.remove(a[i])
                            break
                        elif c[j] not in d:
                            d.insert(j,c[j])
                            c.remove(c[j])
                            c.insert(j,a[i])
                            a.remove(a[i])
                            break

        for i in range(0,9):
            if i <= 2:
                a.append(b[i+3])
            elif i > 2 and i <= 5:
                a.append(c[i])
            elif i > 5 and i <= 8:
                a.append(d[i-3])

    def last_row(self,a,b,c,d,e):
        for i in a:
            if i not in b:
                b.append(i)
            elif i not in c:
                c.append(i)
            elif i not in d:
                d.append(i)

        for i in range(0,9):
            if i <= 2:
                e.append(b[i+6])
            elif i > 2 and i <= 5:
                e.append(c[i+3])
            elif i > 5 and i <= 8:
                e.append(d[i])

    def creating_columns(self,a,b,c,d,e,f,g,h,dc,j,k,l):
        for i in range(0,9):
            if i == 0:
                d.append(a[i])
                d.append(b[i]) 
                d.append(c[i])  
            if i == 1:
                e.append(a[i])
                e.append(b[i]) 
                e.append(c[i])  
            if i == 2:
                f.append(a[i])
                f.append(b[i]) 
                f.append(c[i])  
            if i == 3:
                g.append(a[i])
                g.append(b[i]) 
                g.append(c[i])  
            if i == 4:
                h.append(a[i])
                h.append(b[i]) 
                h.append(c[i])  
            if i == 5:
                dc.append(a[i])
                dc.append(b[i]) 
                dc.append(c[i])  
            if i == 6:
                j.append(a[i])
                j.append(b[i]) 
                j.append(c[i])  
            if i == 7:
                k.append(a[i])
                k.append(b[i]) 
                k.append(c[i])  
            if i == 8:
                l.append(a[i])
                l.append(b[i]) 
                l.append(c[i])

# Change color of button that has been selected even if it's empty
    def replace1(self,widget,number,color):
        self.reset_mode()
        try:
            if self.value1 == [] and self.showing_frame[int(number[0])][int(number[2])] == ' ':
                self.value1 = number
                self.color_button = color
                self.changing_buttons(self.value1,' ','BLUE')
            elif self.value1 != [] and type(number) == str and self.showing_frame[int(number[0])][int(number[2])] == ' ':
                self.value1 = number
                self.color_button = color
                self.changing_buttons(self.value1,' ','BLUE')
            elif number in [1,2,3,4,5,6,7,8,9]:
                if self.main_frame[int(self.value1[0])][int(self.value1[2])] == number:
                    self.changing_buttons(self.value1,number,self.color_button)
                    self.showing_frame[int(self.value1[0])][int(self.value1[2])] = number
                    if self.showing_frame == self.main_frame:
                        self.main_window.info_dialog('You win', 'You have completed the game!!')
                else:
                    self.strike+=1
                    if self.strike<5 and self.strike==1:
                        self.main_window.info_dialog(f'You got {self.strike} strike', f'You got {5-self.strike} strikes left')
                        self.button91.text = (f'strikes: {5-self.strike}')
                    elif self.strike<5 and self.strike>1:
                        self.main_window.info_dialog(f'You got {self.strike} strikes', f'You got {5-self.strike} strike left')
                        self.button91.text = (f'strikes: {5-self.strike}')
                    else:
                        self.main_window.info_dialog(f'You lose', f'You got 5 strikes!!')
                        self.button91.text = (f'strikes: {5}')
                        self.main_window.close()
                self.value1 = []
            elif self.showing_frame[int(number[0])][int(number[2])] != ' ':
                self.value1 = number
                number_inside_button = self.main_frame[int(self.value1[0])][int(self.value1[2])]
                for i in range(0,9):
                    for j in range(0,9):
                        if self.showing_frame[i][j] == number_inside_button:
                            numero = ('{},{}'.format(i,j))
                            self.changing_buttons(numero,number_inside_button,'BLUE')

        except:
            self.main_window.info_dialog('You have not selected a square', 'Please select one to continue')





    



    def changing_buttons(self,number,number1,color):
        if number == '0,0':
            self.button1.style.background_color = color
            self.button1.refresh()
            self.button1.text = number1

        elif number == '0,1':
            self.button2.style.background_color = color
            self.button2.refresh()
            self.button2.text = number1

        elif number == '0,2':
            self.button3.style.background_color = color
            self.button3.refresh()
            self.button3.text = number1

        elif number == '0,3':
            self.button4.style.background_color = color
            self.button4.refresh()
            self.button4.text = number1

        elif number == '0,4':
            self.button5.style.background_color = color
            self.button5.refresh()
            self.button5.text = number1

        elif number == '0,5':
            self.button6.style.background_color = color
            self.button6.refresh()
            self.button6.text = number1

        elif number == '0,6':
            self.button7.style.background_color = color
            self.button7.refresh()
            self.button7.text = number1

        elif number == '0,7':
            self.button8.style.background_color = color
            self.button8.refresh()
            self.button8.text = number1

        elif number == '0,8':
            self.button9.style.background_color = color
            self.button9.refresh()
            self.button9.text = number1



        elif number == '1,0':
            self.button10.style.background_color = color
            self.button10.refresh()
            self.button10.text = number1

        elif number == '1,1':
            self.button11.style.background_color = color
            self.button11.refresh()
            self.button11.text = number1

        elif number == '1,2':
            self.button12.style.background_color = color
            self.button12.refresh()
            self.button12.text = number1

        elif number == '1,3':
            self.button13.style.background_color = color
            self.button13.refresh()
            self.button13.text = number1

        elif number == '1,4':
            self.button14.style.background_color = color
            self.button14.refresh()
            self.button14.text = number1

        elif number == '1,5':
            self.button15.style.background_color = color
            self.button15.refresh()
            self.button15.text = number1

        elif number == '1,6':
            self.button16.style.background_color = color
            self.button16.refresh()
            self.button16.text = number1

        elif number == '1,7':
            self.button17.style.background_color = color
            self.button17.refresh()
            self.button17.text = number1

        elif number == '1,8':
            self.button18.style.background_color = color
            self.button18.refresh()
            self.button18.text = number1



        elif number == '2,0':
            self.button19.style.background_color = color
            self.button19.refresh()
            self.button19.text = number1

        elif number == '2,1':
            self.button20.style.background_color = color
            self.button20.refresh()
            self.button20.text = number1

        elif number == '2,2':
            self.button21.style.background_color = color
            self.button21.refresh()
            self.button21.text = number1

        elif number == '2,3':
            self.button22.style.background_color = color
            self.button22.refresh()
            self.button22.text = number1

        elif number == '2,4':
            self.button23.style.background_color = color
            self.button23.refresh()
            self.button23.text = number1

        elif number == '2,5':
            self.button24.style.background_color = color
            self.button24.refresh()
            self.button24.text = number1

        elif number == '2,6':
            self.button25.style.background_color = color
            self.button25.refresh()
            self.button25.text = number1

        elif number == '2,7':
            self.button26.style.background_color = color
            self.button26.refresh()
            self.button26.text = number1

        elif number == '2,8':
            self.button27.style.background_color = color
            self.button27.refresh()
            self.button27.text = number1



        elif number == '3,0':
            self.button28.style.background_color = color
            self.button28.refresh()
            self.button28.text = number1

        elif number == '3,1':
            self.button29.style.background_color = color
            self.button29.refresh()
            self.button29.text = number1

        elif number == '3,2':
            self.button30.style.background_color = color
            self.button30.refresh()
            self.button30.text = number1

        elif number == '3,3':
            self.button31.style.background_color = color
            self.button31.refresh()
            self.button31.text = number1

        elif number == '3,4':
            self.button32.style.background_color = color
            self.button32.refresh()
            self.button32.text = number1

        elif number == '3,5':
            self.button33.style.background_color = color
            self.button33.refresh()
            self.button33.text = number1

        elif number == '3,6':
            self.button34.style.background_color = color
            self.button34.refresh()
            self.button34.text = number1

        elif number == '3,7':
            self.button35.style.background_color = color
            self.button35.refresh()
            self.button35.text = number1

        elif number == '3,8':
            self.button36.style.background_color = color
            self.button36.refresh()
            self.button36.text = number1


        elif number == '4,0':
            self.button37.style.background_color = color
            self.button37.refresh()
            self.button37.text = number1

        elif number == '4,1':
            self.button38.style.background_color = color
            self.button38.refresh()
            self.button38.text = number1

        elif number == '4,2':
            self.button39.style.background_color = color
            self.button39.refresh()
            self.button39.text = number1

        elif number == '4,3':
            self.button40.style.background_color = color
            self.button40.refresh()
            self.button40.text = number1

        elif number == '4,4':
            self.button41.style.background_color = color
            self.button41.refresh()
            self.button41.text = number1

        elif number == '4,5':
            self.button42.style.background_color = color
            self.button42.refresh()
            self.button42.text = number1

        elif number == '4,6':
            self.button43.style.background_color = color
            self.button43.refresh()
            self.button43.text = number1

        elif number == '4,7':
            self.button44.style.background_color = color
            self.button44.refresh()
            self.button44.text = number1

        elif number == '4,8':
            self.button45.style.background_color = color
            self.button45.refresh()
            self.button45.text = number1



        elif number == '5,0':
            self.button46.style.background_color = color
            self.button46.refresh()
            self.button46.text = number1

        elif number == '5,1':
            self.button47.style.background_color = color
            self.button47.refresh()
            self.button47.text = number1

        elif number == '5,2':
            self.button48.style.background_color = color
            self.button48.refresh()
            self.button48.text = number1

        elif number == '5,3':
            self.button49.style.background_color = color
            self.button49.refresh()
            self.button49.text = number1

        elif number == '5,4':
            self.button50.style.background_color = color
            self.button50.refresh()
            self.button50.text = number1

        elif number == '5,5':
            self.button51.style.background_color = color
            self.button51.refresh()
            self.button51.text = number1

        elif number == '5,6':
            self.button52.style.background_color = color
            self.button52.refresh()
            self.button52.text = number1

        elif number == '5,7':
            self.button53.style.background_color = color
            self.button53.refresh()
            self.button53.text = number1

        elif number == '5,8':
            self.button54.style.background_color = color
            self.button54.refresh()
            self.button54.text = number1



        elif number == '6,0':
            self.button55.style.background_color = color
            self.button55.refresh()
            self.button55.text = number1

        elif number == '6,1':
            self.button56.style.background_color = color
            self.button56.refresh()
            self.button56.text = number1

        elif number == '6,2':
            self.button57.style.background_color = color
            self.button57.refresh()
            self.button57.text = number1

        elif number == '6,3':
            self.button58.style.background_color = color
            self.button58.refresh()
            self.button58.text = number1

        elif number == '6,4':
            self.button59.style.background_color = color
            self.button59.refresh()
            self.button59.text = number1

        elif number == '6,5':
            self.button60.style.background_color = color
            self.button60.refresh()
            self.button60.text = number1

        elif number == '6,6':
            self.button61.style.background_color = color
            self.button61.refresh()
            self.button61.text = number1

        elif number == '6,7':
            self.button62.style.background_color = color
            self.button62.refresh()
            self.button62.text = number1

        elif number == '6,8':
            self.button63.style.background_color = color
            self.button63.refresh()
            self.button63.text = number1



        elif number == '7,0':
            self.button64.style.background_color = color
            self.button64.refresh()
            self.button64.text = number1

        elif number == '7,1':
            self.button65.style.background_color = color
            self.button65.refresh()
            self.button65.text = number1

        elif number == '7,2':
            self.button66.style.background_color = color
            self.button66.refresh()
            self.button66.text = number1

        elif number == '7,3':
            self.button67.style.background_color = color
            self.button67.refresh()
            self.button67.text = number1

        elif number == '7,4':
            self.button68.style.background_color = color
            self.button68.refresh()
            self.button68.text = number1

        elif number == '7,5':
            self.button69.style.background_color = color
            self.button69.refresh()
            self.button69.text = number1

        elif number == '7,6':
            self.button70.style.background_color = color
            self.button70.refresh()
            self.button70.text = number1

        elif number == '7,7':
            self.button71.style.background_color = color
            self.button71.refresh()
            self.button71.text = number1

        elif number == '7,8':
            self.button72.style.background_color = color
            self.button72.refresh()
            self.button72.text = number1


        elif number == '8,0':
            self.button73.style.background_color = color
            self.button73.refresh()
            self.button73.text = number1

        elif number == '8,1':
            self.button74.style.background_color = color
            self.button74.refresh()
            self.button74.text = number1

        elif number == '8,2':
            self.button75.style.background_color = color
            self.button75.refresh()
            self.button75.text = number1

        elif number == '8,3':
            self.button76.style.background_color = color
            self.button76.refresh()
            self.button76.text = number1

        elif number == '8,4':
            self.button77.style.background_color = color
            self.button77.refresh()
            self.button77.text = number1

        elif number == '8,5':
            self.button78.style.background_color = color
            self.button78.refresh()
            self.button78.text = number1

        elif number == '8,6':
            self.button79.style.background_color = color
            self.button79.refresh()
            self.button79.text = number1

        elif number == '8,7':
            self.button80.style.background_color = color
            self.button80.refresh()
            self.button80.text = number1

        elif number == '8,8':
            self.button81.style.background_color = color
            self.button81.refresh()
            self.button81.text = number1


    def randomizer(self):
        # import pdb;pdb.set_trace()
        l = 0
        j = 0
        row1s = randint(1,9)
        row2s = randint(1,9)
        row3s = randint(1,9)
        row4s = randint(1,9)
        row5s = randint(1,9)
        row6s = randint(1,9)
        row7s = randint(1,9)
        row8s = randint(1,9)
        row9s = randint(1,9)
        self.smaller_code(j,l,row1s,self.row1)
        self.smaller_code(j,l,row2s,self.row2)
        self.smaller_code(j,l,row3s,self.row3)
        self.smaller_code(j,l,row4s,self.row4)
        self.smaller_code(j,l,row5s,self.row5)
        self.smaller_code(j,l,row6s,self.row6)
        self.smaller_code(j,l,row7s,self.row7)
        self.smaller_code(j,l,row8s,self.row8)
        self.smaller_code(j,l,row9s,self.row9)
        


    def smaller_code(self,j,l,value,row):
        try:
            while j != value:
                i = randint(1,10)
                if i % 2 == 1:
                    row.pop(l)
                    row.insert(l,' ')
                    j +=1
                    l +=1
                else:
                    l+=1
        except:
            return


    def reset_mode(self):
        self.button1.style.background_color = WHITE
        self.button2.style.background_color = WHITE
        self.button3.style.background_color = WHITE
        self.button4.style.background_color = BLACK
        self.button5.style.background_color = BLACK
        self.button6.style.background_color = BLACK
        self.button7.style.background_color = WHITE
        self.button8.style.background_color = WHITE
        self.button9.style.background_color = WHITE

        self.button10.style.background_color = WHITE
        self.button11.style.background_color = WHITE
        self.button12.style.background_color = WHITE
        self.button13.style.background_color = BLACK
        self.button14.style.background_color = BLACK
        self.button15.style.background_color = BLACK
        self.button16.style.background_color = WHITE
        self.button17.style.background_color = WHITE
        self.button18.style.background_color = WHITE

        self.button19.style.background_color = WHITE
        self.button20.style.background_color = WHITE
        self.button21.style.background_color = WHITE
        self.button22.style.background_color = BLACK
        self.button23.style.background_color = BLACK
        self.button24.style.background_color = BLACK
        self.button25.style.background_color = WHITE
        self.button26.style.background_color = WHITE
        self.button27.style.background_color = WHITE

        self.button28.style.background_color = BLACK
        self.button29.style.background_color = BLACK
        self.button30.style.background_color = BLACK
        self.button31.style.background_color = WHITE
        self.button32.style.background_color = WHITE
        self.button33.style.background_color = WHITE
        self.button34.style.background_color = BLACK
        self.button35.style.background_color = BLACK
        self.button36.style.background_color = BLACK

        self.button37.style.background_color = BLACK
        self.button38.style.background_color = BLACK
        self.button39.style.background_color = BLACK
        self.button40.style.background_color = WHITE
        self.button41.style.background_color = WHITE
        self.button42.style.background_color = WHITE
        self.button43.style.background_color = BLACK
        self.button44.style.background_color = BLACK
        self.button45.style.background_color = BLACK

        self.button46.style.background_color = BLACK
        self.button47.style.background_color = BLACK
        self.button48.style.background_color = BLACK
        self.button49.style.background_color = WHITE
        self.button50.style.background_color = WHITE
        self.button51.style.background_color = WHITE
        self.button52.style.background_color = BLACK
        self.button53.style.background_color = BLACK
        self.button54.style.background_color = BLACK

        self.button55.style.background_color = WHITE
        self.button56.style.background_color = WHITE
        self.button57.style.background_color = WHITE
        self.button58.style.background_color = BLACK
        self.button59.style.background_color = BLACK
        self.button60.style.background_color = BLACK
        self.button61.style.background_color = WHITE
        self.button62.style.background_color = WHITE
        self.button63.style.background_color = WHITE

        self.button64.style.background_color = WHITE
        self.button65.style.background_color = WHITE
        self.button66.style.background_color = WHITE
        self.button67.style.background_color = BLACK
        self.button68.style.background_color = BLACK
        self.button69.style.background_color = BLACK
        self.button70.style.background_color = WHITE
        self.button71.style.background_color = WHITE
        self.button72.style.background_color = WHITE

        self.button73.style.background_color = WHITE
        self.button74.style.background_color = WHITE
        self.button75.style.background_color = WHITE
        self.button76.style.background_color = BLACK
        self.button77.style.background_color = BLACK
        self.button78.style.background_color = BLACK
        self.button79.style.background_color = WHITE
        self.button80.style.background_color = WHITE
        self.button81.style.background_color = WHITE





    def startup(self):
        main_box = toga.Box(style = Pack(direction = COLUMN))
        row1 = toga.Box()
        row2 = toga.Box()
        row3 = toga.Box()
        row4 = toga.Box()
        row5 = toga.Box()
        row6 = toga.Box()
        row7 = toga.Box()
        row8 = toga.Box()
        row9 = toga.Box()
        row10 = toga.Box(style = Pack(padding_top = 30,alignment = CENTER,padding_left = 230))
        self.sudoku_code()
        self.randomizer()
        self.showing_frame = [self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8,self.row9]
        self.button1 = toga.Button(self.row1[0],on_press=partial(self.replace1, number= '0,0',color = 'WHITE'), style=Pack(width=80, height=80,font_size=20, background_color=WHITE, flex=1))
        self.button2 = toga.Button(self.row1[1], on_press=partial(self.replace1, number='0,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button3 = toga.Button(self.row1[2], on_press=partial(self.replace1, number='0,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button4 = toga.Button(self.row1[3], on_press=partial(self.replace1, number='0,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button5 = toga.Button(self.row1[4], on_press=partial(self.replace1, number='0,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button6 = toga.Button(self.row1[5], on_press=partial(self.replace1, number='0,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button7 = toga.Button(self.row1[6], on_press=partial(self.replace1, number='0,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button8 = toga.Button(self.row1[7], on_press=partial(self.replace1, number='0,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button9 = toga.Button(self.row1[8], on_press=partial(self.replace1, number='0,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        
        self.button10 = toga.Button(self.row2[0], on_press=partial(self.replace1, number='1,0',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button11 = toga.Button(self.row2[1], on_press=partial(self.replace1, number='1,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button12 = toga.Button(self.row2[2], on_press=partial(self.replace1, number='1,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button13 = toga.Button(self.row2[3], on_press=partial(self.replace1, number='1,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button14 = toga.Button(self.row2[4], on_press=partial(self.replace1, number='1,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button15 = toga.Button(self.row2[5], on_press=partial(self.replace1, number='1,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button16 = toga.Button(self.row2[6], on_press=partial(self.replace1, number='1,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button17 = toga.Button(self.row2[7], on_press=partial(self.replace1, number='1,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button18 = toga.Button(self.row2[8], on_press=partial(self.replace1, number='1,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        
        self.button19 = toga.Button(self.row3[0], on_press=partial(self.replace1, number='2,0',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button20 = toga.Button(self.row3[1], on_press=partial(self.replace1, number='2,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button21 = toga.Button(self.row3[2], on_press=partial(self.replace1, number='2,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button22 = toga.Button(self.row3[3], on_press=partial(self.replace1, number='2,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button23 = toga.Button(self.row3[4], on_press=partial(self.replace1, number='2,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button24 = toga.Button(self.row3[5], on_press=partial(self.replace1, number='2,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button25 = toga.Button(self.row3[6], on_press=partial(self.replace1, number='2,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button26 = toga.Button(self.row3[7], on_press=partial(self.replace1, number='2,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button27 = toga.Button(self.row3[8], on_press=partial(self.replace1, number='2,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        
        self.button28 = toga.Button(self.row4[0], on_press=partial(self.replace1, number='3,0',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button29 = toga.Button(self.row4[1], on_press=partial(self.replace1, number='3,1',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button30 = toga.Button(self.row4[2], on_press=partial(self.replace1, number='3,2',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button31 = toga.Button(self.row4[3], on_press=partial(self.replace1, number='3,3',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button32 = toga.Button(self.row4[4], on_press=partial(self.replace1, number='3,4',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button33 = toga.Button(self.row4[5], on_press=partial(self.replace1, number='3,5',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button34 = toga.Button(self.row4[6], on_press=partial(self.replace1, number='3,6',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button35 = toga.Button(self.row4[7], on_press=partial(self.replace1, number='3,7',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button36 = toga.Button(self.row4[8], on_press=partial(self.replace1, number='3,8',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        
        self.button37 = toga.Button(self.row5[0], on_press=partial(self.replace1, number='4,0',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button38 = toga.Button(self.row5[1], on_press=partial(self.replace1, number='4,1',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button39 = toga.Button(self.row5[2], on_press=partial(self.replace1, number='4,2',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button40 = toga.Button(self.row5[3], on_press=partial(self.replace1, number='4,3',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button41 = toga.Button(self.row5[4], on_press=partial(self.replace1, number='4,4',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button42 = toga.Button(self.row5[5], on_press=partial(self.replace1, number='4,5',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button43 = toga.Button(self.row5[6], on_press=partial(self.replace1, number='4,6',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button44 = toga.Button(self.row5[7], on_press=partial(self.replace1, number='4,7',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button45 = toga.Button(self.row5[8], on_press=partial(self.replace1, number='4,8',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        
        self.button46 = toga.Button(self.row6[0], on_press=partial(self.replace1, number='5,0',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button47 = toga.Button(self.row6[1], on_press=partial(self.replace1, number='5,1',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button48 = toga.Button(self.row6[2], on_press=partial(self.replace1, number='5,2',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button49 = toga.Button(self.row6[3], on_press=partial(self.replace1, number='5,3',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button50 = toga.Button(self.row6[4], on_press=partial(self.replace1, number='5,4',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button51 = toga.Button(self.row6[5], on_press=partial(self.replace1, number='5,5',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button52 = toga.Button(self.row6[6], on_press=partial(self.replace1, number='5,6',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button53 = toga.Button(self.row6[7], on_press=partial(self.replace1, number='5,7',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button54 = toga.Button(self.row6[8], on_press=partial(self.replace1, number='5,8',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        
        self.button55 = toga.Button(self.row7[0], on_press=partial(self.replace1, number='6,0',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button56 = toga.Button(self.row7[1], on_press=partial(self.replace1, number='6,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button57 = toga.Button(self.row7[2], on_press=partial(self.replace1, number='6,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button58 = toga.Button(self.row7[3], on_press=partial(self.replace1, number='6,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button59 = toga.Button(self.row7[4], on_press=partial(self.replace1, number='6,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button60 = toga.Button(self.row7[5], on_press=partial(self.replace1, number='6,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button61 = toga.Button(self.row7[6], on_press=partial(self.replace1, number='6,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button62 = toga.Button(self.row7[7], on_press=partial(self.replace1, number='6,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button63 = toga.Button(self.row7[8], on_press=partial(self.replace1, number='6,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        
        self.button64 = toga.Button(self.row8[0], on_press=partial(self.replace1, number='7,0',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button65 = toga.Button(self.row8[1], on_press=partial(self.replace1, number='7,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button66 = toga.Button(self.row8[2], on_press=partial(self.replace1, number='7,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button67 = toga.Button(self.row8[3], on_press=partial(self.replace1, number='7,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button68 = toga.Button(self.row8[4], on_press=partial(self.replace1, number='7,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button69 = toga.Button(self.row8[5], on_press=partial(self.replace1, number='7,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button70 = toga.Button(self.row8[6], on_press=partial(self.replace1, number='7,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button71 = toga.Button(self.row8[7], on_press=partial(self.replace1, number='7,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button72 = toga.Button(self.row8[8], on_press=partial(self.replace1, number='7,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))

        self.button73 = toga.Button(self.row9[0], on_press=partial(self.replace1, number='8,0',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button74 = toga.Button(self.row9[1], on_press=partial(self.replace1, number='8,1',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button75 = toga.Button(self.row9[2], on_press=partial(self.replace1, number='8,2',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button76 = toga.Button(self.row9[3], on_press=partial(self.replace1, number='8,3',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button77 = toga.Button(self.row9[4], on_press=partial(self.replace1, number='8,4',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button78 = toga.Button(self.row9[5], on_press=partial(self.replace1, number='8,5',color = 'BLACK'), style=Pack(width=80, height=80, font_size=20,  background_color=BLACK, flex=1))
        self.button79 = toga.Button(self.row9[6], on_press=partial(self.replace1, number='8,6',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button80 = toga.Button(self.row9[7], on_press=partial(self.replace1, number='8,7',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))
        self.button81 = toga.Button(self.row9[8], on_press=partial(self.replace1, number='8,8',color = 'WHITE'), style=Pack(width=80, height=80, font_size=20,  background_color=WHITE, flex=1))

        self.button82 = toga.Button(1, on_press=partial(self.replace1, number=1,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button83 = toga.Button(2, on_press=partial(self.replace1, number=2,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button84 = toga.Button(3, on_press=partial(self.replace1, number=3,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button85 = toga.Button(4, on_press=partial(self.replace1, number=4,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button86 = toga.Button(5, on_press=partial(self.replace1, number=5,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button87 = toga.Button(6, on_press=partial(self.replace1, number=6,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button88 = toga.Button(7, on_press=partial(self.replace1, number=7,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button89 = toga.Button(8, on_press=partial(self.replace1, number=8,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button90 = toga.Button(9, on_press=partial(self.replace1, number=9,color = 'BLACK'), style=Pack(width=30, height=30, font_size=10,  background_color=WHITE, flex=1))
        self.button91 = toga.Label('Strikes left: 5', style=Pack(width=200, height=30, font_size=10,padding_left =30, flex=1))
        row1.add(self.button1)
        row1.add(self.button2)
        row1.add(self.button3)
        row1.add(self.button4)
        row1.add(self.button5)
        row1.add(self.button6)
        row1.add(self.button7)
        row1.add(self.button8)
        row1.add(self.button9)

        row2.add(self.button10)
        row2.add(self.button11)
        row2.add(self.button12)
        row2.add(self.button13)
        row2.add(self.button14)
        row2.add(self.button15)
        row2.add(self.button16)
        row2.add(self.button17)
        row2.add(self.button18)

        row3.add(self.button19)
        row3.add(self.button20)
        row3.add(self.button21)
        row3.add(self.button22)
        row3.add(self.button23)
        row3.add(self.button24)
        row3.add(self.button25)
        row3.add(self.button26)
        row3.add(self.button27)

        row4.add(self.button28)
        row4.add(self.button29)
        row4.add(self.button30)
        row4.add(self.button31)
        row4.add(self.button32)
        row4.add(self.button33)
        row4.add(self.button34)
        row4.add(self.button35)
        row4.add(self.button36)

        row5.add(self.button37)
        row5.add(self.button38)
        row5.add(self.button39)
        row5.add(self.button40)
        row5.add(self.button41)
        row5.add(self.button42)
        row5.add(self.button43)
        row5.add(self.button44)
        row5.add(self.button45)

        row6.add(self.button46)
        row6.add(self.button47)
        row6.add(self.button48)
        row6.add(self.button49)
        row6.add(self.button50)
        row6.add(self.button51)
        row6.add(self.button52)
        row6.add(self.button53)
        row6.add(self.button54)

        row7.add(self.button55)
        row7.add(self.button56)
        row7.add(self.button57)
        row7.add(self.button58)
        row7.add(self.button59)
        row7.add(self.button60)
        row7.add(self.button61)
        row7.add(self.button62)
        row7.add(self.button63)

        row8.add(self.button64)
        row8.add(self.button65)
        row8.add(self.button66)
        row8.add(self.button67)
        row8.add(self.button68)
        row8.add(self.button69)
        row8.add(self.button70)
        row8.add(self.button71)
        row8.add(self.button72)

        row9.add(self.button73)
        row9.add(self.button74)
        row9.add(self.button75)
        row9.add(self.button76)
        row9.add(self.button77)
        row9.add(self.button78)
        row9.add(self.button79)
        row9.add(self.button80)
        row9.add(self.button81)

        row10.add(self.button82)
        row10.add(self.button83)
        row10.add(self.button84)
        row10.add(self.button85)
        row10.add(self.button86)
        row10.add(self.button87)
        row10.add(self.button88)
        row10.add(self.button89)
        row10.add(self.button90)
        row10.add(self.button91)

        main_box.add(row1)
        main_box.add(row2)
        main_box.add(row3)
        main_box.add(row4)
        main_box.add(row5)
        main_box.add(row6)
        main_box.add(row7)
        main_box.add(row8)
        main_box.add(row9)
        main_box.add(row10)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return Sudoku()
