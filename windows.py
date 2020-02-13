from tkinter import *
from support import *
#开头
win =Tk()
win.geometry('800x600')
win.title('这不是LOL')
club = Club()#初始化俱乐部
state = State
market = Market()
market.creat()
#初始化各个界面
frame = []
frame_root =Frame(win)
frame_root.pack()
frame_mkt =Frame(win)
frame_club =Frame(win)
frame = [frame_root, frame_mkt, frame_club]
lr1 = Label(frame_root, text = "资金：").grid(row = 0, column = 0)
lr2 = Label(frame_root, textvariable = club.money).grid(row = 0, column = 1)
def donate():
    club.money.set(club.money.get()+50000)
    print('%s俱乐部获得来自土豪粉丝的5w赞助！')
br2 = Button(frame_root, text = '拉赞助', command = donate)
br2.grid(row =0 ,column = 2)
#页面刷新
def refresh_win(f):
    if f == frame_mkt:
        lbm.delete(0, END)
        for i in range(len(market.player)):
            lbm.insert('end', market.player[i].name)
    elif f == frame_club:
        lbc.delete(0, END)
        for i in range(len(club.player)):
            lbc.insert('end', club.player[i].name)

#页面转换
def change_win(f):
    refresh_win(f)
    for i in range(len(frame)):
        frame[i].pack_forget()
    f.pack()

br1 = Button(frame_root, text ='交易市场', command = lambda :change_win(frame_mkt))
br1.grid(row = 1, column = 1)
#市场按钮
bm1 = Button(frame_mkt,
             text = '返回',
             command = lambda :change_win(frame_root))
bm1.grid(row =0, column =0)
#俱乐部按钮
def change_win_club():
    lbc.delete(0,END)
    for i in range(len(club.player)):
        lbc.insert('end', club.player[i].name)
    for i in range(len(frame)):
        frame[i].pack_forget()
    frame_club.pack()
br3 =Button(frame_root, text = "俱乐部", command = lambda :change_win(frame_club))
br3.grid(row = 1, column = 0)

#选手市场部分
lm1 = Label(frame_mkt,
            text = '自由市场选手').grid(row = 1, column =0, columnspan =2)
lbm = Listbox(frame_mkt)
lbm.grid(row = 2, columnspan = 2)
for i in range(len(market.player)):
    lbm.insert('end',market.player[i].name)
def checkm():
    if lbm.curselection() != ():
        value = lbm.get(lbm.curselection())
        for ii in range(len(market.player)):
            if market.player[ii].name == value:
                i =ii
        varm1[0].set(market.player[i].name)
        varm1[1].set(market.player[i].damage)
        varm1[2].set(market.player[i].control)
        varm1[3].set(market.player[i].viability)
        varm1[4].set(market.player[i].develop)
        varm1[5].set(market.player[i].carry)
        varm1[6].set(market.player[i].support)
        varm1[7].set(market.player[i].fans)
bm2 = Button(frame_mkt,
             text = '查看详情',
             command = checkm)
bm2.grid(row = 0, column =1)
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

bm3 = Button(frame_mkt, text = '购买选手', command = buy_player)
bm3.grid(row = 0, column = 2)


#俱乐部部分

bc1 = Button(frame_club,
             text = '返回',
             command = lambda :change_win(frame_root))
bc1.grid(row =0, column = 0)

lbc = Listbox(frame_club)#选手列表
lbc.grid(row = 2, columnspan = 2)

def checkc():
    i = 0
    if lbc.curselection() != ():
        value = lbc.get(lbc.curselection())
        for ii in range(len(club.player)):
            if club.player[ii].name == value:
                i = ii
        varc1[0].set(club.player[i].name)
        varc1[1].set(club.player[i].damage)
        varc1[2].set(club.player[i].control)
        varc1[3].set(club.player[i].viability)
        varc1[4].set(club.player[i].develop)
        varc1[5].set(club.player[i].carry)
        varc1[6].set(club.player[i].support)
        varc1[7].set(club.player[i].fans)
        bc3.grid(row=3, column=2)
bc2 = Button(frame_club,
             text = '查看详情',
             command = checkc)
bc2.grid(row = 0, column = 1)
lc2 = []
lc2.append(Label(frame_club, text='姓名：').grid(row =3, column =0))
lc2.append(Label(frame_club, text='伤害能力：').grid(row =4, column =0))
lc2.append(Label(frame_club, text='控制能力：').grid(row =5, column =0))
lc2.append(Label(frame_club, text='生存能力：').grid(row =6, column =0))
lc2.append(Label(frame_club, text='发育能力：').grid(row =7, column =0))
lc2.append(Label(frame_club, text='核心能力：').grid(row =8, column =0))
lc2.append(Label(frame_club, text='辅助能力：').grid(row =9, column =0))
lc2.append(Label(frame_club, text='粉丝数目：').grid(row =10, column =0))
varc1 = []
ec1 = []
for i in range(8):
    varc1.append(StringVar())
    varc1[i].set('')
    ec1.append(Entry(frame_club, textvariable = varc1[i], state = 'disabled'))
    ec1[i].grid(row =i+3, column =1)
#改名字
varc2 = StringVar()
varc2.set('修改姓名')
def change_name():
    the_one = 0
    if varc2.get() == '修改姓名':
        if lbc.curselection() != ():
            value = lbc.get(lbc.curselection())
            for i in range(len(club.player)):
                if club.player[i].name == value:
                    the_one = i
            lbc['state'] = 'disabled'
            ec1[0]['state'] = 'normal'
            varc2.set('确定修改')
    else:
        club.player[the_one].name = varc1[0].get()
        lbc['state'] = 'normal'
        ec1[0]['state'] = 'disabled'
        varc2.set('修改姓名')
        refresh_win(frame_club)

bc3 = Button(frame_club, textvariable = varc2, command = change_name)#改名按钮


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




win.mainloop()


