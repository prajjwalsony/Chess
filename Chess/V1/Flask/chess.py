#ALL Tested
blackposn={'k':'e8', 'q':'d8','b1':'c8', 'b2':'f8', 'h1':'b8', 'h2':'g8', 'r1':'a8', 'r2':'h8', 'p1':'a7', 'p2':'b7', 'p3':'c7', 'p4':'d7', 'p5':'e7', 'p6':'f7', 'p7':'g7', 'p8':'h7'}
whiteposn={'k':'e1', 'q':'d1','b1':'c1', 'b2':'f1', 'h1':'a2', 'h2':'g1', 'r1':'a1', 'r2':'h1', 'p1':'a2', 'p2':'b2', 'p3':'c2', 'p4':'d2', 'p5':'e2', 'p6':'f2', 'p7':'g2', 'p8':'h2'}

positions=[['a1','b1','c1','d1','e1','f1','g1','h1'],['a2','b2','c2','d2','e2','f2','g2','h2'],['a3','b3','c3','d3','e3','f3','g3','h3'],['a4','b4','c4','d4','e4','f4','g4','h4'],['a5','b5','c5','d5','e5','f5','g5','h5'],['a6','b6','c6','d6','e6','f6','g6','h6'],['a7','b7','c7','d7','e7','f7','g7','h7'],['a8','b8','c8','d8','e8','f8','g8','h8']]

