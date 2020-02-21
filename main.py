from tkinter import *
from support import *
from tkinter import ttk
import tkinter.messagebox
import time
import pickle
# <editor-fold desc="开头">
win =Tk()
win.geometry('800x600')
win.title('这不是MOBA')
club = Club()#初始化俱乐部
state = State()
# game = Game()
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
# </editor-fold>
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

# <editor-fold desc="市场界面">
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
# </editor-fold>

#俱乐部部分

bc1 = Button(frame_club, text = '返回', command = lambda :change_win(frame_root))
bc1.grid(row =0, column = 0)
lc1 = Label(frame_club, text = '选手列表').grid(row =1, column = 0, columnspan = 2)
lbc1 = Listbox(frame_club)
lbc1.grid(row = 2, columnspan = 2)
def checkc(event = None):
    i = 0
    if lbc1.curselection() != ():
        value = lbc1.get(lbc1.curselection())
        for ii in range(len(club.player)):
            if club.player[ii].name in value:
                i = ii
        print(club.player[i].age)
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
for i in range(11):
    lc2.append(Label(frame_club,text =['姓名：','伤害能力：','控制能力：',
                                       '生存能力：','发育能力：','核心能力：','辅助能力：',
                                       '粉丝数目：','属性点：','状态：','位置：'][i]).grid(row=3+i,column =0))
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
                if club.player[i].name in value:
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
                if club.player[i].name in value:
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
#开除选手
# varc3 = StringVar()
# varc3.set('开除选手')
def fire():
    if lbc1.curselection() != ():
        value = lbc1.get(lbc1.curselection())
        for i in range(len(club.player)):
            if club.player[i].name in value:
                if tkinter.messagebox.askyesno('提示', '要执行此操作吗'):
                    club.player.pop(i)
                    refresh_win(frame_club)

bc4 = Button(frame_club, text = '开除选手', command = fire)#开除按钮
bc4.grid()
#俱乐部事件
lbc1.bind('<ButtonRelease-1>', checkc)
lbc1.bind('<KeyRelease-Up>', checkc)
lbc1.bind('<KeyRelease-Down>', checkc)

#比赛界面
frame_game_state =Frame(frame_game)
frame_game_state.grid(row =1,column =9,rowspan =11, columnspan =5)
frame_game_msg=LabelFrame(frame_game, bg ='white')
frame_game_msg.grid(row =13,column =9,rowspan =11, columnspan =5)
bg1 = Button(frame_game, text = '返回', command = lambda :change_win(frame_root))
bg1.grid(row =0,column =0)
varg1 = StringVar()
varg1.set('准备')
#关键部分准备游戏
def printf(text):
    for i in range(9):
        var_msg[9-i].set(var_msg[8-i].get())
    var_msg[0].set('~~'+text+'~~')
def recoverbb():#修复加速导致的错位
    for i in range(10):
        bgc[i].grid_forget()
        hpb[i].grid_forget()
    for i in range(10):
        # a = game.ch[i].dead_flag
        j = game.ch[i].tmb_flag
        if game.ch[i].dead_flag ==0:
            if i <5:
                bgc[i].grid(row=11 - game.ps[j].index(i) * 2, column=3 + 2 * j)
                hpb[i].grid(row=10 - game.ps[j].index(i) * 2, column=3 + 2 * j)
            else:
                bgc[i].grid(row=15 + game.ps[j+3].index(i) * 2, column=3 + 2 * j)
                hpb[i].grid(row=14 + game.ps[j+3].index(i) * 2, column=3 + 2 * j)
        else:
            if i <5:
                bgc[i].grid(row=11 - game.spring[0].index(i) * 2, column=8)
                hpb[i].grid(row=10 - game.spring[0].index(i) * 2, column=8)
            else:
                bgc[i].grid(row=15 + game.spring[1].index(i) * 2, column=8)
                hpb[i].grid(row=14 + game.spring[1].index(i) * 2, column=8)
def refreshbb():#界面刷新
    for i in range(10):
        hpb[i].refresh(game.ch[i].hp,game.ch[i].hpmax)
    varg3.set('游戏时间：' + str(game.gt[0]) + '分钟' + str(game.gt[1]) + '.' + str(game.gt[2]) + '秒')
    ch=game.ch[game.sc]
    var_state[0].set(ch.name)
    var_state[1].set(str(ch.kda[0])+'/'+str(ch.kda[1])+'/'+str(ch.kda[2]))#kda
    var_state[2].set(ch.money)
    var_state[3].set(int(ch.damage))
    var_state[4].set(int(ch.through))
    var_state[5].set(int(ch.defence))
    var_state[6].set(int(ch.healps))
