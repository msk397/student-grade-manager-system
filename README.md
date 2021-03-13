# student-grade-manager-system
学生成绩管理系统
使用python语言开发，数据库基于mysql，界面采用wxpython

# 一、 背景介绍

近年来，各个学校对于学生成绩的管理还是停留在运用手工操作，随着各个学校的规模不断壮大，学生人数逐年增加。关于学生成绩管理工作所涉及的数据量越来越大，学校靠增加人力、物力来进行学生成绩管理。但人工管理又有着许多缺陷，比如：效率底、易出错、检索信息慢、对学校的管理提供决策信息较为困难等。这种管理手段已不能适应时代的发展，因为它浪费了了许多的人力和物力。并且，学校不能完全掌握每一个学生的学习情况，这样对学校的教学工作及其不利。在信息时代，这种传统的管理方法必然被计算机为基础的信息管理系统所代替。通过本系统，使学校能够充分掌握学生的学习情况，便于学校教学工作的进行和改革。

# 二、 功能介绍

学生成绩管理信息系统共有三个角色，共12种功能：

管理员：

* 添加教师用户：为教师添加该系统的帐户。

* 修改密码：为管理员、教师和学生修改密码。

* 数据库备份：备份整个学生成绩管理系统的数据库，包括表及数据的全部信息。

* 删除数据库：删除数据库中每个学生的成绩及账户。

教师：

* 导入学生成绩：从文件中导入（见文件“模版.xlsx”）或手动输入成绩。

* 修改学生成绩：根据学生的学号或姓名修改成绩。

* 删除学生成绩：根据学生的学号或姓名删除成绩。

* 查询学生成绩：根据学号或姓名查询单个学生的成绩，并得到该同学的成绩分布图；根据班级、科目或总分数批量查询，并规定升序或降序查询，并得到成绩分布图。

* 导出学生成绩：导出数据库中学生的成绩至Excel表格。

* 修改密码：修改自己帐户的密码。

学生：

* 查询成绩：查询自己的成绩，并得到成绩分布图。

* 修改密码：修改自己帐户的密码。

# 三、 详细使用说明

## 3.1. 启动软件

双击“学生成绩管理系统.exe”打开软件，登陆界面如图1所示。

​                   ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133155.png)            

<center>图 1登陆界面<center>

   选择角色，输入对应帐户及密码，即可进入相应界面，管理员界面如图2所示，教师界面如图3所示，学生界面如图4所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133217.png)

<center>图 2管理员界面<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133224.png)

<center>图 3教师界面<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133232.png)

<center>图 4学生界面<center>

 

## 3.2. 教师及学生相关功能：

## 3.2.1. 学生成绩信息初始化

1)       在教师界面，选择“从Excel导入”，导入Excel文件，Excel表格示例如图5所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133238.png)

<center>图 5班级、学号、姓名和成绩模板文件内容示例<center>

2)       手动输入成绩，输入学生的学号、姓名及班级，成绩可以单科添加，无须一次全部添加，如图6所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133250.png)

<center>图 6手动添加成绩  <center>

​     

## 3.2.2. 删除成绩

选择根据学号或姓名删除成绩，然后在输入框输入对应信息即可，如图7所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133306.png)

<center>图 7删除成绩<center>

 

## 3.2.3. 修改成绩

   选择根据学号或姓名修改成绩，然后在输入框输入对应信息即可，成绩为-1的话，默认为不修改该课成绩，如图7所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133343.png)

<center>图 8修改成绩<center>

 

## 3.2.4. 查询成绩

1)       根据姓名或学号查询成绩，输入学号或姓名即可，如图8，图10所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133350.png)

<center>图 9根据学号查询<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133522.png)

<center>图 10根据姓名查询<center>

2)       根据班级、科目或总成绩查询，可以选择升序或降序排序，如图11，图12，图13所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133529.png)

<center>图 11根据班级查询成绩<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133652.png)

<center>图 12根据总分查询成绩<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133703.png)

<center>图 13根据科目查询成绩<center>

 

## 3.2.5. 导出成绩

点击“成绩导出”按钮，选择导出路径及文件名即可，导出时根据总成绩降序导出，如图14所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133713.png)

<center>图 14导出文件示例<center>

 

## 3.2.6. 修改密码（教师及学生共有功能）

   输入旧密码、新密码及确认新密码即可，如图15所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133723.png)

<center>图 15修改密码<center>

## 3.3. 管理员相关功能：

## 3.3.1. 添加教师帐户

为老师添加一个该系统的帐户，输入帐户及密码即可，如图16所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133827.png)

<center>图 16添加教师帐户<center>

 

## 3.3.2. 修改密码

为管理员、教师和学生修改密码，首先选择角色，然后输入用户名、旧密码、新密码及确认新密码即可，如图17所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133834.png)

<center>图 17管理员修改密码<center>

 

## 3.3.3. 数据库备份

点击“数据库备份”按钮，选择备份文件的路径及填写文件名，点击“保存”即可如图18所示，备份内容如图19所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133844.png)

<center>图 18备份示例<center>

 

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133859.png)

<center>图 19备份数据库示例<center>

 

## 3.3.4. 删除数据库

点击“删除数据库”按钮，输入该管理员的密码，如图20所示，就可以删除学生的成绩信息及帐户信息，如图21所示。

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133916.png)

<center>图 20确认密码<center>

 ![](https://cdn.jsdelivr.net/gh/machangxin/Pic/img/20210313133922.png)

<center>图 21提示管理员删除成功<center>

# 四、 总结

对于教师，学生成绩管理系统通过对用户提供的Excel表格中的数据或手动输入的成绩进行抽取，从而在数据库中为该学生添加成绩。还为教师提供了查询、修改及删除学生成绩的功能，方便教师对学生成绩进行操作。此外，还为教师提供了导出成绩的功能，方便教师备份学生成绩。对于管理员，学生成绩管理系统可以让管理员添加教师帐户，为该系统中所有用户修改密码。此外，为了数据安全性考虑，还为管理员提供了备份数据库的功能。该系统利用计算机的高效处理数据的特点代替了原有的人工管理方式,提高了学生成绩管理效率。
