from flask import Flask, request, redirect, render_template, session, url_for


app = Flask(__name__, static_folder="Public")
app.secret_key = "secret_keyyyyyyy"

@app.route("/")
def index():

    return render_template("index.html", state = session["state"])

@app.route("/signin", methods=["POST"])
def signin():
    # session["state"] = True
    username = request.form["username"]
    password = request.form["password"]
    if(username =="test" and password =="test"):
        session["state"] =  True
        return redirect("/member")
    elif(username == "" or password ==""):
        session["state"] =  False
        return redirect(url_for("error", log = "empty"))
    else:
        session["state"] =  False
        return redirect(url_for("error", log = "not match"))
    

@app.route("/signout")
def signout():
    session["state"] =  False
    return redirect("/")

@app.route("/member")
def member():
    if(session["state"]):
        return render_template("success.html", session_state = session["state"]) 
    else:
        return redirect("/")

@app.route("/error")
def error():
    log = request.args.get("log")
    if(log == "empty"):
        return render_template("fail.html", message = "帳號或密碼不能為空")
    elif(log == "not match"):
        return render_template("fail.html", message="帳號或密碼錯誤")
    else:
        return "發生未知的錯誤"


@app.route("/square/<number>")
def square(number):
    num = int(number) * int(number)
    return render_template("squared.html", number=num)
app.run(port=3000)

