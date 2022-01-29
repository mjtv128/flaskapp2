from flask import Flask, render_template
import requests
import urllib.request, json

application = Flask(__name__)
    
@application.route("/", methods=['POST', 'GET'])
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@application.route('/random', methods=['GET'])
def random():
    data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    recipe = None
    for movie in dict["drinks"]:

        recipe = {
            "drink": movie["strDrink"],
            "instructions": movie["strInstructions"]
        }    
    return recipe
    
if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=8000)