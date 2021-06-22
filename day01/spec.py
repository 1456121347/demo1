
id1 = 1
name1 = "清徐葡萄"
price1 = 50
num1 = 580
quan1 = "A+"
add1 = "山西"

#清徐红杏
id2 = 2
name2="清徐红杏"
price2 = 35
num2 = 550
quan2 = "B+"
add2 = "山西"

#汾州核桃
id3 = 3
name3="汾州核桃"
price3 = 35
num3 = 500
quan3 = "B+"
add3 = "山西"

#山西陈醋
id4 = 4
name4="晋城红果"
price4 = 25
num4 = 450
quan4 = "B+"
add4 = "山西"

#原平梨
id5 = 5
name5="原平梨"
price5 = 35
num5 = 500
quan5 = "B+"
add5 = "山西"

#稷山板枣
id6 = 6
name6="吉县苹果"
price6 = 55
num6 = 600
quan6 = "B+"
add6 = "山西"

# 清徐葡萄    清徐红杏     小堡葡萄   晋城红果  太谷壶瓶枣  原平梨   海红果
# 大宁西瓜   吉县苹果    官滩枣   汾州核桃   梁红枣
print("--------------------------家乡水果----------------------------")
print("-编号      名称         价格       数量       品质        产地-")
print("-------------------------------------------------------------------")
print(id1,"\t\t",name1,"\t\t",price1,"\t\t",num1," \t",quan1,"\t\t",add1)
print(id2,"\t\t",name2,"\t\t",price2,"\t\t",num2," \t",quan2,"\t\t",add2)
print(id3,"\t\t",name3,"\t\t",price3,"\t\t",num3," \t",quan3,"\t\t",add3)
print(id4,"\t\t",name4,"\t\t",price4,"\t\t",num4," \t",quan4,"\t\t",add4)
print(id5,"\t\t",name5,"\t\t",price5,"\t\t",num5," \t",quan5,"\t\t",add5)
print(id6,"\t\t",name6,"\t\t",price6,"\t\t",num6," \t",quan6,"\t\t",add6)
print("-------------------------------------------------------------------")
print("总金额：￥",(price1 * num1 + price2 * num2 + price3 * num3 +price4 * num4 + price5 * num5 + price6 * num6),"元")