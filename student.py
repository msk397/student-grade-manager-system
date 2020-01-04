import  wx
from matplotlib import pyplot as plt
class student(wx.App):
    num=None
    def __init__(self, a):
        super(student, self).__init__()
        student.num=a

    def resizebmp(self,image, width, height):  # 图片的转换,限定图片大小 实现缩放
        bmp = image.Scale(width, height).ConvertToBitmap()  # 按照比例缩放
        return bmp

    def grade(self):
        a = student.num
        sql = "select name,course1,course2,course3,sum from grade where num = %s;" % (a)
        from login import conncet
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        row = cr.fetchone()
        self.nameText.SetValue(row[0])
        self.course1Text.SetValue(str(row[1]))
        self.course2Text.SetValue(str(row[2]))
        self.course3Text.SetValue(str(row[3]))
        self.sumText.SetValue(str(row[4]))
        self.numText.SetValue(a)
        good, mid, pa, nopa = 0, 0, 0, 0
        for i in range(1, 4):
            if row[i] >= 85:
                good += 1
            elif row[i] >= 70:
                mid += 1
            elif row[i] >= 60:
                pa += 1
            else:
                nopa += 1
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        labels = [u'优秀', u'中等', u'及格', u'不及格']
        x = [good, mid, pa, nopa]
        colors = ['r', 'g', 'y', 'b']  # 自定义颜色列表
        if good == 0:
            labels.remove(u'优秀')
            x.remove(good)
        if mid == 0:
            labels.remove(u'中等')
            x.remove(mid)
        if pa == 0:
            labels.remove(u'及格')
            x.remove(pa)
        if nopa == 0:
            labels.remove(u'不及格')
            x.remove(nopa)
        pat = "./pic/save.png"
        plt.pie(x, labels=labels, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
        plt.axis('equal')  # 设为标准圆
        plt.savefig(pat)
        plt.close()
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(0, 20))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))

     # 修改密码
    def alterpass(self, event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        sql = "select password from student where username = %s;" % (student.num)
        cr.execute(sql)
        res = cr.fetchone()
        a = res[0]
        if a != self.oldText.GetValue():
            wx.MessageBox('旧密码错误', 'error', wx.OK | wx.ICON_ERROR)
            self.oldText.SetValue("")
            self.newText.SetValue("")
            self.conNewText.SetValue("")
        else:
            if self.conNewText.GetValue() == self.newText.GetValue():
                sql = "update student set pass = %s where username = %s;" % (self.newText.GetValue(), student.num)
                cr.execute(sql)
                db.commit()
                wx.MessageBox("密码修改成功", '提示', wx.OK | wx.ICON_INFORMATION)
                self.oldText.SetValue("")
                self.newText.SetValue("")
                self.conNewText.SetValue("")
            else:
                wx.MessageBox('两次新密码输入不一致', 'error', wx.OK | wx.ICON_ERROR)
                self.oldText.SetValue("")
                self.newText.SetValue("")
                self.conNewText.SetValue("")

    #修改密码界面
    def alterPass(self, event):
            self.alterpassFrame = wx.Frame(None, title="修改密码", size=(350, 250), pos=(500, 120))
            self.alterpassFrame.SetMaxSize((350, 250))
            self.alterpassFrame.SetMinSize((350, 250))
            self.alterpassPanel = wx.Panel(self.alterpassFrame, -1, size=(549, 260))
            self.alterpassPanel.SetBackgroundColour("white")
            img = wx.Image("./pic/mi1.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
            # 设置图片在panel中的位置
            self.staticbmp = wx.StaticBitmap(self.alterpassPanel, -1, img, pos=(0, 140))
            # 调用函数设置图片的大小
            myimg = wx.Image("./pic/mi1.png", wx.BITMAP_TYPE_ANY)
            self.staticbmp.SetBitmap(self.resizebmp(myimg, 76, 72))
            img = wx.Image("./pic/mi2.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
            # 设置图片在panel中的位置
            self.staticbmp = wx.StaticBitmap(self.alterpassPanel, -1, img, pos=(257, 140))
            # 调用函数设置图片的大小
            myimg = wx.Image("./pic/mi2.png", wx.BITMAP_TYPE_ANY)
            self.staticbmp.SetBitmap(self.resizebmp(myimg, 76, 72))
            self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
            self.alterpassFrame.SetIcon(self.icon)
            self.oldLabel = wx.StaticText(self.alterpassPanel, -1, "旧密码", pos=(45, 30))
            self.oldText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 30), size=(150, 20), style=wx.TE_PASSWORD)
            self.newLabel = wx.StaticText(self.alterpassPanel, -1, "新密码", pos=(45, 70))
            self.newText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 70), size=(150, 20), style=wx.TE_PASSWORD)
            self.conNewLabel = wx.StaticText(self.alterpassPanel, -1, "确认新密码", pos=(45, 110))
            self.conNewText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 110), size=(150, 20), style=wx.TE_PASSWORD)
            self.button = wx.Button(self.alterpassPanel, -1, "确  定", size=(100, 25), pos=(125, 160))
            self.alterpassFrame.Bind(wx.EVT_BUTTON, self.alterpass, self.button)
            self.alterpassFrame.Show()

    def frame(self):
        self.studentFrame = wx.Frame(None, title="学生界面", size=(840, 300), pos=(300, 100))
        self.studentFrame.SetMaxSize((840, 300))
        self.studentFrame.SetMinSize((840, 300))
        self.studentPanel = wx.Panel(self.studentFrame, -1, size=(500, 300))
        self.studentPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.studentFrame.SetIcon(self.icon)
        self.numLabel = wx.StaticText(self.studentPanel, -1, "学   号", pos=(55, 30))
        self.numText = wx.TextCtrl(self.studentPanel, -1, pos=(110, 30), size=(90, 20), style=wx.TE_READONLY)
        self.nameLabel = wx.StaticText(self.studentPanel, -1, "姓   名", pos=(55, 90))
        self.nameText = wx.TextCtrl(self.studentPanel, -1, pos=(110, 90), size=(90, 20), style=wx.TE_READONLY)
        self.course1Label = wx.StaticText(self.studentPanel, -1, "语文成绩", pos=(255, 30))
        self.course1Text = wx.TextCtrl(self.studentPanel, -1, pos=(365, 30), size=(50, 20), style=wx.TE_READONLY)
        self.course2Label = wx.StaticText(self.studentPanel, -1, "数学成绩", pos=(255, 90))
        self.course2Text = wx.TextCtrl(self.studentPanel, -1, pos=(365, 90), size=(50, 20), style=wx.TE_READONLY)
        self.course3Label = wx.StaticText(self.studentPanel, -1, "英语成绩", pos=(255, 150))
        self.course3Text = wx.TextCtrl(self.studentPanel, -1, pos=(365, 150), size=(50, 20), style=wx.TE_READONLY)
        self.sumLabel = wx.StaticText(self.studentPanel, -1, "总成绩", pos=(255, 210))
        self.sumText = wx.TextCtrl(self.studentPanel, -1, pos=(365, 210), size=(50, 20), style=wx.TE_READONLY)
        self.alterPassButton = wx.Button(self.studentPanel, -1, "修改密码", size=(100, 25), pos=(90, 150))
        self.studentFrame.Bind(wx.EVT_BUTTON, self.alterPass, self.alterPassButton)
        self.panel = wx.Panel(self.studentFrame, -1, size=(340, 300), pos=(501, 0))
        self.panel.SetBackgroundColour("white")
        self.show = wx.StaticText(self.panel, -1,"您的成绩分布如下图", pos=(100, 0))
        pat = "./pic/student.png"
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.studentPanel, -1, img, pos=(0, 130))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 90, 134))
        self.grade()
        self.studentFrame.Show()