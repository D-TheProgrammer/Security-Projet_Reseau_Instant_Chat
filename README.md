# Security-Projet_Reseau_Instant_Chat
[French] Projet Application de messagerie instantanée en ligne in python  (D'abord ce sera le README en français, puis en anglais)  
[English] Online Instant Messaging Application Project in python (First it will be the French README then the English README After)

<div align="center">
  <img width="500" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/d7baeee2-22f9-4e0c-8cc2-37eb00f8579c">
</div>

### SOMMAIRE / SUMMARY
- Présentation en francais / Presentation in French
- Présentation en anglais / Presentation in English
- Tuoriel dans les deux langues / Tutorial in both languages

## [PRESENTATION EN FRANCAIS]
Le projet que j'ai réalisé consiste en la création d'un système de messagerie en ligne en temps réel, utilisant des sockets pour permettre aux utilisateurs de communiquer facilement en utilisant le modèle client/serveur. Mon programme permet à l'utilisateur de créer un pseudo sur une page, puis de discuter avec une autre personne en insérant son nom pour lui envoyer des
messages. Le système prend en compte la possibilité pour les utilisateurs de quitter à tout moment, ce qui enverra un message à l'autre utilisateur pour le prévenir de leur départ. Si le pseudo du destinataire n'existe pas, aucun message ne sera envoyé.
 
Vous trouverez dans ce projet :  
- un code serveur nommé `serveur_final.py`    
- un code client nommé `client_final.py`  

Les programmes disponibles dans ce dossier de projet fonctionne sans problème !  

Enfin, le code a été commenté en francais (car c'est ma langue natale et que je m'oriente vers des métiers en France) dans le but d'être explicite et facilement compréhensible par tous.  

	

> [!TIP]
> ligne de commande pour lancer le Serveur : 
> ```bash
> python3 serveur_final.py
> ```
> ligne de commande pour lancer un Client : 
> ```bash
> python3 client_final.py
> ```

## [Tutoriel]

#### ÉTAPE 1 : Lancer 1 terminal Serveur et Démarrer 2 terminaux Clients (ou plus). Une fois le serveur lancé, vous accéderez à une page de création de pseudo pour les utilisateurs  
<div align="center">
	<img width="183" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/0b47dcf3-2a44-444b-acbd-4156c71ebeee">
  <img width="184" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/89aafb68-5862-4d29-b0d0-05a3131a0866">
</div>

#### ÉTAPE 2 : Après la création des pseudonymes les pages sont alors personnalisé avec le pseudo choisi en en haut de la page 
<div align="center">
	<img width="397" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/98a2d301-8f35-4c63-8873-efe9d8323219">
</div>

#### ÉTAPE 3 : Dès qu'un deuxième (ou plus) client arrive, un message apparaît pour lui indiquer qu'un nouvel utilisateur s'est connecté 
<div align="center">
  <img width="300" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/52393997-06dd-49ed-8c8d-f96adb3dd6d2">

</div>

#### ÉTAPE 4 : Pour envoyer un message à une personne en particulier, il suffit de saisir le nom de cette personne dans la zone en pointillés nommée "Envoyé A" en haut de l'écran  
<div align="center">
	<img width="407" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/0d9d13aa-a6b9-4337-9121-e066775600b1">
</div>

#### ÉTAPE 5 : Ecrire le message dans la zone disponible en bas de l'écran et appuyez sur “Envoyer” ce bouton changera alors de couleurs    
<div align="center">
	<img width="356" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/d219649b-52b9-4e8b-a9d8-4321af054d28">
</div>

#### ÉTAPE 6 : Pour l'affichage, les messages seront écrits à gauche sur l'écran de l'expéditeur et à droite sur l'écran du destinataire   

<div align="center">
	<img width="414" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/4e1cd0c6-24ef-4340-9955-4cef6e1cc897">
  <img width="414" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/577fc334-d0f0-4c3e-ac97-3a9db4b25d7f">

</div>

#### ÉTAPE 7: Si les messages dépassent en largeur ou que la conversation est longue il est possible faire défiler  

<div align="center">
	<img width="317" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/a4a850c0-033a-4d46-bf6b-76b6f312d569">
  <img width="326" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/acb0f8cb-8f63-423e-966e-d1ad6cbdac8e">
</div>

#### ÉTAPE 8 : Si un client souhaite mettre fin à la conversation il peut envoyer un message "quitter" ou "QUITTER" à un destinataire, ce qui entraînera la fermeture de la page et la fin des sockets   

<div align="center">
	<img width="422" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/b3927aae-1705-42f0-b996-d1a7f0f30837">
</div>
<div align="center">
  <img width="413" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/d07acbd5-9ad2-4c31-bc48-cee23a455829">
</div>


#### ÉTAPE 9 :  La seconde méthode pour quitter consiste à cliquer sur la croix, elle changera de couleur comme le bouton "Envoyer" pour prévenir le client   

<div align="center">
  <img width="409" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/9b85f925-6c7a-46d1-8edf-7e1a72be1ba3">
</div>

#### ÉTAPE 10 :  côté du terminal client,rien ne s'affiche à part les arrivées et les départs   
<div align="center">
 <img width="300" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/5d36adff-cee2-486e-956e-2e4254db7875">
</div>


#### ÉTAPE 11 :  Enfin, il est possible de couper le serveur, ce qui entraînera la fermeture des fenêtres des clients ainsi que de leurs sockets
> [!WARNING]
> il faut faire attention à ne pas fermer le serveur sI des clients sont actifs)


