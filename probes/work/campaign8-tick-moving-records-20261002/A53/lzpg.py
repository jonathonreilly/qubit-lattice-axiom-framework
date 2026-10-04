"""A53 lzpg: lowest state of the wrapped rule on the 24-site cluster INSIDE THE PARTON'S SYMMETRY SECTOR.
Operator A = P_pg D H, with D = prod_a (2 + T_a + T_a^-1)/4 (identity at k = 0, damps k != 0, kills T = -1) and
P_pg = (1/12) sum_g chi(g) g over the cluster point group D3d (coordinate permutations x {+-1}; chi = parton's own
characters, checked to be +-1).  Rule invariance under every g and T_a is checked first.  Start vector = parton, so
|<parton|Ritz_0>|^2 = y_0^2.  Pass 1 only, checkpointed.  Usage: lzpg.py L KEY"""
import sys, signal, time, os, numpy as np
from scipy.linalg import eigh_tridiagonal
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from a53lib import _rank
t0 = time.time(); L, key = int(sys.argv[1]), sys.argv[2]; BUDGET = 240.; MAXM = 110; tag = f"pgA1_L{L}_{key}"; ck = f"lzck_{tag}.npz"
cl = Cluster(np.array([[2, 0, 2], [-2, 2, 2], [0, -2, 2]])); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
ks, J, c4 = load_rule(L, key); H = Ham(X, f, ks, J, c4); S = Sector(N, flip=True); mv = make_mv(H, S)
@nb.njit(cache=True)
def _papply(x, confs, perm, offset, idxlo, h, lomask, flip, top, full):
    y = np.empty_like(x)
    for k in range(len(confs)):
        c = confs[k]; c2 = 0
        for i in range(len(perm)): c2 |= ((c >> i) & 1) << perm[i]
        y[k] = x[_rank(c2, offset, idxlo, h, lomask, flip, top, full)]
    return y
G = lambda x, pm: _papply(x, S.confs, pm, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)
TR = []
for a in range(3):
    pf = np.array([f(X[i] + np.eye(3, dtype=int)[a]) for i in range(N)], np.int64); TR.append((pf, np.argsort(pf).astype(np.int64)))
PG = []
for perm in itertools.permutations(range(3)):
    for sg in (1, -1):
        R = sg * np.eye(3, dtype=int)[list(perm)]
        pm = np.array([f(R @ X[i]) for i in range(N)], np.int64); assert len(set(pm)) == N; PG.append(pm)
p = np.load("parton24.npy"); p /= np.linalg.norm(p)
BP = bilinear_pairs(X, f, ks, J); FS = four_sets(X, f, c4)
def term_defect(pm):
    d = 0.
    for (i, j), v in BP.items():
        d = max(d, abs(BP.get((min(pm[i], pm[j]), max(pm[i], pm[j])), 0.) - v))
    for Sg, w in FS.items():
        cs = [int(pm[s]) for s in Sg]; o = sorted(range(4), key=lambda q: cs[q]); S2 = tuple(cs[q] for q in o)
        inv_ = {o[q]: q for q in range(4)}; w2 = FS.get(S2, np.zeros(3)); ww = np.zeros(3)
        for pi, ((u, v), (x_, y)) in enumerate(PAIRINGS):
            pr = tuple(sorted(tuple(sorted((inv_[a], inv_[b]))) for a, b in ((u, v), (x_, y)))); ww[PAIRINGS.index(pr)] += w[pi]
        d = max(d, np.abs(w2 - ww).max())
    return d
defs = [term_defect(pm) for pm in PG]; tdef = [term_defect(t[0]) for t in TR]
keep = [k for k in range(len(PG)) if defs[k] < 1e-12]; PG = [PG[k] for k in keep]
rng = np.random.default_rng(3); x = rng.standard_normal(S.D); Hx = mv(x)
inv = max(np.abs(mv(G(x, pm)) - G(Hx, pm)).max() for pm in PG[1:3] + [TR[0][0]]) / np.abs(Hx).max()
chi = np.array([p @ G(p, pm) for pm in PG])
print(f"[{tag}] term-list defects: point group {np.round(defs, 12)}, translations {tdef}; kept {len(PG)} elements {keep}; "
      f"matvec invariance check {inv:.1e}; parton characters {np.round(chi, 6)}  [{time.time()-t0:.0f}s]", flush=True)
assert inv < 1e-12 and max(tdef) < 1e-12
wA1 = chi.sum() / len(PG)                     # parton weight in the trivial irrep (A1) of the kept rotation group
print(f"  kept group = proper rotations (D3); parton weight in A1 (k=0 part already 1): {wA1:.6f}", flush=True)
chi = np.ones(len(PG))                        # project onto A1
def symm(w):
    for pf, pb in TR:
        w = (2 * w + G(w, pf) + G(w, pb)) / 4
    out = np.zeros_like(w)
    for c, pm in zip(chi, PG): out += c * G(w, pm)
    return out / len(PG)
pA = symm(p); print(f"  |P_A1 D p|^2 = {pA @ pA:.6f} (should equal the A1 weight)", flush=True); pA /= np.linalg.norm(pA)
if os.path.exists(ck):
    Z = np.load(ck); j = int(Z["j"]); al = list(Z["al"]); be = list(Z["be"]); vp, v = Z["vp"], Z["v"]
else:
    j, al, be, vp, v = 0, [], [0.], np.zeros(S.D), pA.copy()
done = False
while time.time() - t0 < BUDGET:
    w = symm(mv(v)) - be[j] * vp; a = w @ v; w -= a * v; w -= (w @ v) * v; b = np.linalg.norm(w)
    al.append(a); be.append(b); vp, v = v, w / b; j += 1
    if j % 10 == 0 or j >= MAXM:
        th, U = eigh_tridiagonal(np.array(al), np.array(be[1:j]), select='i', select_range=(0, 2))
        print(f"  step {j}: Ritz/N {th[0]/N:+.8f} {th[1]/N:+.8f} {th[2]/N:+.8f}; resid est {be[j]*abs(U[-1,0]):.1e}; "
              f"|<p_A1|Ritz_k>|^2 {U[0,0]**2:.4e} {U[0,1]**2:.3e} {U[0,2]**2:.3e} (x wA1 {wA1:.4f} for the parton)  [{time.time()-t0:.0f}s]", flush=True)
        if j >= MAXM or be[j] * abs(U[-1, 0]) < 1e-6:
            done = True; break
if done:
    os.remove(ck) if os.path.exists(ck) else None; print(f"DONE {tag}")
else:
    np.savez(ck, j=j, al=np.array(al), be=np.array(be), vp=vp, v=v); print(f"  checkpoint step {j}  [{time.time()-t0:.0f}s]")
