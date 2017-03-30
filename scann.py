from db import db
#import os

while True:
    bare = input("scannez le code barre : ")
    #os.execl("clear")
    print(db(bare),"€")
