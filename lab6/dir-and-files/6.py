import string, os
import shutil
if not os.path.exists("chars"):        #если нет директории создает
    os.makedirs("chars")
for letter in string.ascii_uppercase:  #из библеотеки стринг берет заглавные
    with open(letter + ".txt", "w") as f:
        f.writelines("Hello World")


def move_text_files(source_folder, destination_folder):
    # Ensure that both source and destination folders exist
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        print(f"Destination folder '{destination_folder}' does not exist.")
        return

    # Get the list of text files in the source folder
    text_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

    # Move each text file from the source folder to the destination folder
    for letter in string.ascii_uppercase:
        source_file = os.path.join(source_folder, f"{letter}.txt")
        destination_file = os.path.join(destination_folder, f"{letter}.txt")
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Moved '{source_file}' to '{destination_folder}'")
        else:
            print(f"File '{source_file}' does not exist.")

source_folder = r'/Users/bakdaulettursunbaev/Desktop/README/lab6'
destination_folder = r'/Users/bakdaulettursunbaev/Desktop/README/lab6/chars'
move_text_files(source_folder, destination_folder)