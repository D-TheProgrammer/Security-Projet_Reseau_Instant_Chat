#_______!!!!!!!!!!!____PARTIE SERVEUR !!!!!!!!!_________________

#_______PROJET SYSTEME ET RESEAUX COMMUNICATION SERVEUR CLIENT_________
#________PROJET FAIT PAR D-TheProgrammer
#_____________________________________________________
 
#Tout le projet est accompagné par de commentaires 
#afin de rendre le code plus compréhensible

from socket import AF_INET, socket, SOCK_STREAM, SHUT_RDWR
from threading import Thread

def envoi():
    #Boucle infini 
    while True:
        #Creation du socket
            
        connexion_client, adresse_client = s.accept()
        
        liste_adresse[connexion_client] = adresse_client  #on stock sa dans une liste
        Thread(target=reception, args=(connexion_client,)).start()


def reception(connexion_client):  #client en argument
    #reccupere le nom
    pseudo = connexion_client.recv(1024)
    pseudo= pseudo.decode("utf8")
    
    #envoi un message quand une personne arrive
    msg = pseudo + " EST ARRIVE !"
    msg=msg.encode("utf8")
    partage(msg)

    liste_clients[connexion_client] = pseudo  #on met le prenom dans la liste

    while True:
        try:
            if not connexion_client._closed:
                msg = connexion_client.recv(1024)  # on recoit
            else:
                break
        except ConnectionResetError: #si quelquun quitte il ny a pas de message
            break

        #si le message est pas QUITTER
        if msg != bytes("{quitter}", "utf8"):
            partage(msg, pseudo + "")
        
        else:   #si la personne part 
            connexion_client.close()
            del liste_clients[connexion_client]
            
            msg_sortie = pseudo + "a quitter !"
            msg_sortie = msg_sortie.encode("utf8")
            partage(msg_sortie)
            break


def partage(msg, prefix=""):  
   #partage du message a tous le monde selon la liste des clients 
    
    for personne in liste_clients:
        try:
            if not personne._closed:
                prefix_encode= prefix.encode("utf8")
                personne.send(prefix_encode + msg)
        except ConnectionResetError:
            pass




HOST = "127.0.0.1"  #Adresse IP du serveur
PORT = 65432  #Le port utilisé par le serveur

liste_clients = {}  #liste clients
liste_adresse = {}  #liste adresse

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3) #specification du nombre maximum de connexions

print("Serveur lancer")
envoi_client = Thread(target=envoi)
envoi_client.start()

while True:
     
    # Attendre une entrée de l'utilisateur
    commande = input("Entrez 'quitter' ou 'QUITTER' pour fermer le serveur: ")
    if commande == "quitter" or  commande == "QUITTER":
        print("Warning Warning THIS IS NOT A TEST HYBRID-RIIIISE fin du serveur")
        for s in liste_clients:
            s.close()
        try:
            s.shutdown(SHUT_RDWR)
            s.close()
        except OSError:
            pass
        break


envoi_client.join()