from tkinter import *
from support import *
from tkinter import ttk
import time
#开头
win =Tk()
win.geometry('600x600')
win.title('这不是LOL')
club = Club()#初始化俱乐部
state = State()
game = Game()
market = Market()
market.creat()
#初始化各个界面
frame = []
frame_root =Frame(win)
frame_root.grid()
frame_mkt =Frame(win)
frame_club =Frame(win)
frame_game =Frame(win)
frame = [frame_root, frame_mkt, frame_club, frame_game]
lr1 = Label(frame_root, text = "资金：").grid(row = 0, column = 0)
lr2 = Label(frame_root, textvariable = club.money).grid(row = 0, column = 1)
#战队赞助
def donate():
    club.money.set(club.money.get()+50000)
    print('%s俱乐部获得来自土豪粉丝的5w赞助！')

brz = Button(frame_root, text = '拉赞助', command = donate)
brz.grid(row =0, column = 2)
#页面刷新for市场名单
def refresh_win(f):
    if f == frame_mkt:
        lbm.delete(0, END)
        for i in range(len(market.player)):
            lbm.insert('end', market.player[i].name)
    elif f == frame_club:
        lbc1.delete(0, END)
        for i in range(len(club.player)):
            if club.player[i].site != 0:
                lbc1.insert('end', club.player[i].name + '（ '+ str(club.player[i].site)+'号位）')
            else:
                lbc1.insert('end', club.player[i].name)

#页面转换
def change_win(f):
    refresh_win(f)
    for i in range(len(frame)):
        frame[i].grid_forget()
    f.grid()

br1 = Button(frame_root, text ='交易市场', command = lambda :change_win(frame_mkt))#市场按钮
br1.grid(row = 1, column = 1)

br2 = Button(frame_root, text = "俱乐部", command = lambda :change_win(frame_club))#俱乐部按钮
br2.grid(row = 1, column = 0)

br3 = Button(frame_root, text = '比赛', command = lambda :change_win(frame_game))#模拟比赛按钮
br3.grid(row = 1, column = 2)

#选手市场部分
lm1 = Label(frame_mkt, text = '自由市场选手').grid(row = 1, column =0, columnspan =2)
lbm = Listbox(frame_mkt)
lbm.grid(row = 2, columnspan = 2)
for i in range(len(market.player)):
    lbm.insert('end',market.player[i].name)
def checkm(event = None):
    if lbm.curselection() != ():
        value = lbm.get(lbm.curselection())
        for ii in range(len(market.player)):
            if market.player[ii].name == value:
                i =ii
        varm1[0].set(market.player[i].name)
        varm1[1].set(market.player[i].damage)
        varm1[2].set(market.player[i].control)
        varm1[3].set(market.player[i].viability)
        varm1[4].set(market.player[i].farm)
        varm1[5].set(market.player[i].carry)
        varm1[6].set(market.player[i].support)
        varm1[7].set(market.player[i].fans)
lbm.bind('<ButtonRelease-1>', checkm)#事件触发
lbm.bind('<KeyRelease-Up>', checkm)
lbm.bind('<KeyRelease-Down>', checkm)

#市场界面
bm1 = Button(frame_mkt, text = '返回', command = lambda :change_win(frame_root))
bm1.grid(row =0, column =0)
lm2 = []
lm2.append(Label(frame_mkt, text='姓名：').grid(row =3, column =0))
lm2.append(Label(frame_mkt, text='伤害能力：').grid(row =4, column =0))
lm2.append(Label(frame_mkt, text='控制能力：').grid(row =5, column =0))
lm2.append(Label(frame_mkt, text='生存能力：').grid(row =6, column =0))
lm2.append(Label(frame_mkt, text='发育能力：').grid(row =7, column =0))
lm2.append(Label(frame_mkt, text='核心能力：').grid(row =8, column =0))
lm2.append(Label(frame_mkt, text='辅助能力：').grid(row =9, column =0))
lm2.append(Label(frame_mkt, text='粉丝数目：').grid(row =10, column =0))
varm1 = []
em1 = []
for i in range(8):
    varm1.append(StringVar())
    varm1[i].set('')
    em1.append(Entry(frame_mkt, textvariable = varm1[i], state = 'disabled').grid(row =i+3, column =1))
