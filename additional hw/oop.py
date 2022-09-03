# Создать класс User со следующими атрибутами:
# имя, фамилия, почтовый адрес, мобильный номер, пароль, животные
# Создать геттер и сеттер для пароля.
# Создайте класс Pet и добавьте к нему следующие атрибуты:
# кличка, порода, год рождения, хозяин (User)
# Добавьте список из Pet как атрибут экземпляра для User.
# Создайте несколько экземпляров класса User, добавьте к юзерам 1-4 домашних животных

class User:
    def __init__(self, name="Foo", lastname="Bar", adress="homeless", mobile=" ", password=" ", animal=0):
        self.name = name
        self.lastname = lastname
        self.adress = adress
        self.mobile = mobile
        self.password = password
        self.animal = animal

    def __str__(self):
        nick_list = ""
        for i in range(0, len(self.animal)):
            nick_list += (self.animal[i].nick) + " "
        return f"Имя : {self.name} \nФамилия : {self.lastname} \nАдрес : {self.adress} \nСотовый : {self.mobile} \nПароль : {self.password} \nПитомец : {nick_list}"

class Pet:
    def __init__(self, nick="Foo", breed="Bar", birthday="0000-00-00", user="homeless"):
        self.nick = nick
        self.poroda = breed
        self.birthday = birthday
        self.user = user

    def __str__(self):
        return f"Имя питомца: {self.nick} \nПорода : {self.poroda} \nДР : {self.birthday} \nХозяин : {self.user}"


denis = User("Denis", "Lazarev", "Perm", "Mobile")
cat = Pet("Bagira", "casual", "2017-01-01", denis.name)
dog = Pet("Brick", "овчарка", "2015-05-05", denis.name)

denis.animal = [cat, dog]

print(f"{cat} \n")
print(f"{dog} \n")
print(denis)
