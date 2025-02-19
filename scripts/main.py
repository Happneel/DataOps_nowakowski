from fetch_data import fetch_data
from transform_data import transform_data
from visualize_data import visualize_data
from compress_data import compress_data
from benchmark import benchmark

def main():
    print("\n🚀 Lancement du pipeline de données...\n")

    print("📥 Étape 1 : Récupération des données...")
    fetch_data()

    print("\n🛠 Étape 2 : Transformation des données...")
    transform_data()

    print("\n📊 Étape 3 : Génération de la visualisation...")
    visualize_data()

    print("\n🗜 Étape 4 : Compression des données...")
    compress_data()

    print("\n⏳ Étape 5 : Exécution du benchmark...")
    benchmark()

    print("\n🎉 Pipeline terminé avec succès !")

if __name__ == "__main__":
    main()