<div align="center">
  <img width="454" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/01eec196-3c0f-4d00-b0e6-0edb74bba17c">

</div>

___

## [ENGLISH PRESENTATION]
The project I have developed consists of creating a real-time online messaging system, using sockets to allow users to communicate easily using the client/server model. My program allows the user to create a username on a page, then chat with another person by entering their name to send messages. The system takes into account the possibility for users to leave at any time, which will send a message to the other user to notify them of their departure. If the recipient's username does not exist, no message will be sent.

In this project, you will find:
- a server code named `serveur_final.py`
- a client code named `client_final.py`

The programs available in this project folder work without any issues!

Finally, the code has been commented in French (as it is my native language and I am pursuing careers in France) in order to be explicit and easily understandable by everyone.

> [!TIP]
> Command line to launch the Server:
> ```bash
> python3 serveur_final.py
> ```
> Command line to launch a Client:
> ```bash
> python3 client_final.py
> ```


## [Tutorial]

#### STEP 1: Launch 1 Server terminal and Start 2 Client terminals (or more). Once the server is launched, you will access a page for users to create a username.
<div align="center">
	<img width="183" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/0b47dcf3-2a44-444b-acbd-4156c71ebeee">
  <img width="184" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/89aafb68-5862-4d29-b0d0-05a3131a0866">
</div>

#### STEP 2: After creating the usernames, the pages are then personalized with the chosen username displayed at the top of the page.
<div align="center">
	<img width="397" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/98a2d301-8f35-4c63-8873-efe9d8323219">
</div>

#### STEP 3: As soon as a second (or more) client arrives, a message appears to notify them that a new user has connected.
<div align="center">
  <img width="300" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/52393997-06dd-49ed-8c8d-f96adb3dd6d2">
</div>


#### STEP 4: To send a message to a specific person, simply enter the name of that person in the dotted area labeled "Envoyé A" at the top of the screen.
<div align="center">
	<img width="407" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/0d9d13aa-a6b9-4337-9121-e066775600b1">
</div>

#### STEP 5: Write the message in the available area at the bottom of the screen and press "Envoyer". This button will then change colors.
<div align="center">
	<img width="356" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/d219649b-52b9-4e8b-a9d8-4321af054d28">
</div>

#### STEP 6: For display, messages will be written on the left side of the sender's screen and on the right side of the recipient's screen.
<div align="center">
	<img width="414" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/4e1cd0c6-24ef-4340-9955-4cef6e1cc897">
  <img width="414" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/577fc334-d0f0-4c3e-ac97-3a9db4b25d7f">

</div>

#### STEP 7: If the messages exceed the width or if the conversation is long, it is possible to scroll.
<div align="center">
	<img width="317" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/a4a850c0-033a-4d46-bf6b-76b6f312d569">
  <img width="326" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/acb0f8cb-8f63-423e-966e-d1ad6cbdac8e">
</div>


#### STEP 8: If a client wishes to end the conversation, they can send a message "quitter" or "QUITTER" to a recipient, which will result in closing the page and ending the sockets.
<div align="center">
	<img width="422" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/b3927aae-1705-42f0-b996-d1a7f0f30837">
</div>
<div align="center">
  <img width="413" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/d07acbd5-9ad2-4c31-bc48-cee23a455829">
</div>

#### STEP 9: The second method to quit is to click on the cross, it will change color like the "Envoyer" button to notify the client.
<div align="center">
  <img width="409" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/9b85f925-6c7a-46d1-8edf-7e1a72be1ba3">
</div>

#### STEP 10: On the client terminal side, nothing is displayed except for arrivals and departures.
<div align="center">
 <img width="300" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/5d36adff-cee2-486e-956e-2e4254db7875">
</div>


#### STEP 11: Finally, it is possible to shut down the server, which will result in closing the client windows as well as their sockets.
> [!WARNING]
> il faut faire attention à ne pas fermer le serveur sI des clients sont actifs)


<div align="center">
  <img width="454" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Reseau_Instant_Chat/assets/151149998/01eec196-3c0f-4d00-b0e6-0edb74bba17c">

</div>
