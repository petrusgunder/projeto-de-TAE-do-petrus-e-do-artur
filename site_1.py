from flask import Flask

app = Flask("site de eteset")

@app.route("/teste")
def teste():
    return "vai tomar no cu piranhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

app.run()