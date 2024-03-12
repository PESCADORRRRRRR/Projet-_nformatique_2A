from unittest import mock
import datetime
from scraping import WikipediaScraper

@mock.patch.object(WikipediaScraper, "scrape")
def test_rechercher_singles(mock_scrape):
    # Configuration du mock
    mock_scrape.return_value = [
        {
            "titre": "Balance ton quoi",
            "artiste": "Angèle",
            "date": "05/07/2018"
        },
        {
            "titre": "Tout oublier",
            "artiste": "Angèle",
            "date": "22/11/2019"
        }
    ]

    # Fonction pour formater la date
    def formater_date(date):
        try:
            return datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print(f"Erreur de conversion de la date : {date}")
            return None

    # Appel de la méthode à tester
    scraper = WikipediaScraper("https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France")
    singles = scraper.inserer_dans_liste()

    # Vérification des appels au mock
    mock_scrape.assert_called_once()

    # Vérification des arguments passés au mock
    assert mock_scrape.call_args[0][0] == "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

    # Vérification du contenu de la liste des singles
    assert singles == [
        {
            "titre": "Balance ton quoi",
            "artiste": "Angèle",
            "date": "2018-07-05",
            "lien_spotify": None,
            "extrait_audio": None
        },
        {
            "titre": "Tout oublier",
            "artiste": "Angèle",
            "date": "2019-11-22",
            "lien_spotify": None,
            "extrait_audio": None
        }
    ]

