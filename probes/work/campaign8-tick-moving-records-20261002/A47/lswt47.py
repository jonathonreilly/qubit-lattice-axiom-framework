"""A47 lswt47: spin-wave (LSWT) energies of Neel and collinear (pi,pi,0) states for the dual-frame J1-J2
Heisenberg rule (J1' = 1), j = 0.20..0.40.  A43 Holstein-Primakoff library + appended face-diagonal bonds
(same construction as A44 star_j2.py).  E per NN bond = E_site / 3.  Stability = min BdG eigenvalue >= 0."""
import itertools, signal, numpy as np
signal.alarm(200)
D = __file__.rsplit('/', 2)[0]
src = open(D + "/A43/w2_lswt.py").read().split("# 1. Heisenberg ferromagnet")[0]
ns = {}; exec(compile(src, "A43_w2lib", "exec"), ns); Lattice, couplings = ns["Lattice"], ns["couplings"]
FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
cell8 = [list(p) for p in itertools.product([0, 1], repeat=3)]
def make(ms, j):
    lat = Lattice(2 * np.eye(3), cell8, ms, couplings(J=1.))
    for r in range(lat.n):
        for d in FD:
            yv = lat.tau[r] + np.array(d, float)
            for rp in range(lat.n):
                nn = lat.Binv @ (yv - lat.tau[rp])
                if np.allclose(nn, np.round(nn)):
                    lat.bonds.append((r, rp, lat.B @ np.round(nn), 4 * j * np.eye(3))); break
    return lat
def lswt(lat, nk):
    g = (np.arange(nk) + 0.5) / nk * 2 * np.pi - np.pi; Rb = 2 * np.pi * np.linalg.inv(lat.B)
    tot = 0.; minM = np.inf
    for f in itertools.product(g, g, g):
        k = (np.array(f) / (2 * np.pi)) @ Rb
        A, Bm = lat.blocks(k); minM = min(minM, np.linalg.eigvalsh(lat.M(k)).min())
        tot += np.sum(lat.omega(k).real) - np.trace(A).real
    return lat.energy() + 0.5 * tot / nk ** 3 / lat.n, minM
neel8 = [((-1) ** sum(p)) * np.array([0, 0, 1.]) for p in cell8]
col8 = [((-1) ** (p[0] + p[1])) * np.array([0, 0, 1.]) for p in cell8]
rows = []
print("j    | Neel: E_cl/bond  E_LSWT/bond (nk=6, 8)  stable | collinear: E_cl/bond  E_LSWT/bond (nk=6, 8)  stable")
for j in (0.2, 0.25, 0.3, 0.35, 0.4):
    out = []
    row = [j]
    for ms in (neel8, col8):
        lat = make(ms, j); e6, m6 = lswt(lat, 6); e8, m8 = lswt(lat, 8)
        row += [e8 / 3, float(min(m6, m8) > -1e-7), abs(e8 - e6) / 3]
        out.append(f"{lat.energy()/3:+.5f}  {e6/3:+.5f} {e8/3:+.5f}  {'yes' if min(m6, m8) > -1e-7 else 'NO (min %.2e)' % min(m6, m8)}")
    print(f"{j:.2f} | {out[0]} | {out[1]}", flush=True); rows.append(row)
np.save("lswt47.npy", np.array(rows))
