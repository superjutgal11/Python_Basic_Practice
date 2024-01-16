# 클래스 ( 클래스 기본 생성 , __init__ )

# 예를 들어 스타크래프트의 유닛인 마린에 대해 변수를 만들었다.

name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다.".format(name)) # 마린 유닛이 생성되었습니다. {0} 은 단독으로 있을 때는 {} 으로만 써도 된다!!
print("체력은 {0}, 공격력은 {1}입니다.".format(hp,damage)) # 체력은 40, 공격력은 5입니다.

# 탱크 유닛은 일반모드/시즈모드가 있다.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name)) # 탱크 유닛이 생성되었습니다.
print("체력은 {0}, 공격력은 {1}입니다.".format(tank_hp,tank_damage)) # 체력은 150, 공격력은 35입니다.

def attack(name,location,damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 {2} ]".format(name,location,damage))

attack(name,"1 시",damage)
attack(tank_name,"1 시",tank_damage)
# 마린 : 1 시 방향으로 적군을 공격합니다. [ 공격력 5 ]
# 탱크 : 1 시 방향으로 적군을 공격합니다. [ 공격력 35 ]

# 만약 탱크를 한개 더 만들려면 어떻게 해야할까? 우선 변수를 더 만들어 보았다.
tank_name_2 = "탱크"
tank_hp_2 = 150
tank_damage_2 = 35
# 하지만 유닛이 몇십개, 몇백개가 되면 이런식으로 일일히 만들기 쉽자 않다. 그래서 클래스가 필요해진다.
# 클래스는 '붕어빵 틀'이라고 볼 수 있다. 틀은 하나여도 붕어빵은 계속 만들 수 있다. 일반적으로 여러 연관이 있는 변수/함수의 집합이다.

# 지금까지 만든 것을 클래스를 이용해 만들어 보면

class Unit: # class로 클래스 생성
    def __init__(self,name,hp,damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}  ,  공격력 : {1}".format(self.hp,self.damage))
# Unit 이라는 클래스를 만듦.
        
# class 사용 방법
        
마린_1 = Unit("마린",40,5)
마린_2 = Unit("마린",40,5)
탱크_1 = Unit("탱크",150,35)

# 마린 유닛이 생성되었습니다.
# 체력 : 40  ,  공격력 : 5
# 마린 유닛이 생성되었습니다.
# 체력 : 40  ,  공격력 : 5
# 탱크 유닛이 생성되었습니다.
# 체력 : 150  ,  공격력 : 35

# 하나의 클래스로 연관이 있는(이름을 갖고,체력을 갖고,공격력을 갖는) 변수들을 생성했다.

'''
__init__은 파이썬에서 쓰이는 생성자임. 위 마린_1 , 마린_2 , 탱크_1 같은 객체가 만들어질 때, 자동으로 호출된다.
클래스로부터 만들어지는 각각의 개체를 객체라고 하고, 마린_1 , 마린_2 , 탱크_1 는 Unit클래스의 인스턴스라고 표현한다.
객체가 생성될 때에는 self를 제외한 __init__함수에 정의된 인수의 갯수대로 입력이 되어야 한다.
def __init__(self,name,hp,damage): 이 경우 self 빼고 총 3개의 인수를 입력받아야 한다.
즉 위같은 변수에서 객체를 만들 떄, 마린_3 = Unit("마린") 이나 Unit("마린",20) 이런 식으로 인수갯수가 틀리면 사용 불가.
'''