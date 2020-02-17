from tkinter import *
from support import *
from tkinter import ttk
import time
import pickle
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
lbc1 = Listbox(frame_club)
lbc1.grid(row = 2, columnspan = 2)
def checkc(event = None):
    i = 0
    print('触发checkc')
    print(lbc1.curselection())
    if lbc1.curselection() != ():
        value = lbc1.get(lbc1.curselection())
        print(value)
        for ii in range(len(club.player)):
            if club.player[ii].name in value:
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
def change_site():
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

bc3 = Button(frame_club, textvariable = varc4, command = change_site)

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
def refreshbb():
    for i in range(10):
        hpb[i]['maximum'] =game.ch[i].hpmax
        hpb[i]['value'] = game.ch[i].hp
def refreshgame():
    if varg1.get() == '暂停游戏':
        game_time_refresh()
        for i in range(10):
            judgement(game.ch[i])
        refreshbb()
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
    game.player.clear()#清理部分
    print('清理完毕')
    for i in range(len(club.player)):#判定是否能开始
        if club.player[i].site == 1:
            game.player.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 2:
            game.player.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 3:
            game.player.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 4:
            game.player.append(club.player[i])
    for i in range(len(club.player)):
        if club.player[i].site == 5:
            game.player.append(club.player[i])
    if len(game.player) == 5:
        print('选手齐全')
        for i in range(5):
            game.player.append(Player(random_name()))
            game.player[i+5].site = i+1
            game.player[i+5].random_power()
        for i in range(10):##选手信息传递给角色 +++初始化角色
            game.ch.append(Character(game.player[i],i))
        for i in range(5,10):
            game.ch[i].sv_flag = 1#对手标示
        varg1.set('游戏初始化')
def game_init():#功能是把角色对应的按钮放在相应的位置
    #角色属性初始化
    for i in range(10):
        game.ch[i].cal()
    #塔初始化
    game.tower_creat()
    #分路按钮和血条初始化放置
    for i in range(10):
        bgc[i]['text'] = game.ch[i].name + '（' + str(game.ch[i].site) + '号位）'
        hpb[i]['maximum'] =game.ch[i].hpmax
        hpb[i]['value'] = game.ch[i].hp
    for i in [0,5]:
        r =random.randint(0,1)
        if r ==0:
            game.ch[i].tmb_flag = 2
            game.ch[i + 4].tmb_flag = 2
            game.ch[i + 2].tmb_flag = 0
        elif r==1:
            game.ch[i].tmb_flag = 0
            game.ch[i + 4].tmb_flag = 0
            game.ch[i + 2].tmb_flag = 2
        game.ch[i + 1].tmb_flag = 1
        game.ch[i + 3].tmb_flag = random.randint(0,2)
    for i in range(5):
        if game.ch[i].tmb_flag == 0:
            game.ts.append(i)
            bgc[i].grid(row=11 - len(game.ts) * 2, column =3)
            hpb[i].grid(row=10 - len(game.ts) * 2, column =3)
        elif game.ch[i].tmb_flag ==1:
            game.ms.append(i)
            bgc[i].grid(row=11 - len(game.ms) * 2, column =5)
            hpb[i].grid(row=10 - len(game.ms) * 2, column =5)
        elif game.ch[i].tmb_flag ==2:
            game.bs.append(i)
            bgc[i].grid(row=11 - len(game.bs) * 2, column=7)
            hpb[i].grid(row=10 - len(game.bs) * 2, column=7)
    for i in range(5,10):
        if game.ch[i].tmb_flag == 0:
            game.tv.append(i)
            bgc[i].grid(row=16 + len(game.tv) * 2, column=3)
            hpb[i].grid(row=15 + len(game.tv) * 2, column=3)
        elif game.ch[i].tmb_flag == 1:
            game.mv.append(i)
            bgc[i].grid(row=16 + len(game.mv) * 2, column=5)
            hpb[i].grid(row=15 + len(game.mv) * 2, column=5)
        elif game.ch[i].tmb_flag == 2:
            game.bv.append(i)
            bgc[i].grid(row=16 + len(game.bv) * 2, column=7)
            hpb[i].grid(row=15 + len(game.bv) * 2, column=7)
    for i in range(5):
        bgc[i]['fg'] = 'blue'
        bgc[i + 5]['fg'] = 'red'
    #中线初始化放置
    for i in range(3):#中线标签的初始化
        lg1[i].grid(row=13, column=3 + 2 * i)
