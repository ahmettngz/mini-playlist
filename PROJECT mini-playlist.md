PROJECT: mini-playlist

AUTHOR: Ahmet TANGAZ (251478015)

VERSION: v0

DATE: 2026-03-13



==========================================

 		OVERVIEW

==========================================



mini playlist is a programme for listening to music.

It keeps songs listed and allows user to add, add\_list, new\_ list, show\_list, remove\_list, export, shuffle and replace.



All data is persisted in a directory called .miniplaylist/playlists.dat in the current working directory.



==========================================

 		COMMANDS

==========================================



\------------------init--------------------

Usage: python minipl.py init

Creates a .miniplaylist/ directory and an empty playlists.dat file.

If .miniplaylist/ already exists, print "Already initialized" and exit.



\-------------------add--------------------

Usage: python minipl.py add "Dark Red" "Steve Lacy" "Dark Red"

Appends a new song to playlists.dat

Each song has: Name, Author, Album, ID (auto-increment).

Print "Song Added Successfully #<Name>"



\-----------------new\_list-----------------

Usage: python minipl.py new\_list "List Name"

Creates a new list for song in playlist.dat

Each list has: LName, Songs (auto-increment)

Print "New List Created #<LName>"



\-----------------add\_list-----------------

Usage: python minipl.py add\_list





\----------------remove\_list---------------

Usage: python minipl.py remove\_list



\----------------show\_list-----------------

Usage: python minipl.py show\_list



\------------------replace-----------------

Usage: python minipl.py replace



\------------------export------------------

Usage: python minipl.py export



\------------------shuffle-----------------

Usage: python minipl.py shuffle

