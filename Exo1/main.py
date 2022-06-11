import json

def ask_id():
    """Ask the ID of the user and check if is only digit"""
    name = input("Enter your ID ")
    try:
        isnum = name.isnumeric()
        if isnum == True:
            return name
        else:
            print("Only number")
            exit(1)
    except:
        print("Only number are accept")
        exit(1)

def ask_password():
    """Ask the password of the user and check if there is more than 6 character"""
    pwd = input("Enter your password ")
    if len(pwd) < 6:
        print("Wrong password")
        exit(1)
    else:
        return pwd

class Main:
    def __init__(self, name, password):
        """Initialize the class, with the important information: like
            - name
            - password
            - major list
            - class following ...
        """
        self.name = int(name)
        self.password = password
        self.db = {}
        self.i = 0
        self.major_list = ["Physical Education", "Computer Science", "Climate Engineering", "Theater & Movie", "Law", "Business Administration", "History"]
        self.class_following = ["Asia_History", "Civilisation", "Human", "Management", "Hiring", "Analysis_Market", "Criminal_Law", "Familly_Law", "International_Law", "Action_Movie", "History_of_Theater", "Practicing", "Unknown_climate", "Weather", "Global_Warming", "Data_Communication", "Software_Programming", "Security", "Gym", "Football", "Kinesitherapy"]

    def store_database(self, path):
        """load the json file in the dictionnary of the class (self.db)"""
        f = open(path)
        self.db = json.load(f)
        f.close()
        self.check_name()
        return

    def check_name(self):
        """
            Check the name of the user exist in the database, and also for the password
            Create while loop to ask the user to know what he or she wants to do
            in the self.parsing(arg) function
        """
        while self.i < (len(self.db["student_2022"])):
            if self.db["student_2022"][self.i]["id"] == self.name and self.db["student_2022"][self.i]["pwd"] == self.password:
                print("Connected")
                self.show_info()
                arg = self.ask_argument()
                self.parsing(arg)
            self.i += 1
        return

    def check_argument(self, argument):
        """Check the response of the user (only digit and only between 1 and 4)"""
        try:
            isnum = argument.isnumeric()
            i = int(argument)
            if isnum == True and i >= 0 and i <= 4:
                return argument
            else:
                exit(1)
        except:
            print("Only number are accept between 0 and 4")
            exit(1)

    def ask_argument(self):
        """Ask argument to the user """
        display_str = """Choose an action to do (use only number): 
                        -0: Modify your information
                        -1: Adding new student * 
                        -2: Deleting student * 
                        -3: Show information all database * 
                        -4: Show information my information
                        *: Only for teacher
                        """
        argument = input(display_str)
        return self.check_argument(argument)

    def parsing(self, arg):
        """With the response of the user, will refer to the different the function
            modification data,
            adding new data,
            deteling data,
            show the information of the database
            show the information of the user
        """
        arg = int(arg)
        if arg == 0:
            self.modif_data()
        if arg == 1:
            self.adding_data()
        if arg == 2:
            self.deleting_data()
        if arg == 3:
            self.show_all()
        if arg == 4:
            self.show_info()
        else:
            exit(1)

    def write_file(self):
        """Write into the file the modif database"""
        a_file = open("database.json", "w")
        json.dump(self.db, a_file)
        a_file.close()
        exit(0)

    def modif_data(self):
        """Ask to the user which thing he or she wants to modify"""
        display_str = """Choose an action to do (use only number): 
                        -0: Firstname and Lastname
                        -1: Major
                        -2: Date of Birth 
                        -3: Following Class 
                        -4: Password
                        """
        print("Which information you want to modify ?")
        response = input(display_str)
        response = int(self.check_argument(response))
        if response == 0:
            update_name = input("\tNew Firstname: ")
            update_lastname = input("\tNew Lastname: ")
            self.db["student_2022"][self.i]["fname"] = update_name
            self.db["student_2022"][self.i]["lname"] = update_lastname
            self.write_file() # Call the function to write the new database
        if response == 1:
            update_major = input("\tNew Major: ")
            if (update_major in self.major_list):
                self.db["student_2022"][self.i]["major"] = update_major
                self.write_file() # Call the function to write the new database
            else:
                print("\nEnter only good major:", self.major_list)
                self.modif_data()
        if response == 2:
            update_birthday = input("\tNew Birthday date (DD-MM-YYYY): ")
            self.db["student_2022"][self.i]["date"] = update_birthday
            self.write_file()
        if response == 3:
            update_following = input("\tNew Following class: ")
            if (update_following in self.class_following):
                self.db["student_2022"][self.i]["following_class"] = update_following
                self.write_file() # Call the function to write the new database
            else:
                print("\nEnter only good following classes possible:", self.class_following)
                self.modif_data()
        if response == 4:
            new_pwd = input("\tNew password: ")
            if len(new_pwd) > 6:
                self.db["student_2022"][self.i]["following_class"] = new_pwd
                self.write_file() # Call the function to write the new database
            else:
                print("Enter password with 6 letter or digit minimum")
                self.modif_data()
        else:
            exit(1)
    
    def adding_data(self):
        """Adding new data (user with all information)"""
        if (self.db["student_2022"][self.i]["rule"] != "teacher"): ## Check if the user is a teacher
            print("You need to be a teacher to add a new student")
            exit(0)
        else:
            print("\nAdding New Student: ")
            id = input("Student ID: ")
            pwd = input("Student Password: ")
            if len(pwd) < 6:
                print("Password to short")
                self.adding_data()
            fname = input("Student Firstname: ")
            lname = input("Student Lastname: ")
            major = input("Student Major: ")
            if major not in self.major_list:
                print("\nEnter only good major:", self.major_list)
                self.adding_data()
            following_class = input("Student Following Class: ")
            following_class = following_class.split(" ")
            for i in following_class:
                if i not in self.class_following:
                    print("\nEnter only good following classes possible:", self.class_following)
                    self.adding_data()
            res_gender = input("Gender (0 for Male, 1 for Female): ")
            isnum = res_gender.isnumeric()
            if isnum == True and int(res_gender) >= 0 and int(res_gender) <= 1:
                if int(res_gender) == 0:
                    gender = "Male"
                if int(res_gender) == 1:
                    gender = "Female"
            else:
                print("\nEnter 0 for Male or 1 for Female")
                self.adding_data()
            date = input("Birthday Date (DD-MM-YYYY): ")
            new_student = {
                "id": id,
                "pwd": pwd,
                "lname": lname,
                "fname": fname,
                "major": major,
                "following_class": following_class,
                "teaching_class": [],
                "gender": gender,
                "date": date,
                "rule": "student"
            }
            self.db["student_2022"].append(new_student)
            self.write_file() # Call the function to write the new database

    def deleting_data(self):
        """Deleting data, asking the id of the student who will me delete from the database"""
        if (self.db["student_2022"][self.i]["rule"] != "teacher"): ## Check if the user is a teacher
            print("You need to be a teacher to add a new student")
            exit(0)
        i = 0
        delete = input("Enter ID you want to delete: ")
        while i < (len(self.db["student_2022"])):
            if self.db["student_2022"][i]["id"] == int(delete):
                self.db["student_2022"].pop(i)
            i+=1
        self.write_file() # Call the function to write the new database

    def show_all(self):
        if (self.db["student_2022"][self.i]["rule"] != "teacher"): ## Check if the user is a teacher
            print("You need to be a teacher to add a new student")
            exit(0)
        print(self.db["student_2022"])

    def show_info(self):
        print("You are connected as", self.db["student_2022"][self.i]["fname"],  self.db["student_2022"][self.i]["lname"])
        
if __name__ == '__main__':
    name = ask_id() #ask the id of the student
    password = ask_password() #ask the password of the user
    Main(name, password).store_database("database.json") #load the database (json file) into a dictionnary