def game_time_refresh():
    if gt[2] == 9:
        gt[2] =0
        gt[1]+=1
    else:
        gt[2] +=1
    if gt[1] == 60:
        gt[1] =0
        gt[0] +=1
    varg3.set('游戏时间：'+str(gt[0])+'分钟'+str(gt[1])+'.'+str(gt[2])+'秒')
    varg4[0].set(game.ch[game.sc].name)
    varg4[1].set(game.ch[game.sc].hp)
    varg4[2].set(game.ch[game.sc].money)
    varg4[3].set(game.ch[game.sc].damage)
    varg4[4].set(game.ch[game.sc].through)
    varg4[5].set(game.ch[game.sc].defence)
    varg4[6].set(game.ch[game.sc].healps)
def judgement(ch):
    ch.hp+=ch.healps*0.1
    if ch.hp>ch.hpmax:
        ch.hp =ch.hpmax
    ch.busy -=0.1
    if ch.controlcd!=0:
        ch.controlcd-=0.1
    if ch.busy <= 0 and ch.dead_flag == 0:
        b=ch.d+ch.c+ch.v+ch.f
        r =random.randint(1,b)
        if r>=1 and r<ch.d:
            damage_behave(ch)
        elif r>=ch.d and r<ch.d+ch.c:
            control_behave(ch)
        elif r >= ch.d+ch.c and r < ch.d+ch.c+ch.v:
            viability_behave(ch)
        elif r >= ch.d+ch.c+ch.v and r <= b:
            farm_behave(ch)
    elif ch.busy <=0 and ch.dead_flag == 1:
        ch.dead_flag = 0
        bgc[ch.num]['bg'] = 'white'
        back(ch)
def back(ch):
    if ch.tmb_flag == 0 and ch.sv_flag == 0:
        game.ts.append(ch.num)
    elif ch.tmb_flag == 0 and ch.sv_flag == 1:
        game.tv.append(ch.num)
    elif ch.tmb_flag == 1 and ch.sv_flag == 0:
        game.ms.append(ch.num)
    elif ch.tmb_flag == 1 and ch.sv_flag == 1:
        game.mv.append(ch.num)
    elif ch.tmb_flag == 2 and ch.sv_flag == 0:
        game.bs.append(ch.num)
    elif ch.tmb_flag == 2 and ch.sv_flag == 1:
        game.bv.append(ch.num)
def escape(ch):
    if ch.tmb_flag == 0 and ch.sv_flag == 0:
        a = game.ts.index(ch.num)
        game.ts.pop(a)
    elif ch.tmb_flag == 0 and ch.sv_flag == 1:
        a = game.tv.index(ch.num)
        game.tv.pop(a)
    elif ch.tmb_flag == 1 and ch.sv_flag == 0:
        a = game.ms.index(ch.num)
        game.ms.pop(a)
    elif ch.tmb_flag == 1 and ch.sv_flag == 1:
        a = game.mv.index(ch.num)
        game.mv.pop(a)
    elif ch.tmb_flag == 2 and ch.sv_flag == 0:
        a = game.bs.index(ch.num)
        game.bs.pop(a)
    elif ch.tmb_flag == 2 and ch.sv_flag == 1:
        a = game.bv.index(ch.num)
        game.bv.pop(a)
    ch.dead_flag =1
    bgc[ch.num]['bg'] ='black'
    ch.busy += 20
    ch.hp +=ch.hpmax
def search_target(ch):
    target ='初始'
    if ch.tmb_flag == 0 and ch.sv_flag == 0:
        if len(game.tv) !=0:
            r = random.randint(0, len(game.tv) - 1)
            target = game.tv[r]
        else:
            farm_behave(ch)
            target = 'toptower'
    elif ch.tmb_flag == 1 and ch.sv_flag ==0:
        if len(game.mv) != 0:
            r = random.randint(0, len(game.mv) - 1)
            target = game.mv[r]
        else:
            farm_behave(ch)
            target = 'midtower'
    elif ch.tmb_flag == 2 and ch.sv_flag ==0:
        if len(game.bv) != 0:
            r = random.randint(0, len(game.bv) - 1)
            target = game.bv[r]
        else:
            farm_behave(ch)
            target = 'bottower'
    elif ch.tmb_flag == 0 and ch.sv_flag ==1:
        if len(game.ts) != 0:
            r = random.randint(0, len(game.ts) - 1)
            target = game.ts[r]
        else:
            farm_behave(ch)
            target = 'toptower'
    elif ch.tmb_flag == 1 and ch.sv_flag ==1:
        if len(game.ms) != 0:
            r = random.randint(0, len(game.ms) - 1)
            target = game.ms[r]
        else:
            farm_behave(ch)
            target = 'midtower'
    elif ch.tmb_flag == 2 and ch.sv_flag ==1:
        if len(game.bs) != 0:
            r = random.randint(0, len(game.bs) - 1)
            target = game.bs[r]
        else:
            farm_behave(ch)
            target = 'bottower'
    return target# 返回的是编号
