import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="mysql"
    )
mycursor=db.cursor()

#mycursor.execute("CREATE TABLE hotel (roomnumber int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, peopleamount int NOT NULL)")

def checkin():
    entered_name=input('Enter full name: ')
    while True:
        try:
            amount_int = int(input("Enter amount of people: "))
        except ValueError:
            print("That's not an integer number!")
            continue
        else:
            break
    entered_name_str=str(entered_name)
    mycursor.execute("INSERT INTO hotel (name,peopleamount) VALUES ('{0}', '{1}')".format(entered_name_str, amount_int))
    db.commit()
    print('Customer details have been added!')
    print('\n')

def checkout():
    displaycotumers()
    while True:
        try:
            client_room_number = int(input('Please enter the room number of the client in order to execute the check out: '))
        except ValueError:
            print("That's not an integer number!")
            continue
        else:
            break
    try:
        mycursor.execute(f'DELETE FROM hotel WHERE roomnumber = {client_room_number}')
        db.commit()
        print('Room number {0} is empty!'.format(client_room_number))
        print('\n')
    except:
        print('Unable to delete from data.')

def update():
    displaycotumers()
    while True:
        try:
            client_room_number = int(input('Please enter the room number of the client in order to execute the update: '))
            break
        except ValueError:
            print("That's not an integer number!")
            continue
    while True:
        try:
            result = int(input('Enter either 1 in order to update the name or 2 in order to update people amount. Press any other number for exit: '))
        except ValueError:
            print("That's not an integer number!")
            continue
        if result==1:
            new_name=str(input("Enter the new name: "))
            mycursor.execute("UPDATE hotel SET name='{0}' WHERE roomnumber={1}".format(new_name, client_room_number))
            db.commit()
            print('Your change is saved!')
            print('\n')
            break
        elif result==2:
            try:
                new_amount=int(input("Enter the new people amount: "))
            except ValueError:
                print("This is not an integer number!")
                continue
            mycursor.execute(f"UPDATE hotel SET peopleamount={new_amount} WHERE roomnumber={client_room_number}")
            db.commit()
            print('Your change is saved!')
            print('\n')
            break
        else:
            print('Wrong choice, please try again.')
            break

def resethotel():
    mycursor.execute("DROP TABLE IF EXISTS hotel")
    print("The hotel is now empty!")
    print('\n')

def displaycotumers():
    flag=0
    mycursor.execute("SELECT * FROM hotel")
    print('The hotel details:')
    for x in mycursor:
        flag=1
        print(x)
    if flag==0:
        print('The hotel is empty!')
    print('\n')

if __name__=='__main__':
    print("Welcome to the hotel system.")
    print('Please choose one of the following options:')
    while True:
        print('Enter 1 for check in.\nEnter 2 for check out.\nEnter 3 to update\nEnter 4 to display details.\nEnter 5 to reset the system.\nEnter any other number for exit.')
        try:
            result = int(input("Enter your choice: "))
            if result==1:
                checkin()
            elif result==2:
                checkout()
            elif result==3:
                update()
            elif result==4:
                displaycotumers()
            elif result==5:
                resethotel()
                mycursor.execute("CREATE TABLE hotel (roomnumber int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, peopleamount int NOT NULL)")
            else:
                print('Thank you for using our system!')
                break
        except ValueError:
            print("That's not an integer number!")
