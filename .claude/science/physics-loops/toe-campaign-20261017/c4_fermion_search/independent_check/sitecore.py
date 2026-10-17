"""Site-level tables built on my earlier independent core.py (indep_C3).
A string = 7-tuple of site codes (0..63), code = sum_a LX[l_a]<<a | LZ[l_a]<<(a+3)."""
import sys, itertools, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import POS, PIDX, O, act, LX, LZ, lab, TRANS, OVL, to_op, mul, eliminate, local_basis, torus_dim

def code_of(l3):
    c = 0
    for a, l in enumerate(l3):
        c |= LX[l] << a; c |= LZ[l] << (a + 3)
    return c
def labs_of(c): return tuple(lab((c >> a) & 1, (c >> (a + 3)) & 1) for a in range(3))
def to21(S7): return tuple(l for c in S7 for l in labs_of(c))
def from21(S21): return tuple(code_of(S21[3*i:3*i+3]) for i in range(7))

COMM = np.zeros((64, 64), np.uint8)
for p in range(64):
    for q in range(64):
        COMM[p, q] = bin(((p & 7) & (q >> 3)) ^ ((p >> 3) & (q & 7))).count('1') & 1

def tables(soldered):
    """SP[r][i]=site image, ROT[r][c]=code image, SG[r][c]=sign (soldered) of the site Pauli image."""
    SP = np.zeros((24, 7), int); ROT = np.zeros((24, 64), int); SG = np.ones((24, 64), int)
    for r, R in enumerate(O):
        for i in range(7): SP[r, i] = PIDX[tuple(int(v) for v in R.dot(POS[i]))]
        for c in range(64):
            S = [0]*21; S[0:3] = labs_of(c)
            s, T = act(R, tuple(S), soldered)
            ROT[r, c] = code_of(T[0:3]); SG[r, c] = s
    return SP, ROT, SG

def act7(r, S7, SP, ROT):
    out = [0]*7
    for i in range(7): out[SP[r, i]] = ROT[r, S7[i]]
    return tuple(out)

def comm_translates(S, T):
    """True iff S commutes with every translate of T (7-tuples)."""
    for t, pr in OVL.items():
        s = 0
        for i, j in pr: s ^= COMM[S[i], T[j]]
        if s: return False
    return True
