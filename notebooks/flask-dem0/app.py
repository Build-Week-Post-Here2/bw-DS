from flask import Flask
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import category_encoders as ce
import requests
import json 
import pickle 
from new_folder.test import add #example importing module from another file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3

print(add(1)) # testing the imported module

# For turning sqlite into pandas db using read_sql
conn = sqlite3.connect("demo_db.db")

#sample model
df = sns.load_dataset("titanic").dropna()
df1 = pd.read_sql("SELECT * FROM stats", conn)
print(df1.head)
print(df.shape)
X = df.drop(columns="fare")
y = df["fare"]
model = LinearRegression()
encoder = ce.OrdinalEncoder()
X_encode = encoder.fit_transform(X)
model.fit(X_encode,y)
score = model.score(X_encode,y)
print(f"The R2 is {score}")

# #pickle save
filename = "demo_model.sav"
print("Model Saving")
pickle.dump(model, open(filename, "wb"))

# #pickle load
model = pickle.load(open("demo_model.sav", "rb"))
print("Model Loading")
pred = model.predict(X_encode[:10])
print(pred)

# #sample API
API_KEY = "abc123"
stock = "TSLA"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={API_KEY}"
response = requests.get(request_url)
print(response)
print(f"Data type before loading json: {type(response.text)}")
values = json.loads(response.text)
print(f"Type after loading json: {type(values)}")
test = values["Time Series (Daily)"]

# Database
db = SQLAlchemy()
migrate = Migrate()

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128))
    name = db.Column(db.String(128))
    open = db.Column(db.Integer)
    close = db.Column(db.Integer)
    volume = db.Column(db.Integer)

# app factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo_db.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def hello():
        print("VISITED HOME ROUTE")

        stats = Stats.query.filter(Stats.open >= 500).all() #gathering filtered rows
        print(stats)
        open_ls = []
        print(f"{dir(stats[0])}") # looking inside the object
        for _ in stats:
            print(_.open) # choosing our desired attribute (open column)
            open_ls.append(_.open) #appending to a list

        return f"{open_ls}" # displaying on the home screen
    
    @app.route("/refresh")
    def refresh():
        
        db.drop_all()
        db.create_all()

        for x in values['Time Series (Daily)']:
            db_stats = Stats()
            db_stats.date = x
            db_stats.name = stock
            db_stats.open = values['Time Series (Daily)'][x]["1. open"]
            db_stats.close = values['Time Series (Daily)'][x]["4. close"]
            db_stats.volume = values['Time Series (Daily)'][x]["5. volume"]
            db.session.add(db_stats)
        db.session.commit()
        
        return f"Data Refreshed!"

    @app.route("/pred")
    def prediction():
        return f"{pred}"
   

    @app.route("/score")
    def return_score():
        return f"The R2 is {score}"

    return app
