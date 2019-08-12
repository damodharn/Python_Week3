import json


class Clinic:
    def __init__(self):
        self.lst = {"docs": []}
        self.appmt = {}

    def search_name(self, who, name):  # Searches Doctor / Patient by his/her Name.
        if who == 'dc':
            try:
                with open("doctors.json", "r") as f1:
                    self.lst = json.load(f1)
                    f1.close()
            except FileNotFoundError as e:
                print(e)
            else:
                for i in range(len(self.lst["docs"])):
                    if self.lst["docs"][i]["Name"] == name:
                        print("{:<15} {:<5} {:<12} {:<13}".format("Name", "ID", "Speciality", "Availability"))
                        print("____________________________________________________________________")
                        print("{:<15} {:<5} {:<12} 6-12 {:<7}".format(self.lst["docs"][i]["Name"],
                                                                      self.lst["docs"][i]["ID"],
                                                                      self.lst["docs"][i]["Spcl"],
                                                                      self.lst["docs"][i]["Avail"]))
        elif who == 'pt':
            try:
                with open("patients.json", "r") as f1:
                    self.lst = json.load(f1)
                    f1.close()
            except FileNotFoundError as e:
                print(e)
            else:
                for i in range(len(self.lst["pat"])):
                    if self.lst["pat"][i]["Name"] == name:
                        print("{:<15} {:<5} {:<12}".format("Name", "ID", "Contact No."))
                        print("__________________________________________________")
                        print("{:<15} {:<5} {:<12}".format(self.lst["pat"][i]["Name"]
                                                           , self.lst["pat"][i]["ID"], self.lst["pat"][i]["Mob"]))

    def display(self, who):
        if who == 'dc':
            try:
                with open("doctors.json", "r") as f1:
                    self.lst = json.load(f1)
                    f1.close()
            except FileNotFoundError as e:
                print(e)
            else:
                if len(self.lst["docs"]) > 0:
                    print("{:<15} {:<5} {:<12} {:<13}".format("Name", "ID", "Speciality", "Availability"))
                    print("____________________________________________________________________")
                    for i in range(len(self.lst["docs"])):
                        print("{:<15} {:<5} {:<12} 6-12 {:<7}".format(self.lst["docs"][i]["Name"],
                                                                      self.lst["docs"][i]["ID"],
                                                                      self.lst["docs"][i]["Spcl"],
                                                                      self.lst["docs"][i]["Avail"]))
                else:
                    print("No Doctor in the Clinic.")

        elif who == 'pt':
            try:
                with open("patients.json", "r") as f1:
                    self.lst = json.load(f1)
                    f1.close()
            except FileNotFoundError as e:
                print(e)
            else:
                if len(self.lst["pat"]) > 0:
                    print("{:<15} {:<5} {:<12}".format("Name", "ID", "Contact No."))
                    print("__________________________________________________")
                    for i in range(len(self.lst["pat"])):
                        print("{:<15} {:<5} {:<12}".format(self.lst["pat"][i]["Name"]
                                                           , self.lst["pat"][i]["ID"], self.lst["pat"][i]["Mob"]))
                else:
                    print("No patient in Clinic.")

    def appointment(self):
        try:
            self.lst = {"pat": []}
            with open("patients.json", "r") as f1:
                self.lst = json.load(f1)
                f1.close()
        except FileNotFoundError as e:
            print(e)
        else:
            name_pt = input("Enter Name of Patient.")
            for i in range(len(self.lst["pat"])):
                if self.lst["pat"][i]["Name"] == name_pt:
                    name = input("Enter a Name of doctor to fix Appointment.")
                    try:
                        self.lst = {"docs": []}
                        with open("doctors.json", "r") as f1:
                            self.lst = json.load(f1)
                            f1.close()
                    except FileNotFoundError as e:
                        print(e)
                    else:
                        for j in range(len(self.lst["docs"])):
                            if self.lst['docs'][j]['Name'] == name:
                                if self.lst["docs"][j]["cnt"] < 5:
                                    self.lst["docs"][j]["cnt"] += 1
                                    self.save()
                                    print("Your Appointment is Fixed at {} {}".format(6+self.lst["docs"][j]["cnt"]
                                                                                      , self.lst["docs"][j]["Avail"]))
                        # with open("appointmen.json", "r") as f1:
                        #     self.appmt = json.load(f1)
                        #     f1.close()

    def save(self):  # method to save the data to the json file.
        with open('doctors.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

def main():
    cl = Clinic()
    try:
        i = int(input('Enter ur choice:\n1: To Search Doctor(by Name)\n2: To Search Patient(by Name)'
                      '\n3: To Display all the Doctors in clinic\n4: To Display all the Patients in Clinic'
                      '\n5: To Take Appointment of Doctor.'))
        if i == 1:
            name = input("Enter Doctor's Name: ")
            cl.search_name('dc', name)
        elif i == 2:
            name = input("Enter Patient's Name: ")
            cl.search_name('pt', name)
        elif i == 3:
            cl.display('dc')
        elif i == 4:
            cl.display('pt')
        elif i == 5:
            cl.appointment()
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()