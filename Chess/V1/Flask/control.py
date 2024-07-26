#ALL Tested
import database_access as database
import chess
piece_values = {
    'wk': '&#9812;',  # White King
    'wq': '&#9813;',  # White Queen
    'wr': '&#9814;',  # White Rook
    'wb': '&#9815;',  # White Bishop
    'wh': '&#9816;',  # White Knight
    'wp': '&#9817;',  # White Pawn
    'bk': '&#9818;',  # Black King
    'bq': '&#9819;',  # Black Queen
    'br': '&#9820;',  # Black Rook
    'bb': '&#9821;',  # Black Bishop
    'bh': '&#9822;',  # Black Knight
    'bp': '&#9823;'   # Black Pawn
}


def render(id, message):
    code=open("templates/index.html", "r").read()
    data=eval(database.getData(id))
    x=[0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, 9):
        for j in range(1, 9):
            posn=x[i]+str(j)
            piece=''
            for key, value in data[0].items():
                if posn == value:
                    piece=key
                    break
            for key, value in data[1].items():
                if posn == value:
                    piece=key
                    break
            if piece=='':
                code=code.replace("{{"+posn+"}}", '')
            else:
                if piece in data[0].keys():
                    code=code.replace("{{"+data[0][piece]+"}}", piece_values['w'+piece[0]])
                if piece in data[1].keys():
                    code=code.replace("{{"+data[1][piece]+"}}", piece_values['b'+piece[0]])
        code=code.replace("{{turn}}", "its "+data[2]+" turn")
        code=code.replace("{{message}}", message)
    return code
                



def control(id, start, end):
    data=eval(database.getData(id))
    if (start in data[0].values()) and (data[2]=='w'):
        None
    elif (start in data[1].values()) and (data[2]=='b'):
        None
    else:
        print("This is not you piece. Try again!!!")
        return render(id, "This is not you piece. Try again!!!")#"This is not you piece. Try again!!!" #handle this case

    if data[2]=='w':
        color='w'
        p1_position_d=data[0]
        p2_position_d=data[1]
    else:
        color='b'
        p1_position_d=data[1]
        p2_position_d=data[0]

    possible_posn=chess.find_moves(start, p1_position_d, p2_position_d, color)

    if len(possible_posn)==0 or not(end in possible_posn) or possible_posn=="NULL":
        print("Invalid Move")
        return render(id, "Invalid Move")#"Invalid Move" #handle this case

    p1_piece=""
    p2_piece=""
    for key, value in p1_position_d.items():
        if start == value:
            p1_piece=key
            break
    for key, value in p2_position_d.items():
        if end == value:
            p2_piece=key
            break
    p1_position_d[p1_piece]=end #this was the mistake now corrected
    if p2_piece!="":
        val = p2_position_d.pop(p2_piece, None) 

    if color=='w':
        newData=str([p1_position_d, p2_position_d, 'b'])
    elif color=='b':
        newData=str([p2_position_d, p1_position_d, 'w'])
    database.modifyData(id, newData)
    return render(id, "")


# id=1234
# start="a2"
# end="a3"
# newCode=control(id, start, end)
# f=open("templates/newCode.html", 'w')
# f.write(newCode)
# f.close()


# print(render(1234))