"""Independent checker setup (fresh-context agent). Uses only the upstream graph/PSG
definitions (vertices, edges, cycles, rot_vert, trans_vert, psg_sign, gf2_solve).
The translation-invariant gauge is built by a different route from the runner:
GF(2) solve on the full L=4 lattice with explicit translation-invariance rows."""
import itertools, os, sys
import numpy as np

REPO = '/home/user/qubit-lattice-axiom-framework'
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
C = _model._run_reviewed_program(definitions_only=True)

L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']
DIRS = C['DIRS']; VID = C['VID']; EDGES = C['EDGES']; EID = C['EID']; nE = C['nE']
F = dict(square=1, triangle=0, plaquette=1, tube=1)

# ---- gauge: flux rows + u_e = u_{T e} rows for the three unit translations
rows, rhs = [], []
for k, cs in C['cycles'].items():
    for c in cs:
        rows.append(c); rhs.append(F[k])
for t in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    for key in EDGES:
        i, j = tuple(key)
        ti = VID[C['trans_vert'](t, VERTS[i])]; tj = VID[C['trans_vert'](t, VERTS[j])]
        e2 = EID[frozenset((ti, tj))]
        if e2 != EID[key]:
            rows.append([EID[key], e2]); rhs.append(0)
u = C['gf2_solve'](rows, rhs, nE)
assert u is not None
for k, cs in C['cycles'].items():
    assert {int(sum(u[j] for j in c) % 2) for c in cs} == {F[k]}

# ---- signed permutation ops: op = (P, s): basis i -> (-1)^s[i] basis P[i]
def psg(f):
    P, s = C['psg_sign'](f, u)
    assert s is not None
    return (np.asarray(P), np.asarray(s, np.uint8))
def compose(A, B):  # A after B
    PA, sA = A; PB, sB = B
    return (PA[PB], sB ^ sA[PB])
def inverse(A):
    P, s = A; Pi = np.empty_like(P); Pi[P] = np.arange(len(P)); return (Pi, s[Pi])
def dense(A, phase=1.0):
    P, s = A; M = np.zeros((nV, nV), complex); M[P, np.arange(nV)] = (-1.0) ** s; return M * phase
def const_sign(A):
    """If A is +-identity return +1/-1, else None."""
    P, s = A
    if not (P == np.arange(nV)).all() or len(set(s.tolist())) != 1: return None
    return -1 if s[0] else 1

def w1(R):
    p = [DIRS.index(tuple(int(x) for x in R @ np.array(d))) for d in DIRS]; sgn = 1
    for i in range(6):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
    return 0 if sgn == 1 else 1
W1 = [w1(R) for R in ROTS]
ROT = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
INV = psg(lambda q: C['rot_vert'](-np.eye(3, dtype=int), q))
TV = list(itertools.product(range(L), repeat=3))
TR = {t: psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV}
assert all(len(set(TR[t][1].tolist())) == 1 for t in TV)
TR = {t: (P, np.zeros_like(s)) for t, (P, s) in TR.items()}  # translations act without gauge signs

CI = {c: i for i, c in enumerate(CORN)}
def Bloch(k):
    B = np.zeros((nV, 12), complex)
    for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
    return B
kst = np.array([1, -1, 1]) * np.pi / 2
def dmod(x): return ((x + 1) % L) - 1
loc0 = [VID[((0, 0, 0), c)] for c in CORN]

def conj_mat(Hm, A):
    """A H A^{-1} for signed permutation A."""
    P, s = A; sg = (-1.0) ** s; Y = np.zeros_like(Hm); Y[np.ix_(P, P)] = Hm * np.outer(sg, sg); return Y
