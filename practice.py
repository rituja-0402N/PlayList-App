items = ["rituja","rajan",{"family_name":"chandrakant"},"hemal","Sujata","Deepika"]

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
'''
for item in nested_list:
    for subitem in item:
        print(subitem)

i = 0

for item in items:
    print(item)

# Nested Dictionary
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}

for k,v in nested_dict.items():
    print("key",k,"value",v)

data = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "hobbies": ["reading", "painting"]
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "hobbies": ["coding", "gaming"]
    }
}

for k,v in data.items():
    for subk,subv in v.items():
        print("MainKey",k)
        print("Secondkey",subk," : ",subv)
        for i in v['hobbies']:
            print("Hobby List : ",i)



job_list = [
    {
    "postings" :
    [
    {"id":123,
    "name" :"Java Developer",
    },
    {"id":345,
    "name" :"System Engineer",
     }
    ],
"id": 122134,
"despriction":"good jobs"
}
]

for jobs in job_list:
    for k,v in jobs.items():
        print(k,": ",v)
        for i in jobs['postings']:
            for subk,subv in i.items():
                 print(subk ,": ", subv, "id found")
print(jobs.get("postings"))



def greet_user(user:str):
    print(f"Welcome user:{user}")
greet_user("Rituja")

def cal(number):
    return number*2
print(cal(4))

def sendMessage(input):
    words = input.split(' ');
    emojis = {
        ":)" : "😊",
        "(:" : "🙃"
    }
    output =""
    for word in words:
        output += emojis.get(word,word) + " "
    return output

try:
    message = input("Enter your message: ")
    print(sendMessage(message))
except ValueError:
    print("Invalid input")
'''
class Byte:
    def __init__(self,value):
        self.value = value
    def get(self):
        print("Byte get")
    def set(self,value):
        print(f"Byte {value} set")

byte = Byte(3)
byte.get()
byte.set(5)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print(f"Hi, I'm  {self.name} ")
john = Person("John",30)
john.talk()