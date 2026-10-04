"""A53 bench24: 24-site tilted cluster (lattice 2*(1,-1,0), 2*(0,1,-1), 2*(1,1,1)): parton closed shell, wrapped pair
types, sector size, one matvec timing, parton amplitudes (saved) and its exact <H>/N.  Usage: bench24.py L KEY"""
import sys, signal, time, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
t0 = time.time(); L, key = int(sys.argv[1]), sys.argv[2]
cl = Cluster(np.array([[2, 0, 2], [-2, 2, 2], [0, -2, 2]])); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
Phi, gap = mf_state(cl); hev = None
print(f"N={N}; parton MF gap at half filling {gap:.4f}  [{time.time()-t0:.1f}s]", flush=True)
for tw in [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0)]:
    print(f"   (other twists, info) twist {np.round(tw,2)}: gap {mf_state(cl, twist=tw)[1]:.4f}")
disp = [d for k in [(0, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 2)] for d in class_vectors(k)]
mult = {}
for i in range(N):
    for d in disp:
        j = f(X[i] + np.array(d)); assert j != i
        mult.setdefault((min(i, j), max(i, j)), []).append(tuple(sorted(np.abs(d))))
types = {}
for i in range(N):
    for j in range(i + 1, N):
        v = mult.get((i, j)); t = "far" if v is None else "+".join(f"{k[0]}{k[1]}{k[2]}x{v.count(k)}" for k in sorted(set(v)))
        types.setdefault(t, []).append((i, j))
print("pair types: " + ", ".join(f"{t}:{len(v)}" for t, v in sorted(types.items())))
ks, J, c4 = load_rule(L, key)
H = Ham(X, f, ks, J, c4); S = Sector(N, flip=True)
print(f"rule L{L} {key}: {len(H.pairs)} pairs; sector (flip-even) {S.D}  [{time.time()-t0:.1f}s]", flush=True)
mv = make_mv(H, S); x = np.random.default_rng(1).standard_normal(S.D); x /= np.linalg.norm(x)
t1 = time.time(); y = mv(x); t2 = time.time(); y = mv(x); t3 = time.time()
print(f"matvec: first (incl. compile) {t2-t1:.1f}s, second {t3-t2:.2f}s; <x|H|x>/N {x @ y / N:+.5f}", flush=True)
psi = parton_vector(cl, S, Phi); print(f"parton amplitudes {time.time()-t3:.1f}s; max|Im|/max|psi| {np.abs(psi.imag).max()/np.abs(psi).max():.1e}", flush=True)
p = psi.real / np.linalg.norm(psi.real); Hp = mv(p); E = p @ Hp / N; var = (Hp @ Hp - (E * N) ** 2) / N
print(f"parton <H>/N {E:+.6f}; var/N {var:.4f}  [{time.time()-t0:.1f}s]")
np.save("parton24.npy", p)
