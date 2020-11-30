import yaml


##创建一个类（Animal）
class Animal:
    name: str = ""
    age: int = 5
    colour: str = ""
    gender: str = ""

    def __init__(self, name, age, colour, gender):
        self.name = name
        self.age = age
        self.colour = colour
        self.gender = gender

    def call(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


# 创建子类【猫】
class cat1(Animal):
    hair: str = ""

    def __init__(self, name, age, colour, gender, hair):
        super().__init__(name, age, colour, gender)
        self.hair = hair

    def call_1(self):
        print(f"{self.name}会喵喵叫")

    # 猫会捉老鼠
    def grab(self):
        print("猫会捉老鼠")

    def cat2(self):
        print(f"我是{self.name},颜色是{self.colour},现在{self.age}岁了，我是{self.gender},我是{self.hair}的,捉到了一只老鼠")


# 创建子类【狗】
class dog(Animal):
    hair: str = ""

    def __init__(self, name, age, colour, gender, hair):
        super().__init__(name, age, colour, gender)
        self.hair = hair

    def call_2(self):
        print(f"{self.name}会汪汪叫")

    def home(self):
        print("狗会看家")

    def dog2(self):
        print(f"我是{self.name},颜色是{self.colour},现在{self.age}岁了，我是{self.gender},我是{self.hair}的")


# 调用方法
if __name__ == '__main__':
    # ab = cat1("大黄", 24, "yeallo", "母", "短毛")
    # ab.cat2()
    # ab.call_1()
    # ab.grab()
    # abc = dog("大黄", 24, "yeallo", "母", "长毛")
    # abc.dog2()
    # abc.call_2()
    # abc.home()
    with open("sj.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    name = datas['cat1']['name']
    colour = datas['cat1']['colour']
    age = datas['cat1']['age']
    gender = datas['cat1']['gender']
    hair = datas['cat1']['hair']
    ab = cat1(name, age, colour, gender, hair)
    ab.grab()
    ab.cat2()

    name = datas['dog1']['name']
    colour = datas['dog1']['colour']
    age = datas['dog1']['age']
    gender = datas['dog1']['gender']
    hair = datas['dog1']['hair']
    abc = dog(name, age, colour, gender, hair)
    abc.home()
    abc.dog2()
