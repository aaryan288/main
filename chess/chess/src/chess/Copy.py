def finding_all_checks(self, color): 
        # import pdb;pdb.set_trace()
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
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != ' ' or self.pieces_list[int(piece_location[0])][int(piece_location[2])+j][1] != 'K':
                        status1 = True
                except:
                    status1 = True 
                if status1 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0 or self.pieces_list[int(piece_location[0])][int(piece_location[2])-j][1] != 'K':
                        status2 = True
                except: 
                    status2 = True 
                if status2 == False:
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != ' ' or self.pieces_list[int(piece_location[0])+j][int(piece_location[2])][1] != 'K': 
                        status3 = True
                except:
                    status3 = True 
                if status3 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != ' ' or int(piece_location[0])-j < 0:
                        status4 = True
                except: 
                    status4 = True 
                if status4 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] == ' ':
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
        # import pdb;pdb.set_trace()
        for i in range(0,len(bishop_list)):
            piece_location = bishop_places[i]
            for j in range(1,8):
                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != ' ':
                        status5 = True
                except:
                    status5 = True 
                if status5 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                try:
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0 or int(piece_location[0])-j < 0:
                        status6 = True
                except: 
                    status6 = True 
                if status6 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0:
                        status7 = True
                except:
                    status7 = True 
                if status7 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != ' ' or int(piece_location[0])-j < 0:
                        status8 = True
                except: 
                    status8 = True 
                if status8 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] == ' ':
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

        for i in range(0,len(Queen_list)):
            piece_location = Queen_places[i]
            for j in range(1,8):
                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] != ' ':
                        status1 = True
                except:
                    status1 = True 
                if status1 == False and self.pieces_list[int(piece_location[0])][int(piece_location[2])+j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2]) +j))

                try:
                    if self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0:
                        status2 = True
                except: 
                    status2 = True 
                if status2 == False and self.pieces_list[int(piece_location[0])][int(piece_location[2])-j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0]),int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] != ' ':
                        status3 = True
                except:
                    status3 = True 
                if status3 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] != ' ' or int(piece_location[0])-j < 0:
                        status4 = True
                except: 
                    status4 = True 
                if status4 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])-j,int(piece_location[2])))
                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] != ' ':
                        status5 = True
                except:
                    status5 = True 
                if status5 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])+j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])+j))

                try:
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0 or int(piece_location[0])-j < 0:
                        status6 = True
                except: 
                    status6 = True 
                if status6 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])-j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0]-j),int(piece_location[2])-j))

                try:
                    if self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] != ' ' or int(piece_location[2])-j < 0:
                        status7 = True
                except:
                    status7 = True 
                if status7 == False and self.pieces_list[int(piece_location[0])+j][int(piece_location[2])-j] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+j,int(piece_location[2])-j))

                try: 
                    if self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] != ' ' or int(piece_location[0])-j < 0:
                        status8 = True
                except: 
                    status8 = True 
                if status8 == False and self.pieces_list[int(piece_location[0])-j][int(piece_location[2])+j] == ' ':
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
                if self.pieces_list[int(piece_location[0])-2][int(piece_location[2])+1] == ' ' and int(piece_location[0])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])+1))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-2][int(piece_location[2])-1] == ' ' and int(piece_location[0])-2 > -1 and int(piece_location[2])-1 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-2,int(piece_location[2])-1))
            except:
                pass

            try:
                if self.pieces_list[int(piece_location[0])+2][int(piece_location[2])+1] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])+1))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])+2][int(piece_location[2])-1] == ' ' and int(piece_location[2])-1 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])+2,int(piece_location[2])-1))
            except:
                pass 




            try:
                if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+2] == ' ':
                    check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+2))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-2] == ' ' and int(piece_location[0])-1 > -1 and int(piece_location[2])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-2))
            except:
                pass

            try:
                if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-2] == ' ' and int(piece_location[2])-2 > -1:
                    check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-2))
            except:
                pass 

            try:
                if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+2] == ' ' and int(piece_location[0])-1 > -1:
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
                    if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])+1] == ' ' and int(piece_location[0])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])+1))
                except:
                    pass
                try:
                    if self.pieces_list[int(piece_location[0])-1][int(piece_location[2])-1] == ' ' and int(piece_location[2])-1 > -1 and int(piece_location[0])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])-1,int(piece_location[2])-1))
                except:
                    pass
        elif color == self.pieces_left_B:
            for i in range(0,len(pawn_list)):
                piece_location = pawn_places[i]
                try:
                    if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])+1] == ' ':
                        check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])+1))
                except:
                    pass
                try:
                    if self.pieces_list[int(piece_location[0])+1][int(piece_location[2])-1] == ' ' and int(piece_location[2])-1 > -1:
                        check_locations.append('{},{}'.format(int(piece_location[0])+1,int(piece_location[2])-1))
                except:
                    pass


        check_locations = sorted(list(set(check_locations)))
        if color == self.pieces_left_W:
            self.white_checks = check_locations
        elif color == self.pieces_left_B:
            self.black_checks = check_locations

        print(self.black_checks)
        print('\n')
        print(self.white_checks)
        print('\n')