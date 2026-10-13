"""R18-1 s6 (written before running). Auxiliary bU = infinity check OUTSIDE the registered move set.
(1) MILP: minimal integer-invariant pattern delta in {-1,0,1} (G delta = 0 exactly; 4^3 box, every touched row imposed).
(2) Its signed rotations (shift action: delta -> sgn * delta), checked G delta = 0; distinct copies mod translation.
(3) MILP: a gamma = 0 configuration n in {0,1} at L, in the trivial coset, with 1 <= sum n <= 6V-1 (random objective).
(4) Uniform-measure MC on the gamma = 0 set: propose sigma*delta at a random base; accept iff n + sigma*delta in {0,1}.
    Symmetric proposals -> detailed balance for the uniform measure. Report acceptance, distinct states, S(k) channels.
Usage: python3 s6_binf.py L nsweeps seed"""
import numpy as np, itertools, sys, time, pickle
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, csr_matrix, hstack
from common import *
from mc import OFFS, kgrid_dirs
import numba as nb
L, NSW, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); V = L**3
t0 = time.time()
B = 4; slots = [(x, t) for x in itertools.product(range(B), repeat=3) for t in range(6)]; sidx = {s: i for i, s in enumerate(slots)}
rows = {}
for s in slots:
    for g, c in G_entries(*s): rows.setdefault(g, len(rows))
nS = len(slots); A = lil_matrix((len(rows), 2*nS))
for i, s in enumerate(slots):
    for g, c in G_entries(*s): A[rows[g], i] += c; A[rows[g], nS + i] -= c
cons = [LinearConstraint(A.tocsr(), 0, 0)]
P = lil_matrix((nS, 2*nS))
for i in range(nS): P[i, i] = 1; P[i, nS + i] = 1
cons.append(LinearConstraint(P.tocsr(), 0, 1))
lb = np.zeros(2*nS); ub = np.ones(2*nS); lb[sidx[((1, 1, 1), 3)]] = 1
res = milp(c=np.ones(2*nS), constraints=cons, integrality=np.ones(2*nS), bounds=Bounds(lb, ub), options={'time_limit': 60})
x = np.round(res.x).astype(int); d = x[:nS] - x[nS:]
pat = [(slots[i], int(d[i])) for i in range(nS) if d[i] != 0]
print("(1) minimal integer-invariant pattern: weight %d (%s)" % (len(pat), res.message), flush=True)
def rot_signed(supp, R):
    out = []
    for (xx, t), v in supp:
        i, j = TYPES[t]; p = R @ pos(xx, t)
        ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
        sgn = int(R[ii, i]*R[jj, j]); tt = TIDX[tuple(sorted((ii, jj)))]
        base = p - (0.5*(E3[ii] + E3[jj]) if ii != jj else 0)
        out.append(((tuple(int(round(b)) for b in base), tt), v*sgn))
    return out
def Gzero(supp):
    chk = {}
    for (xx, t), v in supp:
        for g, c in G_entries(xx, t): chk[g] = chk.get(g, 0) + c*v
    return all(v == 0 for v in chk.values())
orb = {}
for R in rot_mats():
    r = rot_signed(pat, R); xs = np.array([q[0][0] for q in r]); mn = xs.min(0)
    key = tuple(sorted(((tuple(np.array(q[0][0]) - mn), q[0][1]), q[1]) for q in r))
    keyneg = tuple(sorted((a, -b) for a, b in key))
    if key not in orb and keyneg not in orb: orb[key] = r
pats = list(orb.values())
print("(2) signed rotations: %d distinct copies mod translation and overall sign; all G delta = 0: %s" % (len(pats), all(Gzero(p) for p in pats)), flush=True)
# (3) a gamma = 0 configuration in the trivial coset
G = G_matrix(L); Bm = f2_basis(pattern_vectors(L))
def f2_null(Bm):
    M = (Bm % 2).astype(np.uint8).copy(); r, c = M.shape; piv = []; row = 0
    for col in range(c):
        pr = None
        for i in range(row, r):
            if M[i, col]: pr = i; break
        if pr is None: continue
        M[[row, pr]] = M[[pr, row]]; nz = np.nonzero(M[:, col])[0]; nz = nz[nz != row]; M[nz] ^= M[row]; piv.append(col); row += 1
        if row == r: break
    free = [j for j in range(c) if j not in set(piv)]; H = np.zeros((len(free), c), dtype=np.int64)
    for a, f in enumerate(free):
        H[a, f] = 1
        for i, pc in enumerate(piv):
            if M[i, f]: H[a, pc] = 1
    return H