def buy_player():
    if lbm.curselection() != ():
        value = lbm.get(lbm.curselection())
        for i in range(len(market.player)):
            if market.player[i].name == value:
                the_one = i#pop会导致m.p人数减少
        lbm.delete(the_one)
        club.player.append(market.player.pop(the_one))

bm2 = Button(frame_mkt, text = '购买选手', command = buy_player)
bm2.grid(row = 0, column = 1)

#俱乐部部分

bc1 = Button(frame_club, text = '返回', command = lambda :change_win(frame_root))
bc1.grid(row =0, column = 0)
lc1 = Label(frame_club, text = '选手列表').grid(row =1, column = 0, columnspan = 2)
lbc1 = Listbox(frame_club)#替补选手列表
lbc1.grid(row = 2, columnspan = 2)
def checkc(event = None):
    i = 0
    if lbc1.curselection() != ():
        value = lbc1.get(lbc1.curselection())
        for ii in range(len(club.player)):
            if club.player[ii].name == value:
                i = ii
        varc1[0].set(club.player[i].name)
        varc1[1].set(club.player[i].damage)
        varc1[2].set(club.player[i].control)
        varc1[3].set(club.player[i].viability)
        varc1[4].set(club.player[i].farm)
        varc1[5].set(club.player[i].carry)
        varc1[6].set(club.player[i].support)
        varc1[7].set(club.player[i].fans)
        varc1[8].set(club.player[i].potential)
        varc1[9].set(club.player[i].state)
        varc1[10].set(club.player[i].site)
        bc2.grid(row=3, column=2)
        bc3.grid(row=13, column=2)

#俱乐部界面生成
lc2 = []
lc2.append(Label(frame_club, text='姓名：').grid(row =3, column =0))
lc2.append(Label(frame_club, text='伤害能力：').grid(row =4, column =0))
lc2.append(Label(frame_club, text='控制能力：').grid(row =5, column =0))
lc2.append(Label(frame_club, text='生存能力：').grid(row =6, column =0))
lc2.append(Label(frame_club, text='发育能力：').grid(row =7, column =0))
lc2.append(Label(frame_club, text='核心能力：').grid(row =8, column =0))
lc2.append(Label(frame_club, text='辅助能力：').grid(row =9, column =0))
lc2.append(Label(frame_club, text='粉丝数目：').grid(row =10, column =0))
lc2.append(Label(frame_club, text='属性点：').grid(row =11, column =0))
lc2.append(Label(frame_club, text='状态：').grid(row =12, column =0))
lc2.append(Label(frame_club, text='位置：').grid(row =13, column =0))
varc1 = []
ec1 = []
for i in range(11):
    varc1.append(StringVar())
    varc1[i].set('')
    ec1.append(Entry(frame_club, textvariable = varc1[i], state = 'disabled'))
    ec1[i].grid(row =i+3, column =1)

#选手位置选择
varc3 = IntVar()
varc3.set(1)
rbc1 =Radiobutton(frame_club, text = '1号位', variable = varc3, value = 1)
rbc2 =Radiobutton(frame_club, text = '2号位', variable = varc3, value = 2)
rbc3 =Radiobutton(frame_club, text = '3号位', variable = varc3, value = 3)
rbc4 =Radiobutton(frame_club, text = '4号位', variable = varc3, value = 4)
rbc5 =Radiobutton(frame_club, text = '5号位', variable = varc3, value = 5)

