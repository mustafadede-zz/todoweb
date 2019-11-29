from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Mustafa/Desktop/Code/todo/todo.db'
db = SQLAlchemy(app)
class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)
@app.route("/")
def index():
    todos = todo.query.all()
    return render_template("index.html", todos = todos)
@app.route("/add",methods=["POST"])
def addTodo():
    title= request.form.get("title")
    newToDo = todo(title=title,complete=False)
    db.session.add(newToDo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/edit/<string:id>")
def edittodo(id):
    todom = todo.query.filter_by(id=id).first()
    todom.complete = not todom.complete
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def deletetodo(id):
    todom = todo.query.filter_by(id=id).first()
    db.session.delete(todom)
    db.session.commit()
    return redirect(url_for("index"))
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
