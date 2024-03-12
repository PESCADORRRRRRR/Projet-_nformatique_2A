import unittest
import subprocess
import requests
import time

class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Démarrer le serveur API
        cls.apiprocess = subprocess.Popen(["python", "main.py"])
        cls.wait_for_api()

    @classmethod
    def tearDownClass(cls):
        # Arrêter le serveur API
        cls.apiprocess.terminate()

    @classmethod
    def wait_for_api(cls):
        # Attendre que le serveur API soit prêt à recevoir des requêtes
        url = "http://localhost:5000/"
        delay = 1
        attempts = 10
        for _ in range(attempts):
            try:
                requests.get(url)
                break
            except requests.ConnectionError:
                time.sleep(delay)
        else:
            raise TimeoutError(f"API didn't start in {delay*attempts} seconds")

    def test_get_user_info(self):
        # Effectuer une requête GET à l'endpoint /user
        response = requests.get("http://localhost:5000/user")
        
        # Vérifier que la requête a réussi (code de statut 200)
        self.assertEqual(response.status_code, 200)
        
        # Vérifier que le résultat est cohérent (par exemple, vérifier certains champs dans la réponse JSON)
        user_info = response.json()
        self.assertIn("display_name", user_info)
        self.assertIn("id", user_info)

if __name__ == "__main__":
    unittest.main()