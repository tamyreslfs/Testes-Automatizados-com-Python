class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists"  # OK

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            return f"User {user} removed successfully"
        else:
            return f"User {user} not found"  # Corrigido
