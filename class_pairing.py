class Pairing:
    def __init__(self,num,targets):
        self.num = num
        self.targets = targets

        def finding(self):
            checker = dict()
            for count, value in enumerate(self.num):
                if(self.target - value) in checker:
                    return(checker[self.target - value],count)
                checker[value] = count

sum_num = Pairing([10,20,10,40,50,60,70],60)
print(f"indexes:{sum_num.finding()}")