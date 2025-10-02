class Student:
    def __init__(self, pib: str, group: str, dob: str, address: str = ""):
        self.__pib = pib
        self.__group = group
        self.__dob = dob
        self.__address = address

    def get_pib(self):
        return self.__pib

    def set_pib(self, pib):
        self.__pib = pib

    def get_group(self):
        return self.__group

    def set_group(self, group):
        self.__group = group

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
