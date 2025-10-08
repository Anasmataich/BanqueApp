from banque.compte import Compte

class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher_comptes(self):
        for compte in self.comptes:
            print(compte)

    def __str__(self):
        return f"Client : {self.prenom} {self.nom}"
