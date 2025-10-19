# main.py
from banque.banque import Banque

def print_menu():
    print("\n=== BANQUE APP ===")
    print("1. Créer client")
    print("2. Créer compte pour client")
    print("3. Dépôt")
    print("4. Retrait")
    print("5. Virement")
    print("6. Consulter solde")
    print("7. Historique des transactions")
    print("8. Ajouter des intérêts (feature)") # ✨ Nouveau
    print("9. Quitter") # ✨ Changé

def main():
    bank = Banque("Banque Centrale")
    while True:
        print_menu()
        choice = input("Choix: ").strip()
        try:
            if choice == "1":
                nom = input("Nom du client: ").strip()
                prenom = input("Prénom du client: ").strip()
                c = bank.create_client(nom, prenom)
                print(f"✅ Client créé: {c.prenom} {c.nom} (id={c.id})")

            elif choice == "2":
                bank.afficher_clients()
                cid = input("ID client: ").strip()
                init = float(input("Solde initial (ex: 0): ") or 0)
                acc = bank.create_account(cid, init)
                print(f"✅ Compte créé: id={acc.id}, solde={acc.get_balance():.2f} MAD")

            elif choice == "3":
                aid = input("ID compte: ").strip()
                amount = float(input("Montant à déposer: "))
                t = bank.deposit(aid, amount)
                print("✅ Dépôt effectué. Reçu:", t)

            elif choice == "4":
                aid = input("ID compte: ").strip()
                amount = float(input("Montant à retirer: "))
                t = bank.withdraw(aid, amount)
                print("✅ Retrait effectué. Reçu:", t)

            elif choice == "5":
                a_from = input("Compte source ID: ").strip()
                a_to = input("Compte destination ID: ").strip()
                amount = float(input("Montant du virement: "))
                t1, t2 = bank.transfer(a_from, a_to, amount)
                print(f"✅ Virement de {amount:.2f} MAD effectué de {a_from} vers {a_to}.")

            elif choice == "6":
                aid = input("ID compte: ").strip()
                acc = bank.find_account(aid)
                print(f"💰 Solde du compte {aid}: {acc.get_balance():.2f} MAD")

            elif choice == "7":
                aid = input("ID compte: ").strip()
                hist = bank.account_history(aid)
                print(f"\n--- Historique du compte {aid} ---")
                if not hist:
                    print("Aucune transaction")
                else:
                    for tr in hist:
                        print(tr) 
                print("---------------------------------")
            
            elif choice == "8": 
                aid = input("ID compte: ").strip()
                rate = float(input("Taux d'intérêt en % (ex: 2.5): ") or 2.5)
                t = bank.add_interest(aid, rate)
                print(f"✅ Intérêts ajoutés. Reçu:", t)
                
            elif choice == "9":
                print("Au revoir 👋")
                break

            else:
                print("❌ Choix invalide")

        except Exception as e:
            print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()