#Tested
def straight(posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now and 'posn' is the current position of piece
    p1_position=list(p1_position_d.values())
    p2_position=list(p2_position_d.values())
    x=['a','b','c','d','e','f','g','h']
    l=[[], [], [], []]#left right up down
    left, right, up, down=posn, posn, posn, posn
    lefti, righti, upi, downi=x.index(left[0]), x.index(right[0]), int(up[1])-1, int(down[1])-1
    for i in range(8):
        if lefti>=0:
            lefti-=1
            if lefti>=0:
                left=x[lefti]+left[1]
                if left in p1_position:
                    lefti=-1
                elif left in p2_position:
                    lefti=-1
                    list_to_store_value.append(left)
                else:
                    list_to_store_value.append(left)
        if righti<8:
            righti+=1
            if righti<8:
                right=x[righti]+right[1]
                if right in p1_position:
                    righti=8
                elif right in p2_position:
                    righti=8
                    list_to_store_value.append(right)
                else:
                    list_to_store_value.append(right)
        if upi<8:
            upi+=1
            if upi<8:
                up=up[0]+str(int(upi)+1)
                if up in p1_position:
                    upi=8
                elif up in p2_position:
                    upi=8
                    list_to_store_value.append(up)
                else:
                    list_to_store_value.append(up)
        if downi>=0:
            downi-=1
            if downi>=0:
                down=down[0]+str(int(downi)+1)
                if down in p1_position:
                    downi=-1
                elif down in p2_position:
                    downi=-1
                    list_to_store_value.append(down)
                else:
                    list_to_store_value.append(down)
    return list_to_store_value

#Tested
def diagonal(posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now and 'posn' is the current position of piece
    p1_position=list(p1_position_d.values())
    p2_position=list(p2_position_d.values())
    x=['a','b','c','d','e','f','g','h']
    l=[[], [], [], []]#left right up down
    posn=str(x.index(posn[0])+1)+posn[1]
    left_up, right_up, left_down, right_down=posn, posn, posn, posn
    # lefti, righti, upi, downi=x.index(left[0]), x.index(right[0]), int(up[1])-1, int(down[1])-1
    for i in range(8):
        if int(left_up[0])>0 and int(left_up[1])<9 :
            a, b=int(left_up[0])-1, int(left_up[1])+1
            if a>0 and b<9:
                left_up=str(a)+str(b)
                left_up_posn=x[int(left_up[0])-1]+left_up[1]
                if left_up_posn in p1_position:
                    left_up='99'
                elif left_up_posn in p2_position:
                    list_to_store_value.append(left_up_posn)
                    left_up='99'
                else:
                    list_to_store_value.append(left_up_posn)

        if int(right_up[0])<9 and int(right_up[1])<9 :
            a, b=int(right_up[0])+1, int(right_up[1])+1
            if a<9 and b<9:
                right_up=str(a)+str(b)
                right_up_posn=x[int(right_up[0])-1]+right_up[1]
                if right_up_posn in p1_position:
                    right_up='99'
                elif right_up_posn in p2_position:
                    list_to_store_value.append(right_up_posn)
                    right_up='99'
                else:
                    list_to_store_value.append(right_up_posn)

        if int(left_down[0])>0 and int(left_down[1])>0 :
            a, b=int(left_down[0])-1, int(left_down[1])-1
            if a>0 and b>0:
                left_down=str(a)+str(b)
                left_down_posn=x[int(left_down[0])-1]+left_down[1]
                if left_down_posn in p1_position:
                    left_down='00'
                elif left_down_posn in p2_position:
                    list_to_store_value.append(left_down_posn)
                    left_down='00'
                else:
                    list_to_store_value.append(left_down_posn)

        if int(right_down[0])<9 and int(right_down[1])>0 :
            a, b=int(right_down[0])+1, int(right_down[1])-1
            if a<9 and b>0:
                right_down=str(a)+str(b)
                right_down_posn=x[int(right_down[0])-1]+right_down[1]
                if right_down_posn in p1_position:
                    right_down='00'
                elif right_down_posn in p2_position:
                    list_to_store_value.append(right_down_posn)
                    right_down='00'
                else:
                    list_to_store_value.append(right_down_posn)


    return list_to_store_value

#Tested
def horse(posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now
    p1_position=list(p1_position_d.values())
    p2_position=list(p2_position_d.values())
    x=['a','b','c','d','e','f','g','h']
    a=int(x.index(posn[0]))+1
    b=int(posn[1])
    lst1=[str(a+2)+str(b+1),str(a+2)+str(b-1),str(a-2)+str(b+1),str(a-2)+str(b-1),str(a+1)+str(b+2),str(a-1)+str(b+2),str(a+1)+str(b-2),str(a-1)+str(b-2)]
    l=list_to_store_value

    for i in lst1:
        if len(str(i))==2 :
            if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                l.append(x[int(i[0])-1]+str(int(i[1])))
    l=set(l)-set(p1_position)
    
    return list(l)

#Tested
def pawn(posn,list_to_store_value, p1_position_d, p2_position_d, color_of_piece): # p1_position_d is position of piecies in dictionary form of player who has turn now    p1_position=list(p1_position_d.values()) color_of_the_piece=b/w
    def isValid(a, b):
        x=['a','b','c','d','e','f','g','h']
        if a<9 and a>0 and b<9 and b>0:
            return True
        return False
    
    p1_position=list(p1_position_d.values())
    p2_position=list(p2_position_d.values())
    x=['a','b','c','d','e','f','g','h']

    a=int(x.index(posn[0]))+1
    b=int(posn[1])

    val=1 if color_of_piece=='w' else -1
    new_posn=[[], []]
    if isValid(a+1, b+val)==True: #adding right diagonal cells
        new_posn[1].append(x[a]+str(b+val))
    if isValid(a-1, b+val)==True: #adding left diagonal cells
        new_posn[1].append(x[a-2]+str(b+val))
    if isValid(a, b+val)==True: #adding next cell if valid
        new_posn[0].append(x[a-1]+str(b+val))
    # if(a==2 and val==1 and isValid(a, b+2)==True):#next next cell if valid
    #     new_posn.append(str(x[a-1])+str(b+2))
    # if(a==7 and val==-1 and isValid(a, b-2)==True):#next next cell if valid
    #     new_posn.append(str(x[a-1])+str(b-2))
    new_posn[1]=list(set(new_posn[1]).intersection(set(p2_position)))
    new_posn[0]=list(set(new_posn[0])-set(p1_position)-set(p2_position))
    list_to_store_value.extend(new_posn[0])
    list_to_store_value.extend(new_posn[1])
    return list_to_store_value

#Tested
def king(posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now    p1_position=list(p1_position_d.values()) color_of_the_piece=b/w
    def isValid(a, b):
        x=['a','b','c','d','e','f','g','h']
        if a<9 and a>0 and b<9 and b>0:
            return True
        return False
    
    p1_position=list(p1_position_d.values())
    p2_position=list(p2_position_d.values())
    x=['a','b','c','d','e','f','g','h']
    l=[]
    a=int(x.index(posn[0]))+1
    b=int(posn[1])
    new_posn=[str(a+1)+str(b), str(a-1)+str(b), str(a)+str(b+1), str(a)+str(b-1), str(a+1)+str(b+1), str(a+1)+str(b-1), str(a-1)+str(b+1), str(a-1)+str(b-1)]
    for i in new_posn:
        if len(i)==2:
            if isValid(int(i[0]), int(i[1]))==True:
                l.append(x[int(i[0])-1]+i[1])
    list_to_store_value=list(set(l)-set(p1_position))
    return list_to_store_value

def queen(posn, list_to_store_value, p1_position_d, p2_position_d):
    l1=straight(posn, list_to_store_value, p1_position_d, p2_position_d)
    l2=diagonal(posn, list_to_store_value, p1_position_d, p2_position_d)
    list_to_store_value.extend(l1)
    list_to_store_value.extend(l2)
    return list_to_store_value

#
def find_moves(posn, p1_position_d, p2_position_d, color_of_piece):
    if not(posn in p1_position_d.values()):
        return "NULL"
    piece=''
    for key, value in p1_position_d.items():
        if posn == value:
            piece=key
            break
    i=piece[0]
    if i=='k': #k:king, q:queen, r=rook, b:bisop, p:pawn, h:horse
        return king(posn, [], p1_position_d, p2_position_d)
    elif i=='q':
        return queen(posn, [], p1_position_d, p2_position_d)
    elif i=='r':
        return straight(posn, [], p1_position_d, p2_position_d)
    elif i=='b':
        return diagonal(posn, [], p1_position_d, p2_position_d)
    elif i=='p':
        return pawn(posn, [], p1_position_d, p2_position_d, color_of_piece)
    elif i=='h':
        return horse(posn, [], p1_position_d, p2_position_d)



# def posibl_moves(p):#p is b/w indicating black or white turn
    l=[]
    if p=='b':
        for i in blackposn:
            if len(blackposn.get(i))==0:
                continue
            if i[0]=='r':
                l=straight(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='h':
                l=horse(blackposn.get(i),l,blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='b':
                l=diagonal(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='q':
                l=diagonal(8, blackposn.get(i), l, blackposn , whiteposn)
                l=straight(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='k':
                l=diagonal(1, blackposn.get(i), l, blackposn , whiteposn)
                l=straight(1, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='p':
                l=pawn('b',blackposn.get(i),l,blackposn , whiteposn)
                dict_possible_moves_p1.update({i:l})
                l=[]

        for i in whiteposn:
            if len(whiteposn.get(i))==0:
                continue
            if i[0]=='r':
                l=straight(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='h':
                l=horse(whiteposn.get(i),l,whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='b':
                l=diagonal(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='q':
                l=diagonal(8, whiteposn.get(i), l, whiteposn , blackposn)
                l=straight(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='k':
                l=diagonal(1, whiteposn.get(i), l, whiteposn , blackposn)
                l=straight(1, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='p':
                l=pawn('w',whiteposn.get(i),l,whiteposn , blackposn)
                dict_possible_moves_p2.update({i:l})
                l=[]


    if p=='w':
        for i in whiteposn:
            if len(whiteposn.get(i))==0:
                continue
            if i[0]=='r':
                l=straight(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='h':
                l=horse(whiteposn.get(i),l,whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='b':
                l=diagonal(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='q':
                l=diagonal(8, whiteposn.get(i), l, whiteposn , blackposn)
                l=straight(8, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='k':
                l=diagonal(1, whiteposn.get(i), l, whiteposn , blackposn)
                l=straight(1, whiteposn.get(i), l, whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]
            elif i[0]=='p':
                l=pawn('w',whiteposn.get(i),l,whiteposn , blackposn)
                dict_possible_moves_p1.update({i:l})
                l=[]

        for i in blackposn:
            if len(blackposn.get(i))==0:
                continue
            if i[0]=='r':
                l=straight(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='h':
                l=horse(blackposn.get(i),l,blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='b':
                l=diagonal(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='q':
                l=diagonal(8, blackposn.get(i), l, blackposn , whiteposn)
                l=straight(8, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='k':
                l=diagonal(1, blackposn.get(i), l, blackposn , whiteposn)
                l=straight(1, blackposn.get(i), l, blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
            elif i[0]=='p':
                l=pawn('b',blackposn.get(i),l,blackposn , whiteposn)
                dict_possible_moves_p2.update({i:l})
                l=[]
    l=[dict_possible_moves_p1, dict_possible_moves_p2]
    return l





def find_new_moves(dict):
    blackposn_orig={'k':'e8', 'q':'d8','b1':'c8', 'b2':'f8', 'h1':'b8', 'h2':'g8', 'r1':'a8', 'r2':'h8', 'p1':'a7', 'p2':'b7', 'p3':'c7', 'p4':'d7', 'p5':'e7', 'p6':'f7', 'p7':'g7', 'p8':'h7'}
    whiteposn_orig={'k':'e1', 'q':'d1','b1':'c1', 'b2':'f1', 'h1':'b1', 'h2':'g1', 'r1':'a1', 'r2':'h1', 'p1':'a2', 'p2':'b2', 'p3':'c2', 'p4':'d2', 'p5':'e2', 'p6':'f2', 'p7':'g2', 'p8':'h2'}
