from flask import jsonify, render_template
import requests
from . import paper

# /paper/version/
@paper.route('/<version_jar>')
def download_paper(version_jar):
    # Peticion a la API de paper
    try:
        url = f"https://papermc.io/api/v2/projects/paper/versions/{version_jar}/"
        resp = requests.get(url)
        
        # Build
        build = resp.json()["builds"][-1]
        
        # Version
        url = f"https://papermc.io/api/v2/projects/paper/versions/{version_jar}/builds/{build}"
        resp = requests.get(url)
        version = resp.json()["downloads"]["application"]["name"]
        
        # Download
        url = f"https://papermc.io/api/v2/projects/paper/versions/{version_jar}/builds/{build}/downloads/{version}"
        url = {"link":url}
        return jsonify(url)

    except:
        return render_template('error.html')    
        
"""
version != version_jar
"""