from library import Library


class User(Library):
    def __init__(self, user, password):
        super().__init__()
        self.user = user
        self.password = password

    @staticmethod
    def check_user(user, password):
        # validates user/pass if in system
        pass

