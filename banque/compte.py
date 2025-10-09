# banque/compte.py
import uuid
from .transaction import Transaction # استيراد الكلاس الجديد

class Compte:
    #modi_fief
    def __init__(self, balance=0, id=None):
        self.id = id or str(uuid.uuid4())
        self.balance = balance
        self.transactions = [] # قائمة لتخزين المعاملات كما هو مطلوب في الخطة

    def get_balance(self):
        return self.balance

    def add_transaction(self, ttype, amount, account_from=None, account_to=None):
        # إنشاء كائن من كلاس Transaction
        transaction = Transaction(
            ttype=ttype,
            amount=amount,
            account_from=account_from,
            account_to=account_to
        )
        # إضافة المعاملة إلى القائمة الداخلية
        self.transactions.append(transaction)
        return transaction

    def deposit(self, amount):
        """إيداع مبلغ في هذا الحساب"""
        if amount <= 0:
            raise ValueError("Le montant du dépôt doit être positif")
        self.balance += amount
        # إضافة معاملة جديدة من نوع إيداع
        return self.add_transaction("Dépôt", amount)

    def withdraw(self, amount):
        """سحب مبلغ من هذا الحساب"""
        if amount <= 0:
            raise ValueError("Le montant du retrait doit être positif")
        if amount > self.balance:
            raise ValueError("Solde insuffisant")
        self.balance -= amount
        # إضافة معاملة جديدة من نوع سحب
        return self.add_transaction("Retrait", amount)
        
    def __str__(self):
        return f"Compte {self.id} | Solde: {self.balance:.2f} MAD"