from jinja2 import Environment, FileSystemLoader

class Comms:
    def __init__(self,s,t,n,b):
        self.state = s
        self.tp = t
        self.n = n
        self.c = None
        self.b = b

    def set_c(self,c):
        self.c = c

    def __eq__(self, other):
        return self.state == other.state and self.tp == other.tp and self.n == other.n

    def __str__(self):
        return "s_{},t_{},n_{},b_{},c_{}".format(self.state,self.tp,self.n,self.b,self.c)

    def __repr__(self):
        return "s_{},t_{},n_{},b_{},c_{}".format(self.state,self.tp,self.n,self.b,self.c)

    def __hash__(self):
        return hash((self.state,self.tp,self.n))


class Moves:
    def __init__(self,s,n,c=None,ns=None,i=None,o=None):
        self.state = s
        self.n = n
        self.o = o
        self.i = i
        self.ns = ns
        self.c = c

    def set_i(self,i):
        self.i = i

    def set_c(self,c):
        self.c = c

    def set_ns(self,ns):
        self.ns = ns

    def set_o(self,o):
        self.o = o

    def __eq__(self, other):
        return (self.state == other.state and self.i == other.i
                and self.c == other.c and self.ns == other.ns)

    def __str__(self):
        return "p{},t{},i{},c{},t{},o{}".format(self.n,self.state,self.i,self.c,self.ns,
                self.o)

    def __repr__(self):
         return "p{},t{},i{},c{},t{},o{}".format(self.n,self.state,self.i,self.c,self.ns,
                self.o)

    def __hash__(self):
        return hash((self.state,self.i,self.c,self.ns))

def get_ctrl_ids(content):
    a = set(map(lambda x: int(x[0][1]), content))
    return list(a)

def mk_comms(line, i):
    return Comms(s=int(line[1][1]),t=int(line[2][1]),n=i, b=int(line[3]))

def mk_moves(line, i):
    if line[2] != "":
        return Moves(s=int(line[1][1]),n=i, i=int(line[2][1]),
                c=int(line[3][1]),ns=int(line[4][1]))
    else:
        return Moves(s=int(line[1][1]),n=i, i=None,
                c=int(line[3][1]),ns=int(line[4][1]))

def comms_return(comms):
    lst = []
    for line in c_content:
        if comms.state == int(line[1][1]) and comms.tp == int(line[2][1]):
            lst.append(int(line[-1]))
    comms.set_c(to_int(lst))
    return comms

def to_int(lst):
    t = 0
    for i,d in enumerate(lst):
        t += 2**i if d == 1 else 0
    return t

def moves_return(move):
    lst = []
    for line in m_content:
        if move.ns == int(line[2][1]) and move.n == int(line[0][1]):
            lst.append(int(line[-1]))
    move.set_o(to_int(lst))
    return move

def get_comms(content, index):
    comms = []
    for line in content:
        if int(line[0][1]) == index:
            tmp = mk_comms(line, index)
            if tmp not in comms:
                comms.append(tmp)
    comms = map(comms_return,comms)
    return comms

def get_moves(content, index):
    moves = []
    for line in content:
        if int(line[0][1]) == index and int(line[-1]) == 1:
            tmp = mk_moves(line,index)
            if tmp not in moves:
                moves.append(tmp)
    moves = map(moves_return,moves)
    return moves

def split_(lst):
    return lst.rstrip().split("_")

env = Environment(loader=FileSystemLoader("./"))
tpl =  env.get_template('template.py')
f = "sample_uav_plan.txt"
content = map(split_,open(f).readlines())

c_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'c',content)))
m_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'o',content)))
tau_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'tau',content)))
ctrl_ids = get_ctrl_ids(c_content)

for i in ctrl_ids:
    cs = get_comms(c_content,i)
    cs = list(set(cs))
    ms = get_moves(tau_content,i)
    ms = list(set(ms))
    ctrl = tpl.render(ctrl_name="Controller_{}".format(i), commsifs=cs, moveifs=ms)
    text_file = open("ctrl_{}.py".format(i), "w")
    text_file.write(ctrl)
    text_file.close()

