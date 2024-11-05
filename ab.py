from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/<name>')
def home(name):
    return 'hai dear'+''+name

@app.route('/about/<int:num2>')
def about(num2):
    return f' the value of {num2} is {num2+num2}'

@app.route('/contact/<int:age>')
def contact(age):
    if age>18:
        return f'this is same age'
    elif age==18:
        return f'this is not same age'
    else:
        return f'this is contact page'

@app.route('/product')
def product():
    return render_template('index.html')

@app.route('/product/laptop')
def laptop():
    return render_template('abcd.html')

@app.route('/register',methods=['GET'])
def register():
    name=request.args.get('name')
    age=request.args.get('age')
    email=request.args.get('email')
    address=request.args.get('address')
    return render_template('register.html',name=name,age=age,email=email,address=address)

@app.route('/reg',methods=['POST'])   
def reg():
    name=request.form['name']
    age=request.form['age']
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    return render_template('reg.html',name=name,age=age,email=email,username=username,password=password)
    
if __name__=='__main__':
    app.run(debug=True)