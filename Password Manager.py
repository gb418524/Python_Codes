Title = input("Enter the platform name / site name : ")
Email = input("What Email you use their : ")
U_name = input("What is your User name there : ")
Password = input("What is the password of this user name : ")

if __name__ == "__main__":
    file = open(Title + ".txt", "a")
    file.write("Plattform:" + Title + "\n")
    file.write("Email Adress:" + Email + "\n")
    file.write("Username:" + U_name + "\n" )
    file.write("Password:" + Password + "\n")
    file.write("\n")
    