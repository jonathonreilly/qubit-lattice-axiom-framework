"""T67 Test C: which cubic irreps (of the 24 proper rotations about a site) can a shell of neighbours carry?
Sym^2(R^3) = A1 + E + T2 (metric perturbation h_ij).  Shear (h_xy etc.) is the T2 part.
"""
import itertools, numpy as np
R = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3):
            M[i, p[i]] = s[i]
        if round(np.linalg.det(M)) == 1:
            R.append(M)
assert len(R) == 24
def cls(M):
    tr = np.trace(M); 
    if tr == 3: return "E"
    if tr == 0: return "8C3"
    if tr == -1: return "3C2"
    # tr == 1: C4 (rotation by 90) ; tr == -1 also C2'?  distinguish via M^2
    return "6C4"
# characters by class using (trace, trace of M^2)
def key(M): return (int(np.trace(M)), int(np.trace(M @ M)))
# irreps of O: classes E(1), 8C3, 3C2 (=C4^2), 6C4, 6C2'
chi = {
 "A1": {"E":1,"C3":1,"C2":1,"C4":1,"C2p":1},
 "A2": {"E":1,"C3":1,"C2":1,"C4":-1,"C2p":-1},
 "E":  {"E":2,"C3":-1,"C2":2,"C4":0,"C2p":0},
 "T1": {"E":3,"C3":0,"C2":-1,"C4":1,"C2p":-1},
 "T2": {"E":3,"C3":0,"C2":-1,"C4":-1,"C2p":1},
}
def cname(M):
    t = int(np.trace(M)); t2 = int(np.trace(M @ M))
    if t == 3: return "E"
    if t == 0: return "C3"
    if t == 1: return "C4"
    if t == -1 and t2 == 3: return "C2"     # M^2 = 1 and trace -1: rotation by pi about a coordinate axis
    if t == -1 and t2 == 3: return "C2"
    return "C2p"
# separate C2 (about coordinate axis, diag entries) from C2' (about edge axis: permutes axes)
def cname2(M):
    t = int(np.trace(M))
    if t == 3: return "E"
    if t == 0: return "C3"
    if t == 1: return "C4"
    # t == -1: C2 about coordinate axis is diagonal; C2' is not
    return "C2" if np.count_nonzero(M) == 3 and np.all(M == np.diag(np.diag(M))) else "C2p"
cls_of = [cname2(M) for M in R]
from collections import Counter
print("class sizes:", Counter(cls_of))
def shell(vs):
    return [np.array(v) for v in vs]
shells = {
 "NN (6, distance 1)":   [v for v in itertools.product([-1,0,1], repeat=3) if sum(map(abs,v))==1],
 "NNN (12, sqrt2)":      [v for v in itertools.product([-1,0,1], repeat=3) if sum(map(abs,v))==2],
 "NNNN (8, sqrt3)":      [v for v in itertools.product([-1,0,1], repeat=3) if sum(map(abs,v))==3],
}
def perm_char(vs, M):
    S = {tuple(v) for v in vs}
    return sum(1 for v in vs if tuple(M @ np.array(v)) == tuple(v))
print("target: metric perturbation Sym^2(R^3) decomposes as A1 + E + T2 (shear = T2)")
for name, vs in shells.items():
    ch = [perm_char(vs, M) for M in R]
    mult = {}
    for ir, c in chi.items():
        mult[ir] = round(sum(ch[i] * c[cls_of[i]] for i in range(24)) / 24)
    print(f"{name:22s}: permutation rep = " + " + ".join(f"{m}{ir}" for ir, m in mult.items() if m) )
# axis-directed bond data (one number per undirected axis bond): E+A1 only
print("bond scalar on the 3 undirected axes = the 3-dim rep on {x,y,z}: contains A1+E, no T2")

# undirected lines (unordered {v,-v}) of each shell
def line_char(vs, M):
    L = {frozenset([tuple(v), tuple(-np.array(v))]) for v in vs}
    return sum(1 for l in L if frozenset(tuple(M @ np.array(v)) for v in l) == l), len(L)
for name, vs in shells.items():
    ch = []
    for M in R:
        c, n = line_char(vs, M)
        ch.append(c)
    mult = {ir: round(sum(ch[i] * c[cls_of[i]] for i in range(24)) / 24) for ir, c in chi.items()}
    print(f"undirected lines of {name:22s} ({n}): " + " + ".join(f"{m}{ir}" for ir, m in mult.items() if m))
print("=> Sym^2(R^3)=A1+E+T2 (6 metric components) is carried exactly by the 6 undirected face-diagonal lines; the 3 axis lines carry only A1+E.")
