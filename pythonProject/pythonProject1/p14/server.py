import flask
app=flask.Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    currency=flask.request.values.get("currency","美元")
    f=open("rates.txt","r",encoding="utf-8")
    st="<table border='1'>"
    rows=f.readlines()
    i=0
    for row in rows:
        i=i+1
        s = row.split(",")
        if s[0]==currency or i==1:
            st = st + "<tr>"
            for t in s:
                st = st + "<td>" + t + "</td>"
            st = st + "</tr>"
            if i>1:
                break
    st=st+"</table>"
    f.close()
    return st
app.run(debug=True,host='0.0.0.0',port=80)