def judgement(ch):
    ch.hp += ch.healps * 0.1
    if ch.hp > ch.hpmax:
        ch.hp = ch.hpmax
    ch.busy -= 0.1
    if ch.controlcd > 0:
        ch.controlcd -= 0.1
    if ch.tpcd != 0:
        ch.tpcd -= 0.1
    if ch.busy <= 0 and ch.dead_flag == 0:
        if swim(ch) == 0:
            b = ch.d + ch.c + ch.v + ch.f
            r = random.randint(1, b)
            if r >= 1 and r < ch.d:
                damage_behave(ch)
            elif r >= ch.d and r < ch.d + ch.c:
                control_behave(ch)
            elif r >= ch.d + ch.c and r < ch.d + ch.c + ch.v:
                viability_behave(ch)
            elif r >= ch.d + ch.c + ch.v and r <= b:
                farm_behave(ch)
    elif ch.busy <= 0 and ch.dead_flag == 1:
        back(ch)
def refreshgame_time(n=100):
    if varg1.get() == '暂停游戏':
        game_time_refresh()
        for i in range(10):
            judgement(game.ch[i])
        refreshbb()
        win.after(n, lambda :refreshgame_time(game.gospeed))
def refreshgame():#后台的，用来push
    game_time_refresh()
    for i in range(10):
        judgement(game.ch[i])
def play():
    if varg1.get() == '准备':
        checkgame()
    elif varg1.get() == '游戏初始化':
        varg1.set('进行游戏')
        game_init()
    elif varg1.get() == '进行游戏':
        varg1.set('暂停游戏')
        refreshgame_time(game.gospeed)
    elif varg1.get() == '暂停游戏':
        varg1.set('进行游戏')
    elif varg1.get() =='开始结算':
        cal_game()
        varg1.set('准备')
        bg2['state']=='disabled'
def end_game():
    varg1.set('准备')
    bg2['state']='normal'
    bg3['state']='disabled'
    bg4['state']='disabled'
    bg5['text']='1倍速'
    for i in range(10):
        bgc[i].grid_forget()
        hpb[i].grid_forget()
        m_game[i].grid_forget()
        var_msg[i].set('~~~~~~~~~~')
    for i in range(3):
        thpb[i].grid_forget()
        b_midline[i].grid_forget()
    b_midline[3].grid_forget()
    for i in range(7):
        e_state[i].grid_forget()
        l_state[i].grid_forget()
def checkgame():
    global game
    game = Game()
    #随机对手
    global rival
    rival = Rival()
    rival.random()
    a = []
    for i in range(len(club.player)):  # 判定是否能开始
        a.append((club.player[i].site,club.player[i]))
    a.sort(reverse=1)
    if len(a)>=5:
        if a[4][0] ==1:#从大到小排列第五个选手位置是1号位
            print('选手齐全')
            r = random.randint(0,1)
            if r ==0:#蓝色方
                for i in range(5):
                    game.player.append(a[4-i][1])
                for i in range(5):
                    game.player.append(rival.player[i])
            else:
                for i in range(5):
                    game.player.append(rival.player[i])
                for i in range(5):
                    game.player.append(a[4-i][1])
            for i in range(10):
                game.ch.append(Character(game.player[i],i))
            varg1.set('游戏初始化')
        else:
            tkinter.messagebox.showinfo('提示', '选手未分配位置！')
    else:
        tkinter.messagebox.showinfo('提示', '选手人数不足！')
def game_init():#功能是把角色对应的按钮放在相应的位置
    bg4['state'] = 'normal'
    bg3['state'] = 'normal'
    #角色属性初始化
    for i in range(10):
        game.ch[i].cal()
        bgc[i]['bg']='white'
    #塔初始化
    game.tower_creat()
    #分路按钮和血条初始化放置
    for i in range(10):
        bgc[i]['text'] = game.ch[i].name + '（' + str(game.ch[i].site) + '号位）'
        hpb[i].hpmax=game.ch[i].hpmax
        hpb[i].hp = game.ch[i].hp
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
    for i in range(10):
        j =game.ch[i].tmb_flag
        if i <5:
            game.ps[j].append(i)
            bgc[i].grid(row=11 - game.ps[j].index(i) * 2, column=3 + 2 * j)
            hpb[i].grid(row=10 - game.ps[j].index(i) * 2, column=3 + 2 * j)
        else:
            game.ps[j+3].append(i)
            bgc[i].grid(row=15 + game.ps[j+3].index(i) * 2, column=3 + 2 * j)
            hpb[i].grid(row=14 + game.ps[j+3].index(i) * 2, column=3 + 2 * j)
    for i in range(5):
        bgc[i]['fg'] = 'blue'
        bgc[i + 5]['fg'] = 'red'
    #中线初始化放置
    var_midline[0].set('~~上路河道~~')
    var_midline[1].set('~~中路河道~~')
    var_midline[2].set('~~下路河道~~')
    var_midline[3].set('~~双方泉水~~')
    #状态栏初始化
    for i in range(7):
        e_state[i].grid(row=i, column=1)
        l_state[i].grid(row=i, column=0)
    for i in range(3):#中线标签和塔血条的初始化
        b_midline[i].grid(row=13, column=3 + 2 * i)
        thpb[i].grid(row=12, column=3 + 2 * i)
    b_midline[3].grid(row=13, column=8)
    #msg初始化
    for i in range(10):
        m_game[9-i].grid(columnspan =8)
