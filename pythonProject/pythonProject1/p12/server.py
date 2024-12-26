import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    f=open("rates.csv","r",encoding="utf-8")
    st='<table width="314" border="1">'
    rows = f.readlines()
    for row in rows:
        s = row.split(",")
        if len(s) == 6:
            st = st + "<tr>"
            for t in s:
                st = st + "<td>" + t + "</td>"
            st = st + "</tr>"
    st+='</table>'
    return st
    return "这是网站首页"
app.run(host="0.0.0.0",port="80")