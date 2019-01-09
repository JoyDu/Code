# coding=utf-8
#d定义Home类
class Home(object):
    def __init__(self,area):
        self.area=area
        self.containsItem=[]
    def __str__(self):
        msg="当前房间可用面积为："+str(self.area)
        if  len(self.containsItem)>0:
            msg=msg+" 容纳的物品有："
            for temp in self.containsItem:
                msg+=(temp.getName()+", ")
            msg=msg.rstrip(", ")
        return msg
    def accommodateItem(self,item):
        needArea=item.getUsedArea()
        if  self.area>needArea:
            self.containsItem.append(item)
            self.area-=needArea
        else:
            print("房间可用面积为%d,当前存放物品需要面积为%d"%(self.area,needArea))
# 定义家具类
class Furnitrue(object):
    def __init__(self,area,name):
        self.name=name
        self.area=area
    def __str__(self):
        msg=self.name+"的面积为"+str(self.area)
        return msg
    def getUsedArea(self):
        return self.area
    def getName(self):
        return self.name
joyduHome=Home(200)
print(joyduHome)
bed=Furnitrue(4,"bed")
print(bed)
joyduHome.accommodateItem(bed)
tv=Furnitrue(200,"TV")
print(tv)
joyduHome.accommodateItem(tv)

        