"""Two qubits per site (spin soldered by ACTION, flavour unsoldered): star-supported
cubic-covariant Pauli rules. Vectorized filter over all 16^7 strings.

Site label L = 4*s + f, s = spin Pauli, f = flavour Pauli (0=I,1=X,2=Y,3=Z).
Keep g if g commutes with every translate (overlapping) of R g for every R in O.
"""
import itertools, sys, time, pickle
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
ACTION = sys.argv[1] if len(sys.argv) > 1 else 'full'
FACTION = sys.argv[2] if len(sys.argv) > 2 else 'trivial'
O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)

def sp1(a, b): return int(a != 0 and b != 0 and a != b)
SP = np.array([[sp1(l1 >> 2, l2 >> 2) ^ sp1(l1 & 3, l2 & 3) for l2 in range(16)] for l1 in range(16)], np.uint8)

def labmap(Qm):
    m = np.zeros(4, int); m[0] = 0
    for a in (1, 2, 3):
        col = Qm[:, a - 1]; m[a] = int(np.nonzero(col)[0][0]) + 1
    return m
RT = []   # (position permutation, 16-label map)
for M in O:
    pos = [SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR]
    ms, mf = labmap(c1.Q(M, ACTION)), labmap(c1.Q(M, FACTION))
    lm = np.array([4 * ms[l >> 2] + mf[l & 3] for l in range(16)], np.uint32)
    RT.append((pos, lm))
# overlaps: shift s; pairs (i, j) with STAR[i] == STAR[j] + s  (g at 0, other at s)
SH = []
for s in itertools.product(range(-2, 3), repeat=3):
    pr = [(i, j) for i in range(7) for j in range(7) if tuple(np.subtract(STAR[i], STAR[j])) == s]
    if pr: SH.append((s, pr))
log('shifts with overlap', len(SH))

def nib(a, i): return (a >> (4 * i)) & 15
def transform(a, k):
    pos, lm = RT[k]; out = np.zeros_like(a)
    for i in range(7): out |= lm[nib(a, i)] << (4 * pos[i])
    return out
def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for s, pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr: par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok

N = 16 ** 7; CH = 1 << 22; surv = []
for start in range(0, N, CH):
    a = np.arange(start, min(N, start + CH), dtype=np.uint32)
    if start == 0: a = a[1:]
    a = a[commutes_all(a, a)]
    for k in range(1, 24):
        if a.size == 0: break
        a = a[commutes_all(a, transform(a, k))]
    surv.append(a)
    if (start // CH) % 8 == 0: log(f'chunk {start // CH}/{N // CH}: survivors so far {sum(x.size for x in surv)}')
S = np.concatenate(surv); log('self-orbit-commuting strings', S.size)
pickle.dump(S, open(f'surv_{ACTION}_{FACTION}.pkl', 'wb'))
