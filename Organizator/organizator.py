# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Bem vindo ao Organizator!
# O objetivo deste código é organizar uma pasta em sub-pastas, 
# cada uma contendo diferentes tipos de arquivos.
# Para que funcione, você deve iniciar o código, e mover um
# arquivo para a pasta original.
# 
# Você poderá receber alguns erros, ainda está em fase de desenvolvimento..
# Mas para um teste que provavelmente funcionará, você pode organizar
# Os seus downloads, basta colocar o diretório certo e baixar alguma coisa leve!
#
#
# Sinta-se livre para criar um fork do repositório, 
# e mudar a criação das sub-pastas, os tipos dos arquivos e etc.
#
# Enjoy \o/
#
# - Kallardian
# https://github.com/Kallardian
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#these packages below need to be installed
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pip install watchdog

import os
import time

#folder to organize
original_folder = r'D:\Downloads' 

#sub-folders destination, if you want to create the sub-folders in the same path as the original -> destination_folder = original_folder
destination_folder = r'D:\Downloads' 

#sub-folders and files extensions of each:
Images = [".png", ".jpg", ".gif",".bmp", ".raw", ".jpeg", ".jfif"]
Documents = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pps", ".pptx", ".csv"]
Videos = [".mkv", ".mp4", ".avi", ".mov", ".rmvb"]
Audios = [".mp3", ".wma", ".aac", ".ogg", ".ac3", ".wav", ".m4a"]
PDFs = [".pdf"]
Compressed = [".rar", ".zip", ".7z"]
Applications = [".exe"]

#This class is called every time a file is moved or copied
class Organizator(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(original_folder):
            full_original_path = os.path.join(original_folder, file)
            if os.path.isfile(full_original_path):   
                file_name, file_ext = os.path.splitext(file)
                file_ext = file_ext.lower()
                try:
                    time.sleep(5)
                    if file_ext == ".tmp":
                        pass
                    elif file_ext in (Images):
                        MoveFile(full_original_path, destination_folder, file, "Images")

                    elif file_ext in (Documents):
                        MoveFile(full_original_path, destination_folder, file, "Documents")

                    elif file_ext in (Videos):
                        MoveFile(full_original_path, destination_folder, file, "Videos")

                    elif file_ext in (Audios):
                        MoveFile(full_original_path, destination_folder, file, "Audios")

                    elif file_ext in (PDFs):
                        MoveFile(full_original_path, destination_folder, file, "PDFs")

                    elif file_ext in (Compressed):
                        MoveFile(full_original_path, destination_folder, file, "Compressed")

                    elif file_ext in (Applications):
                        MoveFile(full_original_path, destination_folder, file, "Applications")

                    else:
                        MoveFile(full_original_path, destination_folder, file, "Others") 
                except PermissionError:
                    print("Aconteceu algum erro de permissão, leia o comentário inicial!")
                except FileExistsError:
                    print(f"Já existe um arquivo chamado {file}, desculpe. Poderia renomea-lo?")
                    

#function to create the sub-folders and move the right file to them
def MoveFile(full_original_path, destination_folder, file, type):
    src = os.path.join(destination_folder, type)
    try:
        os.mkdir(src)
        print(f"Pasta {type} foi criada com sucesso!")
    except FileExistsError:
        pass
    src = os.path.join(destination_folder, type, file) 
    os.rename(full_original_path, src)
    print(f"O arquivo {file} foi movido para a pasta {type} com sucesso!")

event_handler = Organizator()
observer = Observer()
observer.schedule(event_handler, original_folder, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
