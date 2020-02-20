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
        self.age = 16
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
        self.cv = 0 #改名字
class Character:
    def __init__(self, player,num,sv_flag =0):
        self.num = num
        self.money = 600
        self.hpmax = 500
        self.hp = 500
        self.location = ''
        self.location_target =''
        self.speed = 1.2
        self.damage = 40
        self.through = 0
        self.healps = 2
        self.defence = 0 #a/(x+a)为有效伤害公式a=10时有：x=0，受100%伤害；x=10,受50%伤害
        self.controltime = 1.2
        self.controlcd = 0
        self.tpcd = 0#70
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
        self.tmb_flag = 4 # 0，1，2top mid bot
        self.dead_flag = 0
        self.kda = [0,0,0]
    def cal(self):
        self.damage= 40 + self.money * 0.018 * self.d * 0.01
        self.healps= 3 + self.money * 0.0007 * self.v * 0.01
        self.hpmax = 500 +self.money * 0.07 * self.v * 0.01
        self.defence = 5 + self.money *0.0012 * self.v * 0.01
        self.through = self.money *0.0005 * self.d * 0.01
        self.controltime = 1.2 + self.money * 0.0003 * self.c * 0.01
        self.controlcd = 20 - self.money * 0.0003 * self.c * 0.01
class Tower:
    def __init__(self,num):
        self.hpmax = num * 3000 + 3000
        self.hp = num * 3000 + 3000
        self.damage = 30 * num + 90
        self.defence = 9 + 3 * num
class Game:
    def __init__(self):
        self.tower = [[],[]]#wofang
        self.player = []
        self.ch = []#角色
        self.ps = [[],[],[],[],[],[]] #角色分路容器
        self.sc = 0 #选择的角色,查看属性用的
        self.tmb_avi =[[0,1,2],[0,1,2]]
        self.spring = []#泉水玩家坑
        self.gt = [0,0,0]#游戏时间 分钟 秒钟0.1秒
        self.resource = [[300,300,300],[300,300,300],[300,300,300]]#9个元素三路资源
        self.pressure = [[0,0,0],[0,0,0]]

    def tower_creat(self):
        for i in range(3):
            self.tower[0].append([])
            for j in range(3):
                self.tower[0][i].append(Tower(j))
        for i in range(3):
            self.tower[1].append([])
            for j in range(3):
                self.tower[1][i].append(Tower(j))
    def resource_fresh(self):
        self.resource = [[300, 300, 300], [300, 300, 300], [300, 300, 300]]
class Market:
    def __init__(self):
        self.player = []

    def creat(self):
        for i in range(random.randint(7,15)):
            self.player.append(Player(random_name()))
            self.player[i].random_power()
#随机中文名
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
class Hpbar:
    def __init__(self,master,height =18,width =100,hpmax =100,hp =100, bg='pink',fg ='green'):
        self.master =master
        self.height =height
        self.width = width
        self.hpmax = hpmax
        self.hp = hp
        self.bg = bg
        self.fg = fg
        self.canvas = Canvas(master, width=self.width, height = self.height, bg=self.bg)
        length = self.width*hp/hpmax
        self.line = self.canvas.create_rectangle(0,0,length+1,self.height+1, fill=self.fg)
        self.lt = self.canvas.create_text(self.width/2,self.height/2,text = str(int(self.hp))+'/'+str(int(self.hpmax)))

    def grid(self,row =0,column = 0,rowspan =1,columnspan =1):
        self.canvas.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    def grid_forget(self):
        self.canvas.grid_forget()
    def refresh(self,hp,hpmax):
        self.hp =hp
        self.hpmax =hpmax
        length = self.width*hp/hpmax
        self.canvas.coords(self.line,(0,0,length+1,self.height+1))
        self.canvas.delete(self.lt)
        self.lt = self.canvas.create_text(self.width/2,self.height/2,text = str(int(self.hp))+'/'+str(int(self.hpmax)))






