#2
class UserNotFoundError(Exception):
    def __init__(self, username):
        self.username = username
class UserDatabase:
    def __init__(self):
        self.vocabulary = {"elin": {"name": "Zhenia", "age": 16},
            ".waqz": {"name": "Zahar", "age": 20},
            "8floven8": {"name": "Gleb", "age": 40} }

    def get_user(self, username):
        if username in self.vocabulary:
            return self.vocabulary[username]
        else:
            raise UserNotFoundError(username)

database = UserDatabase()
try:
    user = database.get_user("elin")
    print(f"Користувач {user} є в цій базі даних")
except UserNotFoundError as a:
    print(f"Користувача {a.username} немає в цій базі даних\n"
          f"Спробуйте ще раз")