def tower_set(ch):
    a=''
    if ch.num<5:
        a+='我方'
        if ch.tmb_flag == 0:
            a += '上路'
            a +=str(4 - len(game.towerv[0])) + '塔'
            varg2[0].set(a)
        elif ch.tmb_flag == 1:
            a += '中路'
            a += str(5 - len(game.towerv[1])) + '塔'
            varg2[1].set(a)
        else:
            a += '下路'
            a += str(4 - len(game.towerv[2])) + '塔'
            varg2[2].set(a)
    else:
        a+='对方'
        if ch.tmb_flag == 0:
            a += '上路'
            a += str(4 - len(game.towers[0])) + '塔'
            varg2[0].set(a)
        elif ch.tmb_flag == 1:
            a += '中路'
            a += str(5 - len(game.towers[1])) + '塔'
            varg2[1].set(a)
        else:
            a += '下路'
            a += str(4 - len(game.towers[2])) + '塔'
            varg2[2].set(a)
def hit_tower(ch):
    tower_set(ch)
    a = ch.tmb_flag
    ch.busy +=ch.speed
    if ch.num <5:
        ch.hp -= game.towerv[a][0].damage * 10/(10 + ch.defence)
        game.towerv[a][0].hp -= ch.damage * 10/(10 + game.towerv[a][0].defence - ch.through)
        thpb[a]['maximun']=game.towerv[a][0].hpmax
        thpb[a]['value'] = game.towerv[a][0].hp
        if game.towerv[a][0].hp <=0:
            game.towerv[a].pop(0)
        if a == 0 and len(game.towerv[a]) == []:
            for i in game.ts:
                move(i,1)
            for i in game.tv:
                move(i,1)
        elif a == 2 and len(game.towerv[a]) == []:
            for i in game.bs:
                move(i,1)
            for i in game.bv:
                move(i,1)
    else:
        ch.hp -= game.towers[a][0].damage * 10/(10 + ch.defence)
        game.towers[a][0].hp -= ch.damage * 10/(10 + game.towers[a][0].defence - ch.through)
        thpb[a]['maximun'] = game.towers[a][0].hpmax
        thpb[a]['value'] = game.towers[a][0].hp
        if game.towers[a][0].hp <=0:
            game.towers[a].pop(0)
        if a == 0 and len(game.towers[a]) == []:
            for i in game.ts:
                move(i,1)
            for i in game.tv:
                move(i,1)
        elif a == 2 and len(game.towers[a]) == []:
            for i in game.bs:
                move(i,1)
            for i in game.bv:
                move(i,1)
    if len(game.towers[a]) == [] or len(game.towerv[a]) == []:
        varg1.set('结束了！')
def move(num, tmb):#num号玩家移动到tmb位置
    a = game.ch[num].tmb_flag
    bgc[num].grid_forget()
    hpb[num].grid_forget()
    if num <5:
        if a == 0:
            game.ts.pop(num)
        elif a ==1:
            game.ms.pop(num)
        else:
            game.bs.pop(num)
        if tmb ==0:
            game.ts.append(num)
            bgc[i].grid(row=11 - len(game.ts) * 2, column=3)
            hpb[i].grid(row=10 - len(game.ts) * 2, column=3)
        elif tmb==1:
            game.ms.append(num)
            bgc[i].grid(row=11 - len(game.ms) * 2, column=5)
            hpb[i].grid(row=10 - len(game.ms) * 2, column=5)
        else:
            game.bs.append(num)
            bgc[i].grid(row=11 - len(game.bs) * 2, column=7)
            hpb[i].grid(row=10 - len(game.bs) * 2, column=7)
    else:
        if a == 0:
            game.tv.pop(num)
        elif a ==1:
            game.mv.pop(num)
        else:
            game.bv.pop(num)
        if tmb ==0:
            game.tv.append(num)
            bgc[i].grid(row=16 + len(game.tv) * 2, column=3)
            hpb[i].grid(row=15 + len(game.tv) * 2, column=3)
        elif tmb==1:
            game.mv.append(num)
            bgc[i].grid(row=16 + len(game.mv) * 2, column=5)
            hpb[i].grid(row=15 + len(game.mv) * 2, column=5)
        else:
            game.bv.append(num)
            bgc[i].grid(row=16 + len(game.bv) * 2, column=7)
            hpb[i].grid(row=15 + len(game.bv) * 2, column=7)
    game.ch[num].busy +=3
def damage_behave(ch):
    if type(search_target(ch)) == int:
        target = game.ch[search_target(ch)]
        target.hp -= ch.damage*10/(10+target.defence-ch.through)
        ch.busy += ch.speed
        if target.hp <= 0:
            escape(target)
            target.busy += 10
            ch.money += 100+target.money/10
    else:
        hit_tower(ch)
