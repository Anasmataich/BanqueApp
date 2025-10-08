# banque/banque.py
from .client import Client
from .compte import Compte

class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.clients = {} # استخدام dictionary أفضل للبحث السريع بالـ ID
        self.comptes = {}

    def create_client(self, nom, prenom):
        c = Client(nom, prenom)
        self.clients[c.id] = c
        return c

    def find_client(self, client_id):
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client introuvable")
        return client

    def create_account(self, client_id, solde_initial=0):
        client = self.find_client(client_id)
        acc = Compte(solde_initial)
        client.ajouter_compte(acc)
        self.comptes[acc.id] = acc
        return acc

    def find_account(self, account_id):
        account = self.comptes.get(account_id)
        if not account:
            raise ValueError("Compte introuvable")
        return account

    def deposit(self, account_id, amount):
        # البحث عن الحساب ثم استدعاء دالة الإيداع الخاصة به
        acc = self.find_account(account_id)
        return acc.deposit(amount)

    def withdraw(self, account_id, amount):
        # البحث عن الحساب ثم استدعاء دالة السحب الخاصة به
        acc = self.find_account(account_id)
        return acc.withdraw(amount)

    def transfer(self, from_id, to_id, amount):
        if from_id == to_id:
            raise ValueError("Les comptes source et destination ne peuvent pas être identiques")
            
        acc_from = self.find_account(from_id)
        acc_to = self.find_account(to_id)

        # التحقق من الرصيد قبل أي عملية
        if amount > acc_from.get_balance():
            raise ValueError("Solde insuffisant pour le virement")

        # تتم العملية هنا لأنها تخص حسابين
        acc_from.balance -= amount
        acc_to.balance += amount
        
        # تسجيل معاملتين، واحدة لكل حساب
        t1 = acc_from.add_transaction("Virement sortant", amount, account_to=to_id)
        t2 = acc_to.add_transaction("Virement entrant", amount, account_from=from_id)
        return (t1, t2)

    def account_history(self, account_id):
        # الآن هذه الدالة تعمل بشكل صحيح لأن acc.transactions موجود
        acc = self.find_account(account_id)
        return acc.transactions
        
    def add_interest(self, account_id, rate_percentage):
        # ✨ Partie 8: Implémentation de la fonctionnalité d'intérêts
        acc = self.find_account(account_id)
        interest = acc.get_balance() * (rate_percentage / 100.0)
        acc.balance += interest
        return acc.add_transaction("Ajout d'intérêts", interest)

    def afficher_clients(self):
        print(f"🏦 Liste des clients de la banque {self.nom} :")
        if not self.clients:
            print("Aucun client enregistré.")
            return
        for client_id, client in self.clients.items():
            print(f"- {client.prenom} {client.nom} (id={client_id})")