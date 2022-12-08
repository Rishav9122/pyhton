class tables:
    x=int(input())
    def tables2(self):
        for i in range(2, self.x + 1):
            for j in range(1, 11):
                print (i, "*", j, "=", i * j)
ab=tables()
ab.tables2()
