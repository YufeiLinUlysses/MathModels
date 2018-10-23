from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from MathModel.linearRegression.LR import LR
import os
import pandas as pd
"""
global dest

app = Flask(__name__)
CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/showCSV')
def showCSV():
    df = pd.read_csv('./testData/linearRegression/basicTest.csv')
    return df.to_html()
@app.route('/')
def index():
    return render_template('upload.html')

@app.route("/upload", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT,'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        dest = destination
        print(destination)
        file.save(destination)
    return render_template("complete.html")

@app.route('/lr',methods= ['GET','POST'])"""
def linReg():
    nameOfRel = 'Cigarette_Consumption-CHD_Mortality'
    filePath = "./testData/linearRegression/test1.csv"#Need to read and get the file path from an uploaded file to the server
    lr = LR(filePath)
    lr.calculation()
    lr.draw(nameOfRel)
    return render_template('linearRegression.html')

linReg()
#if __name__ == '__main__':
 #   app.run(debug = True, host = 'localhost')

