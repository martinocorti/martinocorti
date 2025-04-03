# Importiamo le librerie che ci serviranno per lo sviluppo della task:
import os
import sys
import shutil
import csv

# Cambia la directory di lavoro alla cartella in cui si trova lo script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Definisce i percorsi di origine e le sottocartelle di destinazione:
source_folder = 'files'
dest_folders = {
    'audio': os.path.join(source_folder, 'audio'),
    'doc': os.path.join(source_folder, 'docs'),
    'image': os.path.join(source_folder, 'images')
}
recap_file = os.path.join(source_folder, 'recap.csv')

# Crea le sottocartelle se non esistono
for folder in dest_folders.values():
    os.makedirs(folder, exist_ok=True)

# Estensioni associate ai tipi di file:
file_types = {
    'audio': ['.mp3', '.wav', '.flac'],
    'doc': ['.txt', '.doc', '.docx', '.pdf', '.odt'],
    'image': ['.jpg', '.jpeg', '.png', '.gif']
}

# Controlla se il file recap.csv esiste, altrimenti lo crea con l'intestazione:
if not os.path.exists(recap_file):
    with open(recap_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Type', 'Size (bytes)'])

# Richiedi all'utente il nome del file da spostare
filename = input("Inserisci il nome del file da spostare (inclusa l'estensione): ")

# Stampa i file nella cartella per conferma
try:
    print("Contenuto della cartella 'files':", os.listdir(source_folder))
except FileNotFoundError:
    print(f"Errore: la cartella '{source_folder}' non esiste.")
    sys.exit()

# Verifica se il file esiste
file_path = os.path.join(source_folder, filename)
if not os.path.isfile(file_path):
    print(f"Errore: Il file '{filename}' non esiste nella cartella '{source_folder}'.")
    sys.exit()

# Determina il tipo di file in base all'estensione
file_size = os.path.getsize(file_path)
file_ext = os.path.splitext(filename)[1].lower()
file_type = None

for type_name, extensions in file_types.items():
    if file_ext in extensions:
        file_type = type_name
        break

# Se è un file di tipo riconosciuto, spostalo
if file_type:
    print(f"{filename} type:{file_type} size:{file_size}B")
    shutil.move(file_path, dest_folders[file_type])
    # Scrivi le informazioni nel file recap.csv
    with open(recap_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([filename, file_type, file_size])
else:
    print(f"Errore: Il file '{filename}' non è di un tipo riconosciuto.")

        

