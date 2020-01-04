import wx
import pymysql

from admin import admin
from student import student
from teacher import teacher


class Login(wx.Frame):
    def resizebmp(self,image, width, height):  # 图片的转换,限定图片大小 实现缩放
        bmp = image.Scale(width, height).ConvertToBitmap()  # 按照比例缩放
        return bmp

    def pd(self,a, b, c):
        dec = {"管理员":"root", "教师": "teacher", "学生": "student"}
        sql = "select username,password from %s;"%(dec[c])
        cr.execute(sql)
        results = cr.fetchall()
        for row in results:
            if row[0] == a and row[1] == b:
                return True
        return False

    def Login(self,event):
        a = self.rbox.GetStringSelection()
        if a == "管理员":
            if self.pd(self.userText.GetValue(), self.passText.GetValue(), a):
                ui = admin(self.userText.GetValue())
                ui.frame()
                self.loginFrame.Close()
            else:
                wx.MessageBox('用户名或密码错误', 'error', wx.OK | wx.ICON_ERROR)
                self.userText.SetValue("")
                self.passText.SetValue("")
        elif a == "教师":
            if self.pd(self.userText.GetValue(), self.passText.GetValue(), a):
                ui = teacher(self.userText.GetValue())
                ui.frame()
                self.loginFrame.Close()
            else:
                wx.MessageBox('用户名或密码错误', 'error', wx.OK | wx.ICON_ERROR)
                self.userText.SetValue("")
                self.passText.SetValue("")
        else:
            if self.pd(self.userText.GetValue(), self.passText.GetValue(), a):
                ui = student(self.userText.GetValue())
                ui.frame()
                self.loginFrame.Close()
            else:
                wx.MessageBox('用户名或密码错误', 'error', wx.OK | wx.ICON_ERROR)
                self.userText.SetValue("")
                self.passText.SetValue("")

    def frame(self):
        self.loginFrame = wx.Frame(None, title="学生成绩管理系统", size=(340, 240), pos=(500, 300))
        self.loginFrame.SetMaxSize((340, 240))
        self.loginFrame.SetMinSize((340, 240))
        self.loginPanel = wx.Panel(self.loginFrame, -1, size=(340, 240))
        self.loginPanel.SetBackgroundColour("white")
        img = wx.Image("./pic/login.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  # 转换成位图,将图片转换成二进制这样类似
        # 设置图片在panel中的位置
        self.staticbmp = wx.StaticBitmap(self.loginPanel, -1, img, pos=(0, 70))
        # 调用函数设置图片的大小
        myimg = wx.Image("./pic/login.jpg", wx.BITMAP_TYPE_ANY)
        self.staticbmp.SetBitmap(self.resizebmp(myimg, 70, 130))
        self.icon = wx.Icon("./pic/icon.ico", wx.BITMAP_TYPE_ICO)
        self.loginFrame.SetIcon(self.icon)
        lblList = ['管理员','教师', '学生']
        self.rbox = wx.RadioBox(self.loginPanel, label='选择角色', pos=(60, 20), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.userLable = wx.StaticText(self.loginPanel, -1, "用户名", pos=(50, 90))
        self.userText = wx.TextCtrl(self.loginPanel, -1,pos=(110, 90), size=(150, 20))
        self.passLable = wx.StaticText(self.loginPanel, -1, "密   码", pos=(50, 120))
        self.passText = wx.TextCtrl(self.loginPanel, -1,pos=(110, 120),size=(150, 20), style=wx.TE_PASSWORD)
        self.loginButton = wx.Button(self.loginPanel, -1, "登陆", size=(50, 25), pos=(140, 160))
        self.loginFrame.Bind(wx.EVT_BUTTON, self.Login, self.loginButton)
        self.loginFrame.Show()

def conncet():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='123456',
                         db='python',
                         charset='utf8')
    return db

def createdb():
    sql = """create table if not exists grade(
              num varchar(20) primary key,
              name varchar(20),
              class varchar(20) not null,
              course1 double(5,2) DEFAULT -1 ,
              course2 double(5,2) DEFAULT -1,
              course3 double(5,2) DEFAULT -1,
              sum double(5,2) DEFAULT 0);"""
    cr.execute(sql)
    sql = """create table if not exists student(
              username varchar(20) primary key,
              name varchar(20),
              password varchar(20) not null DEFAULT '123456');"""
    cr.execute(sql)

if __name__ == '__main__':
    db = conncet()
    global cr
    cr = db.cursor()
    createdb()
    app = wx.App()
    ui = Login()
    ui.frame()
    app.MainLoop()