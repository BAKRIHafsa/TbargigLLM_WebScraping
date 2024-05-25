from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json
import os
from application.hespress import scraping  # Adjust the import based on your project structure

app = Flask(__name__)
CORS(app)

# Define the directory for saving the JSON file
json_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json_files')
os.makedirs(json_directory, exist_ok=True)
json_file_path = os.path.join(json_directory, 'scraping_results.json')

@app.route("/scrape", methods=['GET'])
def scrape():
    # Call your scraping function
    liste = scraping()
    
    # Save the result to a JSON file 
    with open(json_file_path, "w", encoding='utf-8') as json_file:
        json.dump(liste, json_file, ensure_ascii=False, indent=4)
    
    return jsonify({"message": "Scraping completed and data saved to JSON file"})

@app.route("/get_json", methods=['GET'])
def get_json():
    # Serve the JSON file
    return send_file(json_file_path, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