varc4 = StringVar()
varc4.set('改位置')
def change_set():
    if lbc1.curselection() != ():
        if varc4.get() == '改位置':
            rbc1.grid(row=11, column=3)
            rbc2.grid(row=11, column=4)
            rbc3.grid(row=11, column=5)
            rbc4.grid(row=11, column=6)
            rbc5.grid(row=11, column=7)
            value = lbc1.get(lbc1.curselection())
            for i in range(len(club.player)):
                if club.player[i].name == value:
                    club.cs = i
            varc4.set('确定')
            lbc1['state'] = 'disabled'
        else:

            for i in range(len(club.player)):
                if club.player[i].site == varc3.get():
                    club.player[i].site = 0
                    club.player[i].active = 0
            club.player[club.cs].active = 1
            club.player[club.cs].site = varc3.get()
            lbc1['state'] = 'normal'
            varc4.set('改位置')
            rbc1.grid_forget()
            rbc2.grid_forget()
            rbc3.grid_forget()
            rbc4.grid_forget()
            rbc5.grid_forget()
            refresh_win(frame_club)

bc3 = Button(frame_club, textvariable = varc4, command = change_set)

#改名字
varc2 = StringVar()
varc2.set('修改姓名')
def change_name():
    if varc2.get() == '修改姓名':
        if lbc1.curselection() != ():
            value = lbc1.get(lbc1.curselection())
            for i in range(len(club.player)):
                if club.player[i].name == value:
                    club.cv = i
            lbc1['state'] = 'disabled'
            ec1[0]['state'] = 'normal'
            varc2.set('确定修改')
    else:
        club.player[club.cv].name = varc1[0].get()
        lbc1['state'] = 'normal'
        ec1[0]['state'] = 'disabled'
        varc2.set('修改姓名')
        refresh_win(frame_club)

bc2 = Button(frame_club, textvariable = varc2, command = change_name)#改名按钮

#俱乐部事件
lbc1.bind('<ButtonRelease-1>', checkc)
lbc1.bind('<KeyRelease-Up>', checkc)
lbc1.bind('<KeyRelease-Down>', checkc)

#比赛界面
bg1 = Button(frame_game, text = '返回', command = lambda :change_win(frame_root))
bg1.grid()
varg1 = StringVar()
varg1.set('准备')
#关键部分准备游戏
def refreshgame():
    if varg1.get() == '暂停游戏':
        for i in range(5):
            game.cs[i].hp +=game.cs[i].healps*0.1
            game.cv[i].hp +=game.cv[i].healps*0.1
        for i in game.top_player_s:
            game.cs[i].busy -=0.1
            if game.cs[i].busy <= 0:
                game.cs[i].busy =game.cs[i].speed
                game.cs[i].money += game.cs[i].f
                if game.top_player_v !=[]:
                    r = random.randint(0,len(game.top_player_v)-1)
                    r = game.top_player_v[r]
                    game.cv[r].hp -= game.cs[i].damage*20/(20+game.cv[r].defence)
        for i in game.mid_player_s:
            game.cs[i].busy -=0.1
            if game.cs[i].busy <= 0:
                game.cs[i].busy =game.cs[i].speed
                game.cs[i].money += game.cs[i].f
                if game.mid_player_v !=[]:
                    r =random.randint(0,len(game.mid_player_v)-1)
                    r=game.mid_player_v[r]
                    game.cv[r].hp -= game.cs[i].damage*20/(20+game.cv[r].defence)
        for i in game.bot_player_s:
            game.cs[i].busy -=0.1
            if game.cs[i].busy <= 0:
                game.cs[i].busy =game.cs[i].speed
                game.cs[i].money += game.cs[i].f
                if game.bot_player_v !=[]:
                    r =random.randint(0,len(game.bot_player_v)-1)
                    r=game.bot_player_v[r]
                    game.cv[r].hp -= game.cs[i].damage*20/(20+game.cv[r].defence)
        for i in game.top_player_v:
            game.cv[i].busy -=0.1
            if game.cv[i].busy <= 0:
                game.cv[i].busy =game.cv[i].speed
                game.cv[i].money += game.cv[i].f
                if game.top_player_s !=[]:
                    r =random.randint(0,len(game.top_player_s)-1)
                    r=game.top_player_s[r]
                    game.cs[r].hp -= game.cv[i].damage*20/(20+game.cs[r].defence)
        for i in game.mid_player_v:
            game.cv[i].busy -=0.1
            if game.cv[i].busy <= 0:
                game.cv[i].busy =game.cv[i].speed
                game.cv[i].money += game.cv[i].f
                if game.mid_player_s !=[]:
                    r =random.randint(0,len(game.mid_player_s)-1)
                    r=game.mid_player_s[r]
                    game.cs[r].hp -= game.cv[i].damage*20/(20+game.cs[r].defence)
        for i in game.bot_player_v:
            game.cv[i].busy -=0.1
            if game.cv[i].busy <= 0:
                game.cv[i].busy =game.cv[i].speed
                game.cv[i].money += game.cv[i].f
                if game.bot_player_s !=[]:
                    r =random.randint(0,len(game.bot_player_s)-1)
                    r=game.bot_player_s[r]
                    game.cs[r].hp -= game.cv[i].damage*20/(20+game.cs[r].defence)
        for i in range(5):
            hps[i]['maximum'] = game.cs[i].hpmax
            hps[i]['value'] = game.cs[i].hp
            hpv[i]['maximum'] = game.cs[i].hpmax
            hpv[i]['value'] = game.cs[i].hp
        varg3.set(varg3.get()+1)

        win.after(100, refreshgame)
