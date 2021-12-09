from seat import Seat
from card import Card
from ticket import Ticket

class User:

    def __init__(self, name) -> None:
        self.name = name
    
    def buy(self, Seat, Card):
        """Buys the ticked if the card if valid"""
        if Seat.is_free():
            if Card.validate(price=Seat.price()):
                Seat.occupy()
                ticket = Ticket(user=self, price=Seat.price(), seat_number=Seat.seat_id)
                ticket.to_pdf()
                return "Purchas successful!"
            else:
                return "There was a problem with your card!"  #Ovo se aktivira ako card.validate iz nekog razloga vrati None, nije lepo ukucan broj, primera radi
        else:
            return "This seat is taken!"