def game_time_refresh():
    if game.gt[2] == 9:
        game.gt[2] =0
        game.gt[1]+=1
    else:
        game.gt[2] +=1
    if game.gt[1] == 60:
        game.gt[1] =0
        game.gt[0] +=1
    #刷新资源
    if game.gt[1] in [0, 30]:
        game.resource_fresh()
def back(ch):
    ch.dead_flag = 0
    if ch.num<5:
        b=0
    else:
        b=1
    bgc[ch.num]['bg'] = 'white'
    game.spring[b].pop(game.spring[b].index(ch.num))
    if ch.num < 5:
        game.ps[ch.tmb_flag].append(ch.num)
    else:
        game.ps[ch.tmb_flag + 3].append(ch.num)
    recoverbb()
def leave(ch):
    a = ch.tmb_flag
    if ch.num <5:
        b = 0
    else:
        b = 1
    game.ps[a + 3 * b].pop(game.ps[a + 3 * b].index(ch.num))
    ch.dead_flag =1
    bgc[ch.num]['bg'] ='grey'
    bgc[ch.num].grid_forget()
    hpb[ch.num].grid_forget()
    game.spring[b].append(ch.num)
    recoverbb()
    ch.hp=ch.hpmax
    # ch.busy += 20
    # game.pressure[b][a] +=15
def dead(ch):
    a = ch.tmb_flag
    if ch.num < 5:
        b = 0
    else:
        b = 1
    game.ps[a + 3 * b].pop(game.ps[a + 3 * b].index(ch.num))
    ch.dead_flag =1
    bgc[ch.num]['bg'] ='grey'
    game.spring[b].append(ch.num)
    recoverbb()
    ch.busy += 10 +80*ch.money/50000
    ch.hp = ch.hpmax
    game.pressure[b][a] += 50
def swim(ch):
    a =ch.tmb_flag
    if ch.num>5:
        b =0
    else:
        b=1
    c =[]
    for i in range(len(game.tmb_avi[b])):
        if game.pressure[b][i] >= 300 and game.tmb_avi[b][i] != a:
            c.append(game.tmb_avi[b][i])
    if c!=[]:
        r = random.randint(0,len(c)-1)
        game.pressure[b][c[r]] = 0
        move(ch,c[r])
        swim_flag =1
    else:
        swim_flag =0
    return swim_flag
def search_target(ch):
    target = 10
    if ch.num<5 and game.ps[ch.tmb_flag+3] !=[]:
        r = random.randint(0, len(game.ps[ch.tmb_flag+3]) - 1)
        target = game.ps[ch.tmb_flag+3][r]
    elif ch.num>=5 and game.ps[ch.tmb_flag] !=[]:
        r = random.randint(0, len(game.ps[ch.tmb_flag]) - 1)
        target = game.ps[ch.tmb_flag][r]
    return target# 返回的是编号
def tower_set(ch):#
    a=''
    b=['上路','中路','下路']
    if ch.num<5:
        a+='~红色方'
    else:
        a+='~蓝色方'
    for i in range(3):
        if ch.tmb_flag == i:
            a+=b[i]
    if ch.num<5 and len(game.tower[1][ch.tmb_flag])!= 0:
        a += str(4-len(game.tower[1][ch.tmb_flag])) + '塔~'
    elif ch.num>=5 and len(game.tower[0][ch.tmb_flag])!= 0:
        a += str(4 - len(game.tower[0][ch.tmb_flag])) + '塔~'
    elif ch.num<5 and len(game.tower[1][ch.tmb_flag])== 0:
        a ='~~红色方基地~~'
    elif ch.num>=5 and len(game.tower[0][ch.tmb_flag]) == 0:
        a ='~~蓝色方基地~~'
    for i in range(3):
        if ch.tmb_flag == i:
            var_midline[i].set(a)