def play():
    print(varg1.get())
    if varg1.get() == '准备':
        print('准备执行checkgame')
        checkgame()
    elif varg1.get() == '游戏初始化':
        varg1.set('开始游戏')
        game_init()
    elif varg1.get() == '开始游戏':
        varg1.set('暂停游戏')
        refreshgame()
    elif varg1.get() == '暂停游戏':
        varg1.set('开始游戏')
def checkgame():
    game.player_self.clear()#清理部分
    game.player_rival.clear()
    print('清理完毕')
    for i in range(len(club.player)):#判定是否能开始
        if club.player[i].site == 1:
            game.player_self.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 2:
            game.player_self.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 3:
            game.player_self.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 4:
            game.player_self.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 5:
            game.player_self.append(club.player[i])
    if len(game.player_self) == 5:
        print('选手齐全')
        for i in range(5):
            game.player_rival.append(Player(random_name()))
            game.player_rival[i].site = i+1
            game.player_rival[i].random_power()
        for i in range(5):##选手信息传递给角色 +++初始化角色
            game.cs.append(Character(game.player_self[i]))
            game.cv.append(Character(game.player_rival[i]))
        varg1.set('游戏初始化')
def game_init():#功能是把角色对应的按钮放在相应的位置
    #角色属性初始化
    for i in range(5):
        game.cs[i].cal()
        game.cv[i].cal()
    #角色按钮和分路初始化
    rl = ['t1', 'm1', 'b1']
    r = random.randint(0, 1)
    if r == 1:
        game.cs[0].location = 'b1'
        game.cs[4].location = 'b1'
        game.cs[2].location = 't1'
    else:
        game.cs[0].location = 't1'
        game.cs[4].location = 't1'
        game.cs[2].location = 'b1'
    game.cs[1].location = 'm1'
    game.cs[3].location = rl[r]
    r = random.randint(0, 1)
    if r == 1:
        game.cv[0].location = 'b1'
        game.cv[4].location = 'b1'
        game.cv[2].location = 't1'
    else:
        game.cv[0].location = 't1'
        game.cv[4].location = 't1'
        game.cv[2].location = 'b1'
    game.cv[1].location = 'm1'
    r = random.randint(0, 2)
    game.cv[3].location = rl[r]
    for i in range(5):
        bcs[i]['text'] = game.cs[i].name + '（' + str(game.cs[i].site) + '号位）'
        bcv[i]['text'] = game.cv[i].name + '（' + str(game.cv[i].site) + '号位）'
    #各个角色按钮位置初始化
    for i in range(5):
        hps[i]['maximum'] = game.cs[i].hpmax
        hps[i]['value'] = game.cs[i].hp
        hpv[i]['maximum'] = game.cv[i].hpmax
        hpv[i]['value'] = game.cv[i].hp
        if game.top.count(game.cs[i].location) !=0:
            game.top_player_s.append(i)
            bcs[i].grid(row=4 + 2 * len(game.top_player_s), column=3)
            hps[i].grid(row=3 + 2 * len(game.top_player_s), column=3)
        elif game.mid.count(game.cs[i].location) !=0:
            game.mid_player_s.append(i)
            bcs[i].grid(row=4 + 2 * len(game.mid_player_s), column=5)
            hps[i].grid(row=3 + 2 * len(game.mid_player_s), column=5)
        elif game.bot.count(game.cs[i].location) !=0:
            game.bot_player_s.append(i)
            bcs[i].grid(row=4 + 2 * len(game.bot_player_s), column=7)
            hps[i].grid(row=3 + 2 * len(game.bot_player_s), column=7)
    for i in range(5):
        hpv[i]['maximum'] = game.cv[i].hpmax
        hpv[i]['value'] = game.cv[i].hp
        if game.top.count(game.cv[i].location) !=0:
            game.top_player_v.append(i)
            bcv[i].grid(row=14 + 2 * len(game.top_player_v), column=3)
            hpv[i].grid(row=13 + 2 * len(game.top_player_v), column=3)
        elif game.mid.count(game.cv[i].location) !=0:
            game.mid_player_v.append(i)
            bcv[i].grid(row=14 + 2 * len(game.mid_player_v), column=5)
            hpv[i].grid(row=13 + 2 * len(game.mid_player_v), column=5)
        elif game.bot.count(game.cv[i].location) !=0:
            game.bot_player_v.append(i)
            bcv[i].grid(row=14 + 2 * len(game.bot_player_v), column=7)
            hpv[i].grid(row=13 + 2 * len(game.bot_player_v), column=7)
    for i in range(3):#中线标签的初始化
        lg1[i].grid(row=13, column=3 + 2 * i)
    
    
