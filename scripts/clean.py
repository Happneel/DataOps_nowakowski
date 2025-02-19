import os
import glob

def clean_project():
    print("\n🧹 Nettoyage du projet en cours...\n")

    # Définition des fichiers et dossiers à supprimer
    files_to_remove = [
        "data/dataset.csv",
        "data/dataset_clean.csv",
        "data/dataset.csv.gz",
        "data/dataset_clean.csv.gz",
        "reports/covid_trend.html",
        "benchmarks/benchmark_results.txt"
    ]

    # Suppression des fichiers listés
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"✅ Supprimé : {file}")
        else:
            print(f"⚠️ Fichier non trouvé : {file}")

    # Suppression des fichiers CSV temporaires
    for file in glob.glob("data/*.csv"):
        os.remove(file)
        print(f"✅ Supprimé : {file}")

    # Suppression des fichiers compressés temporaires
    for file in glob.glob("data/*.gz"):
        os.remove(file)
        print(f"✅ Supprimé : {file}")

    print("\n🎉 Nettoyage terminé avec succès !")

if __name__ == "__main__":
    clean_project()
