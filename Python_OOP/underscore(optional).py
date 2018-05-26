class Underscore(object):
    def map(self,cb):
        pass
    def reduce(self,cb):
        pass
    def find(self,li,cb):
        pass
    def filter(self,li,cb):
        newLi = []

        for i in range(0,len(li)):
            if cb(li[i]):
                newLi.append(li[i])

        return newLi
    def reject(self,cb):
        pass

_ = Underscore()
print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)