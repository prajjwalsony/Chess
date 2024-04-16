blackposn={'k':'e8', 'q':'d8','b1':'c8', 'b2':'f8', 'h1':'b8', 'h2':'g8', 'r1':'a8', 'r2':'h8', 'p1':'a7', 'p2':'b7', 'p3':'c7', 'p4':'d7', 'p5':'e7', 'p6':'f7', 'p7':'g7', 'p8':'h7'}
whiteposn={'k':'e1', 'q':'d1','b1':'c1', 'b2':'f1', 'h1':'b1', 'h2':'g1', 'r1':'a1', 'r2':'h1', 'p1':'a2', 'p2':'b2', 'p3':'c2', 'p4':'d2', 'p5':'e2', 'p6':'f2', 'p7':'g2', 'p8':'h2'}

positions=[['a1','b1','c1','d1','e1','f1','g1','h1'],['a2','b2','c2','d2','e2','f2','g2','h2'],['a3','b3','c3','d3','e3','f3','g3','h3'],['a4','b4','c4','d4','e4','f4','g4','h4'],['a5','b5','c5','d5','e5','f5','g5','h5'],['a6','b6','c6','d6','e6','f6','g6','h6'],['a7','b7','c7','d7','e7','f7','g7','h7'],['a8','b8','c8','d8','e8','f8','g8','h8']]

def straight(no_of_times,posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now and 'posn' is the current position of piece
    lst=list(p1_position_d)
    p1_position=[]
    p2_position=[]
    for i in lst:
        p1_position.append(p1_position_d.get(i))
        p2_position.append(p2_position_d.get(i))
    
    n=int(no_of_times)
    x=[0,'a','b','c','d','e','f','g','h']
    a=int(x.index(posn[0]))
    b=int(posn[1])
    ap=a
    am=a
    bp=b
    bm=b
    l=list_to_store_value
    for i in range(n):
        bp=bp+1
        try:
            if bp<9:
                pn=x[a]+str(bp)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position :
                break
        except:
            None

    for i in range(n):
        bm=bm-1
        try:
            if bm>0:
                pn=x[a]+str(bm)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position :
                break
        except:
            None
    
    for i in range(n):
        ap=ap+1
        try:
            if ap<9:
                pn=x[ap]+str(b)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position :
                break
        except:
            None

    for i in range(n):
        am=am-1
        try:
            if am>0:
                pn=x[am]+str(b)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position :
                break
        except:
            None

    return l     

def diagonal(no_of_times,posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now
    lst=list(p1_position_d)
    p1_position=[]
    p2_position=[]
    for i in lst:
        p1_position.append(p1_position_d.get(i))
        p2_position.append(p2_position_d.get(i))
    
    n=int(no_of_times)
    x=[0,'a','b','c','d','e','f','g','h']
    a=int(x.index(posn[0]))
    b=int(posn[1])
    am,ap,bm,bp=a,a,b,b
    l=list_to_store_value
    for i in range(n):
        ap,bp=ap+1,bp+1
        try:
            if ap<9 and bp<9:
                pn=x[ap]+str(bp)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position:
                break
        except:
            None

    am,ap,bm,bp=a,a,b,b
    for i in range(n):
        ap,bm=ap+1,bm-1
        try:
            if ap<9 and bm>0:
                pn=x[ap]+str(bm)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position:
                break
        except:
            None

    am,ap,bm,bp=a,a,b,b
    for i in range(n):
        am,bp=am-1,bp+1
        try:
            if am>0 and bp<9:
                pn=x[am]+str(bp)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position:
                break
        except:
            None
    am,ap,bm,bp=a,a,b,b
    for i in range(n):
        am,bm=am-1,bm-1
        try:
            if am>0 and bm>0:
                pn=x[am]+str(bm)
                l.append(pn)
            if pn in p1_position:
                l.pop()
                break
            if pn in p2_position:
                break
        except:
            None
    return l

def horse(posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now
    lst=list(p1_position_d)
    p1_position=[]
    p2_position=[]
    for i in lst:
        p1_position.append(p1_position_d.get(i))
        p2_position.append(p2_position_d.get(i))
    x=['x','a','b','c','d','e','f','g','h']
    a=int(x.index(posn[0]))
    b=int(posn[1])
    lst1=[str(a+2)+str(b+1),str(a+2)+str(b-1),str(a-2)+str(b+1),str(a-2)+str(b-1),str(a+1)+str(b+2),str(a-1)+str(b+2),str(a+1)+str(b-2),str(a-1)+str(b-2)]
    l=list_to_store_value
    l1=[]

    for i in lst1:
        if len(str(i))==2 :
            if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                l1.append(i)
    for i in l1:
        #print(i)
        l.append(x[int(i[0])]+str(int(i[1])))
        
    l=set(l)-set(p1_position)
    
    return list(l)

def pawn(color_of_piece,posn,list_to_store_value, p1_position_d, p2_position_d): # p1_position_d is position of piecies in dictionary form of player who has turn now
    lst=list(p1_position_d)
    p1_position=[]
    p2_position=[]
    for i in lst:
        p1_position.append(p1_position_d.get(i))
        p2_position.append(p2_position_d.get(i))
    x=[0,'a','b','c','d','e','f','g','h']
    a=int(x.index(posn[0]))
    b=int(posn[1])
    l=list_to_store_value
    lm1=[]
    lk1=[]
    lm=[]
    lk=[]
    if b==2 and color_of_piece=='w':
        lm1=[str(a)+str(b+1),str(a)+str(b+2)]
        lk1=[str(a+1)+str(b+1),str(a-1)+str(b+1)]
    elif color_of_piece=='w' :
        lm1=[str(a)+str(b+1)]
        lk1=[str(a+1)+str(b+1),str(a-1)+str(b+1)]

    if color_of_piece=='w':
        for i in lm1:
            if len(str(i))==2 :
                if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                    lm.append(x[int(i[0])]+str(i[1]))

        for i in lk1:
            if len(str(i))==2 :
                if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                    lk.append(x[int(i[0])]+str(i[1]))
        lk=set(lk)
        lm=set(lm)-set(p1_position)-set(p2_position)
        lk=lk.intersection(set(p2_position))
        lx=list(lk.union(lm))
        for i in lx:
            l.append(i)

    if b==7 and color_of_piece=='b':
        lm1=[str(a)+str(b-1),str(a)+str(b-2)]
        lk1=[str(a+1)+str(b-1),str(a-1)+str(b-1)]
    elif color_of_piece=='b' :
        lm1=[str(a)+str(b-1)]
        lk1=[str(a+1)+str(b-1),str(a-1)+str(b-1)]
    if color_of_piece=='b':
        for i in lm1:
            if len(str(i))==2 :
                if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                    lm.append(x[int(i[0])]+str(i[1]))

        for i in lk1:
            if len(str(i))==2 :
                if int(i[0])<9 and int(i[0])>0 and int(i[1])<9 and int(i[1])>0:
                    lk.append(x[int(i[0])]+str(i[1]))
        lk=set(lk)
        lm=set(lm)-set(p1_position)-set(p2_position)
        lk=lk.intersection(set(p2_position))
        lx=list(lk.union(lm))
        for i in lx:
            l.append(i)
    
    return l





dict_possible_moves_p1={}
dict_possible_moves_p2={}
def posibl_moves(p):#p is b/w indicating black or white turn
    l=[]
    if p=='b':
        for i in blackposn:
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

l=posibl_moves('b')
print(l[0])