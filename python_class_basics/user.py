class User:
    def __init__(self, name, email, job_desc, password):  # constructor
        # attributes/properties
        self.name = name
        self.email = email
        self.job_desc = job_desc
        self.password = password

    # methods
    def changePassword(self, newPass):
        self.password = newPass
        print("Password changed\n")

    def changeJobDesc(self, new_desc):
        self.job_desc = new_desc
        print(f"Job description for user {self.name} has been updated\n")

    def getUserInfo(self):
        print(f"Getting information for user...\n")
        print(
            f"Username: {self.name} \nEmail: {self.email}\n{self.name} works as {self.job_desc}\n")
