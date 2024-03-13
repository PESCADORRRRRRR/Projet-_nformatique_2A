
import os
import requests
import base64
import json

from dotenv import load_dotenv

class Manager:
    """
    Classe pour gérer les requêtes à l'API Spotify et rechercher des informations audio.
    """

    def __init__(self, client_id, client_secret):
        """
        Initialise le gestionnaire avec les informations d'identification Spotify.

        Args:
            client_id (str): ID client Spotify.
            client_secret (str): Secret client Spotify.
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def rechercher_audio_artiste_titre(self, artist_name, song_title):
        """
        Recherche et retourne les informations audio (titre, lien Spotify, extrait audio) d'une piste
        correspondant à l'artiste et au titre spécifiés.

        Args:
            artist_name (str): Nom de l'artiste.
            song_title (str): Titre de la chanson.

        Returns:
            dict: Dictionnaire contenant les informations audio de la piste trouvée.
                {
                    "titre": (str) Titre de la piste,
                    "lien_spotify": (str) Lien Spotify de la piste,
                    "extrait_audio": (str) URL de l'extrait audio de la piste
                }
            None: Si aucune piste n'a été trouvée.
        """

        # Obtenir le jeton d'accès à partir de l'API Spotify
        auth_url = "https://accounts.spotify.com/api/token"
        auth_headers = {
            "Authorization": "Basic "
            + base64.b64encode(
                (self.client_id + ":" + self.client_secret).encode("utf-8")
            ).decode("utf-8")
        }
        auth_data = {"grant_type": "client_credentials"}
        auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
        auth_data = auth_response.json()
        access_token = auth_data["access_token"]

        # Effectuer une requête à l'API Spotify pour rechercher la piste de l'artiste et du titre spécifiés
        url = "https://api.spotify.com/v1/search"
        params = {
            "q": f"artist:{artist_name} track:{song_title}",
            "type": "track",
            "limit": 1,
        }
        headers = {"Authorization": "Bearer " + access_token}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        # Vérifier si une piste a été trouvée
        if (
            "tracks" in data
            and "items" in data["tracks"]
            and len(data["tracks"]["items"]) > 0
        ):
            track = data["tracks"]["items"][0]
            audio_info = {
                "titre": track["name"],
                "lien_spotify": track["external_urls"]["spotify"],
                "extrait_audio": track["preview_url"],
            }
            return audio_info
        else:
            return None


# Chargement des variables d'environnement
load_dotenv()

# Création du gestionnaire avec les informations d'identification
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
manager = Manager(client_id, client_secret)

# Exemple d'utilisation
artist_name = "Tam sir"
song_title = "Coup du marteau"
audio_info = manager.rechercher_audio_artiste_titre(artist_name, song_title)

if audio_info:
    print(f"Titre: {audio_info['titre']}")
    print(f"Lien Spotify: {audio_info['lien_spotify']}")
    print(f"Extrait audio: {audio_info['extrait_audio']}")
else:
    print(f"Aucune piste trouvée pour l'artiste {artist_name} et le titre {song_title}")
