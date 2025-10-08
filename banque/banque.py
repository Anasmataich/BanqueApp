from banque.client import Client

class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.clients = []

    def ajouter_client(self, client):
        self.clients.append(client)

    def afficher_clients(self):
        print(f"🏦 Liste des clients de la banque {self.nom} :")
        for client in self.clients:
            print("-", client)
