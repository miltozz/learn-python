"""Module for class definition of a user"""


class User:
    """Represents a user

    Args:
        name (string): The name of the user
        email (string): The email of the user
        job_description (string): The job description of the user
        password (string): User's password.. in plaintext 😎
    """

    def __init__(self, name, email, job_description, password):  # constructor
        # attributes/properties
        self.name = name
        self.email = email
        self.job_description = job_description
        self.password = password

    # methods
    def change_password(self, new_pass):
        """Method to change a user's password

        Args:
            new_pass (string): The new password
        """
        self.password = new_pass
        print("Password changed\n")

    def change_job_description(self, new_description):
        """Method to change a users's job description

        Args:
            new_description (string): The new, job description
        """
        self.job_description = new_description
        print(f"-->Job description for user {self.name} has been updated\n")

    def get_user_info(self):
        """Method to get user information"""
        print("Getting information for user...\n")
        print(
            f"Username: {self.name} \nEmail: {self.email}\n{self.name} works as {self.job_description}\n")  # noqa: E501
