"""
mini-playlist v0
AUTHOR: Ahmet TANGAZ
Kapsam: Elimden gelen tüm seyleri basit halde yazacagim.
Sinirlamalar: Dongu ve listekullanilmadi.
"""

import sys
import os


def init():
    # .miniplaylist adında bir klasör oluşturur ve içine playlists.dat adında boş bir dosya oluşturur.
    if not os.path.exists(".miniplaylist"):
        os.mkdir(".miniplaylist")
        f=open(".miniplaylist/playlists.dat", "w")
        f.close()
        print("Mini-Playlist initialized successfully.")
        return
    else:
        print("Already initialized.")
        return

def add(song_name, singer, album):
    # .miniplaylist/playlists.dat dosyasına şarkı bilgilerini ekler.
    if not os.path.exists(".miniplaylist/playlists.dat"):
        print("Not initialized. Run: python minipl.py init")
        return
    
    #Dongu kullanmadiğim icin alternatif bir yontemle sarkilarin ID'sini belirliyorum.
    with open(".miniplaylist/playlists.dat", "r") as f:
        content = f.read()
    ID = content.count("\n") + 1

    with open(".miniplaylist/playlists.dat", "a") as f:
        f.write(f"{ID}|{song_name}|{singer}|{album}\n")
    print (f"Song Added Successfully {song_name}")
    return

def remove():
    print("Remove function is not implemented yet.")
    return
def show():
    print("Show function is not implemented yet.")
    return

if len(sys.argv) < 2:
    print("Usage: python minipl.py [init|add|remove|show] [arguments]")
    sys.exit(1)
command = sys.argv[1]

if command == "init":
        init()
        
elif command == "add":
    if len(sys.argv) != 5:
        print("Usage: python minipl.py add [song_name] [singer] [album]")
        sys.exit(1)
    song_name = sys.argv[2]
    singer = sys.argv[3]
    album = sys.argv[4]
    add(song_name, singer, album)
elif command == "remove":
    remove()
elif command == "show":
    show()
else:
    print("Unknown command. Use: init, add, remove, show")
    sys.exit(1)
