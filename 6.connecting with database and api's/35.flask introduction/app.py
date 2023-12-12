from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

''' yek form hoga jha pr data ko input krenge , 
ar vo data ko form ke through pass karna chahiye python code ke andr'''

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template("index.html")

@app.route('/math',methods=['POST'])
def math_operator():   # client side se jo v input aayega vo yha capture hoga
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
         

        
        if(ops == 'subtract'):
            r = num1 - num2
            result = 'the difference of '+ str(num1) +' and '+ str(num2) + " is " + str(r)

        if(ops == 'divide'):
            r = num1 / num2
            result = 'the division of '+ str(num1) +' and '+ str(num2) + " is " + str(r)

        if(ops == 'multiply'): 
            r = num1 * num2
            result = 'the multiplication of '+ str(num1) +' and '+ str(num2) + " is " + str(r)

          
        return render_template('results.html', result = result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")