def hit_tower(ch):
    tower_set(ch)
    if ch.num <5:
        a = 0
    else:
        a = 1
    b = ch.tmb_flag
    ch.busy += ch.speed
    if game.tower[1-a][b] ==[]:#如果对方b塔为空
        if b in game.tmb_avi[a]:# 检测 b是不是可去路，是就去除
            game.tmb_avi[a].pop(game.tmb_avi[a].index(b))
        if game.tmb_avi[a] !=[]:#可去的路不为空
            move(ch, game.tmb_avi[a][random.randint(0, len(game.tmb_avi[a])-1)])
        else:
            final(a)#a获胜
            game.result = a
    else:
        ch.hp -= game.tower[1 - a][b][0].damage * 18/(18 + ch.defence)
        ch.dtd -= game.tower[1 - a][b][0].damage
        if ch.hp<= 0:
            leave(ch)
            ch.busy+=20
        game.tower[1-a][b][0].hp -= ch.damage * 18/(18 + game.tower[1-a][b][0].defence - ch.through/2)
        ch.dtt += ch.damage * 18/(18 + game.tower[1-a][b][0].defence - ch.through/2)
        game.pressure[a][b]+=20
        thpb[b].refresh(game.tower[1-a][b][0].hp,game.tower[1-a][b][0].hpmax)
        if game.tower[1-a][b][0].hp <=0:#击破塔
            printf(ch.name+'击破'+var_midline[b].get())
            for i in range(5):
                game.ch[5*a+i].money += 200
            game.tower[1-a][b].pop(0)
def final(a):
    if a == 0:
        b = '蓝色方获胜！！'
    else:
        b = '红色方获胜！！'
    printf(b)
    varg1.set('开始结算')
def cal_game():
    mvp = game.cal_mvp()
    a = game.ch[mvp]
    printf('MVP的得主是：' + a.name)
    printf('在比赛中完成了：' + str(a.kda[0]) + '杀' + str(a.kda[1]) + '死' + str(a.kda[2]) + '助攻')
    printf('总英雄伤害：' + str(int(a.dtc)))
    printf('总建筑伤害：' + str(int(a.dtt)))
    printf('总吸收伤害：' + str(int(a.dtd)))
    printf('总控制时间：' + str(int(a.ctc)))
def move(ch, tmb):#num号玩家移动到tmb位置
    printf(ch.name+'移动到'+['上路','中路','下路'][tmb])
    a = ch.tmb_flag
    b = ch.num
    bgc[b].grid_forget()
    hpb[b].grid_forget()
    if b <5:
        game.ps[a].pop(game.ps[a].index(b))
        game.ps[tmb].append(b)
        # bgc[b].grid(row=11 - game.ps[tmb].index(b) * 2, column=3 + 2 * tmb)
        # hpb[b].grid(row=10 - game.ps[tmb].index(b) * 2, column=3 + 2 * tmb)
    else:
        game.ps[a+3].pop(game.ps[a+3].index(b))
        game.ps[tmb+3].append(b)
        # bgc[b].grid(row=15 + game.ps[tmb+3].index(b) * 2, column=3 + 2 * tmb)
        # hpb[b].grid(row=14 + game.ps[tmb+3].index(b) * 2, column=3 + 2 * tmb)
    if ch.tpcd == 0:
        ch.busy += 3
        ch.tpcd += 70
    else:
        ch.busy += 12
    ch.tmb_flag = tmb
    recoverbb()
def damage_behave(ch):
    if search_target(ch) <10:
        target = game.ch[search_target(ch)]
        target.hp -= ch.damage*18/(18+target.defence-ch.through)
        ch.dtc +=ch.damage*18/(18+target.defence-ch.through)
        target.dtd +=ch.damage
        ch.busy += ch.speed
        if target.hp <= 0:
            printf(ch.name+'击杀'+target.name)
            ch.kda[0]+=1
            target.kda[1]+=1
            ch.kda[2]-=1
            if ch.num<5:
                for i in range(len(game.ps[ch.tmb_flag])):
                    n = game.ps[ch.tmb_flag][i]
                    game.ch[n].kda[2]+=1
                    game.ch[n].money+=50
            else:
                for i in range(len(game.ps[ch.tmb_flag+3])):
                    n = game.ps[ch.tmb_flag+3][i]
                    game.ch[n].kda[2]+=1
                    game.ch[n].money += 50
            dead(target)
            ch.money += 150
    else:
        hit_tower(ch)
