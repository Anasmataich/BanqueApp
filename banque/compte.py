# banque/compte.py
import uuid
from .transaction import Transaction 

class Compte:
    def __init__(self, balance=0, id=None):
        self.id = id or str(uuid.uuid4())
        self.balance = balance
        self.transactions = [] 
        
    def get_balance(self):
        return self.balance

    def add_transaction(self, ttype, amount, account_from=None, account_to=None):

        transaction = Transaction(
            ttype=ttype,
            amount=amount,
            account_from=account_from,
            account_to=account_to
        )

        self.transactions.append(transaction)
        return transaction

    def deposit(self, amount):
        """إيداع مبلغ في هذا الحساب"""
        if amount <= 0:
            raise ValueError("Le montant du dépôt doit être positif")
        self.balance += amount

        return self.add_transaction("Dépôt", amount)

    def withdraw(self, amount):
        """سحب مبلغ من هذا الحساب"""
        if amount <= 0:
            raise ValueError("Le montant du retrait doit être positif")
        if amount > self.balance:
            raise ValueError("Solde insuffisant")
        self.balance -= amount

        return self.add_transaction("Retrait", amount)
    def virement(self ,compte_source ,compte_dest , montant):
        pass
        
    def __str__(self):
        return f"Compte {self.id} | Solde: {self.balance:.2f} MAD"