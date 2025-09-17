class User:
    def __init__(self, id, name, platform):
        self.id = id
        self.name = name
        self.platform = platform

class Transaction:
    def __init__(self, id, amount, user_id, platform):
        self.id = id
        self.amount = amount
        self.user_id = user_id
        self.platform = platform