import sys
sys.path.insert(0, '../c4')
from tubestats import t_junction_tube
from legs import *
X, Z = 1, 3
LEGSETS = [[(4,0,0),(0,4,0),(0,0,4)], [(-4,0,0),(0,-4,0),(0,0,-4)], [(4,0,0),(-4,0,0),(0,0,4)], [(4,4,0),(0,4,4),(4,0,4)]]
def edgecode(S): return [A] + [plaq(c, S) for c in range(3)]
for name, S in [('plain', [(),(),()]), ('T-framed', [(((0,-1,0),0),((0,1,0),0)), (((0,0,-1),1),((0,0,1),1)), (((-1,0,0),2),((1,0,0),2))]),
                ('earlier solver-"fermion"', [(((-1,0,0),2),), (), (((1,0,0),0),)])]:
    out = []
    for legs in LEGSETS:
        r = t_junction_tube(edgecode(S), 3, [((0,0,0),0)], legs, R=5)
        out.append(r[0])
    print(name, out, flush=True)