H = f2_null(Bm); nH = H.shape[0]; nS6 = 6*V
A1 = hstack([csr_matrix(G), csr_matrix((G.shape[0], nH))]); A2 = hstack([csr_matrix(H), csr_matrix(-2*np.eye(nH))])
A3 = hstack([csr_matrix(np.ones((1, nS6))), csr_matrix((1, nH))])
rng = np.random.default_rng(seed)
r3 = milp(c=np.concatenate([rng.normal(size=nS6), np.zeros(nH)]), constraints=[LinearConstraint(A1, 0, 0), LinearConstraint(A2, 0, 0), LinearConstraint(A3, nS6//4, 3*nS6//4)],
          integrality=np.ones(nS6 + nH), bounds=Bounds(np.zeros(nS6 + nH), np.concatenate([np.ones(nS6), np.full(nH, nS6)])), options={'time_limit': 120})
if r3.x is None:
    print("(3) L=%d: no gamma=0 configuration found within the time limit (%s)" % (L, r3.message)); sys.exit()
n0 = np.round(r3.x[:nS6]).astype(np.int64)
print("(3) L=%d: gamma=0 start configuration: sum n = %d, G n = 0: %s, in trivial coset: %s (%.0fs)" %
      (L, n0.sum(), bool(np.all(G @ n0 == 0)), bool(np.all((H @ n0) % 2 == 0)), time.time() - t0), flush=True)
# (4) MC
maxw = max(len(p) for p in pats); PT = np.zeros((len(pats), maxw, 5), dtype=np.int64)
for a, p in enumerate(pats):
    for b, ((xx, t), v) in enumerate(p): PT[a, b] = (xx[0], xx[1], xx[2], t, v)
NW = np.array([len(p) for p in pats])
@nb.njit(cache=True)
def run(n, L, PT, NW, nmoves, sd):
    np.random.seed(sd); acc = 0
    for m in range(nmoves):
        a = np.random.randint(PT.shape[0]); bx = np.random.randint(L); by = np.random.randint(L); bz = np.random.randint(L)
        sg = 1 if np.random.random() < 0.5 else -1; ok = True
        for b in range(NW[a]):
            t = PT[a, b, 3]; v = sg*PT[a, b, 4]
            s = n[t, (bx + PT[a, b, 0]) % L, (by + PT[a, b, 1]) % L, (bz + PT[a, b, 2]) % L] + v
            if s < 0 or s > 1: ok = False; break
        if ok:
            acc += 1
            for b in range(NW[a]):
                t = PT[a, b, 3]; v = sg*PT[a, b, 4]
                n[t, (bx + PT[a, b, 0]) % L, (by + PT[a, b, 1]) % L, (bz + PT[a, b, 2]) % L] += v
    return acc
n = n0.reshape(6, L, L, L).copy()
kd = kgrid_dirs(L); klist = [(nm, m, v) for nm, lst in kd.items() for m, vecs in lst for v in vecs]
K = np.array([2*np.pi*np.array(v)/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist]); ph = np.exp(-1j*(K @ OFFS.T))
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); accs = 0; seen = set(); per = max(NSW//nb_, 1)
moves_per = len(pats)*V
for b in range(nb_):
    for it in range(per):
        accs += run(n, L, PT, NW, moves_per, seed*100000 + b*1000 + it)
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T*ph
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F)/V; seen.add(hash(n.tobytes()))
    Mb[b] /= per
assert np.all(G @ n.reshape(-1) == 0)
print("(4) L=%d uniform gamma=0 MC: %d sweeps x %d moves, acceptance %.2e, distinct measured states %d of %d, gamma=0 preserved: True (%.0fs)" %
      (L, nb_*per, moves_per, accs/(nb_*per*moves_per), len(seen), nb_*per, time.time() - t0), flush=True)
pickle.dump(dict(L=L, bU=np.inf, klist=klist, K=K, Mb=Mb, Gb=np.zeros((nb_, len(klist))), Eb=np.zeros(nb_), Etr=np.zeros(3), acc=accs/(nb_*per*moves_per),
                 secs=time.time() - t0, neq=0, nme=nb_*per, every=1, init="binf"), open("../data/binf_L%d.pkl" % L, "wb"))
