# coding=utf-8
# from helper import *
import helper
h = helper.Helper()


def testAdd():
    print(h.add(12, 21))


def testSubstract():
    print(h.subtract(21, 12))


if __name__ == "__main__":
    testAdd()
    testSubstract()
    print(__name__)
