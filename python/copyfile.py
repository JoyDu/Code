# coding=utf-8
import os


# 拷贝文件
def copyFile():
    paths = os.path.abspath('./python/box.html')
    oldFileName = "box.html"
    oldFile = open(paths, 'r')
    if oldFile:
        # 获取文件后缀
        fileFlagNum = oldFileName.rfind('.')
        if fileFlagNum > 0:
            fileFlag = oldFileName[fileFlagNum:]
        # 创建新的文件名字
        newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag

        # 创建新文件
        newFile = open(newFileName, 'w')
        for lineContent in oldFile.readlines():
            newFile.write(lineContent)
        # 关闭文件
        oldFile.close()
        newFile.close()
    os.rename(newFileName, "box(复件).html")
    os.remove("box(复件).html")


# 文件夹常用操作
def operatDir():
    # 获取当前目录
    currentDir = os.getcwd()
    print(currentDir)

    # 改变默认目录
    os.chdir("../")
    print(os.getcwd())

    # 创建文件夹
    os.mkdir("测试文件夹")

    # 获取目录列表
    currentDirList = os.listdir(os.getcwd())
    for dirItem in currentDirList:
        print(dirItem)
    os.rmdir("测试文件夹")


def getAllDir():
    rootPath = "../"
    os.chdir(rootPath)
    dirList = os.listdir(os.getcwd())
    for dirItem in dirList:
        fileFlagNum = dirItem.rfind('.')
        if fileFlagNum > 0:
            print(dirItem)
        else:
            print("")


getAllDir()
