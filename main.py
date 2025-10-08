from banque.client import Client
from banque.compte import Compte
from banque.banque import Banque

def main():
    # Création de la banque
    banque = Banque("Banque Centrale")

    # Création d'un client
    client1 = Client("Mataich", "Anas")

    # Création de comptes pour ce client
    compte1 = Compte("C001", 1000)
    compte2 = Compte("C002", 2500)

    # Association des comptes au client
    client1.ajouter_compte(compte1)
    client1.ajouter_compte(compte2)

    # Ajout du client à la banque
    banque.ajouter_client(client1)

    # Tests des opérations
    compte1.deposer(500)
    compte1.retirer(300)
    compte2.retirer(3000)  # test insuffisance

    # Affichage des informations
    banque.afficher_clients()
    client1.afficher_comptes()

if __name__ == "__main__":
    main()
