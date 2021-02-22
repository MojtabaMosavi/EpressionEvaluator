
class Exp(object):
    ''' Base class to create ploymorphic behavior
    two common characteristic of expresions str and ability to be evaluated'''
    def __str__(self):
        return ''

    def eval(self):
        return 0

class Num(Exp):
    '''A class to create representation of numbers
    following classes are assumed to perform operation on a instace of this class '''
    def __init__(self,num):
        self.num = num
    def __str__(self):
        return str(self.num)
    def eval(self):
        return self.num


class Add(Exp):
    ''' addition class, assumes that eval is called on a object of type Num '''
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def __str__(self):
        return '('+str(self.left)+ ') + (' + str(self.right)  +')'

    # evaluting the expression recursively from left left leaf node
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(Exp):
    ''' subtraction class, assumes that eval is called on a object of type Num '''

    def __init__(self,left,right):
        self.left = left
        self.right = right

    def __str__(self):
        return '('+str(self.left)+') - ('+str(self.right)+')'

    # evaluting the expression recursively from left left leaf node
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(Exp):
    ''' multiplication class, assumes that eval is called on a object of type Num '''
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def __str__(self):
        return '('+str(self.left)+') * ( '+str(self.right)+')'

    # evaluting the expression recursively from left left leaf node
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Exp):
    ''' Division class, assumes that eval is performed on a object of type Num '''
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def __str__(self):
        return '('+str(self.left)+') / ('+str(self.right)+')'

    # evaluting the expression recursively from left left leaf node
    def eval(self):
        return self.left.eval() / self.right.eval()

if __name__ == '__main__':
    operation = [Div(Num(2),Num(10)), Mul(Num(4),Num(10)),Add(Num(10),Num(40)),Sub(Num(40),Num(39))]
    # polymorphic bahavior ---> because Exp is the parent of all other classes
    # inheritance heirarchy ---> all object types are guaranteed
    # to have the method eval and __str__
    for operation in operation:
        print(operation,'==',operation.eval())
