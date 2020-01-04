
import os
import subprocess

import  wx

class admin(wx.App):
    num = None
    def __init__(self,a):
        super(admin, self).__init__()
        admin.num = a


    def resizebmp(self,image, width=700, height=350):  # 图片的转换,限定图片大小 实现缩放
        bmp = image.Scale(width, height).ConvertToBitmap()  # 按照比例缩放
        return bmp
    #主界面
    def frame(self):
        self.adminFrame = wx.Frame(None,title = "管理员界面",size = (700,350),pos = (400,200))
        self.adminFrame.SetMaxSize((700,350))
        self.adminFrame.SetMinSize((700,350))
        self.adminPanel = wx.Panel(self.adminFrame,-1,size = (700,350))
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.adminFrame.SetIcon(self.icon)
        img = wx.Image("./pic/admin.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.adminPanel, -1, img, pos=(0, 0))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/admin.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg))
        self.addTeacher1 = wx.Button(self.staticbmp,-1,"添加教师账户",size = (100,25),pos = (300,20))
        self.addTeacher = wx.Button(self.adminPanel,-1, "添加教师账户", size=(100, 25), pos=(300, 20))
        self.alterButton1 = wx.Button(self.staticbmp,-1,"修改密码",size = (100,25),pos = (300,70))
        self.alterButton = wx.Button(self.adminPanel, -1, "修改密码", size=(100, 25), pos=(300, 70))
        self.saveButton1 = wx.Button(self.staticbmp, -1, "数据库备份", size=(100, 25), pos=(300, 120))
        self.saveButton = wx.Button(self.adminPanel, -1, "数据库备份", size=(100, 25), pos=(300, 120))
        self.deleteButton1 = wx.Button(self.staticbmp, -1, "删除数据库", size=(100, 25), pos=(300, 170))
        self.deleteButton = wx.Button(self.adminPanel, -1, "删除数据库", size=(100, 25), pos=(300, 170))
        self.adminFrame.Bind(wx.EVT_BUTTON, self.alterPass, self.alterButton)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.saveDb, self.saveButton)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.deleteDb, self.deleteButton)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.alterPass, self.alterButton1)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.saveDb, self.saveButton1)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.deleteDb, self.deleteButton1)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.addTea, self.addTeacher)
        self.adminFrame.Bind(wx.EVT_BUTTON, self.addTea, self.addTeacher1)
        self.adminFrame.Show()


    #修改密码操作
    def alterpass(self,event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        a = self.rbox.GetStringSelection()
        b = self.user_text.GetValue()
        if a == "管理员":
            a = "root"
        elif a== "学生":
            a = "student"
        else:
            a = "teacher"
        sql = "select password from %s where username = '%s';" % (a, b)
        cr.execute(sql)
        res = cr.fetchone()
        c = res[0]
        if c != self.old_text.GetValue():
            wx.MessageBox('旧密码错误，请重新输入', '错误', wx.OK | wx.ICON_ERROR)
        else:
            if self.conNew_text.GetValue() == self.new_text.GetValue():
                sql = "update %s set password = %s where username = '%s';" % (a, self.new_text.GetValue(), b)
                cr.execute(sql)
                db.commit()
                wx.MessageBox("修改成功！", '修改成功', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox('两次新密码输入不一致，请重新输入', '错误', wx.OK | wx.ICON_ERROR)
        self.old_text.SetValue("")
        self.new_text.SetValue("")
        self.conNew_text.SetValue("")
    #修改密码界面
    def alterPass(self,event):
        self.alterPassFrame = wx.Frame(None, title="修改密码", size=(400, 300), pos=(500, 120))
        self.alterPassFrame.SetMaxSize((400,300))
        self.alterPassFrame.SetMinSize((400, 300))
        self.alterPassPanel = wx.Panel(self.alterPassFrame, -1, size=(400, 300))
        self.alterPassPanel.SetBackgroundColour("white")
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.alterPassFrame.SetIcon(self.icon)
        img = wx.Image("./pic/mi1.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.alterPassPanel, -1, img, pos=(0, 170))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/mi1.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg,95,90))

        img = wx.Image("./pic/mi2.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.alterPassPanel, -1, img, pos=(305, 170))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/mi2.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 95, 90))
        lblList = ['管理员', '教师','学生']
        self.rbox = wx.RadioBox(self.alterPassPanel, label='选择角色', pos=(5, 55), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.user_label = wx.StaticText(self.alterPassPanel, -1, "用户名", pos=(95, 30))
        self.user_text = wx.TextCtrl(self.alterPassPanel, -1, pos=(170, 30), size=(150, 20))
        self.old_label = wx.StaticText(self.alterPassPanel, -1, "旧密码", pos=(95, 70))
        self.old_text = wx.TextCtrl(self.alterPassPanel, -1, pos=(170, 70), size=(150, 20), style=wx.TE_PASSWORD)
        self.new_label = wx.StaticText(self.alterPassPanel, -1, "新密码", pos=(95, 110))
        self.new_text = wx.TextCtrl(self.alterPassPanel, -1, pos=(170, 110), size=(150, 20), style=wx.TE_PASSWORD)
        self.conNew_label = wx.StaticText(self.alterPassPanel, -1, "确认新密码", pos=(95, 150))
        self.conNew_text = wx.TextCtrl(self.alterPassPanel, -1, pos=(170, 150), size=(150, 20), style=wx.TE_PASSWORD)
        self.con_button = wx.Button(self.alterPassPanel, -1, "确  定", size=(100, 25), pos=(140, 190))
        self.alterPassFrame.Bind(wx.EVT_BUTTON, self.alterpass, self.con_button)
        self.alterPassFrame.Show()


    def pd(self,str):
        sql = "select username from teacher;"
        from login import conncet
        db = conncet()
        cr = db.cursor()
        cr.execute(sql)
        results = cr.fetchall()
        for row in results:
            if row[0] == str:
                return True
        return False
    def add(self,event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        a = str(self.numText.GetValue().strip())
        if self.pd(a):
            wx.MessageBox('账户重复', 'error', wx.OK | wx.ICON_ERROR)
        else:
            print(a)
            b = str(self.nameText.GetValue().strip())
            #data = (a, b)
            sql = "insert into teacher (username,password) values ('%s','%s');" %(a,b)
            cr.execute(sql)
            db.commit()
    #界面
    def addTea(self,event):
        self.headFrame = wx.Frame(None, title="添加教师账户", size=(350, 300), pos=(500, 100))
        self.headFrame.SetMaxSize((350, 300))
        self.headFrame.SetMinSize((350, 300))
        self.headPanel = wx.Panel(self.headFrame, -1, size=(350, 300))
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.headFrame.SetIcon(self.icon)
        img = wx.Image("./pic/ad.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.headPanel, -1, img, pos=(80, 100))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/ad.png", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 150,100))
        self.headPanel.SetBackgroundColour("white")
        self.numLabel = wx.StaticText(self.headPanel, -1, "账    户", pos=(30, 30))
        self.nameLabel = wx.StaticText(self.headPanel, -1, "密   码", pos=(30, 60))
        self.addButton = wx.Button(self.headPanel, -1, "添  加", size=(50, 25), pos=(130, 210))
        self.headFrame.Bind(wx.EVT_BUTTON, self.add, self.addButton)
        self.numText = wx.TextCtrl(self.headPanel, -1, pos=(120, 30), size=(150, 20))
        self.nameText = wx.TextCtrl(self.headPanel, -1, pos=(120, 60), size=(150, 20))
        self.headFrame.Show()


    #数据库删除
    def deletedb(self,event):
        from login import conncet
        db = conncet()
        cr = db.cursor()
        passWord = self.deleteDbText.GetValue()
        sql = "select password from root where username = '%s';"%(admin.num)
        cr.execute(sql)
        res = cr.fetchone()
        a = res[0]
        if a == passWord:
            sql = "drop table grade,student;"
            cr.execute(sql)
            db.commit()
            wx.MessageBox("删除成功", '成功', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("密码错误", 'error', wx.OK | wx.ICON_ERROR)
    #删除数据库界面
    def deleteDb(self,event):
        self.deleteDbFrame = wx.Frame(None,title = "确认密码",size = (300,200),pos = (600,200))
        self.deleteDbFrame.SetMaxSize((300, 200))
        self.deleteDbFrame.SetMinSize((300, 200))
        self.deleteDbPanel = wx.Panel(self.deleteDbFrame,size=(300,200))
        self.icon = wx.Icon(name="./pic/icon.ico", type=wx.BITMAP_TYPE_ICO)
        self.deleteDbFrame.SetIcon(self.icon)
        self.deleteDbPanel.SetBackgroundColour("white")
        img = wx.Image("./pic/mi.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.deleteDbPanel, -1, img, pos=(0, 90))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/mi.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 70, 70))
        self.deleteDbLable = wx.StaticText(self.deleteDbPanel,-1,"确认密码",pos = (20,50))
        self.deleteDbText = wx.TextCtrl(self.deleteDbPanel,-1,pos = (100,50),size = (150,20),style = wx.TE_PASSWORD)
        self.deleteDbButton = wx.Button(self.deleteDbPanel, -1, "确  定", size=(100, 25), pos=(90, 120))
        self.deleteDbFrame.Bind(wx.EVT_BUTTON,self.deletedb,self.deleteDbButton)
        self.deleteDbFrame.Show()


    #数据库备份
    def saveDb(self,event):
        wildcard = 'sql文件(*.sql)|*.*'
        dialog = wx.FileDialog(None, '数据库备份', os.getcwd(), '', wildcard, wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            #os.chdir("C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin")#mysql地址，需要单独设置
            key = "123456"  # 设置你的数据库密码
            path = dialog.GetPath() + ".sql"
            fileName = os.path.basename(path)
            res = subprocess.run("cd C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin & mysqldump -u root -p%s python > %s" % (key,path), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            wx.MessageBox("已导出至" + fileName, '导出成功', wx.OK | wx.ICON_INFORMATION)
            #os.chdir("C:\\Users\\21450\\Desktop\\jk1703ltt")