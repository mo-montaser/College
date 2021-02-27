"""
3.  Write a class called Password_manager. The class should have a list called old_passwords
    that holds all of the user’s past passwords. The last item of the list is the user’s current pass-
    word. There should be a method called get_password that returns the current password
    and a method called set_password that sets the user’s password. The set_password
    method should only change the password if the attempted password is different from all
    the user’s past passwords. Finally, create a method called is_correct that receives a string
    and returns a boolean True or False depending on whether the string is equal to the current
    password or not.

"""


class Password_manager:
    def __init__(self, old_passwords: list):
        self.old_passwords = old_passwords
        self.current_password = old_passwords[-1]

    def get_password(self):
        return self.current_password

    def set_password(self, new_password):
        if new_password in self.old_passwords:
            print('The password must be different from the past passwords')
        else:
            self.old_passwords.append(new_password)
            self.current_password = self.old_passwords[-1]

    def is_correct(self, password):
        if (password == self.current_password):
            return True
        else:
            return False


# password_list = ['ABCDEF', '123456', 'qwerty']
# p = Password_manager(password_list)
# print(p.current_password)
# print(p.is_correct('qwerty'))
# p.set_password('zxc123')
# print(p.current_password)
