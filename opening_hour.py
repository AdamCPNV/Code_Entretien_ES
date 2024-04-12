#autore : Adam Sifate
#date : 12.04.2024
#contact : adamsifate@gmail.ch

import datetime

class Magasin():
    def __init__(self) -> None:
        self.weeks = [["Mon", "08:00", "16:00"], ["Tue", "08:00", "12:00", "14:00", "18:00"], ["Wed", "08:00", "16:00"], ["Thu", "08:00", "12:00","14:00", "18:00"], ["Fri", "08:00", "16:00"], ["Sat", "08:00", "12:00"], ["Sun", "00:00", "00:00"]]

    def find_same_schedule(self, liste1):
        liste2 = []
        liste3 = list(self.weeks)
        for days in liste1:
            if liste1[0][1] == days[1] and liste1[0][2] == days[2]:
                liste2.append(days[0])
                time = (days[1],days[2])
                liste3.remove(days)

        return (liste2,time),liste3  

    def schedule(self):
        
        
        same_schedule = self.find_same_schedule(self.weeks)
        other_schedule = same_schedule[1]
        print("Opening time for : ")
        for same in same_schedule[0][0]:
            print(str(same), end=", ")
        print (same_schedule[0][1][0], same_schedule[0][1][1])

        for same in other_schedule:
            print(str(same).replace("'", "").replace("[", "").replace("]", ""))

    def find_days(self, day):
        for i in range(7):
            try:
                print(self.weeks[i].index(day))
                return i

            except:
                None 

    def edit_schedule(self, schedule_changeover_day):

                index = self.find_days(schedule_changeover_day)
                print("entrer l heur de ouverture")
                self.weeks[index][1] = input()
                print("entrer l heur de fermeture")
                self.weeks[index][2] = input()
                print("The schedules you have changed " +self.weeks[index])

    def IsOpenOn(self, date):

        day = date.strftime("%a")

        index = self.find_days(day)


        if date.strftime("%H:%M") >= self.weeks[index][1] and date.strftime("%H:%M") <= self.weeks[index][2]:
           return True
        else:
            return False
        
    def NextOpeningDate(self,date):

        while self.IsOpenOn(date) != True:
            date = date + datetime.timedelta(days=1)

        print("Next opening is the :" + str(date))



magasin = Magasin()
