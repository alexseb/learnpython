
class A(object):
    def __init__(self):
        self.name = 'A' 

    def show(self):
	print self.name

class B(A):
    def __init__(self):
	super(B, self).__init__()
        self.bname = 'B' 

    def show(self):
	A.show(self)
 	print self.bname



obj = B()

obj.show()
	

