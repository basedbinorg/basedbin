from flask import render_template, request, url_for
from app import app
from tinydb import TinyDB,Query
from faker import Faker


@app.route('/', methods = ["POST","GET"])
def index():
    if request.method == "POST":
        text = request.form["textarea"]
        randomUrl = generateID()
        #createEntry(randomUrl,text)
        return text + str(randomUrl) 
    else:    
        return render_template('index.html')
    
@app.route("/<id>")
def id(id):
    text = entry.query.filter_by(id=id).first()
    return render_template('entry.html', text=text)
    
def createEntry(id,text):
    db = TinyDB('db.json')
    db.insert({'id':id,'text':text})
    
def generateID():
    fake = Faker()

    url=fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
    url = str(url).replace(" ","")

    return url