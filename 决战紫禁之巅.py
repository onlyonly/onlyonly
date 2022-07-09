# 决战紫禁之巅
import random
import time


class Role:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        pass

    def tong(self, enemy_people):
        enemy_people.blood -= 10
        print('{}捅了{}一刀'.format(self.name, enemy_people.name))
        pass

    def kan_ren(self, enemy_people):
        enemy_people.blood -= 15
        print('{}砍了{}一刀'.format(self.name, enemy_people.name))
        pass

    def add_blood(self):
        if self.blood >= 100:
            print('{}血量充足，无需补血，补充血量无效...'.format(self.name))
            pass
        elif self.blood + 10 > 100:
            add_v = 100 - self.blood
            self.blood = 100
            print('{}补充了{}血量，血量最多为100'.format(self.name, add_v))
            pass
        else:
            self.blood += 10
            print('{}吃了一颗药丸，增加了10血量'.format(self.name))
            pass

    def __str__(self):
        return '{}的血量还有{}'.format(self.name, self.blood)
        pass

    pass


xmcx = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)

while True:
    random_who = random.randint(1, 2)
    who = 'xmcx'
    enemy = 'ygc'
    if random_who == 1:
        who = 'ygc'
        enemy = 'xmcx'
        pass

    random_action = random.randint(1, 2)
    action = '.tong({})'.format(enemy)
    if random_action == 1:
        action = '.kan_ren({})'.format(enemy)
        pass
    action.format(enemy)

    operation = who + action
    eval(operation)

    random_add_blood = random.randint(1, 2)
    add_blood = 'xmcx.add_blood()'
    if random_add_blood == 1:
        add_blood = 'ygc.add_blood()'
        pass
    eval(add_blood)

    print(xmcx)
    print(ygc)
    if xmcx.blood <= 0 or ygc.blood <= 0:
        break
        pass
    print('===================================================================')
    time.sleep(1)
    pass

failed = xmcx.name if xmcx.blood <= 0 else ygc.name
print('对战结束了...{}输了'.format(failed))