def control_behave(ch):
    if ch.controlcd ==0:
        if type(search_target(ch)) == int:
            target = game.ch[search_target(ch)]
            target.busy += ch.controltime
            ch.controlcd +=20
            ch.busy+=0.5
        else:
            judgement(ch)
    else:
        judgement(ch)
def viability_behave(ch):
    if ch.hpmax-5*ch.hp>0:
        escape(ch)
    else:
        ch.hp += ch.healps*7
        ch.busy += 1
def farm_behave(ch):
    ch.money += ch.f*1.5
    ch.busy += ch.speed
    ch.cal()
bg2 = Button(frame_game, textvariable = varg1, command = play)
bg2.grid(row =0, column =1)
bgc = []#角色按钮
hpb = []#血条
thpb = []
for i in range(3):
    thpb.append(ttk.Progressbar(frame_game).grid(row=13, column=4+2*i))
#罗嗦的一段
def checkch0():
    game.sc =0
def checkch1():
    game.sc =1
def checkch2():
    game.sc =2
def checkch3():
    game.sc =3
def checkch4():
    game.sc =4
def checkch5():
    game.sc =5
def checkch6():
    game.sc =6
def checkch7():
    game.sc =7
def checkch8():
    game.sc =8
def checkch9():
    game.sc =9
bgc.append(Button(frame_game,bg='white',command =checkch0))
bgc.append(Button(frame_game,bg='white',command =checkch1))
bgc.append(Button(frame_game,bg='white',command =checkch2))
bgc.append(Button(frame_game,bg='white',command =checkch3))
bgc.append(Button(frame_game,bg='white',command =checkch4))
bgc.append(Button(frame_game,bg='white',command =checkch5))
bgc.append(Button(frame_game,bg='white',command =checkch6))
bgc.append(Button(frame_game,bg='white',command =checkch7))
bgc.append(Button(frame_game,bg='white',command =checkch8))
bgc.append(Button(frame_game,bg='white',command =checkch9))
for i in range(10):
    hpb.append(ttk.Progressbar(frame_game))


lg1 =[]
varg2 = []#中线label
for i in range(3):
    varg2.append(StringVar())
    lg1.append(Label(frame_game, textvariable=varg2[i]))
varg2[0].set('上路一塔')
varg2[1].set('中路一塔')
varg2[2].set('下路一塔')
gt =[0, 0, 0]#时间
varg3 = StringVar()
varg3.set('游戏时间：'+str(gt[0])+'分钟'+str(gt[1])+'.'+str(gt[2])+'秒')
lg2 = Label(frame_game,textvariable =varg3).grid(row =0,column =2,columnspan = 6)

lg3 = []#25起
eg1 = []
varg4 =[]
for i in range(7):
    varg4.append(StringVar())
    eg1.append(Entry(frame_game, textvariable=varg4[i], state ='disabled').grid(row =25+i,column =3,columnspan =4))
lg3.append(Label(frame_game,text = '姓名').grid(row =25, column = 2))
lg3.append(Label(frame_game,text = '生命').grid(row =26, column = 2))
lg3.append(Label(frame_game,text = '经济').grid(row =27, column = 2))
lg3.append(Label(frame_game,text = '伤害').grid(row =28, column = 2))
lg3.append(Label(frame_game,text = '穿透').grid(row =29, column = 2))
lg3.append(Label(frame_game,text = '防御').grid(row =30, column = 2))
lg3.append(Label(frame_game,text = '恢复').grid(row =31, column = 2))


####测试用代码
# club.player.append(Player('1号工具人'))
# club.player.append(Player('2号工具人'))
# club.player.append(Player('3号工具人'))
# club.player.append(Player('4号工具人'))
# club.player.append(Player('5号工具人'))
# for i in range(5):
#     club.player[i].site =1+i
#     club.player[i].random_power()

def save():
    data = []
    data.append(club.player)
    f = open('save.pckl', 'wb')
    pickle.dump(data, f)
    f.close()

def load():
    f = open('save.pckl', 'rb')
    data = pickle.load(f)
    f.close()
    club.player.clear()
    club.player +=data[0]
#menubar
menubar = Menu(win)
#　定义一个空的菜单单元
filemenu = Menu(menubar, tearoff=0)  # tearoff意为下拉
menubar.add_cascade(label='开始', menu=filemenu)
filemenu.add_command(label='保存',command = save)#存储功能实装！
filemenu.add_command(label='载入',command = load)
# 分隔线
filemenu.add_separator()
filemenu.add_command(label='退出', command = win.quit)
win.config(menu =menubar)



win.mainloop()


