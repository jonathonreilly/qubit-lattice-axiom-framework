#!/usr/bin/env python3
"""COROLLARY check, part 1 (independent model: B7_check/chk_core.py, own GF(2) gauge + brute-force PSG,
no import of the repo model).

Checks the ingredients of the doubling corollary (item 6 of the scale-ladder note):
 (a) every commuting axis-C2 pair: fibre lifts anticommute; doubly fixed set = the 8 points (pi/2)(+-1)^3;
     at each of those points the affine action k -> R k + pi s_R acts LINEARLY on q = k - k_c (q -> R q).
 (b) convention check: U_g H(k) U_g^T = H(R_g k + pi s_g) for a real-space-symmetrised H at off-grid k.
 (c) zero tilt: for D2-only symmetric H, at every cube point every (2-fold) level has tr(P dH P) = 0.
     Also for D2' = {E, C2z, C2(xy), C2(x-y)} at its doubly fixed points.
 (d) O-symmetric H: 2-fold levels at k* are isotropic at linear order; 4-fold (G3/2) levels are NOT in general;
     2-fold levels at k*+pi e_x are uniaxial about x.
"""
import itertools, sys, os
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check')
from chk_core import OH, LAM, UF, PROPER, fibre_image, same_k, wrap, find, torus_ops, Hk, mults

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

c2x, c2y, c2z = (find(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1]))
c2xy = find([[0, 1, 0], [1, 0, 0], [0, 0, -1]]); c2xmy = find([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])
CUBE = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
kst = np.array([1, -1, 1]) * np.pi / 2
N = 24; grid = [np.array(t) * 2 * np.pi / N for t in itertools.product(range(N), repeat=3)]
rng = np.random.default_rng(20261018)

# (a)
ok_a = True; info = []
for a, b in ((c2x, c2y), (c2y, c2z), (c2z, c2x)):
    anti = np.allclose(UF[a] @ UF[b], -UF[b] @ UF[a])
    fx = [k for k in grid if same_k(fibre_image(a, k), k) and same_k(fibre_image(b, k), k)]
    eight = len(fx) == 8 and all(any(same_k(k, c) for c in CUBE) for k in fx)
    lin = True
    for c in CUBE:
        for _ in range(5):
            q = rng.normal(size=3) * 0.3
            for g in (a, b):
                lin &= same_k(fibre_image(g, c + q), c + OH[g] @ q)
    ok_a &= anti and eight and lin; info.append((anti, len(fx), lin))
check("(a) each axis-C2 pair: lifts anticommute, doubly fixed set (N=24 grid, exhaustive since fixed points lie in (pi/2)Z^3) = the 8 cube points, "
      "and at every cube point k_c the affine map acts linearly: R(k_c+q)+pi s_R = k_c + R q (mod 2pi)", ok_a, f"{info}")
fxp = [k for k in grid if same_k(fibre_image(c2z, k), k) and same_k(fibre_image(c2xy, k), k)]
check("(a') D2' pair (C2z, C2(xy)) anticommutes; its doubly fixed set is nonempty and contains k*",
      np.allclose(UF[c2z] @ UF[c2xy], -UF[c2xy] @ UF[c2z]) and any(same_k(k, kst) for k in fxp),
      f"{len(fxp)} doubly fixed points: {[tuple(np.round(wrap(k)/np.pi, 2)) for k in fxp]}")

# random symmetric Hamiltonians, real-space symmetrisation on L = 4 (range 1 < L/2)
T4 = torus_ops(4)
def random_sym(idx, seed, r=1):
    rr = np.random.default_rng(seed)
    h = {d: rr.normal(size=(12, 12)) + 1j * rr.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)}
    A = T4['from_blocks'](h); A = (A + A.conj().T) / 2
    Gs = [T4['G'](g) for g in idx]
    S = sum(G @ A @ G.T for G in Gs) / len(Gs)
    hb = T4['to_blocks'](S, r)
    assert np.allclose(T4['from_blocks'](hb), S)
    return hb
def dHk(h, k, i):
    out = np.zeros((12, 12), complex)
    for d, B in h.items(): out += (-1j * d[i]) * np.exp(-1j * np.dot(k, d)) * B
    return out
D2 = [find(np.eye(3, dtype=int)), c2x, c2y, c2z]
D2p = [find(np.eye(3, dtype=int)), c2z, c2xy, c2xmy]

# (b)
hO = random_sym(PROPER, 1)
okb = True
for _ in range(10):
    k = rng.uniform(-np.pi, np.pi, 3)
    for g in PROPER:
        okb &= np.allclose(UF[g] @ Hk(hO, k)[0] @ UF[g].T, Hk(hO, fibre_image(g, k))[0])
check("(b) convention: U_g H(k) U_g^T = H(R_g k + pi s_g) at 10 random off-grid k, all 24 proper g", okb)

def level_blocks(H, tol=1e-8):
    w, V = np.linalg.eigh(H); out = []; i = 0
    while i < 12:
        j = i
        while j + 1 < 12 and w[j + 1] - w[i] < tol: j += 1
        out.append((w[i], V[:, i:j + 1])); i = j + 1
    return out

