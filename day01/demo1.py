# center自动居中，空缺部分可以自定义进行不全
# print("欢迎来到json水果商城".center(20,"*"))

# 从键盘输入一个人的信息并存储到变量里
# （姓名，身份证号，年龄，性别，身高，体重）
# list = []
# a = input("请输入姓名：")
# b = input("请输入身份证：")
# c = input("性别：")
# d = input("身高：")
# e = input("体重：")
# aa = [a,b,c,d,e]
# list.append(aa)
# for i in list:
#     print(i)
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# list.append(e)
# print(list)





# hint = ["请输入姓名：", "请输入身份证：", "性别：", "身高：", "体重："]
# list = []
# for i in range(5):
#     list.append(input(hint[i]))
# print(list)





print("*************************12月的衣服销量*********************")
print("*"*60)
print("* 日期 *   服装名称  *   价格/件	* 库存数量	* 销售量/每日  *")
print("*"*60)
print("# 1号	   羽绒服	     253.6	   500	          10       *")
print("# 2号	   牛仔裤	     86.3	   600	          60       *")
print("# 3号	   风衣	         96.8	   335	          43       *")
print("# 4号	   皮草	         135.9	   855	          63       *")
print("# 5号	   T血	         65.8	   632	          63       *")
print("# 6号	   衬衫	         49.3	   562	          120      *")
print("# 7号	   牛仔裤	     86.3	   600	          72       *")
print("# 8号	   羽绒服	     253.6	   500	          69       *")
print("# 9号	   牛仔裤	     86.3	   600	          35       *")
print("# 10号	   羽绒服	     253.6	   500	          140      *")
print("# 11号	   牛仔裤	     86.3	   600	          90       *")
print("# 12号	   皮草	         135.9	   855	          24       *")
print("# 13号	   T血	         65.8	   632	          45       *")
print("# 14号	   风衣	         96.8	   335	          25       *")
print("# 15号	   牛仔裤	     86.3	   600	          60       *")
print("# 16号	   T血	         65.8	   632	          129      *")
print("# 17号	   羽绒服	     253.6	   500	          10       *")
print("# 18号	   风衣	         96.8	   335	          43       *")
print("# 19号	   T血	         65.8	   632	          63       *")
print("# 20号	   牛仔裤	     86.3	   600	          60       *")
print("# 21号	   皮草	         135.9	   855	          63       *")
print("# 22号	   风衣	         96.8	   335	          60       *")
print("# 23号	   T血	         65.8	   632	          58       *")
print("# 24号	   牛仔裤	     86.3	   600	          140      *")
print("# 25号	   T血	         65.8	   632	          48       *")
print("# 26号	   风衣	         96.8	   335	          43       *")
print("# 27号	   皮草	         135.9	   855	          57       *")
print("# 28号	   羽绒服	     253.6	   500	          10       *")
print("# 29号	   T血	         65.8	   632	          63       *")
print("# 30号	   风衣	         96.8	   335	          78       *")
print("*"*60)
#羽绒服
a = 253.6 * (10+69+140+10+10)
#牛仔裤
b = 86.3 * (60+72+35+90+60+60+140)
#风衣
c = 96.8*(43+25+43+60+43+78)
#皮草
d = 135.9 * (63+24+63+57)
#T血
e = 65.8 * (63+45+129+63+58+48+63)
#衬衫
f = 49.3 * (120)
g = a+ b + c + d + e + f
print("12月份消费总金额：￥",g)

print("羽绒服服的销售占比：",a/g*100,"%")
print("牛仔裤的销售占比：",b/g*100,"%")
print("风衣的销售占比：",c/g*100,"%")
print("皮草的销售占比：",d/g*100,"%")
print("T血的销售占比：",e/g*100,"%")
print("衬衣的销售占比：",f/g*100,"%")










