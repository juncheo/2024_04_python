# class Animal:
#     def __init__(self, name, bread):
#         self.name = name
#         self.bread = bread
#
#     def eat(self):
#         print("냠냠냠")
#
#     def sound(self):
#         pass
#
#
#     def introduce(self):
#         print(f"이름:{self.name},종:{self.bread}")
#
#
#
#
#
# class Dog(Animal):
#     def sound(self):
#         print("멍멍")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("냐옹")
#
#
#
# a = Dog("킹율","이탈리안하우스")
# b = Cat("제니","치즈냥이")
# a.eat()
# a.sound()
# a.introduce()
# b.eat()
# b.sound()
# b.introduce()






# 퀴즈
# 관리자, 편집자, 뷰어 라는 각각 사용자가 존재합니다.
# 모두 접근하기라는 함수를 가지고 있습니다.
# 모두 username이라는 속성도 가지고 있습니다.
# 관리자 - 유저만들기
# 편집자 - 편집하기
# 뷰어 - 조회하기


class Management:
    def __init__(self,username):
        self.username = username

    def access(self):
        pass


class Manager(Management):
    def createUser(self):
        print("유저만들기")

    def access(self):
        print("접근합니다")


class Editor(Management):
    def editing(self):
        print("편집하기")

    def access(self):
        print("접근합니다")


class Viewer(Management):
    def view(self):
        print("조회하기")

    def access(self):
        print("접근합니다")
















