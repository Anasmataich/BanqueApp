class Compte:
    def __init__(self, numero, solde=0.0):
        self.numero = numero
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"💰 Dépôt de {montant} DH effectué. Nouveau solde : {self.solde} DH")

    def retirer(self, montant):
        if montant > self.solde:
            print("⚠️ Solde insuffisant pour ce retrait !")
        else:
            self.solde -= montant
            print(f"💸 Retrait de {montant} DH effectué. Nouveau solde : {self.solde} DH")

    def __str__(self):
        return f"Compte N°{self.numero} | Solde : {self.solde} DH"
