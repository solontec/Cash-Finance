class UserService:
    def register(self, email: str, password: str):
        return{
            "message": "User registred",
            "email": email
        }