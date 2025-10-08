# banque/transaction.py
import uuid
from datetime import datetime

class Transaction:
    def __init__(self, ttype, amount, account_from=None, account_to=None):
        """
        ttype: نوع المعاملة (e.g., "Dépôt", "Retrait")
        amount: المبلغ
        account_from: الحساب المصدر (لعمليات التحويل)
        account_to: الحساب الهدف (لعمليات التحويل)
        """
        self.id = str(uuid.uuid4())
        self.date = datetime.now()
        self.ttype = ttype
        self.amount = amount
        self.account_from = account_from
        self.account_to = account_to

    def __str__(self):
        # تمثيل المعاملة كنص لسهولة الطباعة
        date_str = self.date.strftime("%Y-%m-%d %H:%M:%S")
        details = f"{date_str} | {self.ttype:<18} | {self.amount:>8.2f} MAD"
        if self.account_from:
            details += f" | from: {self.account_from}"
        if self.account_to:
            details += f" | to: {self.account_to}"
        return details