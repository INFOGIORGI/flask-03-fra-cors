from flask import Flask, render_template

app = Flask(__name__)

dati = (("Mela", "1", "0.50"),("Pane", "2", "1.20"),("Latte", "2", "0.99"),("Pasta", "4", "1.50"),("Uova", "1", "2.30"))


@app.route("/")
def home():
    return render_template("home.html", titolo = "Home")

@app.route("/details")
def details():
   return render_template("details.html", titolo = "Details", dati = dati)

@app.route("/details_s/<nScaffale>")
def details_s(nScaffale):
    lista=[]
    for i in dati:
        if i[1]==nScaffale:
            lista.append(i)

    return render_template("details_s.html", titolo = "Dettagli Scaffali", lista = lista)



app.run(debug=True)
