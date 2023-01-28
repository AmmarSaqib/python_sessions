"""
1- code structure
2- conventions
"""


class Stack:
    def __init__(self, values=[]):
        self.__stack = values

    def push(self, value):
        try:
            self.stack.append(value)
            return True
        except:
            return False

    def pop(self):
        val = None
        try:
            val = self.stack.pop()
            return True, val
        except:
            return False, val

    def get_stack(self):
        return self.__stack


if __name__ == "__main__":

    stack_1 = Stack([1, 2, 4])
    print(stack_1.get_stack())

    print(stack_1.push(5))
    print(stack_1.get_stack())

    print(stack_1.pop())
    print(stack_1.get_stack())
