import pandas as pd

def transform_data():
    df = pd.read_csv("data/dataset.csv", index_col=0, parse_dates=True)
    df.dropna(inplace=True)  # Suppression des valeurs manquantes
    df.to_csv("data/dataset_clean.csv")
    print("✅ Transformation des données terminée.")

if __name__ == "__main__":
    transform_data()
