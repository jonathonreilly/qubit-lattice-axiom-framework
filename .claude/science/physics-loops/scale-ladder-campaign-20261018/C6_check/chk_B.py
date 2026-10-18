#!/usr/bin/env python3
"""C6_check part B (independent spot-check of the nu = 1 energetics).

Own geometry (chk_geometry), own gauge solve (galois), L = 4 Bloch supercell (the C6 worker used a 2^3
supercell): K-grid nk^3 on the 4^3 cell gives the same fine momenta as the worker's 6^3 grid on 2^3 when
nk = 3 (effective L = 12) and nk = 4 gives effective L = 16.
Standard convention: h_{j<-i} = -|t| (-1)^{u_e}; 1111 = pi through every face = the repo corner model.
Also: the repo convention t1 = -1, t2 = 0.2 with the chiral term (orientation computed geometrically:
counterclockwise about the outward body diagonal), lambda = -0.5, u-pattern 1011.
"""
import itertools, os, sys, time
import numpy as np
import galois

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chk_geometry import Corner, VEC, CORN, cid

GF = galois.GF(2)
TYPES = ('square', 'triangle', 'plaquette', 'tube')
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


T0 = time.time()
import sys as _s
L = int(_s.argv[1]) if len(_s.argv) > 1 else 2
G = Corner(L)
fl = G.face_list()
M = np.zeros((len(fl), G.E), np.uint8)
for r, (_, f) in enumerate(fl):
    M[r, f] = 1   # faces have distinct edges
R = None


def solve(rhs):
    A = GF(np.concatenate([M, rhs[:, None]], axis=1)).row_reduce()
    A = np.array(A, dtype=np.uint8)
    u = np.zeros(G.E, np.uint8)
    for row in A:
        nz = np.nonzero(row[:G.E])[0]
        if len(nz) == 0:
            assert not row[G.E]
            continue
        u[nz[0]] = row[G.E]
    assert ((M.astype(int) @ u) % 2 == rhs).all()
    return u


I = np.array([e[0] for e in G.edges]); J = np.array([e[1] for e in G.edges])
W = np.array([e[2] for e in G.edges], float)
ONS = np.array([e[3] == 'onsite' for e in G.edges])

# chiral orientation: corner position = (d + e)/2 relative to its site
cpos = {c: (VEC[c[0]] + VEC[c[1]]) / 2.0 for c in CORN}
tri_or = []   # (q, r, edge) oriented q -> r
for s in range(G.N):
    v = G.site(s)
    for sx, sy, sz in itertools.product((0, 1), repeat=3):
        cs = [(0 + sx, 2 + sy), (2 + sy, 4 + sz), (4 + sz, 0 + sx)]
        cs = [tuple(sorted(c)) for c in cs]
        n = VEC[0 + sx] + VEC[2 + sy] + VEC[4 + sz]
        p = [cpos[c] for c in cs]
        if np.dot(np.cross(p[1] - p[0], p[2] - p[0]), n) < 0:
            cs = cs[::-1]
        for a in range(3):
            q, r = cs[a], cs[(a + 1) % 3]
            tri_or.append((G.vid(v, q), G.vid(v, r), G.edge(v, q, v, r)))


def spectrum(u, nk, t1, t2, lam=0.0):
    sgn = (-1.0) ** u
    amp = -np.where(ONS, t1, t2) * sgn
    ev = []
    for n in itertools.product(range(nk), repeat=3):
        K = 2 * np.pi * np.array(n) / nk
        H = np.zeros((G.V, G.V), complex)
        a = amp * np.exp(1j * W @ K)
        np.add.at(H, (J, I), a)
        np.add.at(H, (I, J), np.conj(a))
        if lam:
            for q, r, e in tri_or:
                # on-site edges carry no winding
                H[r, q] += 1j * lam * sgn[e]; H[q, r] += -1j * lam * sgn[e]
        assert np.allclose(H, H.conj().T)
        ev.append(np.linalg.eigvalsh(H))
    return np.sort(np.concatenate(ev))


