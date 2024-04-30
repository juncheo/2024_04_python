# dict

person = {
    'name': "김준철",
    'age': 29,
    'town': "인천",
    'coffeeList': ["아메리카노","라떼","민트"],
    'academy':{
        "first":"java",
        "second": "c-langauge",
        "third": "python",
    },
}

print(f"이름: {person["name"]} 동네: {person["town"]} 좋아하는커피:{person["coffeeList"][2]}")
print(f"세번째 수업: {person["academy"]["third"]}")

# 데이터 생성
person["gender"] = "woman"

# 데이터 삭제
del person["town"]
print(person)



print(person.keys()) # key
print(person.values()) # values
print(person.items()) # k- v 모두











