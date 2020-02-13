import random
from tkinter import *
#state
class State:
    def __init__(self):
        self.player =[]
        self.frame =[]
#选手对象
class Player:
    def __init__(self,name =''):
        #基本属性，
        self.num = 0
        self.name = name
        self.potential = 0
        self.damage = 0
        self.control = 0
        self.viability = 0
        self.develop = 0
        self.carry = 0
        self.support = 0
        self.state = 'C'#S A B C D E
        self.fans = 0

class Club:
    def __init__(self):
        self.name = '天王俱乐部'
        self.money = IntVar()
        self.money.set(0)
        self.player = []



class Market:
    def __init__(self):
        self.player = []

    def creat(self):
        for i in range(random.randint(5,15)):
            self.player.append(Player())
            self.player[i].num = i
            self.player[i].name = random_name()
            random_power(self.player[i])

#随即中文名
def random_name():
    name =''
    i = random.randint(1,2)
    last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯',
                  '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明',
                  '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    mid_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
               '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
               '乾', '坤', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    first_names =['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
               '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
               '乾', '坤']
    r = random.randint(0,len(last_names)-1)
    name += last_names[r]
    r = random.randint(0,len(mid_names)-1)
    name += mid_names[r]
    r = random.randint(0,len(first_names)-1)
    name += first_names[r]
    return name

def random_power(player):
    player.damage = random.randint(0, 100)
    player.control = random.randint(0, 100)
    player.viability = random.randint(0, 100)
    player.develop = random.randint(0, 100)
    player.carry = random.randint(0, 100)
    player.support = random.randint(0, 100)
    player.fans = random.randint(100, 10000)






