import uuid

class Client:
    def __init__(self, nom, prenom, id=None):
        """
        nom: اسم العميل
        prenom: لقب العميل
        id: معرف العميل (يمكن توليده تلقائيًا)
        """
        self.id = id or str(uuid.uuid4())  # توليد UUID إذا لم يكن موجود
        self.nom = nom
        self.prenom = prenom
        self.comptes = []  # قائمة الحسابات المرتبطة بالعميل

    # إضافة حساب للعميل
    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    # عرض جميع الحسابات المرتبطة بالعميل
    def afficher_comptes(self):
        if not self.comptes:
            print(f"Le client {self.prenom} {self.nom} n'a aucun compte.")
            return
        print(f"Comptes du client {self.prenom} {self.nom}:")
        for compte in self.comptes:
            print(compte)

    # تمثيل العميل كسلسلة نصية
    def __str__(self):
        return f"{self.prenom} {self.nom} (id={self.id})"
