from flask import Flask, render_template
from sqlalchemy import create_engine
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