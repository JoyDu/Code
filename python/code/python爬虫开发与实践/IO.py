# coding=utf-8
def openFile():
    with open(r'test.txt', 'w') as fileWriter:
        fileWriter.write('测试文件写入')
    with open(r'test.txt', 'r') as fileReader:
        for line in fileReader.readlines():
            print(line.strip())


openFile()
