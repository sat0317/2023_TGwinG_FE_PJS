class Item:
    def __init__(self, 가격=1000, 재고=0):
        self.가격 = 가격
        self.재고 = 재고

ABC = {
    "커피": Item(2000, 10),
    "콜라": Item(1500, 5)
}

ABC["사이다"] = Item(1200, 7)

for i in ABC:
    print(i, ABC[i].가격, ABC[i].재고)