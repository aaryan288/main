elif self.count %2 == 0:
    if ','.join(self.value1) in self.black_checks:
        if ','.join(self.value2) in self.black_checks:
            self.value1 = ''
            self.value2 = ''
            # self.count+= 1
            return

        elif self.pieces_list[int(self.value2[0])][int(self.value2[1])] == '  ':
            self.white_king_position = ','.join(self.value2)
            self.replace()
        else:
            if ','.join(self.value2) != '  ':
                self.pieces_left_B.remove(self.pieces_list[int(self.value2[0])][int(self.value2[1])])
                attacker = self.pieces_list[int(self.value2[0])][int(self.value2[1])]
            self.pieces_list[int(self.value1[0])][int(self.value1[1])] = '  '
            self.pieces_list[int(self.value2[0])][int(self.value2[1])] = self.piece
            self.finding_all_checks(self.pieces_left_B)
            if ','.join(self.value2) in self.black_checks:
                self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
                try:
                    self.pieces_list[int(self.value2[0])][int(self.value2[1])] = attacker
                except:
                    self.pieces_list[int(self.value2[0])][int(self.value2[1])] = '  '
                try:
                    self.pieces_left_B.append(attacker)
                except:
                    self.value1 = ''
                    self.value2 = ''
                self.value1 = ''
                self.value2 = ''
            else: 
                self.changeing_value('1', ','.join(self.value2),self.piece)
                self.changeing_value('1', ','.join(self.value1), '  ')
                self.finding_all_checks(self.pieces_left_W)
                self.finding_all_checks(self.pieces_left_B)
                self.white_king_position = ','.join(self.value2)
                self.value1 = ''
                self.value2 = ''
                self.count += 1
                if self.checkmate_white_pieces(attacker):
                    print('Game over')

    elif ','.join(self.value2) in self.black_checks:
        self.value1 = ''
        self.value2 = ''
        # self.count+= 1
        return
else:
    if ','.join(self.value1) in self.white_checks:
        if ','.join(self.value2) in self.white_checks:
            self.value1 = ''
            self.value2 = ''
            # self.count+= 1
            return
        elif self.pieces_list[int(self.value2[0])][int(self.value2[1])] == '  ':
            self.black_king_position = ','.join(self.value2)
            self.replace()
        else:
            if ','.join(self.value2) != '  ':
                self.pieces_left_W.remove(self.pieces_list[int(self.value2[0])][int(self.value2[1])])
                attacker = self.pieces_list[int(self.value2[0])][int(self.value2[1])]
            self.pieces_list[int(self.value1[0])][int(self.value1[1])] = '  '
            self.pieces_list[int(self.value2[0])][int(self.value2[1])] = self.piece
            self.finding_all_checks(self.pieces_left_W)
            if ','.join(self.value2) in self.white_checks:
                self.pieces_list[int(self.value1[0])][int(self.value1[1])] = self.piece
                try:
                    self.pieces_list[int(self.value2[0])][int(self.value2[1])] = attacker
                except:
                    self.pieces_list[int(self.value2[0])][int(self.value2[1])] = '  '
                try:
                    self.pieces_left_W.append(attacker)
                except:
                    self.value1 = ''
                    self.value2 = ''
                self.value1 = ''
                self.value2 = ''
            else: 
                self.changeing_value('1', ','.join(self.value2),self.piece)
                self.changeing_value('1', ','.join(self.value1), '  ')
                self.finding_all_checks(self.pieces_left_W)
                self.finding_all_checks(self.pieces_left_B)
                self.black_king_position = ','.join(self.value2)
                self.value1 = ''
                self.value2 = ''
                self.count += 1
                if self.checkmate_white_pieces(attacker):
                    print('Game over')
    elif ','.join(self.value2) in self.white_checks:
        self.value1 = ''
        self.value2 = ''
        # self.count+= 1
        return


self.finding_all_checks(self.pieces_left_W)
self.finding_all_checks(self.pieces_left_B)