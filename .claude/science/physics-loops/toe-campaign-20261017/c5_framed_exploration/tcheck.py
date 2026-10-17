import sys, itertools
import numpy as np
exec(open('orbit_size.py').read().split("fermions = [")[0])
sys.path.insert(0, '../c4')
from stats import t_junction
S = [(((0,-1,0),0),((0,1,0),0)), (((0,0,-1),1),((0,0,1),1)), (((-1,0,0),2),((1,0,0),2))]
gens = [A] + [plaq(c, S) for c in range(3)]
stab = [M for M in O if same(gens, [rot_gen(g, M) for g in gens])]
print('stabilizer order', len(stab), '(T has 12)')
for legs in ([(1,0,0),(0,1,0),(0,0,1)], [(-1,0,0),(0,-1,0),(0,0,-1)], [(2,0,0),(0,2,0),(0,0,2)], [(1,0,0),(0,1,0),(-1,-1,0)], [(1,1,0),(0,1,1),(1,0,1)]):
    print('legs', legs, 'T-junction', t_junction(gens, 3, 0, legs, R=3))
MUL = {(1,2):(3,1),(2,1):(3,3),(2,3):(1,1),(3,2):(1,3),(3,1):(2,1),(1,3):(2,3)}
def torus(gens, L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    R_, ops = [], []
    for v in itertools.product(range(L), repeat=3):
        for g in gens:
            x = np.zeros(2*n, np.uint8); op = {}
            for p, labs in g.items():
                for a, l in enumerate(labs):
                    if not l: continue
                    q = idx([v[i] + p[i] for i in range(3)], a)
                    if q in op:
                        Q = op[q]; op[q] = 0 if Q == l else MUL[(Q, l)][0]
                    else: op[q] = l
            op = {q: l for q, l in op.items() if l}
            for q, l in op.items():
                if l in (1, 2): x[q] ^= 1
                if l in (2, 3): x[n + q] ^= 1
            R_.append(x); ops.append(op)
    r, N = c1.f2_rank_and_null(np.array(R_))
    return n - r, len(N)
for L in (4, 5, 6):
    print('torus L', L, '(log2 code dim, relations):', torus(gens, L), flush=True)
