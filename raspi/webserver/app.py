import flask
from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

versionNr =0

@app.route("/new", methods=['POST'])
def newcard():
    data = request.form
    print(data['ueberschrift'])
    print(data['text'])
    print(data['code'])
    global speichern
    speichern = Notiz(data['ueberschrift'], data['text'])
    global versionNr
    versionNr = versionNr + 1
    return index()

@app.route('/version')
def version ():
    global versionNr
    return str(versionNr)


@app.route("/current")
def currentcard():
    return flask.render_template('Truthahn.html', ueberschrift = speichern.ueberschrift, notiz = speichern.notizen)




@dataclass
class Notiz:
    ueberschrift: str
    notizen: str
speichern= Notiz(" " ," " )



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
