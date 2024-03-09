

#_______!!!!!!!!!!!____PARTIE CLIENT !!!!!!!!!_________________

#_______PROJET SYSTEME ET RESEAUX COMMUNICATION SERVEUR CLIENT_________
#________PROJET FAIT PAR D-TheProgrammer
#_____________________________________________________
 
#Tout le projet est accompagné par de commentaires 
#afin de rendre le code plus compréhensible

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from PIL import ImageTk, Image

#pour envoyer les messages 
def envoi():
    if receveur.get() != "" and message.get() != "":
        server_msg = ":" + receveur.get() + ":" + message.get()
         
        if message.get().lower() == "quitter": #si le message est quitter on appel la fonction quitter
            fermer()
        else :
            zone_tchat.insert(tk.END, nom_expe.get() + " : " + message.get() + "\n") #ecrit le message du client a GAUCHE 

            receveur.set("")  #donc la on reset pour que l'utilisateur puisse ecrire apres
            message.set("") 

            server_msg = server_msg.encode("utf8")
            my_socket.send(server_msg)


#receiption
def reception():
    while True:
        try:
            server_msg = my_socket.recv(1024)
            server_msg = server_msg.decode("utf8") #decode le message
            msg_split = server_msg.split(":") #separation du message du second client 
                                            #car le message est compose de "NOM Envoyeur |  Nom Receveur  | Message"
            
            if len(msg_split) > 1:
                nom_cible = msg_split[1]
                if nom_cible == nom_expe.get():  # Si le nom_cible == pseudo du client de la page on affiche le message
                    #Affiche le message du second client ou du server et retour a la ligne
                    zone_tchat.insert(tk.END, msg_split[0].rjust(50) + " : " + msg_split[2] + "\n") #ce message du second client est affiché a DROITE 

            if len(msg_split) == 1:
                zone_tchat.insert(tk.END, server_msg)
                print(server_msg)

        except (OSError, ConnectionResetError ):  #Capture les erreur pour arreter
            my_socket.close()
            fenetre.quit()
            break


#On masque la page nom_exprditeur (qui permet de regler le pseudo) et on place le reste 
def masquer_nom_expediteur():
    entry_nom_expe.place_forget()
    label_pseudo.place_forget()
    bout_enregistrer_nom_expe.place_forget()

    label_image_chat.place(x=0, y=0)
    titre_tchat.place(x=125, y=25)
    zone_tchat.place(x=137, y=90)

    label_receveur.place(x=305, y=35)
    entry_receveur.place(x=425, y=35)

    entry_message.place(x=141, y=382)
    bar_defile.place(x=600, y=265)
    bar_defileHORI.place(x=580, y=320)
    bar_defile.lift(zone_tchat)
    bar_defileHORI.lift(zone_tchat)


    bout_envoyer.place(x=521, y=377)
    bout_quitter.place(x=535, y=25)


def crea_pseudo():  
    server_msg = nom_expe.get()
    titre_tchat.config(text=f"Chat de {nom_expe.get()}") #Mise a jour du nom de la fenetre chat avec le pseudo choisi
    server_msg = server_msg.encode("utf8")
    my_socket.send(server_msg)
    masquer_nom_expediteur()


def fermer(): #pour fermer avec message ou la croix 
    server_msg = " EST PARTIE !!!!"
    server_msg = server_msg.encode("utf8")
    my_socket.send(server_msg)
    my_socket.close()
    fenetre.quit()


#cReattion de la fenetre et de sa taille 
fenetre = tk.Tk()
fenetre.title("Page Client")
fenetre.configure(bg="#ffffff")
fenetre.geometry("750x450") 
fenetre.resizable(False, False)


#On place la case pour le nom de l'expediteur sur une image
image_background_pseudo = Image.open("fond_pseudo_projetChat.png")
image_tk_pseudo = ImageTk.PhotoImage(image_background_pseudo)
label_pseudo = tk.Label(fenetre, image=image_tk_pseudo)
label_pseudo.place(x=0, y=0)

nom_expe = tk.StringVar() 
entry_nom_expe = tk.Entry(fenetre,width=16,  font=("Arial", 16), bg= "#E2E2E2", borderwidth=0, highlightthickness=0, textvariable=nom_expe)
entry_nom_expe.place(x=470, y=260)

bout_enregistrer_nom_expe = tk.Button(fenetre, text="Enregistrer",  font=("Arial", 16), height=1, width=13, borderwidth=0, highlightthickness=0, relief="groove", bg= "#E2E2E2", fg="black", activeforeground="green",command=crea_pseudo)
bout_enregistrer_nom_expe.place(x=485, y=330)


#On place une case pour envoyer un message a une personne specifiquement 
#Le tout sur un fond
image_background_chat = Image.open("fond_chat_projetChat.png")
image_tk_chat = ImageTk.PhotoImage(image_background_chat)
label_image_chat = tk.Label(fenetre, image=image_tk_chat)


receveur = tk.StringVar()  
label_receveur = tk.Label(fenetre, text="Envoyé A :", font=("Arial", 16), width=10, height=1, bg="#4C5280", fg="#E2E2E2")
entry_receveur = tk.Entry(fenetre, font=("Arial", 16), width=8, bg="#4C5280",fg="#E2E2E2", border=0, textvariable=receveur)


#Zone pour le message et bouton pour envoyer
message = tk.StringVar(fenetre, value='Message :')
entry_message = tk.Entry(fenetre,  font=("Arial", 18), bg="#36415D", width=27, border=0,fg="#E2E2E2",textvariable=message)


#Zone tchat avec barre defillement
bar_defile = tk.Scrollbar(fenetre)
bar_defileHORI = tk.Scrollbar(fenetre)

titre_tchat = tk.Label(fenetre, text=" Tchat: ", font="Ubuntu 14", height=2, bg="#4F6A86", fg="#E2E2E2")
zone_tchat = tk.Listbox(fenetre, height=10, width=38, font=("Arial", 16), bg="#E3E4FF", border=0, borderwidth=0, highlightthickness=0, yscrollcommand=bar_defile.set, xscrollcommand=bar_defileHORI.set)

bar_defile.config(command=zone_tchat.yview , width=30, relief="sunken")
bar_defileHORI.config(command=zone_tchat.xview , width=30, orient="horizontal", relief="sunken")


#bouton pour envoyer le message
bout_envoyer = tk.Button(fenetre, text="Envoyer", font=("Arial", 16), height=1, borderwidth=0, highlightthickness=0,relief="groove", bg="#85A1DB" ,fg="#483659", activebackground="#85A1DB" , activeforeground="green",command=envoi)

#Bouton pour quitter la page en fin de page
bout_quitter = tk.Button(fenetre, text="QUITTER", font=("Arial", 14), height=2, borderwidth=0, highlightthickness=0, bg="#C1272D",fg="#E2E2E2", relief='groove',activebackground="#C1272D" , activeforeground="blue",command=fermer)

#On ferrme en appuyant sur la croix
fenetre.protocol("WM_DELETE_WINDOW", fermer)


HOST = "127.0.0.1"  #Adresse IP du serveur
PORT = 65432  #Le port utilisé par le serveur

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect((HOST, PORT))

recep_client = Thread(target=reception)
recep_client.start()


fenetre.mainloop()