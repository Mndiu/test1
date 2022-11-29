from flask import Flask

app=Flask(__name__) #initiate an application with name app and application task should be flask

@app.route("/") # initiating root endpoint with flask
def index():
        return"hello from docker"

@app.route("/display") # initiating display endpoint
def display():
    return"display from docker"

if __name__=="__main__":  #checks if program run in the module
    app.run(host="0.0.0.0", port=8015)
