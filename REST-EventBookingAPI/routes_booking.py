from flask import request
from models import Booking, Event, db

def getBookedEventsByUserID(id):
    evenemens = db.session.query(Booking).filter(Booking.userID == id)
    return {'bookings': bookingListToJson(evenemens)}

def addBooking():
    booking = Booking(
        userID = request.json['userID'],
        userEmail = request.json['userEmail'],
        bookedSeats = request.json['bookedSeats'],
        event = Event.query.get_or_404(request.json['eventID'])
    )

    booking.event.remainingSeats -= request.json['bookedSeats']
    
    db.session.add(booking)
    db.session.commit()
    return {'booking': booking.toJSON()}

def deleteBooking(id):
    booking = Booking.query.get_or_404(id)
    booking.event.remainingSeats += booking.bookedSeats
    db.session.delete(booking)
    db.session.commit()
    return {'status': 'succes'}

def bookingListToJson(list):
    output = []
    for booking in list:
        output.append(booking.toJSON())
    return output
