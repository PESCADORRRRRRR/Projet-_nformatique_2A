import os
from dotenv import load_dotenv
from flask import Flask, request

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Chargement des variables d'environnement depuis un fichier .env
load_dotenv()

# Configuration de l'application Flask
app = Flask(__name__)

# Configuration de l'accès à l'API Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-read-playback-state",
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
))

# Définition de l'endpoint racine
@app.route("/")
def index():
    return "Welcome to the Spotify API!"

# Définition d'un endpoint pour obtenir les informations de l'utilisateur
@app.route("/user")
def get_user_info():
    user_info = sp.current_user()
    return user_info

# Définition d'un endpoint pour obtenir les playlists de l'utilisateur
@app.route("/playlists")
def get_user_playlists():
    playlists = sp.current_user_playlists()
    return playlists

# Point d'entrée principal
if __name__ == "__main__":
    app.run(debug=True)