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
        self.name = name
        self.potential = 0
        self.damage = 0
        self.control = 0
        self.viability = 0
        self.farm = 0
        self.carry = 0
        self.support = 0
        self.state = 0 #S A B C D E
        self.fans = 0
        self.site = 0 #上路 中路 下路 游走 辅助
        self.level = 0
        self.active = 0
    def level_cal(self):
        self.level = self.damage + self.control + self.viability + self.farm + self.carry + self.support#待定
    def add_point(self, point):
        self[str(point)] += 1
    def random_power(self):
        self.damage = random.randint(20, 80)
        self.control = random.randint(20, 80)
        self.viability = random.randint(20, 80)
        self.farm = random.randint(20, 80)
        self.carry = random.randint(20, 80)
        self.support = random.randint(20, 80)
        self.fans = random.randint(100, 10000)
class Club:
    def __init__(self):
        self.name = '天王俱乐部'
        self.money = IntVar()
        self.money.set(0)
        self.player = []
        self.cs = 0 #界面选中的

class Character:
    def __init__(self, player,num,sv_flag =0):
        self.num = num
        self.money = 600
        self.hpmax = 500
        self.hp = 500
        self.location = ''
        self.location_target =''
        self.speed = 1.1
        self.damage = 40
        self.through = 0
        self.healps = 2
        self.defence = 0 #a/(x+a)为有效伤害公式a=10时有：x=0，受100%伤害；x=10,受50%伤害
        self.controltime = 1.2
        self.controlcd = 0
        self.name = player.name
        self.site = player.site
        self.d = player.damage + player.state
        self.c = player.control + player.state
        self.v = player.viability + player.state
        self.f = player.farm + player.state
        self.carry = player.carry + player.state
        self.support = player.support + player.state
        self.busy = 0
        self.sv_flag = sv_flag#
        self.tmb_flag = 0
        self.dead_flag = 0
    def cal(self):
        self.damage= 30 + self.money * 0.01 * self.d * 0.01
        self.healps= 3 + self.money * 0.002 * self.v * 0.01
        self.hpmax = 500 +self.money * 0.07 * self.v * 0.01
        self.defence = 8 + self.money *0.003 * self.v * 0.01
        self.through = self.money *0.0007 * self.v * 0.01
        self.controltime = 1.2 + self.money * 0.0003 * self.c * 0.01
        self.controlcd = 20 - self.money * 0.0003 * self.c * 0.01



class Game:
    def __init__(self):
        self.player = []
        self.ch = []
        self.top = ['t1','st2','st3','vt2','vt1']
        self.mid = ['m1', 'sm2', 'sm3', 'vm2', 'vm1','bases','basev']
        self.bot = ['b1', 'sb2', 'sb3', 'vb2', 'vb1']
        self.ts = []
        self.tv = []
        self.ms = []
        self.mv = []
        self.bs = []
        self.bv = []

class Market:
    def __init__(self):
        self.player = []

    def creat(self):
        for i in range(random.randint(7,15)):
            self.player.append(Player(random_name()))
            self.player[i].random_power()

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
    first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
               '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
               '乾', '坤']
    r = random.randint(0,len(last_names)-1)
    name += last_names[r]
    r = random.randint(0,len(mid_names)-1)
    name += mid_names[r]
    r = random.randint(0,len(first_names)-1)
    name += first_names[r]
    return name







