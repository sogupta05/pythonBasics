#there is an inbuilt iterator for the inbuilt objects, which implememts __iter__ and __next__ functions
# these are also used for the for loop
#so it you want to create iterator for custom objects then you have to implement __iter__ and __next__ functions
#then you will be able to use FOR loop for custom objects too

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = 0
        if self.num > 10:
            raise StopIteration
        else:
            val = self.num
            self.num += 1
            return val


values = TopTen()
print(values.__next__())
print(next(values))
print(next(values))
print(values.__next__())
for i in values:
    print(i)