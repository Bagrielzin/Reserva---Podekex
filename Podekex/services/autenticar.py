class Autenticar:
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password

    def realizar_autenticacao(self) -> bool:
        return self.__login == "admin" and self.__password == "abc123"