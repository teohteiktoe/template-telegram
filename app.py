from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return(render_template("index.html"))

@app.route('/telegram', methods=['GET','POST'])
def telegram():
    
    return(render_template("telegram.html"))

if __name__ == '__main__':
    app.run()