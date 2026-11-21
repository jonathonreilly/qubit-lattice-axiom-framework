"""Criterion (written first). Colour form of Prop 2.2, used at line 336 and never written in the text.
K_col(E) := -2 sum_cyc A^col_k(E_i, E_j) + 2 eps_abc eps_fgh sum_p V_p(E_1^{af}, E_2^{bg}, E_3^{ch}), E_i^{af} = delta^{af} G J_i + grad theta_i^{af}.
Isotropic limit must return K_total (check to 1e-10). PASS if K_col does not change, relative 1e-10, under random colour-mixing theta_i^{af} on all three slots at once.
If it changes, line 336 and therefore Theorem 3.8 for colour-mixing gauge parts fail."""
import numpy as np
from wnlib import *

T = 6
d = 4
rng = np.random.default_rng(8)
x = (3,) * 4
tails = line(x, 3, 2)
p1 = plaq(x, 0, 1)
p2 = lasso(tails[0], plaq(tails[1], 1, 2))
t3, e3 = line(x, 1, -2)
p3 = lasso(t3, plaq(e3, 2, 0))
paths = [p1, p2, p3]
Js = [current(p, T, d) for p in paths]
Es0 = [green(J, T, d) for J in Js]
eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def amn(M, N):
    return np.trace(M) * np.trace(N) - np.trace(M @ N)


def Acol(path, E, F):
    # E, F: dict-like arrays shape (3,3,d,T...)
    inc = [(b[2], (b[1],) + tuple(c % T for c in b[0])) for b in path]
    Em = [s * np.array([[E[a, f][i] for f in range(3)] for a in range(3)]) for s, i in inc]
    Fm = [s * np.array([[F[a, f][i] for f in range(3)] for a in range(3)]) for s, i in inc]
    tot = 0.0
    for s in range(len(inc)):
        for t in range(s + 1, len(inc)):
            tot += amn(Em[s], Fm[t]) - amn(Em[t], Fm[s])
    return tot


def Kcol(E1, E2, E3):
    kc = -2 * (Acol(paths[0], E2, E3) + Acol(paths[1], E3, E1) + Acol(paths[2], E1, E2))
    kv = 0.0
    for (a, b, c), s1 in eps.items():
        for (f, g, h), s2 in eps.items():
            kv += s1 * s2 * sumV(E1[a, f], E2[b, g], E3[c, h], T, d)
    return kc, 2 * kv


def iso(E):
    out = np.zeros((3, 3) + E.shape)
    for a in range(3):
        out[a, a] = E
    return out


E = [iso(e) for e in Es0]
kc0 = K_comp(paths, Es0, T)
kv0 = 12 * sumV(*Es0, T, d)
kc1, kv1 = Kcol(*E)
print(f"isotropic: K_comp {kc0:.10f} vs {kc1:.10f}; K_vert {kv0:.10f} vs {kv1:.10f}")
base = kc1 + kv1
for trial in range(4):
    Es = [e.copy() for e in E]
    for i in range(3):
        for a in range(3):
            for f in range(3):
                Es[i][a, f] = Es[i][a, f] + grad0(0.2 * rng.normal(size=(T,) * d), d)
    kc, kv = Kcol(*Es)
    print(f"trial {trial}: K_comp_col {kc:.6f}, K_vert_col {kv:.6f}, total {kc+kv:.10f}, rel change {abs(kc+kv-base)/abs(base):.2e}", flush=True)