# (c) zero tilt at doubly fixed points for D2 and D2'
maxtilt = 0.0; maxv = 0.0; allev = True; nlev = 0
for seed in range(10, 16):
    h = random_sym(D2, seed)
    for c in CUBE:
        for e, P in level_blocks(Hk(h, c)[0]):
            allev &= P.shape[1] % 2 == 0; nlev += 1
            hs = [P.conj().T @ dHk(h, c, i) @ P for i in range(3)]
            maxtilt = max(maxtilt, max(abs(np.trace(x)) / P.shape[1] for x in hs))
            maxv = max(maxv, max(np.linalg.norm(x) for x in hs))
check("(c) D2-only symmetric H (6 random, range 1): every level at all 8 cube points is even, and the tilt tr(P dH P)/dim vanishes",
      allev and maxtilt < 1e-10 and maxv > 1e-2, f"{nlev} levels, max |tilt| {maxtilt:.1e}, max |linear term| {maxv:.2f}")
maxtilt = 0.0; allev = True; nl = 0
for seed in range(20, 24):
    h = random_sym(D2p, seed)
    for c in fxp:
        for e, P in level_blocks(Hk(h, c)[0]):
            allev &= P.shape[1] % 2 == 0; nl += 1
            maxtilt = max(maxtilt, max(abs(np.trace(P.conj().T @ dHk(h, c, i) @ P)) for i in range(3)))
check("(c') D2'-only symmetric H: levels even and tilt zero at its doubly fixed points (no vector is fixed by two perpendicular C2s)",
      allev and maxtilt < 1e-10, f"{nl} levels, max |tilt| {maxtilt:.1e}")
# control: one C2 only -> doublets not forced, and an accidental 2-fold level would admit tilt; we only check non-degeneracy
h1 = random_sym([find(np.eye(3, dtype=int)), c2x], 30)
m1 = [mults(np.linalg.eigvalsh(Hk(h1, c)[0]), 1e-8) for c in CUBE]
check("(c'') control: with C2x alone the cube-point levels are generically simple", all(max(m) == 1 for m in m1), f"{m1[0]}")

# (d) O-symmetric: isotropy at k* for 2-fold vs 4-fold levels; uniaxial at k*+pi e_x
dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
iso2 = []; iso4 = []; uni = []
for seed in range(40, 46):
    h = random_sym(PROPER, seed)
    for e, P in level_blocks(Hk(h, kst)[0]):
        hs = [P.conj().T @ dHk(h, kst, i) @ P for i in range(3)]
        sp = np.array([np.linalg.eigvalsh(sum(d[i] * hs[i] for i in range(3))) for d in dirs])
        top = np.abs(sp).max(axis=1)
        (iso2 if P.shape[1] == 2 else iso4).append(np.ptp(top) / top.mean())
    kx = kst + np.array([np.pi, 0, 0])
    for e, P in level_blocks(Hk(h, kx)[0]):
        if P.shape[1] != 2: continue
        hs = [P.conj().T @ dHk(h, kx, i) @ P for i in range(3)]
        sp = np.array([np.linalg.eigvalsh(sum(d[i] * hs[i] for i in range(3)))[1] for d in dirs])
        vpar = np.linalg.eigvalsh(hs[0])[1]; vperp = np.linalg.eigvalsh(hs[1])[1]
        pred = np.sqrt(vpar ** 2 * dirs[:, 0] ** 2 + vperp ** 2 * (dirs[:, 1] ** 2 + dirs[:, 2] ** 2))
        uni.append((np.max(np.abs(sp - pred)), abs(vpar - vperp) / max(vpar, vperp, 1e-12), np.linalg.eigvalsh(hs[2])[1] - vperp))
check("(d1) O-symmetric H: every 2-fold level at k* has an isotropic linear splitting (v sigma.q)",
      len(iso2) > 0 and max(iso2) < 1e-8, f"{len(iso2)} doublets, max relative spread {max(iso2):.1e}")
check("(d2) O-symmetric H: 4-fold (G3/2) levels at k* are generically ANISOTROPIC at linear order (two invariant couplings J.q and J^3.q), "
      "so 'a band touching at k* is isotropic at linear order' holds for 2-fold touchings only",
      len(iso4) > 0 and min(iso4) > 1e-3, f"{len(iso4)} quartets, relative spread of top branch speed in [{min(iso4):.3f}, {max(iso4):.3f}]")
check("(d3) O-symmetric H: 2-fold levels at k*+pi e_x are uniaxial about x: speed^2 = v_par^2 q_x^2 + v_perp^2 q_perp^2",
      len(uni) > 0 and max(u[0] for u in uni) < 1e-8 and max(abs(u[2]) for u in uni) < 1e-8,
      f"{len(uni)} doublets, max fit residual {max(u[0] for u in uni):.1e}, relative v_par/v_perp difference up to {max(u[1] for u in uni):.2f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
