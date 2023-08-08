import requests
from urllib.parse import urlparse

def get_robots_txt_content(URL_SITO):
    # Ottieni l'URL completo del file robots.txt
    URL_ROBOTS = URL_SITO.rstrip("/") + "/robots.txt"
    
    try:
        response = requests.get(URL_ROBOTS)
        response.raise_for_status()  # Controlla se la richiesta è andata a buon fine
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Errore recon robots.txt per {URL_SITO}: {e}")
        return None

def save_to_file(URL_SITO, content):
    # Estrai il nome del sito dal dominio
    domain = urlparse(URL_SITO).netloc
    filename = f"{domain}_robots.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Il file {filename} è stato creato con successo.")
    except Exception as e:
        print(f"Errore durante il salvataggio del file {filename}: {e}")

def main():
    sites = []
    while True:
        URL_SITO = input("Inserisci URL completo del sito oppure digita 'fine' per terminare: ")
        if URL_SITO.lower() == 'fine':
            break
        sites.append(URL_SITO)

    for site in sites:
        content = get_robots_txt_content(site)
        if content:
            save_to_file(site, content)

if __name__ == "__main__":
    main()