str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)
        #print(self.str)로 수정해야함

g = GString()
g.set("First Message")
g.print()
