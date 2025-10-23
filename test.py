def test_virement():
    bank = Banque("Banque Centrale")
    c1 = bank.create_client("Ali", "Test")
    c2 = bank.create_client("Sara", "Test")
    a1 = bank.create_account(c1.id, 500)
    a2 = bank.create_account(c2.id, 200)
    bank.transfer(a1.id, a2.id, 100)
    assert a1.get_balance() == 400
    assert a2.get_balance() == 300
