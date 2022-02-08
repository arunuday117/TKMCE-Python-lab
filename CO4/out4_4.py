class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,other):
        h=self.hour+other.hour
        m=self.minute+other.minute
        s=self.second+other.second
        return Time(h,m,s)
    def __str__(self):
        return str(self.hour)+"'"+str(self.minute)+"''"+str(self.second)+"'''"
t1=Time(1,34,10)
t2=Time(20,34,50)
t3=t1+t2
print(t3)
