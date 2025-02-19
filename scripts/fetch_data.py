import requests
import pandas as pd

def fetch_data():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df_cases = pd.DataFrame.from_dict(data["cases"], orient='index', columns=["New Cases"])
        df_deaths = pd.DataFrame.from_dict(data["deaths"], orient='index', columns=["Deaths"])
        df = df_cases.join(df_deaths)
        df.index = pd.to_datetime(df.index, format="%m/%d/%y", errors='coerce')
        df.to_csv("../data/dataset.csv")
        print("✅ Données récupérées avec succès.")
    else:
        print("❌ Erreur:", response.status_code, response.text)

if __name__ == "__main__":
    fetch_data()
