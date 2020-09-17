class BuySafe:
    def buy_safe(self,style,year):
        price = 0
        total = 0
        if style == "意外":
            if year == 1:
                price = 10
            elif year == 3:
                price = 8
            total = price * year
        elif style == "重疾":
            if year == 1:
                price = 20
            elif year == 3:
                price = 15
            total = price * year
        return total