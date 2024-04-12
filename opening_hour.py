#autore : Adam Sifate
#date : 12.04.2024
#contact : adamsifate@gmail.ch

import datetime
import sys

class Magasin():
    def __init__(self) -> None:
        self.weeks = [["Mon", "08:00", "16:00"], ["Tue", "08:00", "12:00", "14:00", "18:00"], ["Wed", "08:00", "16:00"], ["Thu", "08:00", "12:00","14:00", "18:00"], ["Fri", "08:00", "16:00"], ["Sat", "08:00", "12:00"], ["Sun", "00:00", "00:00"]]

    #param liste1 : liste
    #return liste
    def find_same_schedule(self, liste1):
        liste2 = []
        liste3 = list(self.weeks)
        for days in liste1:
            if liste1[0][1] == days[1] and liste1[0][2] == days[2]:
                liste2.append(days[0])
                time = (days[1],days[2])
                liste3.remove(days)

        return (liste2,time),liste3  

    #param : None
    #return : None
    def schedule(self):
        
        
        same_schedule = self.find_same_schedule(self.weeks)
        other_schedule = same_schedule[1]
        print("Opening time for : ")
        for same in same_schedule[0][0]:
            print(str(same), end=", ")
        print (same_schedule[0][1][0], same_schedule[0][1][1])

        for same in other_schedule:
            print(str(same).replace("'", "").replace("[", "").replace("]", ""))

        return None

    #param : None
    #return : int
    def find_days(self, day):
        for i in range(7):
            try:
                print(self.weeks[i].index(day))
                return i

            except:
                None 

    #param date : datetime
    #return : bool
    def IsOpenOn(self, date):

        day = date.strftime("%a")

        index = self.find_days(day)


        if date.strftime("%H:%M") >= self.weeks[index][1] and date.strftime("%H:%M") <= self.weeks[index][2]:
           return True
        else:
            return False
        
    #param date : date
    #retunr None    
    def NextOpeningDate(self,date):
        while True:
            index =self.find_days(date.strftime("%a"))
            date = date + datetime.timedelta(days=1)
            if self.weeks[index][1] != "00:00":
                print(self.weeks[index][1])
                print ("The next opening is the : " + str(date))
                return None

magasin = Magasin()

arg = sys.argv[1]

match arg :

    case "schedule":
        magasin.schedule()
    
    case "IsOpenOn":
        if magasin.IsOpenOn(datetime.datetime.now()):
            print("Open")
        else:
            print("Close")

    case "NextOpeningDate":
        magasin.NextOpeningDate(datetime.date.today())

    case _ :
        print("Invalid argument")