class Taxi:
    def __init__(self,id,currentSpot='A',freeTime=1,earning=0,trips=[],booked=False):
        self.id = id
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.earning = earning
        self.trips = trips
        self.booked = booked

    def setTaxiDetails(self,currentSpot,freeTime,earning,tripDetail,booked):
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.earning = earning
        self.trips.append(tripDetail)
        self.booked = booked
    
    def printDetails(self):
        print(f"Taxi-{self.id} TotalEarnings:{self.earning} currentSpot:{self.currentSpot} status: {self.booked} freeTime: {self.freeTime}")



class Booking:
    taxiList = []
    def createTaxi(self,size):
        self.taxiList = []
        for i in range(size):
            taxi = Taxi(i)
            self.taxiList.append(taxi)
        return self.taxiList

    def getFreeTaxi(self,pickLoc,dropLoc,pickTime):
        for i in self.taxiList:
            if(i.freeTime<pickTime and i.freeTime+(ord(i.currentSpot)-ord(pickLoc))< pickTime):
                return i


    def book(self):
        pickLoc = input("enter Location for pickup:  ")
        if(pickLoc > 'F'):
            print("We cover till location F")
            print("booking canceled")
            return
        dropLoc = input("enter Drop location:        ")
        if(dropLoc > 'F'):
            print("We cover till location F")
            print("booking canceled")
            return
        pickTime = int(input("enter pickup Time      "))
        taxi = self.getFreeTaxi(pickLoc,dropLoc,pickTime)
    # def setTaxiDetails(self,currentSpot,freeTime,earning,tripDetail,booked):
        if(taxi):
            distance = abs((ord(taxi.currentSpot)-ord(dropLoc)))
            tripDetail = {
                pickLoc,
                dropLoc,
                pickTime
            }
            taxi.setTaxiDetails(dropLoc,taxi.freeTime+distance,taxi.earning+(distance*5),tripDetail,True)
    
        




def main():
    booking = Booking() 
    taxiList = booking.createTaxi(5)
    choice = 0
    topic = """
    Taxi booking application 
    enter number to continue
    """
    banner = """
    1. book
    2. check taxi details
    3. quit
    """
    print(topic)
    while not choice ==3:
        print(banner)
        choice = int(input())
        if(choice ==1):
            booking.book()
        elif(choice ==2):
            for taxi in taxiList:
                taxi.printDetails()
main()


