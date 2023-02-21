from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import pandas as pd
app = Flask(__name__)
engine = create_engine("sqlite:///Pokemon_data.sqlite")
print(engine)
#df = pd.read_sql("Select * from Pokemon",engine)
#print(df)
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
#Pokemon_table = Base.classes.pokemon
#session = Session(engine)
#variable = session.query(Pokemon_table).first()
#print(variable)
@app.route("/map_data")
def connection():
    session = Session(bind=engine)
    execute_string = "select * from Pokemon"
    results = engine.execute(execute_string).fetchall()
    session.close()
    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "Point",
                "coordinates": [str(lon), str(lat)],
                },
            "properties" : {
                "pokemon_name": str(name),
                "weight": str(weight),
                "fighting_type": str(type),
                "height": str(height),
                "region": str(region),
                "Main_ability": str(fighting_type),
                "attack": str(attack),
                "defence": str(defence),
                "growth_rate": str(growth_rate),
                "ability": str(ability)
            },
        } for name, type, growth_rate, ability, height, weight, attack, defence, fighting_type,  region, lat, lon, gender in results]
    }
    return (geojson)
@app.route("/Pokemon_data")
def pokemon_growth():
    session = Session(bind=engine)
    execute_string = "select * from Pokemon"
    Pokemon = engine.connect().execute(text(execute_string)).fetchall()
    growth_rate = []
    for row in Pokemon:
        growth_rate.append({
                                    "Pokemon name": row[0],
                                    "Growth rate": row[2],
                                    "Main ability": row[3],
                                    "Attack": row[7],
                                    "Defense": row[8]
                            })
    session.close()
    # Return dictionary as a JSON file for JS processing
    return(jsonify(growth_rate))
@app.route("/a",methods=[])
def landing():
    if request.method=='POST':
        name_pokemon=request.form.get('pokeName')
        result=query(name_pokemon)
        return render_template("",result =result)
    return render_template("index.html")
def query():
    return 0
# @app.route("/submit")
# def submit():
#     print("submit")
if __name__ == '__main__':
    app.run(debug=True)