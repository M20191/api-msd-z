from flask import jsonify
from . import spigot

# spigot/version_jar
@spigot.route('/<version_jar>')
def download_spigot(version_jar):
    spigot_download = {
    "1":"https://download.getbukkit.org/spigot/spigot-1.18.2.jar",
    "2": "https://download.getbukkit.org/spigot/spigot-1.18.1.jar",
    "3": "https://download.getbukkit.org/spigot/spigot-1.17.1.jar",
    "4": "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar",
    "5": "https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar",
    "6": "https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar",
    "7": "https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar",
    "8": "https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar",
    }
    url = spigot_download[version_jar]
    url = {"link":url}
    return jsonify(url)