from user import User
from seat import Seat
from card import Card

name = input("Enter your full name: ")
seat_id = input("Preferred seat number: ")
card_type = input("Enter your card type: ")
card_number = input("Enter your card number: ")
card_cvc = input("Enter your card cvc: ")
card_holder = input("Card holder name: ")



the_user = User(name=name)
the_seat = Seat(seat_id=seat_id)
the_card = Card(type_id=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

print(the_user.buy(Seat=the_seat, Card=the_card))