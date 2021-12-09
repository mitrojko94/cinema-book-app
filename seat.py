import sqlite3

class Seat:

    database = "cinema.db"

    def __init__(self, seat_id) -> None:
        self.seat_id = seat_id
    
    def price(self):
        """Get the price of a certain seat"""
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("SELECT price FROM Seat WHERE seat_id=?", [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price
        
        

    def is_free(self):
        """Check in the database if a seat is taken or not"""
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("SELECT taken FROM Seat WHERE seat_id=?", [self.seat_id])
        data = cursor.fetchall()[0][0]  

        if data == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if seat is free"""
        if self.is_free():
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            cursor.execute("UPDATE Seat SET taken=? WHERE seat_id=?", [1, self.seat_id])
            conn.commit()
            conn.close()
