from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")     # @app.route ke help se client function ko access kar pa rha h
def hello_world():
    return "<h1>Hello,World!</h1>"

@app.route("/hello_world1")  
def hello_world1():
    return "<h1>Hello,World!1</h1>"  # ham hello_world1 and hello_world2 ko 
                               # access kar pa rha h hello world vale function se
                               # bas address ke last me path add karna h(/hello_world1 and hello_world2)
@app.route("/hello_world2")  
def hello_world2():
    return "<h1>Hello,World!2</h1>"

@app.route("/test")
def test():
  a = 5+6
  return('this is my function to run app {}') .format(a) 


# ab esa function bnayenge, jo ki input v le, client se, jab vo server ko access kare

@app.route("/test2/test2")
def test2():
   data = request.args.get('x')
   return 'this is a data input form my url {}'.format(data)     

if __name__ == "__main__":
     app.run(host="0.0.0.0")

# server client architecture bna rhe h 
'''
   ------------------     ------------------
   | server         |     |    client      |    
   |  .py(code)     |     |                |
   |                |     |                |
   |                |     |                |
   |                |     |                |
   ------------------     ------------------
 # server ke andr code   # client isko access kar
   run karte rhenge.       ke output nikalega.
                           with the help of rest architecture.
                           (http protocol)
'''
# jha pr python me likha hua code , hmara server ban jayega
# server bnayega kon ? , Flask hamara server bnayega
# client iske andr jitna v function likha h usse access kar payega

'''
 upar vale code ka output ham browser me access kar pa rhe h

 * yha pr browser hmara client ho gya ,
 * vs me py language me code hamara server ho gya ,
 * http://192.168.29.174:5000 is url se client kisi me bhi server ko access kar payega.

'''


