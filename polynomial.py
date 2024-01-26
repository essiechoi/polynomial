class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def toInt(self):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, n):
        if type(self.p1) != Int and type(self.p2) != Int:
            return n + n
        elif type(self.p1) != Int:
            return n + self.p2.toInt()
        elif type(self.p2) != Int:
            return n + self.p1.toInt()
        else:
            return self.p1.toInt() + self.p2.toInt()

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Div):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, n):
        if type(self.p1) != Int and type(self.p2) != Int:
            return n * n
        elif type(self.p1) != Int:
            return n * self.p2.toInt()
        elif type(self.p2) != Int:
            return self.p1.toInt() * n
        else:
            return self.p1.toInt() * self.p2.toInt()

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Mul):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Mul):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Mul):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, n):
        dividend, divisor = n, n 
        if type(self.p1) != Int:
            divisor = self.p2.toInt()
        elif type(self.p2) != Int:
            dividend = self.p1.toInt()
        elif type(self.p1) == Int and type(self.p2) == Int:
            dividend, divisor = self.p1.toInt(),  self.p2.toInt()
        if divisor == 0:
            print("cannot divide by 0")
            return
        else:
            return dividend / divisor

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, n):
        if type(self.p1) != Int and type(self.p2) != Int:
            return n - n
        elif type(self.p1) != Int:
            return n - self.p2.toInt()
        elif type(self.p2) != Int:
            return self.p1.toInt() - n
        else:
            return self.p1.toInt() - self.p2.toInt()

if __name__ == "__main__" :

    # poly = Add( Add( Int(4), Int(3)), Sub( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
    # print(poly)
    # test = Mul(Int(4), Div (Int(5), Sub(Int(2), Int(2))))
    # print(test)
    # test1 =  Sub(X(), Int(2))
    # print(test1.evaluate(-1))
    # poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
    # print(poly.evaluate(-1))
    poly = Div(Int(4), X())
    print(poly.evaluate(0))
    # Output: 6