# 변수[구조체] + 함수 = 클래스
# 명사 + 동사
# 변수들[name, breed,happiness] + 함수들[barking, introducing] =Dog
class Dog:
    def  __init__(self, a, b):
        self.name = a
        self.breed = b
        self.happiness = 0
a = Dog("제니","푸들")
b = Dog("맥스","비글")
c = Dog("킹율","시바")

# 함수들

    def intro(self):
        print(f"{self.name},{self.breed}")


a = Dog("제니","푸들")
b = Dog("맥스","비글")
c = Dog("킹율","시바")
a.intro()
b.intro()
c.intro()
