from ciscosparkapi import CiscoSparkAPI

def spark_init():
    api = CiscoSparkAPI()

    # Find all rooms that have 'ciscosparkapi Demo' in their title
    all_rooms = api.rooms.list()
    demo_rooms = [room for room in all_rooms if 'Mr_Xavier' in room.title]

    # Delete all of the demo rooms
    for room in demo_rooms:
        api.rooms.delete(room.id)

    # Create a new demo room
    room_patient = api.rooms.create('Mr_Xavier')
    # Add people to the new demo room
    email_addresses = ["enuta.gabriela@gmail.com", "estadieu.pl@gmail.com"]
    for email in email_addresses:
        api.memberships.create(room_patient.id, personEmail=email)

    # Post a message to the new room, and upload a file
    api.messages.create(room_patient.id, text="Welcome to the room!", files=[""]])
    
    
    return([api, room_patient])

def spark_send(api, room, message):
    api.messages.create(roomId=room.id, toPersonId=None, toPersonEmail=None, text=message, markdown=None, files=None)

