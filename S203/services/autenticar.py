class Autenticar:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def realizar_autenticacao(self) -> bool:
        return self.login == "admin" and self.password == "1234"