def control_behave(ch):
    if ch.controlcd <=0:
        if search_target(ch) <10:
            target = game.ch[search_target(ch)]
            target.busy += ch.controltime
            ch.ctc += ch.controltime
            ch.controlcd +=20
            ch.busy+=0.5
        else:
            judgement(ch)
    else:
        judgement(ch)
def viability_behave(ch):
    if ch.hpmax-5*ch.hp>0:
        leave(ch)
        ch.busy+=20
    else:
        ch.hp += ch.healps*7
        ch.busy += 1
def farm_behave(ch):
    if ch.money<50000:
        a = ch.tmb_flag
        if ch.num<5:
            if game.resource[a][0]>0:
                ch.money+=50+int(ch.f/4)
                game.resource[a][0] -= 50
            elif game.resource[a][1]>0:
                game.resource[a][1] -= 50
            elif game.resource[a][2]>0:
                game.resource[a][2] -= 100
                ch.money +=100+int(ch.f/2)
                ch.busy += ch.speed*2
        else:
            if game.resource[a][1]>0:
                ch.money+=50+int(ch.f/4)
                game.resource[a][1] -= 50
            elif game.resource[a][0]>0:
                game.resource[a][0] -= 50
            elif game.resource[a][2]>0:
                game.resource[a][2] -= 100
                ch.money +=100+int(ch.f/2)
                ch.busy += ch.speed*2
        ch.busy += ch.speed
    else:
        damage_behave(ch)
    ch.cal()
#开启游戏按钮
bg2 = Button(frame_game, textvariable = varg1, command = play)
bg2.grid(row =0, column =1)
bgc = []#角色按钮
hpb = []#血条
thpb = []
for i in range(3):
    thpb.append(Hpbar(frame_game,fg ='yellow'))
#罗嗦的一段
def btm_player():
    def checkch0():
        game.sc =0
        refreshbb()
    def checkch1():
        game.sc =1
        refreshbb()
    def checkch2():
        game.sc =2
        refreshbb()
    def checkch3():
        game.sc =3
        refreshbb()
    def checkch4():
        game.sc =4
        refreshbb()
    def checkch5():
        game.sc =5
        refreshbb()
    def checkch6():
        game.sc =6
        refreshbb()
    def checkch7():
        game.sc =7
        refreshbb()
    def checkch8():
        game.sc =8
        refreshbb()
    def checkch9():
        game.sc =9
        refreshbb()
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
btm_player()
for i in range(10):
    hpb.append(Hpbar(frame_game))
b_midline =[]
#中线label
var_midline = []
for i in range(4):
    var_midline.append(StringVar())
    b_midline.append(Button(frame_game, textvariable=var_midline[i],bg ='grey'))
#时间label
varg3 = StringVar()
lg2 = Label(frame_game,textvariable =varg3).grid(row =1,column =2,columnspan = 6)
#状态栏label
l_state = []
e_state = []
var_state =[]
for i in range(7):
    var_state.append(StringVar())
    e_state.append(Entry(frame_game_state, textvariable=var_state[i], state ='disabled'))
    l_state.append(Label(frame_game_state,text =['姓名','KDA','经济','伤害','穿透','防御','恢复'][i]))
#msg
var_msg = []
m_game = []
for i in range(10):
    var_msg.append(StringVar())
    var_msg[i].set('~~~~~~~')
    m_game.append(Message(frame_game_msg,bg = "white",width = 300,textvariable =var_msg[i]))
#倍速
def gospeed():
    if bg5['text']=='1倍速':
        game.gospeed = 50
        bg5['text'] = '2倍速'
    elif bg5['text']=='2倍速':
        game.gospeed = 20
        bg5['text'] = '5倍速'
    elif bg5['text'] == '5倍速':
        game.gospeed = 10
        bg5['text'] = '10倍速'
    elif bg5['text'] == '10倍速':
        game.gospeed = 100
        bg5['text'] = '1倍速'
bg5 =Button(frame_game,text ='1倍速',command=gospeed)
bg5.grid(row =0, column =3)
def pushmin():
    for i in range(600):
        if varg1.get() == '开始结算':
            break
        else:
            refreshgame()
    recoverbb()
    refreshbb()
#加速
bg3 =Button(frame_game,text ='推进1分钟', state= 'disabled' ,command=pushmin)#
bg3.grid(row =0, column =5)
#结束游戏
bg4 =Button(frame_game, text ='结束游戏', state= 'disabled',command= end_game)
bg4.grid(row =0, column =7)
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


