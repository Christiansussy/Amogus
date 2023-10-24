# import folium library
from flask import *
import folium


app = Flask(__name__)


@app.route('/')
def index():
    mapOby = folium.Map(location=[20.658486188041294, 82.65014648437501], zoom_start=7)

    # inject html into the map html
    mapOby.get_root().html.add_child(folium.Element("""
    <div style="position: fixed; 
     top: 50px; left: 70px; width: 150px; height: 70px; 
     background-color:orange; border:2px solid grey;z-index: 900;">
    <h5>Hello World!!!</h5>
    <button>Test Button</button>
    </div>
    """))

    mapOby.save('output.html')

    return mapOby._repr_html_()

if __name__ == '__main__':
    app.run(host='0.0.0.0')