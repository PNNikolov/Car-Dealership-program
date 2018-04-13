
class Garage:
    def __init__(self, carList):
        self.availableCar = carList
        #self.allCars = carList

    def displayAvailableCar(self):
        #print()
        print("Available Cars")
        print("---------------")
        i=1
        for car in self.availableCar:
            print(i)
            print(car)
            i+=1
    def rendCar (self,requestedNumber):     
        if requestedNumber > len(self.availableCar):
            print("Car with this number does not exist! Please try again. ")
            return
        #print(self.availableCar[requestedNumber])
        #print(len(self.availableCar))
        
        requestedCar = self.availableCar[requestedNumber];
        self.availableCar.remove(self.availableCar[requestedNumber])
        print("You have bought a:\n" + str(requestedCar))

class Car:
    def __init__ (self, available, plate, make, model, Engine_size, fuel_type, Break_Horse_Power, price, colour, year, gearbox, seats, mileage, condition, car_from):
        self.Availabilty = available
        self.Plate = plate
        self.Make = make
        self.Model = model
        self.Engine_size = Engine_size
        self.fuel_type = fuel_type
        self.BHP = Break_Horse_Power
        self.Price = price
        self.Colour= colour       
        self.Year = year
        self.Gearbox = gearbox
        self.seats = seats    
        self.Mileage = mileage
        self.Condition = condition
        self.car_from = car_from
        
    def __str__(self):
        return "Make: " + self.Make + "\nModel: " + self.Model + "\nIs it available: " + self.Availabilty + "\nPlate: " + self.Plate + "\nEngine: " + self.Engine_size + "\nFuel: " + self.fuel_type + "\nBHP: " + self.BHP + "\nPrice: " + self.Price + "\nColour: " + self.Colour + "\nYear: " + self.Year + "\nGearbox: " + self.Gearbox + "\nSeats: " + self.seats + "\nMileage: " + self.Mileage + "\nCondition: " + self.Condition + "\nCar From: " + self.car_from + "\n"
                
class Customer:
    def requestCar (self):
        print("Please enter the numer of the car you want:")
        self.car = input ()
        return self.car
        print()
        
   

car0 = Car ('Yes', 'Y182 UEE', 'Audi ', 'A4', '1.9cc', 'Diesel', '101', '4000 pounds', 'Silver', '2001', 'Manual', '4+1', '89,000', 'Used', 'Dealership')
car1 = Car ('Yes', 'AU55 OYF', 'Citroen ', 'C4', '1.6cc', 'Diesel', '109', '2000 pounds', 'Black', '2005', 'Manual', '4+1', '135,000', 'Used', 'Dealership')
car2 = Car ('Yes', 'RF57 OVK', 'Mercedes ', 'C-Class', '1.8cc', 'Petrol', '158', '5000 pounds', 'Red', '2008', 'Manual', '4+1', '106,000', 'Used', 'Dealership')
car3 = Car ('Yes', 'CY58 CFN', 'Volkswagen', 'Golf-5 R32', '3.2cc', 'Petrol', '247', '13000 pounds ', 'Grey', '2008', 'Automatic', '4+1', '34,000', 'Used', 'Privet - Trader')
car4 = Car ('Yes', 'OV63 OPP', 'Seat', 'Leon', '2.0cc', 'Diesel', '181', '9700 pounds', 'Orange', '2013', 'Automatic', '4+1', '47,200', 'Used', 'Dealership')
car5 = Car ('Yes', 'DN64 CXM', 'Skoda', 'Octavia - Estate', '2.0cc', 'Diesel', '181', '14500 pounds', 'White', '2014', 'Manual', '4+1', '29000', 'Used', 'Prived - Trader')
car6 = Car ('Soon', 'I4 SMR', 'Audi', 'Q7', '3.0cc', 'Diesel', '229', '7000 pounds', 'Dark Grey', '2006', 'Automatic', '5+2', '119000', 'Used', 'Dealership')
car7 = Car ('Yes', '786 AA', 'Lamborghini', 'Hurican-LP610', '5.2cc', 'Petrol', '602', '150000 pounds', 'Gloss White', '2017', 'Automatic', '2', '127', 'new', 'Dealership')
car8 = Car ('Soon', 'GV14 DJX', 'Vauxhall', 'Astra', '2.0cc', 'Diesel', '163', '7200 pounds', 'Red', '2014', 'Automatic', '4+1', '37000', 'Used', 'Privet - Trader')
car9 = Car ('Soon', 'GV14 DJX', 'Vauxhall', 'Astra', '2.0cc', 'Diesel', '163', '7200 pounds', 'Red', '2014', 'Automatic', '4+1', '37000', 'Used', 'Privet - Trader')

garage = Garage([car0,car1,car2,car3,car4,car5,car6,car7,car8,car9])

customer = Customer()
print "Welcome to our website"
loop = 'true'
while (loop == 'true'):
    username = raw_input("Username Please: ")
    password = raw_input("Password Please: ")
    if(username == "John" and password == "123456"):
        print 'Logged in Successfully as ' + username
        loop = 'false'
        loop1 = 'true'
        while(loop1 == 'true'):
            command = raw_input(username + " you can type one of the folowing comands: run, Run, RUN.  ")
            if(command == "run" or command == "Run" or command == "RUN" ):
                break
            else:
                print "'" + command + "' is not valid comand!"
    else:
        print 'Invalid credentials!'

while True:
    print ("Enter 1 to display available car")
    print ("Enter 2 to request for a car")
    print ("Enter 3 to exit")
    userChoice = int(input())

    if userChoice is 1:
        garage.displayAvailableCar()
    elif userChoice is 2:
        requestCar = customer.requestCar()
        garage.rendCar(requestCar - 1)
    elif userChoice is 3:
        quit()


  
