import os
import  wx
from xlrd import open_workbook
from xlwt import Workbook
from matplotlib import pyplot as plt

class teacher(wx.App):
    num=None
    def __init__(self,a):
        super(teacher, self).__init__()
        teacher.num=a

    def resizebmp(self,image, width, height):  # 图片的转换,限定图片大小 实现缩放
        bmp = image.Scale(width, height).ConvertToBitmap()  # 按照比例缩放
        return bmp
    #主界面
    def frame(self):
        self.teacherFrame = wx.Frame(None, title=u"学生成绩管理系统", size=(700, 500), pos=(300, 200))
        self.teacherFrame.SetMaxSize((700, 500))
        self.teacherFrame.SetMinSize((700, 500))
        self.teacherPanel = wx.Panel(self.teacherFrame, -1, size=(750, 500))
        img = wx.Image("./pic/teacher.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.teacherPanel, -1, img, pos=(0, 0))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/teacher.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg,700,450))
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.teacherFrame.SetIcon(self.icon)

        self.menubar = wx.MenuBar()

        self.menu3 = wx.Menu()
        self.item5 = wx.MenuItem(self.menu3, wx.ID_ANY, u"根据学号查询", wx.EmptyString, wx.ITEM_NORMAL)
        self.item6 = wx.MenuItem(self.menu3, wx.ID_ANY, u"根据姓名查询", wx.EmptyString, wx.ITEM_NORMAL)
        self.item10 = wx.MenuItem(self.menu3, wx.ID_ANY, u"根据班级查询", wx.EmptyString, wx.ITEM_NORMAL)
        self.item7 = wx.MenuItem(self.menu3, wx.ID_ANY, u"根据科目查询", wx.EmptyString, wx.ITEM_NORMAL)
        self.item9 = wx.MenuItem(self.menu3, wx.ID_ANY, u"根据总分数查询", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu3.Append(self.item5)
        self.menu3.Append(self.item6)
        self.menu3.Append(self.item7)
        self.menu3.Append(self.item9)
        self.menu3.Append(self.item10)
        self.menubar.Append(self.menu3, u"查询成绩")

        self.menu2 = wx.Menu()
        self.item3 = wx.MenuItem(self.menu2, wx.ID_ANY, u"修改成绩", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu2.Append(self.item3)
        self.menubar.Append(self.menu2, u"修改成绩")



        self.menu4 = wx.Menu()
        self.item12 = wx.MenuItem(self.menu4, wx.ID_ANY, u"删除成绩", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu4.Append(self.item12)
        self.menubar.Append(self.menu4, u"删除成绩")

        self.menu1 = wx.Menu()
        self.item1 = wx.MenuItem(self.menu1, wx.ID_ANY, u"Excel导入", wx.EmptyString, wx.ITEM_NORMAL)
        self.item2 = wx.MenuItem(self.menu1, wx.ID_ANY, u"手动输入", wx.EmptyString, wx.ITEM_NORMAL)
        self.item8 = wx.MenuItem(self.menu1, wx.ID_ANY, u"成绩导出", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu1.Append(self.item1)
        self.menu1.Append(self.item2)
        self.menu1.Append(self.item8)
        self.menubar.Append(self.menu1, u"导入/导出成绩")


        self.menu5 = wx.Menu()
        self.item11 = wx.MenuItem(self.menu5, wx.ID_ANY, u"修改密码", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu5.Append(self.item11)
        self.menubar.Append(self.menu5, u"其它")
        self.teacherFrame.SetMenuBar(self.menubar)

        self.teacherFrame.Bind(wx.EVT_MENU, self.fileIn, id=self.item1.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.head, id=self.item2.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.numAlter, id=self.item3.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.numSelect, id=self.item5.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.nameSelect, id=self.item6.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.courseSelect, id=self.item7.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.sumSelect, id=self.item9.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.classSelect, id=self.item10.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.out, id=self.item8.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.alterPass, id=self.item11.GetId())
        self.teacherFrame.Bind(wx.EVT_MENU, self.numDelete, id=self.item12.GetId())
        self.teacherFrame.Show()


    # 判断是否导入重复
    def pd(self,str):
        sql = "select num from grade;"
        from login import conncet
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        results = cr.fetchall()
        for row in results:
            if row[0] == str:
                return True
        return False
    #从文件导入
    def fileIn(self, event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        wild = 'Excel 文件(*.xls,*.xlsx)|*.*'
        dialog = wx.FileDialog(None, '选择Excel文件', os.getcwd(), '', wild, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            fileName = os.path.basename(dialog.GetPath())
            ExcelFile = open_workbook(dialog.GetPath())
            sheet = ExcelFile.sheet_by_index(0)
            row = sheet.nrows
            for i in range(1, row):
                a = str("%.0f" % float(sheet.cell(i, 0).value))
                if self.pd(a):
                    d = float(sheet.cell(i, 3).value)
                    e = float(sheet.cell(i, 4).value)
                    f = float(sheet.cell(i, 5).value)
                    if self.Select(a, "course1") >= 0 and self.Select(a, "course2")>=0 and self.Select(a, "course3")>=0:
                        wx.MessageBox('学号为' + a + '的同学，其全部成绩已登入数据库，请勿重复添加', 'error', wx.OK | wx.ICON_ERROR)
                    if self.Select(a, "course1") >= 0 and d > 0:
                        wx.MessageBox('学号为'+a+'的同学，语文成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                        d = self.Select(a, "course1")
                    if self.Select(a, "course2") >= 0 and e > 0:
                        wx.MessageBox('学号为'+a+'的同学，数学成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                        e = self.Select(a, "course2")
                    if self.Select(a, "course3") >= 0 and f > 0:
                        wx.MessageBox('学号为'+a+'的同学，英语成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                        f = self.Select(a, "course3")
                    if d < 0:
                        d = -1
                    if e < 0:
                        e = -1
                    if f < 0:
                        f = -1
                    g = 0
                    if d > 0:
                        g = g + d
                    if e > 0:
                        g = g + e
                    if f > 0:
                        g = g + f
                    sql = "UPDATE grade SET course1=%.2f,course2=%.2f,course3=%.2f,sum=%.2f WHERE num= %s;" % (d, e, f, g, a)
                    cr.execute(sql)
                    db.commit()
                    continue
                b = str(sheet.cell(i, 1).value)
                c = str(sheet.cell(i, 2).value)
                d = float(sheet.cell(i, 3).value)
                e = float(sheet.cell(i, 4).value)
                f = float(sheet.cell(i, 5).value)
                if d<0:
                    d=-1
                if e<0:
                    e=-1
                if f<0:
                    f=-1
                g=0
                if d>0:
                    g=g+d
                if e>0:
                    g=g+e
                if f>0:
                    g=g+f
                sql = "INSERT INTO grade (num, name, class,course1,course2,course3,sum) VALUES ( '%s', '%s','%s', %.2f,%.2f,%.2f,%.2f);" % (a, b, c, d, e, f, g)
                cr.execute(sql)
                db.commit()
                sql = "insert into student (username,password,name) values ('%s','123456','%s');" % (a, b)
                cr.execute(sql)
                db.commit()
            wx.MessageBox("已从" + fileName + "文件导入！", '导入成功', wx.OK | wx.ICON_INFORMATION)
            dialog.Destroy()


    # 手动输入
    def add(self,event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        try:
            a = str("%.0f" % float(self.numText.GetValue().strip()))
            if self.pd(a):
                d = float(self.course1Text.GetValue())
                e = float(self.course2Text.GetValue())
                f = float(self.course3Text.GetValue())
                if self.Select(a, "course1") >= 0 and self.Select(a, "course2")>=0 and self.Select(a, "course3")>=0:
                    wx.MessageBox('学号为' + a + '的同学，其全部成绩已登入数据库，请勿重复添加', 'error', wx.OK | wx.ICON_ERROR)
                if self.Select(a, "course1") >= 0 and d > 0:
                    wx.MessageBox('学号为' + a + '的同学，语文成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    d = self.Select(a, "course1")
                if self.Select(a, "course2") >= 0 and e > 0:
                    wx.MessageBox('学号为' + a + '的同学，数学成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    e = self.Select(a, "course2")
                if self.Select(a, "course3") >= 0 and f > 0:
                    wx.MessageBox('学号为' + a + '的同学，英语成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    f = self.Select(a, "course3")
                if d < 0:
                    d = -1
                if e < 0:
                    e = -1
                if f < 0:
                    f = -1
                g = 0
                if d > 0:
                    g = g + d
                if e > 0:
                    g = g + e
                if f > 0:
                    g = g + f
                sql = "UPDATE grade SET course1=%.2f,course2=%.2f,course3=%.2f,sum=%.2f WHERE num= %s;" % (d, e, f, g, a)
                cr.execute(sql)
                db.commit()
            else:
                b = str(self.nameText.GetValue().strip())
                c = str(self.classText.GetValue().strip())
                d = float(self.course1Text.GetValue())
                e = float(self.course2Text.GetValue())
                f = float(self.course3Text.GetValue())
                if self.Select(a,"course1")>=0 and d>0:
                    wx.MessageBox('course1成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    d=-1
                if self.Select(a,"course1")>=0 and d<0:
                    d=self.Select(a,"course1")
                if self.Select(a,"course2")>=0 and e>0:
                    wx.MessageBox('course2成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    e=-1
                if self.Select(a,"course2")>=0 and e<0:
                    e=self.Select(a,"course2")
                if self.Select(a,"course3")>=0 and f>0:
                    wx.MessageBox('course3成绩已存在，若想修改请前往修改页面', 'error', wx.OK | wx.ICON_ERROR)
                    f=-1
                if self.Select(a,"course3")>=0 and f<0:
                    f=self.Select(a,"course3")
                if d<0:
                    d=-1
                if e<0:
                    e=-1
                if f<0:
                    f=-1
                g = 0
                if d > 0:
                    g = g + d
                if e > 0:
                    g = g + e
                if f > 0:
                    g = g + f
                data = (a, b, c, d, e, f, g)
                sql = "INSERT INTO grade (num, name, class,course1,course2,course3,sum) VALUES ( '%s', '%s','%s', %.2f,%.2f,%.2f,%.2f);" % data
                cr.execute(sql)
                db.commit()
                if not self.pd(a):
                  data = (a, b)
                  sql = "insert into student (username,password,name) values ('%s','123456','%s');" % data
                  cr.execute(sql)
                  db.commit()
                wx.MessageBox("导入成功", '导入成功', wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
                wx.MessageBox('输入不合法，请重新输入', '错误', wx.OK | wx.ICON_ERROR)
        finally:
                self.numText.SetValue("")
                self.nameText.SetValue("")
                self.classText.SetValue("")
                self.course3Text.SetValue(-1)
                self.course1Text.SetValue(-1)
                self.course2Text.SetValue(-1)
    #查询学号为a，科目b
    def Select(self,a, b):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        sql = "select %s from grade where num = %s;" % (b, a)
        cr.execute(sql)
        res = cr.fetchone()
        if res == None:
            return -1
        return res[0]
    #手动添加页面
    def head(self, event):
        self.headFrame = wx.Frame(None, title="手动添加", size=(350, 300), pos=(500, 100))
        self.headFrame.SetMaxSize((350,300))
        self.headFrame.SetMinSize((350, 300))
        self.headPanel = wx.Panel(self.headFrame, -1, size=(350, 300))
        self.headPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.headFrame.SetIcon(self.icon)
        img = wx.Image("./pic/addGrade2.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.headPanel, -1, img, pos=(-5, 195))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/addGrade2.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 76, 76))

        img = wx.Image("./pic/addGrade1.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.headPanel, -1, img, pos=(262, 195))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/addGrade1.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 76, 76))
        self.tipLabel = wx.StaticText(self.headPanel, -1, "成绩小于零，则不添加该科成绩", pos=(80, 5))
        self.numLabel = wx.StaticText(self.headPanel, -1, "学   号", pos=(30, 30))
        self.nameLabel = wx.StaticText(self.headPanel, -1, "姓   名", pos=(30, 60))
        self.classLabel = wx.StaticText(self.headPanel, -1, "班   级", pos=(30, 90))
        self.course1Label = wx.StaticText(self.headPanel, -1, "语文成绩", pos=(30, 120))
        self.course2Label = wx.StaticText(self.headPanel, -1, "数学成绩", pos=(30, 150))
        self.course3Label = wx.StaticText(self.headPanel, -1, "英语成绩", pos=(30, 180))
        self.addButton = wx.Button(self.headPanel, -1, "添  加", size=(50, 25), pos=(130, 210))
        self.headFrame.Bind(wx.EVT_BUTTON, self.add, self.addButton)
        self.numText = wx.TextCtrl(self.headPanel, -1, pos=(120, 30), size=(150, 20))
        self.nameText = wx.TextCtrl(self.headPanel, -1, pos=(120, 60), size=(150, 20))
        self.classText = wx.TextCtrl(self.headPanel, -1, pos=(120, 90), size=(150, 20))
        self.course1Text = wx.SpinCtrlDouble(self.headPanel, -1, pos=(120, 120), size=(150, 20))
        self.course1Text.SetRange(-1, 100)
        self.course1Text.SetValue(-1)
        self.course1Text.SetIncrement(1)
        self.course2Text = wx.SpinCtrlDouble(self.headPanel, -1, pos=(120, 150), size=(150, 20))
        self.course2Text.SetRange(-1, 100)
        self.course2Text.SetValue(-1)
        self.course2Text.SetIncrement(1)
        self.course3Text = wx.SpinCtrlDouble(self.headPanel, -1, pos=(120, 180), size=(150, 20))
        self.course3Text.SetRange(-1, 100)
        self.course3Text.SetValue(-1)
        self.course3Text.SetIncrement(1)
        self.headFrame.Show()

    #修改成绩
    # 查询姓名为a，科目b的成绩
    def select1(self, a, b):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        sql = "select %s from grade where name = '%s';" % (b, a)
        cr.execute(sql)
        res = cr.fetchone()
        if res == None:
            return -1
        return res[0]
    def pd1(self, a):  # 查询数据库中有几位姓名为a的学生
        from login import conncet
        sql = "select name from grade;"
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        results = cr.fetchall()
        i = 0
        for row in results:
            if row[0] == a:
                i += 1
            else:
                pass
        return i
    def pd2(self,a):#查询数据库中有无学号为a的同学
        from login import conncet
        sql = "select num from grade;"
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        results = cr.fetchall()
        for row in results:
            if row[0] == a:
                return True
            else:
                pass
        return False
    def numalter(self,event):
        if self.rbox.GetStringSelection()=='学       号':
            from login import conncet
            try:
                a = str("%.0f" % float(self.numText.GetValue().strip()))
                if self.pd2(a):
                    if float(self.course1Text.GetValue()) < 0:
                        d=self.Select(a,"course1")
                    else:
                        d = float(self.course1Text.GetValue())
                    if float(self.course2Text.GetValue()) < 0:
                        e=self.Select(a,"course2")
                    else:
                        e = float(self.course2Text.GetValue())
                    if float(self.course3Text.GetValue()) < 0:
                        f=self.Select(a,"course3")
                    else:
                        f = float(self.course3Text.GetValue())
                    g = 0
                    if d > 0:
                        g = g + d
                    if e > 0:
                        g = g + e
                    if f > 0:
                        g = g + f
                    db = conncet()
                    cr = db.cursor()
                    sql = "UPDATE grade SET course1=%.2f,course2=%.2f,course3=%.2f,sum=%.2f WHERE num= %s;" % (d, e, f, g, a)
                    cr.execute(sql)
                    db.commit()
                    wx.MessageBox("修改成功！", '修改成功', wx.OK | wx.ICON_INFORMATION)
                else:
                    wx.MessageBox('成绩表中无此人', 'error', wx.OK | wx.ICON_ERROR)
            except Exception as e:
                wx.MessageBox('输入不合法', 'error', wx.OK | wx.ICON_ERROR)
            finally:
                self.numText.SetValue("")
                self.course1Text.SetValue(-1)
                self.course2Text.SetValue(-1)
                self.course3Text.SetValue(-1)
        else:
            from login import conncet
            try:
                a = str(self.numText.GetValue().strip())
                na = self.pd1(a)
                if na == 1:
                    if float(self.course1Text.GetValue()) < 0:
                        d = self.select1(a, "course1")
                    else:
                        d = float(self.course1Text.GetValue())
                    if float(self.course2Text.GetValue()) < 0:
                        e = self.select1(a, "course2")
                    else:
                        e = float(self.course2Text.GetValue())
                    if float(self.course3Text.GetValue()) < 0:
                        f = self.select1(a, "course3")
                    else:
                        f = float(self.course3Text.GetValue())
                    g = d + e + f
                    db = conncet()
                    cr = db.cursor()
                    sql = "UPDATE grade SET course1=%.2f,course2=%.2f,course3=%.2f,sum=%.2f WHERE name='%s';" % (
                        d, e, f, g, a)
                    cr.execute(sql)
                    db.commit()
                    wx.MessageBox("修改成功！", '修改成功', wx.OK | wx.ICON_INFORMATION)
                elif na == 0:
                    wx.MessageBox('成绩表中无此人', 'error', wx.OK | wx.ICON_ERROR)
                else:
                    na = str(na)
                    wx.MessageBox('有' + na + '位同学叫' + a + ',无法根据姓名修改，请前往学号修改界面', 'error', wx.OK | wx.ICON_ERROR)
            except Exception as e:
                wx.MessageBox('输入不合法', 'error', wx.OK | wx.ICON_ERROR)
            finally:
                self.numText.SetValue("")
                self.course1Text.SetValue(-1)
                self.course2Text.SetValue(-1)
                self.course3Text.SetValue(-1)
    #界面
    def numAlter(self,event):
        self.numAlterFrame = wx.Frame(None, title="修改成绩", size=(450, 250), pos=(500, 120))
        self.numAlterFrame.SetMaxSize((450,250))
        self.numAlterFrame.SetMinSize((350, 250))
        self.numAlterPanel = wx.Panel(self.numAlterFrame, -1, size=(450, 250))
        self.numAlterPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.numAlterFrame.SetIcon(self.icon)
        img = wx.Image("./pic/alter.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.numAlterPanel, -1, img, pos=(0, 130))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/alter.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 70, 92))
        lblList = ['学       号', '姓      名']
        self.rbox = wx.RadioBox(self.numAlterPanel, label='选择删除方式', pos=(25, 20), choices=lblList, majorDimension=1,
                                style=wx.RA_SPECIFY_COLS)
        self.tipLabel = wx.StaticText(self.numAlterPanel, -1, "成绩为-1，默认不修改", pos=(180, 5))
        self.numLabel = wx.StaticText(self.numAlterPanel, -1, "学号或姓名", pos=(145, 30))
        self.numText = wx.TextCtrl(self.numAlterPanel, -1, pos=(230, 30), size=(150, 20))
        self.course1Label = wx.StaticText(self.numAlterPanel, -1, "语文成绩", pos=(145, 60))
        self.course1Text = wx.SpinCtrlDouble(self.numAlterPanel, -1, pos=(230, 60), size=(150, 20))
        self.course1Text.SetRange(-1, 100)
        self.course1Text.SetValue(-1)
        self.course1Text.SetIncrement(1)
        self.course2Label = wx.StaticText(self.numAlterPanel, -1, "数学成绩", pos=(145, 90))
        self.course2Text = wx.SpinCtrlDouble(self.numAlterPanel, -1, pos=(230, 90), size=(150, 20))
        self.course2Text.SetRange(-1, 100)
        self.course2Text.SetValue(-1)
        self.course2Text.SetIncrement(1)
        self.course3Label = wx.StaticText(self.numAlterPanel, -1, "英语成绩", pos=(145, 120))
        self.course3Text = wx.SpinCtrlDouble(self.numAlterPanel, -1, pos=(230, 120), size=(150, 20))
        self.course3Text.SetRange(-1, 100)
        self.course3Text.SetValue(-1)
        self.course3Text.SetIncrement(1)
        self.alterButton = wx.Button(self.numAlterPanel, -1, "修  改", size=(50, 25), pos=(245, 155))
        self.numAlterFrame.Bind(wx.EVT_BUTTON, self.numalter, self.alterButton)
        self.numAlterFrame.Show()


    #根据姓名查询成绩
    def nameselect(self,event):
        from login import conncet
        try:
            a = str(self.nameText.GetValue().strip())
            na = self.pd1(a)
            if na==1:
                sql = "select course1,course2,course3,sum from grade where name = '%s';" % (a)
                db = conncet()
                cr = db.cursor()
                cr.execute(sql)
                row = cr.fetchone()
                self.course1Text.SetValue(str(row[0]))
                self.course2Text.SetValue(str(row[1]))
                self.course3Text.SetValue(str(row[2]))
                self.sumText.SetValue(str(row[3]))
                good, mid, pa, nopa = 0, 0, 0, 0
                for i in range(0, 3):
                    if row[i] >= 85:
                        good += 1
                    elif row[i] >= 70:
                        mid += 1
                    elif row[i] >= 60:
                        pa += 1
                    else:
                        nopa += 1
                self.show.SetValue(a+"同学成绩分布如下")
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
                plt.pie(x,labels=labels, autopct='%1.2f%%',textprops = {'fontsize':20, 'color':'k'},colors = colors)
                plt.axis('equal')#设为标准圆
                plt.savefig(pat)
                plt.close()
                img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
                # 设置图片在panel中的位置
                staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(0, 20))
                # 调用函数设置图片的大小
                myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
                staticbmp.SetBitmap(self.resizebmp(myimg,267,200))
            elif na==0:
                wx.MessageBox('成绩表中无姓名为'+a+'的同学', 'error', wx.OK | wx.ICON_ERROR)
            else:
                na =str(na)
                wx.MessageBox('有' + na + '位同学叫' + a + ',无法根据姓名查询，请前往学号查询界面', 'error', wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox('姓名输入有误', 'error', wx.OK | wx.ICON_ERROR)
    #界面
    def nameSelect(self,event):
        self.nameSelectFrame = wx.Frame(None, title="根据姓名查询", size=(618, 240), pos=(200, 120))
        self.nameSelectFrame.SetMaxSize((618,240))
        self.nameSelectFrame.SetMinSize((618, 240))
        self.nameSelectPanel = wx.Panel(self.nameSelectFrame, -1, size=(350, 300),pos = (0,0))
        self.nameSelectPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.nameSelectFrame.SetIcon(self.icon)
        self.nameLabel = wx.StaticText(self.nameSelectPanel, -1, "姓   名", pos=(5, 30))
        self.nameText = wx.TextCtrl(self.nameSelectPanel, -1, pos=(60, 30), size=(90, 20))
        self.course1Label = wx.StaticText(self.nameSelectPanel, -1, "语文成绩", pos=(165, 15))
        self.course1Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 15), size=(50, 20), style=wx.TE_READONLY)
        self.course2Label = wx.StaticText(self.nameSelectPanel, -1, "数学成绩", pos=(165, 50))
        self.course2Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 50), size=(50, 20), style=wx.TE_READONLY)
        self.course3Label  = wx.StaticText(self.nameSelectPanel, -1, "英语成绩", pos=(165, 85))
        self.course3Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 85), size=(50, 20), style=wx.TE_READONLY)
        self.sumLabel = wx.StaticText(self.nameSelectPanel, -1, "总成绩", pos=(165, 120))
        self.sumText = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 120), size=(50, 20), style=wx.TE_READONLY)
        self.selectButton = wx.Button(self.nameSelectPanel, -1, "查  询", size=(50, 25), pos=(55, 85))
        self.panel = wx.Panel(self.nameSelectFrame, -1, size=(267, 200),pos = (350,0))
        self.panel.SetBackgroundColour("white")
        self.show = wx.TextCtrl(self.panel, -1, pos=(50, 0), size=(160, 20), style=wx.TE_READONLY)
        self.nameSelectFrame.Bind(wx.EVT_BUTTON, self.nameselect, self.selectButton)
        pat = "./pic/login.png"
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.nameSelectPanel, -1, img, pos=(0, 110))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 88, 88))
        self.nameSelectFrame.Show()
        self.nameSelectFrame.Show()


    #根据学号查询成绩
    def selectname(self,a):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        sql = "select name from grade where num = %s;" % (a)
        cr.execute(sql)
        res = cr.fetchone()
        if res == None:
            return -1
        return res[0]
    def numselect(self,event):
        from login import conncet
        try:
            a = str("%.0f" % float(self.nameText.GetValue().strip()))
            if self.pd2(a):
                sql = "select course1,course2,course3,sum from grade where num = %s;" % (a)
                db = conncet()
                cr = db.cursor()
                cr.execute(sql)
                row = cr.fetchone()
                self.course1Text.SetValue(str(row[0]))
                self.course2Text.SetValue(str(row[1]))
                self.course3Text.SetValue(str(row[2]))
                self.sumText.SetValue(str(row[3]))
                good, mid, pa, nopa = 0, 0, 0, 0
                for i in range(0, 3):
                    if row[i] >= 85:
                        good += 1
                    elif row[i] >= 70:
                        mid += 1
                    elif row[i] >= 60:
                        pa += 1
                    else:
                        nopa += 1
                self.show.SetValue("姓名为"+self.selectname(a) + "的同学成绩分布如下")
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
                staticbmp.SetBitmap(self.resizebmp(myimg,267,200))
            else:
                wx.MessageBox('成绩表中无学号为' + a + '的同学', 'error', wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox('学号输入有误', '错误', wx.OK | wx.ICON_ERROR)
    #界面
    def numSelect(self,event):
        self.nameSelectFrame = wx.Frame(None, title="根据学号查询", size=(618, 240), pos=(200, 120))
        self.nameSelectFrame.SetMaxSize((618,240))
        self.nameSelectFrame.SetMinSize((618, 240))
        self.nameSelectPanel = wx.Panel(self.nameSelectFrame, -1, size=(350, 300))
        self.nameSelectPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.nameSelectFrame.SetIcon(self.icon)
        self.nameLabel = wx.StaticText(self.nameSelectPanel, -1, "学    号", pos=(5, 30))
        self.nameText = wx.TextCtrl(self.nameSelectPanel, -1, pos=(60, 30), size=(90, 20))
        self.course1Label = wx.StaticText(self.nameSelectPanel, -1, "语文成绩", pos=(165, 15))
        self.course1Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 15), size=(50, 20), style=wx.TE_READONLY)
        self.course2Label = wx.StaticText(self.nameSelectPanel, -1, "数学成绩", pos=(165, 50))
        self.course2Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 50), size=(50, 20), style=wx.TE_READONLY)
        self.course3Label = wx.StaticText(self.nameSelectPanel, -1, "英语成绩", pos=(165, 85))
        self.course3Text = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 85), size=(50, 20), style=wx.TE_READONLY)
        self.sumLabel = wx.StaticText(self.nameSelectPanel, -1, "总成绩", pos=(165, 120))
        self.sumText = wx.TextCtrl(self.nameSelectPanel, -1, pos=(260, 120), size=(50, 20), style=wx.TE_READONLY)
        self.selectButton = wx.Button(self.nameSelectPanel, -1, "查  询", size=(50, 25), pos=(55, 85))
        self.panel = wx.Panel(self.nameSelectFrame, -1, size=(267, 200), pos=(350, 0))
        self.panel.SetBackgroundColour("white")
        self.show = wx.TextCtrl(self.panel, -1, pos=(0, 0), size=(260, 20), style=wx.TE_READONLY)
        self.nameSelectFrame.Bind(wx.EVT_BUTTON, self.numselect, self.selectButton)
        pat = "./pic/login.png"
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.nameSelectPanel, -1, img, pos=(0, 110))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 88, 88))
        self.nameSelectFrame.Show()


    #根据单科成绩查询
    def courseselect(self,event):
        self.show.SetValue("")
        from login import conncet
        db = conncet()
        cr = db.cursor()
        a = self.rbox.GetStringSelection()
        e= self.rbox1.GetStringSelection()
        dec = {"语   文":"course1","数   学":"course2","英   语":"course3"}
        if e == '降  序':
            sql = "select num,class,name,{0} from grade order by {0} DESC;".format(dec[a])
        else:
            sql = "select num,class,name,{0} from grade order by {0};".format(dec[a])
        # 执行SQL语句
        cr.execute(sql)
        self.show.AppendText("学    号\t\t班   级\t\t姓    名\t\t" + a + "\n")
        # 获取所有记录列表
        results = cr.fetchall()
        good, mid, pa, nopa = 0, 0, 0, 0
        for row in results:
            self.show.AppendText(str(row[0])+"\t\t")
            self.show.AppendText(str(row[1]) + "\t")
            self.show.AppendText(str(row[2]) + "\t\t")
            self.show.AppendText(str(row[3]) + "\t\t")
            if row[3] >= 85:
                good += 1
            elif row[3] >= 70:
                mid += 1
            elif row[3] >= 60:
                pa += 1
            else:
                nopa += 1
        self.show1.SetValue(a + "科目成绩分布如下")
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
        staticbmp.SetBitmap(self.resizebmp(myimg,400,300))
    #界面
    def courseSelect(self,event):
        self.courseFrame = wx.Frame(None, title="根据课程查询", size=(1060, 340), pos=(200, 120))
        self.courseFrame.SetMaxSize((1060,340))
        self.courseFrame.SetMinSize((1060, 340))
        self.coursePanel = wx.Panel(self.courseFrame, -1, size=(700, 300))
        self.coursePanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.courseFrame.SetIcon(self.icon)
        img = wx.Image("./pic/good.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.coursePanel, -1, img, pos=(0, 215))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/good.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 90, 90))
        lbl = ['语   文', '数   学', '英   语']
        lbl1 = ['降  序','升   序']
        self.rbox = wx.RadioBox(self.coursePanel, label='选择课程', pos=(20, 10), choices=lbl,majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.rbox1 = wx.RadioBox(self.coursePanel, label='选择排序', pos=(20, 130), choices=lbl1, majorDimension=1,style=wx.RA_SPECIFY_COLS)
        self.show = wx.TextCtrl(self.coursePanel, -1, pos=(155, 30), size=(490, 210),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.panel = wx.Panel(self.courseFrame, -1, size=(400, 340), pos=(651, 0))
        self.panel.SetBackgroundColour("white")
        self.show1 = wx.TextCtrl(self.panel, -1, pos=(100, 0), size=(200, 20), style=wx.TE_READONLY)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.courseselect)
        self.rbox1.Bind(wx.EVT_RADIOBOX, self.courseselect)
        self.courseFrame.Show()


    #根据总分查询
    def sumselect(self,event):
        from login import conncet
        a = self.rbox.GetStringSelection()
        self.show.SetValue("")
        if a=='降  序':
            sql = "select num,class,name,course1,course2,course3,sum from grade order by sum DESC;"
        else:
            sql = "select num,class,name,course1,course2,course3,sum from grade order by sum;"
        good1, mid1, pa1, nopa1 = 0, 0, 0, 0
        good2, mid2, pa2, nopa2 = 0, 0, 0, 0
        good3, mid3, pa3, nopa3 = 0, 0, 0, 0
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        results = cr.fetchall()
        self.show.AppendText("学    号\t\t班    级\t\t姓    名\t\t语文成绩\t\t数学成绩\t\t英语成绩\t\t总成绩\n")
        for row in results:
            self.show.AppendText(str(row[0]) + "\t\t")
            self.show.AppendText(str(row[1]) + "\t")
            self.show.AppendText(str(row[2]) + "\t\t")
            self.show.AppendText(str(row[3]) + "\t\t")
            self.show.AppendText(str(row[4]) + "\t\t")
            self.show.AppendText(str(row[5]) + "\t\t")
            self.show.AppendText(str(row[6]))
            self.show.AppendText("\n")
            if row[3] >= 85:
                good1 += 1
            elif row[3] >= 70:
                mid1 += 1
            elif row[3] >= 60:
                pa1 += 1
            else:
                nopa1 += 1
            if row[4] >= 85:
                good2 += 1
            elif row[4] >= 70:
                mid2 += 1
            elif row[4] >= 60:
                pa2 += 1
            else:
                nopa2 += 1
            if row[5] >= 85:
                good3 += 1
            elif row[5] >= 70:
                mid3 += 1
            elif row[5] >= 60:
                pa3 += 1
            else:
                nopa3 += 1
        self.show1.SetValue("算法成绩分布如下")
        self.show2.SetValue("数学成绩分布如下")
        self.show3.SetValue("英语成绩分布如下")
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        labels1 = [u'优秀', u'中等', u'及格', u'不及格']
        x1 = [good1, mid1, pa1, nopa1]
        colors = ['r', 'g', 'y', 'b']  # 自定义颜色列表
        if good1 == 0:
            labels1.remove(u'优秀')
            x1.remove(good1)
        if mid1 == 0:
            labels1.remove(u'中等')
            x1.remove(mid1)
        if pa1 == 0:
            labels1.remove(u'及格')
            x1.remove(pa1)
        if nopa1 == 0:
            labels1.remove(u'不及格')
            x1.remove(nopa1)
        pat = "./pic/save1.png"
        plt.pie(x1, labels=labels1, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
        plt.axis('equal')  # 设为标准圆
        plt.savefig(pat)
        plt.close()
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(0, 40))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg,320,240))
        labels2 = [u'优秀', u'中等', u'及格', u'不及格']
        x2 = [good2, mid2, pa2, nopa2]
        if good2 == 0:
            labels2.remove(u'优秀')
            x2.remove(good2)
        if mid2 == 0:
            labels2.remove(u'中等')
            x2.remove(mid2)
        if pa2 == 0:
            labels2.remove(u'及格')
            x2.remove(pa2)
        if nopa2 == 0:
            labels2.remove(u'不及格')
            x2.remove(nopa2)
        pat = "./pic/save2.png"
        plt.pie(x2, labels=labels2, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
        plt.axis('equal')  # 设为标准圆
        plt.savefig(pat)
        plt.close()
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(330, 40))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))
        labels3 = [u'优秀', u'中等', u'及格', u'不及格']
        x3 = [good3, mid3, pa3, nopa3]
        if good3 == 0:
            labels3.remove(u'优秀')
            x3.remove(good3)
        if mid3 == 0:
            labels3.remove(u'中等')
            x3.remove(mid3)
        if pa3 == 0:
            labels1.remove(u'及格')
            x1.remove(pa3)
        if nopa3 == 0:
            labels3.remove(u'不及格')
            x3.remove(nopa3)
        pat = "./pic/save3.png"
        plt.pie(x3, labels=labels3, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
        plt.axis('equal')  # 设为标准圆
        plt.savefig(pat)
        plt.close()
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(660, 40))
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))
    #界面
    def sumSelect(self,event):
        self.sumFrame = wx.Frame(None, title="根据总分输出", size=(1005, 600), pos=(200, 20))
        self.sumFrame.SetMaxSize((1005,600))
        self.sumFrame.SetMinSize((1005, 600))
        self.sumPanel = wx.Panel(self.sumFrame, -1, size=(900, 300))
        self.sumPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.sumFrame.SetIcon(self.icon)
        img = wx.Image("./pic/good.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.sumPanel, -1, img, pos=(0, 0))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/good.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 100, 100))
        self.show = wx.TextCtrl(self.sumPanel, -1, pos=(180, 30), size=(790, 220),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.sumFrame.Show()
        lbl = ['升   序','降  序']
        self.rbox = wx.RadioBox(self.sumPanel, label='选择排序', pos=(20, 120), choices=lbl, majorDimension=1,
                                style=wx.RA_SPECIFY_COLS)
        self.panel = wx.Panel(self.sumFrame, -1, size=(1005, 340), pos=(0, 281))
        self.panel.SetBackgroundColour("white")
        self.show1 = wx.TextCtrl(self.panel, -1, pos=(80, 0), size=(130, 20), style=wx.TE_READONLY)
        self.show2 = wx.TextCtrl(self.panel, -1, pos=(400, 0), size=(150, 20), style=wx.TE_READONLY)
        self.show3 = wx.TextCtrl(self.panel, -1, pos=(720, 0), size=(150, 20), style=wx.TE_READONLY)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.sumselect)


    #根据班级查询
    def classelect(self,event):
        from login import conncet
        try:
            self.show.SetValue("")
            a = str(self.classText.GetValue().strip())
            e = self.rbox.GetStringSelection()
            if e=="降序":
                sql = "select num,name,course1,course2,course3,sum from grade where class = '%s' order by sum DESC;" % (a)
            else:
                sql = "select num,name,course1,course2,course3,sum from grade where class = '%s' order by sum;" % (a)
            good1, mid1, pa1, nopa1 = 0, 0, 0, 0
            good2, mid2, pa2, nopa2 = 0, 0, 0, 0
            good3, mid3, pa3, nopa3 = 0, 0, 0, 0
            db = conncet()
            cr = db.cursor()
            cr.execute(sql)
            results = cr.fetchall()
            self.show.AppendText("学    号\t\t姓    名\t\t语文成绩\t\t数学成绩\t\t英语成绩\t\t总成绩\n")
            for row in results:
                self.show.AppendText(str(row[0])+"\t\t")
                self.show.AppendText(str(row[1])+"\t\t")
                self.show.AppendText(str(row[2])+"\t\t")
                self.show.AppendText(str(row[3])+"\t\t")
                self.show.AppendText(str(row[4])+"\t\t")
                self.show.AppendText(str(row[5])+"\t\t")
                self.show.AppendText("\n")
                if row[2] >= 85:
                    good1 += 1
                elif row[2] >= 70:
                    mid1 += 1
                elif row[2] >= 60:
                    pa1 += 1
                else:
                    nopa1 += 1
                if row[3] >= 85:
                    good2 += 1
                elif row[3] >= 70:
                    mid2 += 1
                elif row[3] >= 60:
                    pa2 += 1
                else:
                    nopa2 += 1
                if row[4] >= 85:
                    good3 += 1
                elif row[4] >= 70:
                    mid3 += 1
                elif row[4] >= 60:
                    pa3 += 1
                else:
                    nopa3 += 1
            self.show1.SetValue("语文成绩分布如下")
            self.show2.SetValue("数学成绩分布如下")
            self.show3.SetValue("英语成绩分布如下")
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            labels1 = [u'优秀', u'中等', u'及格', u'不及格']
            x1 = [good1, mid1, pa1, nopa1]
            colors = ['r', 'g', 'y', 'b']  # 自定义颜色列表
            if good1 == 0:
                labels1.remove(u'优秀')
                x1.remove(good1)
            if mid1 == 0:
                labels1.remove(u'中等')
                x1.remove(mid1)
            if pa1 == 0:
                labels1.remove(u'及格')
                x1.remove(pa1)
            if nopa1 == 0:
                labels1.remove(u'不及格')
                x1.remove(nopa1)
            pat = "./pic/save1.png"
            plt.pie(x1, labels=labels1, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
            plt.axis('equal')  # 设为标准圆
            plt.savefig(pat)
            plt.close()
            img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
            # 设置图片在panel中的位置
            staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(0, 40))
            # 调用函数设置图片的大小
            myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
            staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))
            labels2 = [u'优秀', u'中等', u'及格', u'不及格']
            x2 = [good2, mid2, pa2, nopa2]
            if good2 == 0:
                labels2.remove(u'优秀')
                x2.remove(good2)
            if mid2 == 0:
                labels2.remove(u'中等')
                x2.remove(mid2)
            if pa2 == 0:
                labels2.remove(u'及格')
                x2.remove(pa2)
            if nopa2 == 0:
                labels2.remove(u'不及格')
                x2.remove(nopa2)
            pat = "./pic/save2.png"
            plt.pie(x2, labels=labels2, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
            plt.axis('equal')  # 设为标准圆
            plt.savefig(pat)
            plt.close()
            img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
            # 设置图片在panel中的位置
            staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(330, 40))
            # 调用函数设置图片的大小
            myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
            staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))
            labels3 = [u'优秀', u'中等', u'及格', u'不及格']
            x3 = [good3, mid3, pa3, nopa3]
            if good3 == 0:
                labels3.remove(u'优秀')
                x3.remove(good3)
            if mid3 == 0:
                labels3.remove(u'中等')
                x3.remove(mid3)
            if pa3 == 0:
                labels3.remove(u'及格')
                x3.remove(pa3)
            if nopa3 == 0:
                labels3.remove(u'不及格')
                x3.remove(nopa3)
            pat = "./pic/save3.png"
            plt.pie(x3, labels=labels3, autopct='%1.2f%%', textprops={'fontsize': 20, 'color': 'k'}, colors=colors)
            plt.axis('equal')  # 设为标准圆
            plt.savefig(pat)
            plt.close()
            img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
            staticbmp = wx.StaticBitmap(self.panel, -1, img, pos=(660, 40))
            myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
            staticbmp.SetBitmap(self.resizebmp(myimg, 320, 240))
        except Exception as e:
            wx.MessageBox('班级输入有误，请检查', '错误', wx.OK | wx.ICON_ERROR)
    #界面
    def classSelect(self,event):
        self.classFrame = wx.Frame(None, title="根据班级查询", size=(1005, 640), pos=(200, 70))
        self.classFrame.SetMaxSize((1005,640))
        self.classFrame.SetMinSize((1005, 640))
        self.classPanel = wx.Panel(self.classFrame, -1, size=(1005, 300))
        self.classPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.classFrame.SetIcon(self.icon)
        self.classLabel = wx.StaticText(self.classPanel, -1, "班   级", pos=(150, 10))
        self.classText = wx.TextCtrl(self.classPanel, -1, pos=(250, 10), size=(70, 20))
        self.selectButton = wx.Button(self.classPanel, -1, "查    询", size=(50, 25), pos=(620, 10))
        self.show = wx.TextCtrl(self.classPanel, -1, pos=(105, 70), size=(690, 210),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.classFrame.Bind(wx.EVT_BUTTON, self.classelect, self.selectButton)
        lblList = ['降序', '升序']
        self.rbox = wx.RadioBox(self.classPanel, pos=(400, -5), choices=lblList,majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.show.AppendText("学    号\t\t姓    名\t\t语文成绩\t\t数学成绩\t\t英语成绩\t总成绩\n")
        self.panel = wx.Panel(self.classFrame, -1, size=(1005, 340), pos=(0, 300))
        self.panel.SetBackgroundColour("white")
        pat = "./pic/class.png"
        img = wx.Image(pat, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        staticbmp = wx.StaticBitmap(self.classPanel, -1, img, pos=(840, 50))
        # 调用函数设置图片的大小
        myimg = wx.Image(pat, wx.BITMAP_TYPE_ANY)
        staticbmp.SetBitmap(self.resizebmp(myimg, 150, 150))
        self.show1 = wx.TextCtrl(self.panel, -1, pos=(80, 0), size=(130, 20), style=wx.TE_READONLY)
        self.show2 = wx.TextCtrl(self.panel, -1, pos=(400, 0), size=(150, 20), style=wx.TE_READONLY)
        self.show3 = wx.TextCtrl(self.panel, -1, pos=(720, 0), size=(150, 20), style=wx.TE_READONLY)
        self.classFrame.Show()


    #成绩导出
    def out(self,event):
        from login import conncet
        wildcard = 'Excel 文件(*.xls,*.xlsx)|*.*'
        dialog = wx.FileDialog(None, '导出成绩', os.getcwd(), '', wildcard, wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            book = Workbook(encoding='utf-8')
            sheet1 = book.add_sheet('成绩')
            path = dialog.GetPath() + ".xls"
            fileName = os.path.basename(path)
            sheet1.write(0, 0, "学号")
            sheet1.write(0, 1, "姓名")
            sheet1.write(0, 2, "班级")
            sheet1.write(0, 3, "语文")
            sheet1.write(0, 4, "数学")
            sheet1.write(0, 5, "英语")
            sheet1.write(0, 6, "总成绩")
            sql = "select num,name,class,course1,course2,course3,sum from grade order by sum DESC;"
            db = conncet()
            cr = db.cursor()
            cr.execute(sql)
            results = cr.fetchall()
            i = 1
            for row in results:
                sheet1.write(i, 0, row[0])
                sheet1.write(i, 1, row[1])
                sheet1.write(i, 2, row[2])
                sheet1.write(i, 3, row[3])
                sheet1.write(i, 4, row[4])
                sheet1.write(i, 5, row[5])
                sheet1.write(i, 6, row[6])
                i += 1
            book.save(path)
            wx.MessageBox("已导出至" + fileName, '导出成功', wx.OK | wx.ICON_INFORMATION)

    
    #修改密码
    def alterpass(self,event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        sql = "select password from teacher where username = '%s';" % (teacher.num)
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
                sql = "update teacher set password = %s where username = '%s';" % (self.newText.GetValue(), teacher.num)
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
    #界面
    def alterPass(self,event):
        self.alterpassFrame = wx.Frame(None, title="修改密码", size=(350, 250), pos=(500, 120))
        self.alterpassFrame.SetMaxSize((350,250))
        self.alterpassFrame.SetMinSize((350, 250))
        self.alterpassPanel = wx.Panel(self.alterpassFrame, -1, size=(549, 260))
        self.alterpassPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.alterpassFrame.SetIcon(self.icon)
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
        self.oldLabel = wx.StaticText(self.alterpassPanel, -1, "旧密码", pos=(45, 30))
        self.oldText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 30), size=(150, 20), style=wx.TE_PASSWORD)
        self.newLabel = wx.StaticText(self.alterpassPanel, -1, "新密码", pos=(45, 70))
        self.newText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 70), size=(150, 20), style=wx.TE_PASSWORD)
        self.conNewLabel = wx.StaticText(self.alterpassPanel, -1, "确认新密码", pos=(45, 110))
        self.conNewText = wx.TextCtrl(self.alterpassPanel, -1, pos=(130, 110), size=(150, 20), style=wx.TE_PASSWORD)
        self.button = wx.Button(self.alterpassPanel, -1, "确  定", size=(100, 25), pos=(125, 160))
        self.alterpassFrame.Bind(wx.EVT_BUTTON, self.alterpass, self.button)
        self.alterpassFrame.Show()


    #删除成绩
    def numdelete(self,event):
        if self.rbox.GetStringSelection()=='学       号':
            from login import conncet
            try:
                a = str("%.0f" % float(self.numText.GetValue().strip()))
                if self.pd2(a):
                    db = conncet()
                    cr = db.cursor()
                    sql = "select num from grade;"
                    cr.execute(sql)
                    res = cr.fetchall()
                    for row in res:
                        if row[0] == a:
                            sql = "delete from grade where num = %s" % (a)
                            cr.execute(sql)
                            db.commit()
                            sql = "delete from student where username = %s" % (a)
                            cr.execute(sql)
                            db.commit()
                    wx.MessageBox("删除成功！", '删除成功', wx.OK | wx.ICON_INFORMATION)
                else:
                     wx.MessageBox('没有学号为'+a+'的学生', '错误', wx.OK | wx.ICON_ERROR)
            except Exception as e:
                wx.MessageBox('输入不合法，请检查', '错误', wx.OK | wx.ICON_ERROR)
        else:
            from login import conncet
            try:
                a = str(self.numText.GetValue().strip())
                na = self.pd1(a)
                if na == 1:
                    db = conncet()
                    cr = db.cursor()
                    sql = "select name from grade;"
                    cr.execute(sql)
                    res = cr.fetchall()
                    for row in res:
                        if row[0] == a:
                            sql = "delete from grade where name = '%s'" % (a)
                            cr.execute(sql)
                            db.commit()
                            sql = "delete from student where name = '%s'" % (a)
                            cr.execute(sql)
                            db.commit()
                    wx.MessageBox("删除成功", '提示', wx.OK | wx.ICON_INFORMATION)
                elif na == 0:
                    wx.MessageBox('没有姓名为' + a + '的学生', 'error', wx.OK | wx.ICON_ERROR)
                else:
                    na = str(na)
                    wx.MessageBox('有' + na + '位同学叫' + a + ',无法根据姓名删除，请前往学号删除界面', 'error', wx.OK | wx.ICON_ERROR)
            except Exception as e:
                wx.MessageBox('输入不合法，请检查', 'error', wx.OK | wx.ICON_ERROR)
    #界面
    def numDelete(self,event):
        self.numDeleteFrame = wx.Frame(None, title="删除学生成绩", size=(380, 200), pos=(500, 120))
        self.numDeleteFrame.SetMaxSize((380,200))
        self.numDeleteFrame.SetMinSize((380, 200))
        self.numDeletePanel = wx.Panel(self.numDeleteFrame, -1, size=(549, 260))
        self.numDeletePanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.numDeleteFrame.SetIcon(self.icon)
        lblList = ['学       号', '姓      名']
        self.rbox = wx.RadioBox(self.numDeletePanel, label='选择删除方式', pos=(25, 20), choices=lblList, majorDimension=1,
                                style=wx.RA_SPECIFY_COLS)
        self.numText = wx.TextCtrl(self.numDeletePanel, -1, pos=(155, 30), size=(150, 20))
        self.deleteButton = wx.Button(self.numDeletePanel, -1, "删   除", size=(50, 25), pos=(170, 70))
        self.numDeleteFrame.Bind(wx.EVT_BUTTON, self.numdelete, self.deleteButton)
        img = wx.Image("./pic/delete.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.numDeletePanel, -1, img, pos=(270,70))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/delete.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg,100,100))
        self.numDeleteFrame.Show()