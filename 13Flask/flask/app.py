from flask import Flask

app = Flask(__name__) 
# it creates an instance of the Flask class, which will be your WSGI application

#WSGI application
if __name__ ==  "__main__": 
    app.run()