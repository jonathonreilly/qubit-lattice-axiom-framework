"""A53 an24: anatomy of the 24-site Lanczos state vs the parton (same quantities as t1_16) + translation eigenvalues.
Usage: an24.py L KEY TAG     (loads gs24_<TAG>.npy and parton24.npy)"""
import sys, signal, time, numpy as np
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from a53lib import _rank
t0 = time.time(); L, key, tag = int(sys.argv[1]), sys.argv[2], sys.argv[3]; once = tag.endswith("_once")
cl = Cluster(np.array([[2, 0, 2], [-2, 2, 2], [0, -2, 2]])); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
ks, J, c4 = load_rule(L, key); H = Ham(X, f, ks, J, c4, once=once); S = Sector(N, flip=True); mv = make_mv(H, S)
g = np.load(f"gs24_{tag}.npy"); p = np.load("parton24.npy"); g /= np.linalg.norm(g); p /= np.linalg.norm(p)
Hg = mv(g); Eg = g @ Hg; Hp = mv(p); Ep = p @ Hp
print(f"[{tag}] GS <H>/N {Eg/N:+.8f} (residual {np.linalg.norm(Hg - Eg*g):.1e}); parton <H>/N {Ep/N:+.6f}; gap {(Ep-Eg)/N:+.4f}/site; "
      f"|<GS|parton>|^2 {(g @ p)**2:.3e}; parton weight on <H> below its own mean: E_p var/N {(Hp@Hp - Ep**2)/N:.4f}", flush=True)

@nb.njit(cache=True)
def _permov(x, y, confs, perm, offset, idxlo, h, lomask, flip, top, full):
    s = 0.
    for k in range(len(confs)):
        c = confs[k]; c2 = 0
        for i in range(len(perm)):
            c2 |= ((c >> i) & 1) << perm[i]
        s += x[k] * y[_rank(c2, offset, idxlo, h, lomask, flip, top, full)]
    return s
for a in range(3):
    perm = np.array([f(X[i] + np.eye(3, dtype=int)[a]) for i in range(N)], np.int64)
    tg = _permov(g, g, S.confs, perm, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)
    tp = _permov(p, p, S.confs, perm, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)
    print(f"  <T_e{a+1}>: GS {tg:+.6f}   parton {tp:+.6f}")
disp = [d for k in [(0, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 2)] for d in class_vectors(k)]
mult = {}
for i in range(N):
    for d in disp:
        j = f(X[i] + np.array(d)); mult.setdefault((min(i, j), max(i, j)), []).append(tuple(sorted(np.abs(d))))
types = {}
for i in range(N):
    for j in range(i + 1, N):
        v = mult.get((i, j)); t = "far" if v is None else "+".join(f"{k[0]}{k[1]}{k[2]}x{v.count(k)}" for k in sorted(set(v)))
        types.setdefault(t, []).append((i, j))
Cg = paircorr(g, S); Cp = paircorr(p, S)
print(f"  S check: GS {Cg.sum()/4:.1e}, parton {Cp.sum()/4:.1e}  [{time.time()-t0:.0f}s]")
for t, v in sorted(types.items()):
    a = np.array([Cg[i, j] for i, j in v]); b = np.array([Cp[i, j] for i, j in v])
    print(f"  <s.s> {t:12s} ({len(v):2d} pairs): GS mean {a.mean():+.4f} (min {a.min():+.4f} max {a.max():+.4f})   parton {b.mean():+.4f}")
parts_g, parts_p = [], []
for kc, Jc in zip(ks, J):
    if abs(Jc) < 1e-12: continue
    m1 = make_mv(Ham(X, f, [kc], [1.], np.zeros(8), once=once), S); parts_g.append(f"{kc}:{Jc:+.3f}*{g @ m1(g)/N:+.3f}"); parts_p.append(f"{kc}:{p @ m1(p)/N:+.3f}")
for k in range(8):
    if abs(c4[k]) < 1e-12: continue
    m1 = make_mv(Ham(X, f, [], [], np.eye(8)[k]), S); parts_g.append(f"{F4N[k]}:{c4[k]:+.3f}*{g @ m1(g)/N:+.3f}"); parts_p.append(f"{F4N[k]}:{p @ m1(p)/N:+.3f}")
print("  GS decomposition (coef*<op>/N): " + " ".join(parts_g)); print("  parton <op>/N: " + " ".join(parts_p), flush=True)
P8 = spin_projectors(8); P4 = spin_projectors(4); P3 = spin_projectors(3)
cubes = [[f(X[a] + np.array(o)) for o in itertools.product((0, 1), repeat=3)] for a in range(N)]
plaqs = []
for a in range(N):
    for (u, w) in ((0, 1), (0, 2), (1, 2)):
        e = np.eye(3, dtype=int); plaqs.append([f(X[a]), f(X[a] + e[u]), f(X[a] + e[u] + e[w]), f(X[a] + e[w])])
tris = sorted({tuple(sorted([f(X[a]), f(X[a] + np.array([2, 0, 0])), f(X[a] + np.array([4, 0, 0]))])) for a in range(N)})
for nm, vec in (("GS", g), ("parton", p)):
    v = full_vector(vec, S)
    cw = np.array([np.trace(rdm(v, N, cb) @ P8[0.0]) for cb in cubes]); pw = np.array([np.trace(rdm(v, N, pq) @ P4[0.0]) for pq in plaqs])
    tw = np.array([np.trace(rdm(v, N, list(tr)) @ P3[0.5]) for tr in tris])
    print(f"  {nm}: singlet weight cubes {cw.mean():.3f} [{cw.min():.3f},{cw.max():.3f}] (random 0.055); plaquettes {pw.mean():.3f} "
          f"[{pw.min():.3f},{pw.max():.3f}] (random 0.125); (002)-triangles S=1/2 weight {tw.mean():.3f} (random 0.5; {len(tris)} triangles)  [{time.time()-t0:.0f}s]", flush=True)
    del v
# cube-singlet product placed on the 24-site cluster (three 2x2x2 cubes tile it: 2Z^3 / lattice = Z_3)
from t2_prod import lowest_singlets
loc = [np.array(o) for o in itertools.product(range(2), repeat=3)]; fo = open_index(loc)
sing, Sc, _ = lowest_singlets(bilinear_pairs(loc, fo, ks, J), four_sets(loc, fo, c4), 8)
E0c, xc, _ = sing[0]; amp = np.zeros(256); amp[Sc.confs] = xc
if Sc.flip: amp[(~Sc.confs) & Sc.full] = xc
amp /= np.linalg.norm(amp)
origins = [np.array([0, 0, 0]), np.array([2, 0, 0]), np.array([4, 0, 0])]
cubesites = [[f(o + l) for l in loc] for o in origins]; assert len(set(sum(cubesites, []))) == N
Psi = np.ones(S.D)
for cs in cubesites:
    pat = np.zeros(S.D, np.int64)
    for l, s in enumerate(cs): pat |= ((S.confs >> s) & 1) << l
    Psi *= amp[pat]
Psi /= np.linalg.norm(Psi); Ec = Psi @ mv(Psi) / N
print(f"  cube-singlet product on the 24-site cluster: open-cube GS E/8 {E0c/8:+.5f}; wrapped <H>/N {Ec:+.5f}; "
      f"|<GS|cubes>|^2 {(Psi @ g)**2:.4f}; |<parton|cubes>|^2 {(Psi @ p)**2:.4f}  [{time.time()-t0:.0f}s]")
