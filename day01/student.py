#通讯录

# 保存用户的信息
nameList = []
while True:
    #1.输出功能选项
    print('*'*33)
    print('*  欢迎进入第一通讯录系统   *')
    print('*      1.查找信息               *')
    print('*      2.增加信息               *')
    print('*      3.修改信息               *')
    print('*      4.删除信息               *')
    print('*      5.显示全部信息           *')
    print('*      6.退出系统               *')
    print('*'*33)
    data=[
    #   [   '姓名'      '电话'       '性别'     '地址'],
        [ '李小花'  ,'13812341234', '女'  ,'东北黄花岗小刘庄'],
        ['王二狗'  ,'13566667777', '男'  ,'刘家窑冒烟儿胡同'],
        ['刘三胖'  ,'13322222222', '女'  , '窦店大红灯笼村' ],
        ['史铁柱'  ,'17199994444', '男'  ,    '隔壁老王庄'  ],
        ['隔壁老王','18733339999', '男'  ,    '御上史香村'  ]
        ]
     #2.等待用户的选择
    a = int(input('请输入你选择的数字:'))
    #3.根据用户输入进行相应操作
    if a == 1:
        name = input('请输入您要查找的姓名:')
        for abName in data:
            if name in abName:
                print(abName)
                
                print("恭喜你有此人")
                break
    elif a == 2:
        name = input('请输入姓名:')
        telephone = input('请输入电话:')
        gender = input('请输入性别:')
        site = input('请输入地址:')

        a = []
        a.append(name)
        a.append(telephone)
        a.append(gender)
        a.append(site)
        print(a)
        data.append(a)
        print(data)

    elif a == 3:
        name = input('请输入需要修改的用户姓名:')
        id = 0
        for i in range(len(data)):
            if name in data[i]:
                id = i
        telephone = input('请输入需要修改的用户电话:')
        gender = input('请输入需要修改的用户性别:')
        site = input('请输入修改的用户地址:')
        data[id] = [name,telephone,gender,site]
        print(data)
        
    elif a == 4:
        name = input('请输入要删除的学生姓名：')
        for cbName in data:
            if name in cbName:
                data.remove(cbName)
                print(data)

    elif a == 5:
        data.append(nameList)
        print(data)


    elif a == 6:
        confirm = input('亲,确定要退出程序么(yes/no)?')
        confirm = confirm.lower()
        if confirm =='yes':
            break
       
