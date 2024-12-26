import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    return flask.render_template("quotes.html")
app.run(debug=True,host="0.0.0.0",port="80")
app.run()