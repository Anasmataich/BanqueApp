from datetime import datetime

class Transaction:
    def __init__(self, type_operation, montant):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type_operation = type_operation
        self.montant = montant

    def __str__(self):
        return f"[{self.date}] {self.type_operation} de {self.montant} DH"