bg2 = Button(frame_game, textvariable = varg1, command = play)
bg2.grid(column =1)
lg1 =[]
varg2 = []
for i in range(3):
    varg2.append(StringVar())
    lg1.append(Label(frame_game, textvariable=varg2[i]))
varg2[0].set('上路一塔')
varg2[1].set('中路一塔')
varg2[2].set('下路一塔')
varg3 = IntVar()
varg3.set(0)
lg2 = Label(frame_game,textvariable =varg3).grid()
bcs = []#我方角色池
bcv = []#敌方角色池
hps = []
hpv = []
for i in range(5):
    bcs.append(Button(frame_game,fg ="blue"))
    bcv.append(Button(frame_game,fg ="red"))
    hps.append(ttk.Progressbar(frame_game))
    hpv.append(ttk.Progressbar(frame_game))
#menubar
menubar = Menu(win)
#　定义一个空的菜单单元
filemenu = Menu(menubar, tearoff=0)  # tearoff意为下拉
menubar.add_cascade(label='开始', menu=filemenu)
filemenu.add_command(label='保存')
filemenu.add_command(label='载入')
# 分隔线
filemenu.add_separator()
filemenu.add_command(label='退出', command = win.quit)
win.config(menu =menubar)

####测试用代码
club.player.append(Player('1号工具人'))
club.player.append(Player('2号工具人'))
club.player.append(Player('3号工具人'))
club.player.append(Player('4号工具人'))
club.player.append(Player('5号工具人'))
for i in range(5):
    club.player[i].site =1+i
    club.player[i].random_power()

win.mainloop()


