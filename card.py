import sqlite3
from seat import Seat

class Card:

    database = "banking.db"

    def __init__(self, type_id, number, cvc, holder) -> None:
        self.type_id = type_id
        self.number = number
        self.cvc = cvc
        self.holder = holder
    
    def validate(self, price):
        """Checks if card if valid and has balance. Subtracts price from balance"""
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM Card WHERE number=? and cvc=?", [self.number, self.cvc])
        data = cursor.fetchall()

        if data:  #Izvrsava se samo ako ima neki novac na racunu, a ako nema bice samo prazna litsa []
            balance = data[0][0]
            if balance >= price:
                cursor.execute("UPDATE Card SET balance=? WHERE number=? and cvc=?", [balance - price, self.number, self.cvc])
                conn.commit()
                conn.close()
                return True