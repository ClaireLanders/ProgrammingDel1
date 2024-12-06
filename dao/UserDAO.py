from model.models import User


class UserDAO:
    def __init__(self):
        """Initialises the UserDAO with a sample collection of users"""
        self.users = [User(1, 'administrator', 'admin@admin.com', 'password', 'administrator'),
                      User(2, 'customer', 'cust@cust.com', 'password', 'customer')]

    def getuser(self, user_id):
        """
        Retrieves a single user by its ID
        Args: user_id(int): the ID of the user to retrieve.
        Returns: User: the user with the given ID
        """
        for user in self.users:
            if user.user_id == user_id:
                return user

    def getuserbyemail(self, email):
        """
        Retrieves a single user by its email
        Args: email(str): the email of the user to retrieve.
        Returns: User: the user with the given email
        """
        for user in self.users:
            if user.email == email:
                return user

    def getuserbyusername(self, username):
        """
        Retrieves a single user by its username
        Args: email(str): the username of the user to retrieve.
        Returns: User: the user with the given username
        """
        for user in self.users:
            if user.username == username:
                return user

    def get_all_users(self):
        """Retrieves all users registered """

        return self.users


if __name__ == '__main__':
    udao = UserDAO()
    print(udao.getuser(1))
    print(udao.getuser(2))
