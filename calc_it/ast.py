from rply.token import BaseBox


class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Exponent(BinaryOp):
    def eval(self):
        return self.left.eval() ** self.right.eval()


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Subtract(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multiply(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Divide(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
