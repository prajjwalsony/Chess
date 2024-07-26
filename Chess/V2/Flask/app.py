#Testing to be done
from flask import Flask,render_template,request, render_template_string
import control

app=Flask(__name__)

@app.route('/')
def home():
    id=1234
    # code=control.render(id)
    return render_template('index.html')

@app.route('/',methods=["POST"])
def Guest():
    id=int(request.form["id"])
    start=request.form['start']
    end=request.form['end']
    newCode=control.control(id, start, end)
    return render_template_string(newCode)
    # f=open("templates/newCode.html", 'w')
    # f.write(newCode)
    # return render_template('newCode.html')

@app.route('/p',methods=["POST"])
def func():
    id=int(request.form["id"])
    posn=request.form["posn"]
    newCode=control.possible_moves_list(id, posn)
    return render_template_string(newCode)

if __name__=='__main__':
    app.run(debug=False)
    