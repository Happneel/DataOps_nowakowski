import gzip
import shutil

def compress_data():
    files_to_compress = ["../data/dataset_clean.csv", "../data/dataset.csv"]

    for file in files_to_compress:
        with open(file, 'rb') as f_in:
            with gzip.open(f"{file}.gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"✅ Fichier compressé : {file}.gz")

if __name__ == "__main__":
    compress_data()
