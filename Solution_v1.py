"""
mini-playlist v1
AUTHOR: Ahmet TANGAZ

--- V1 TASKS ---
1. Task: `show` komutunu while/for döngüsü kullanarak dosyadan satır satır okuyacak şekilde implemente et.
2. Task: `remove` komutunu, dosyadaki tüm satırları bir listeye alıp, silinecek ID'yi filtreleyerek dosyayı baştan yazacak şekilde geliştir.
3. Task: Tüm komutlardaki hata mesajlarını (Error Handling) SPEC belgesindeki standartlarla birebir uyumlu hale getir.
----------------
"""
import sys
import os

FILE_PATH = ".miniplaylist/playlists.dat"

def init():
    if not os.path.exists(".miniplaylist"):
        os.mkdir(".miniplaylist")
        with open(FILE_PATH, "w") as f:
            pass
        print("Mini-Playlist initialized successfully.")
    else:
        print("Already initialized.")
        sys.exit(1)

def add(song_name, singer, album):
    if not os.path.exists(FILE_PATH):
        print("Not initialized. Run: python minipl.py init")
        sys.exit(1)
    
    with open(FILE_PATH, "r") as f:
        content = f.read()
    ID = content.count("\n") + 1

    with open(FILE_PATH, "a") as f:
        f.write(f"{ID}|{song_name}|{singer}|{album}\n")
    print(f"Song Added Successfully #{song_name}")

def show():
    if not os.path.exists(FILE_PATH):
        print("Not initialized. Run: python minipl.py init")
        sys.exit(1)
        
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
        
    if len(lines) == 0:
        print("List is empty")
        return
        
    for line in lines:
        print(line.strip())

def remove(song_id):
    if not os.path.exists(FILE_PATH):
        print("Not initialized. Run: python minipl.py init")
        sys.exit(1)
        
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
        
    with open(FILE_PATH, "w") as f:
        removed = False
        for line in lines:
            if line.startswith(f"{song_id}|"):
                removed = True
                song_name = line.split("|")[1]
            else:
                f.write(line)
                
    if removed:
        print(f"Song Successfully Removed #{song_name}")
    else:
        print("You don't have song to remove")

def main():
    if len(sys.argv) < 2:
        print("Usage: python minipl.py [init|add|remove|show] [arguments]")
        sys.exit(1)
        
    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add":
        if len(sys.argv) != 5:
            print("Unknown command: add [args]")
            sys.exit(1)
        add(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "show":
        show()
    elif command == "remove":
        if len(sys.argv) != 3:
            print("Unknown command: remove [args]")
            sys.exit(1)
        remove(sys.argv[2])
    else:
        print(f"Unknown command: {command} [args]")
        sys.exit(1)

if __name__ == "__main__":
    main()