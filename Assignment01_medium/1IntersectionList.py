class Common:
    def listCommon(self, list1, list2):
        commonList = list(set(list1) & set(list2))
        return commonList


if __name__ == '__main__':
    c = Common()
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(c.listCommon(list1, list2))
