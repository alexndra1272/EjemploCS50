from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


#Conexion a la base de datos
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        origen = request.form.get("origin")
        destino = request.form.get("destination")
        duracion = request.form.get("duration")
        if not origen or not destino or not duracion:
            return "Rellene todos los campos"
        sql = text("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)")
        db.execute(sql,
                {"origin": origen, "destination": destino, "duration": duracion})
        db.commit()
        return redirect("/")
    return render_template("add.html")