def E_nu(ev, nu):
    nsites = len(ev) / 12
    return ev[:int(round(nu * nsites))].sum() / nsites


PATS = list(itertools.product((0, 1), repeat=4))
NK = 12 // L; NK2 = 16 // L
if L == 4:
    PATS = [(0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 1, 1)]
gauges = {F: solve(np.array([F[TYPES.index(k)] for k, _ in fl], np.uint8)) for F in PATS}
print(f"gauges solved t={time.time()-T0:.0f}s", flush=True)
lab = lambda F: ''.join(map(str, F))
worker = {0.2: {'0000': -4.0222, '0010': -4.0224, '1000': -3.0259, '1011': -2.8026, '1111': -2.1686},
          1.0: {'0000': -4.6109, '0010': -4.5757, '1000': -4.3121, '1011': -3.3692, '1111': -3.0974}}
for t2 in (0.2, 1.0):
    E3 = {F: E_nu(spectrum(gauges[F], NK, 1.0, t2), 1) for F in PATS}
    order = sorted(PATS, key=lambda F: E3[F])
    print(f"\nt2 = {t2}, nu = 1, standard convention, {L}^3 cell x {NK}^3 K (effective L = 12):  t={time.time()-T0:.0f}s")
    for F in order:
        print(f"   {lab(F)}  E = {E3[F]:.4f}" + (f"   (worker {worker[t2][lab(F)]:.4f})" if lab(F) in worker[t2] else ''))
    rk = order.index((1, 1, 1, 1)) + 1
    exc = E3[(1, 1, 1, 1)] - E3[(0, 0, 0, 0)]
    print(f"   corner 1111 rank {rk}/16; excess over flux-free 0000: {exc:+.4f}")
    dev = max(abs(E3[tuple(int(c) for c in k)] - v) for k, v in worker[t2].items() if tuple(int(c) for c in k) in E3)
    check(f"t2={t2}: my nu=1 energies of 5 patterns agree with the worker's table to 2e-3 (different cell, gauge, code)", dev < 2e-3, f"max dev {dev:.1e}")
    if L == 2: check(f"t2={t2}: corner pattern 1111 ranks 15th or 16th at nu = 1 and lies >= 1.5 per site above flux-free", rk >= 15 and exc > 1.5,
          f"rank {rk}, excess {exc:.3f}")
    if t2 == 0.2:
        # convergence spot check nk = 4 (effective L = 16) for the corner and the flux-free pattern
        e4c = E_nu(spectrum(gauges[(1, 1, 1, 1)], NK2, 1.0, t2), 1); e40 = E_nu(spectrum(gauges[(0, 0, 0, 0)], NK2, 1.0, t2), 1)
        print(f"   nk=4 (eff. L=16): 1111 {e4c:.4f}, 0000 {e40:.4f}, excess {e4c-e40:+.4f}  t={time.time()-T0:.0f}s")
        check("excess stable between effective L = 12 and 16 to 1e-2", abs((e4c - e40) - exc) < 1e-2)

# chiral term, repo convention
if L == 4:
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}'); sys.exit(0)
print(f"\nrepo convention t1 = -1, t2 = 0.2, lambda = -0.5, nu = 1 (u-pattern labels; corner = 1011): t={time.time()-T0:.0f}s")
Ec = {F: E_nu(spectrum(gauges[F], NK, -1.0, 0.2, -0.5), 1) for F in PATS}
order = sorted(PATS, key=lambda F: Ec[F])
rk = order.index((1, 0, 1, 1)) + 1
print("   ", [(lab(F), round(Ec[F], 4)) for F in order])
print(f"   corner 1011 rank {rk}/16, E = {Ec[(1,0,1,1)]:.4f}, best {lab(order[0])} {Ec[order[0]]:.4f}")
check("with the chiral term the corner pattern is not the lowest uniform sector at nu = 1 (worker: rank 6/16, -3.5257)", rk > 1,
      f"rank {rk}; dev from worker E {abs(Ec[(1,0,1,1)] + 3.5257):.1e}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time()-T0:.0f}s)")
