from flask import jsonify
from . import purpur


# /purpur/version
@purpur.route('/<version_jar>')
def download_purpur(version_jar):
    url = f"https://api.purpurmc.org/v2/purpur/{version_jar}/latest/download"      
    url = {"link":url}
    return jsonify(url)

    