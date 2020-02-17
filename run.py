import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
#    return "<h1>Hello</1><h2> World_3</>" esta es una forma de poner html 
#    pero no es la mas aducuada. En la linea de abajoveremos otra forma
     return render_template("index.html")
     

@app.route('/about')
def about():
    return render_template("about.html", page_title="About", array = [1, 2, 3, "esto es inyectado desde python"])
# En la linea de arriba hemos colocado texto en page_title = "About"
# es diferente a las funcines que estan debajo

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        
        # print("Hello, Is there anybody there? ")  ESTO SE VE EN LA CONSOLA
        # print(request.form)
        flash ("Thanks {}, we have recived your message!".format(request.form["name"]))
        
    return render_template("contact.html")
    
@app.route('/careers')
def careers():
    return render_template("careers.html")    

@app.route('/about2')
def about2():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about2.html", page_title="About_2 json", company=data)
    
@app.route('/about2/<member_name>')
def about2_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj ["url"] == member_name:
                member = obj
                
    return render_template("member.html", member=member)    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)