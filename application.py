import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(("postgres://yxkzoadjpbhjku:093d2515b7d9cf92c08974375cd9160eb53bb1369e7bfc8663d4900f4e8b263f@ec2-52-202-22-140.compute-1.amazonaws.com:5432/d64l5knk7htk1a"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
