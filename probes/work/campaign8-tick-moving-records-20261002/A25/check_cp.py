"""A25 check 2: curl-split (C = curl h, p) "Yee for spin-2" leapfrog on the parity-role lattice.
Q1 exact constraint algebra per layer (C-rows div_1 C, tr C; momentum row; Hamiltonian row on C)
Q2 spectrum (15x15 Bloch blocks): exactly 4 non-unit eigenvalues = the 2 TT polarizations of check 1
Q3 exact intertwining with the (h,p) tick: C(t) = Curl h(t) on a random trajectory
Q4 role-lattice embedding on Z^3 (side 2L, roles r(y) = (y+s) mod 2): every layer reads only the
   site itself and face-neighbour sites (Manhattan 1); inputs per output
Q5 site-centred covariance with role relabelling: for rotations about sites of every role class and
   for unit translations, O L_s O^T == L_{s'} exactly; which (centre, rotation) keep s' = s
Supplied toy only; tau = 1/2 dyadic so identities are exact in floating point."""
import sys, time, itertools
import numpy as np
import scipy.sparse as sp
from stag2 import *

t0 = time.time()
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
tau = 0.5
rng = np.random.default_rng(7)
ops = build(L, 'stag')
lat = ops['lat']; n = lat.n
D, Vp, Mp, R, Div, Curl, J = (ops[k] for k in ('D', 'Vp', 'Mp', 'R', 'Div', 'Curl', 'J'))
div1C, trC, RC = ops['div1C'], ops['trC'], ops['RC']
# vector curl of the gauge parameter: w_l = eps_lki d_k xi_i  (face perpendicular to l)
t = [(l, i, EPS[l, k, i], (k,)) for l in range(3) for k in range(3) for i in range(3) if EPS[l, k, i] != 0]
CurlV = assemble(lat, FACEP_OFF, XI_OFF, t, 'stag')
A = (Curl @ Mp).tocsr()                 # C-layer generator
B = (0.5 * Curl.T @ J).tocsr()          # p-layer generator
print(f'L={L}  cells={n}  state (C,p) dim {15*n}')
print('Q1 exact constraint algebra (0.0 = exactly zero):')
print(f'   C-layer keeps C-rows:   |div1C A| = {maxabs(div1C @ A)},  |trC A| = {maxabs(trC @ A)}')
print(f'   C-layer, Hamiltonian row on C: |RC A + Div D^T| = {maxabs(RC @ A + Div @ D.T)}  (preserved iff D^T p = 0)')
print(f'   p-layer, momentum row:  |D^T B + (1/2) CurlV^T div1C| = {maxabs(D.T @ B + 0.5 * CurlV.T @ div1C)}  '
      f'(summation by parts; so D^T p is preserved iff div1C C = 0, itself preserved by every layer)')
print(f'   p-layer leaves C (hence all C-rows and RC C) untouched by construction')

# ---------------------------------------------------------------- Q2
ks = kgrid(L)
Kc1, Pp, Kc2 = layers_cp(ops, tau)
U = (Kc2 @ Pp @ Kc1).tocsr()
Z15 = C_OFF + H_OFF
Uk = bloch(lat, U, Z15, Z15, ks)
cnt, trdev, phdev = [], 0.0, 0.0
for ik, k in enumerate(ks):
    if np.allclose(k, 0):
        continue
    s = 2 * np.sin(k / 2)
    th = 2 * np.arcsin(tau * np.linalg.norm(s) / 2)
    lam = np.array([np.exp(1j * th)] * 2 + [np.exp(-1j * th)] * 2)
    Uj = np.eye(15, dtype=complex)
    for j in range(1, 16):
        Uj = Uj @ Uk[ik]
        trdev = max(trdev, abs(np.trace(Uj) - (11 + np.sum(lam ** j))))
    ev = np.linalg.eigvals(Uk[ik])
    cnt.append(int(np.sum(np.abs(np.angle(ev)) > 1e-5)))
print(f'Q2 power traces j=1..15: spectrum = 1 x11 + {{e^(+-i theta) x2}} with cos theta = 1 - tau^2 s^2/2: max dev {trdev:.1e} over {len(ks)-1} k')
print(f'   eigvals with |phase|>1e-5 per k: min {min(cnt)}, max {max(cnt)}  (4 = two polarizations)')

# ---------------------------------------------------------------- Q3
K1, P1_, K2 = layers_hp(ops, tau)
Dd = D.toarray(); Rd = R.toarray()
p0 = rng.normal(size=6 * n); h0 = rng.normal(size=6 * n)
p0 -= Dd @ np.linalg.lstsq(Dd, p0, rcond=None)[0]
h0 -= Rd.T @ np.linalg.lstsq(Rd.T, h0, rcond=None)[0]
zhp = np.concatenate([h0, p0]); zcp = np.concatenate([Curl @ h0, p0])
wC = wm = wH = wB = 0.0
for step in range(100):
    for Lh, Lc in ((K1, Kc1), (P1_, Pp), (K2, Kc2)):
        zhp = Lh @ zhp; zcp = Lc @ zcp
        C = zcp[:9 * n]; p = zcp[9 * n:]
        wC = max(wC, np.abs(C - Curl @ zhp[:6 * n]).max() / np.abs(C).max())
        wm = max(wm, np.abs(D.T @ p).max() / np.abs(p).max())
        wH = max(wH, np.abs(RC @ C).max() / np.abs(C).max())
        wB = max(wB, max(np.abs(div1C @ C).max(), np.abs(trC @ C).max()) / np.abs(C).max())
print(f'Q3 100 ticks, every layer: |C - Curl h|/|C| <= {wC:.1e}; relative rows: momentum {wm:.1e}, Hamiltonian {wH:.1e}, C-compatibility {wB:.1e}')

# ---------------------------------------------------------------- Q4/Q5  role lattice on Z^3
N = 2 * L
nz = N ** 3
zc = np.array(np.unravel_index(np.arange(nz), (N, N, N))).T
site = lambda y: ((y[..., 0] % N) * N + (y[..., 1] % N)) * N + (y[..., 2] % N)
NSLOT = 15   # slots 0-5: p_(ij) (H_PAIR); 6-14: C_(lj) (C_PAIR)


def embed(s):
    """global(15 slots x Z^3 sites) <- staggered (C,p) index, for role pattern s"""
    rows, cols = [], []
    s = np.array(s)
    for c in range(9):
        y = 2 * lat.coords + np.array(C_OFF[c]) + s
        rows += list((6 + c) * nz + site(y)); cols += list(c * n + np.arange(n))
    for c in range(6):
        y = 2 * lat.coords + np.array(H_OFF[c]) + s
        rows += list(c * nz + site(y)); cols += list(9 * n + c * n + np.arange(n))
    return sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(NSLOT * nz, 15 * n))


def lift(Mstag, E):
    act = sp.diags(np.asarray(E.sum(1)).ravel())
    return (E @ Mstag @ E.T + sp.identity(NSLOT * nz) - act).tocsr()


def rot_global(Rm, cz):
    P, sg = perm_sign(Rm)
    det = round(np.linalg.det(Rm))
    y2 = site((zc - cz) @ Rm.T + cz)
    rows, cols, vals = [], [], []
    for a, (i, j) in enumerate(H_PAIR):
        rows += list(hidx(P[i], P[j]) * nz + y2); cols += list(a * nz + np.arange(nz)); vals += [sg[i] * sg[j]] * nz
    for c, (l, j) in enumerate(C_PAIR):
        rows += list((6 + cidx(P[l], P[j])) * nz + y2); cols += list((6 + c) * nz + np.arange(nz))
        vals += [sg[l] * sg[j] * det] * nz
    return sp.csr_matrix((vals, (rows, cols)), shape=(NSLOT * nz, NSLOT * nz))


E0 = embed((0, 0, 0))
layers0 = [lift(Kc1, E0), lift(Pp, E0)]
# reach on Z^3
for name, Lg in zip(('C-layer', 'p-layer'), layers0):
    M = (Lg - sp.identity(NSLOT * nz)).tocoo()
    keep = M.data != 0
    yr = zc[M.row[keep] % nz]; yc = zc[M.col[keep] % nz]
    d = (yc - yr + N // 2) % N - N // 2
    man = np.abs(d).sum(1)
    # distinct input sites (excluding the output site) per output component
    per = {}
    for r, cc, m in zip(M.row[keep], M.col[keep], man):
        if m > 0:
            per.setdefault(r, set()).add(cc % nz)
    print(f'Q4 {name} on Z^3 (side {N}): max Manhattan reach {man.max()}, max Chebyshev {np.abs(d).max()}; '
          f'distinct neighbour sites read per output component: {sorted(set(len(v) for v in per.values()))}')
# which roles read which
roles = lambda y: tuple(int(b) for b in (y % 2))

Ostats = {}
cent = {'vertex(000)': (0, 0, 0), 'face(110)': (1, 1, 0), 'face(101)': (1, 0, 1), 'face(011)': (0, 1, 1),
        'edge(100)': (1, 0, 0), 'edge(010)': (0, 1, 0), 'edge(001)': (0, 0, 1), 'cube(111)': (1, 1, 1)}
cache = {(0, 0, 0): layers0}


def layers_for(s):
    if s not in cache:
        E = embed(s)
        cache[s] = [lift(Kc1, E), lift(Pp, E)]
    return cache[s]


allok = True
for cname, cz in cent.items():
    keep_p = keep_all = 0
    for Rm in signed_perms():
        sprime = tuple(int(v) for v in ((Rm @ (np.zeros(3) - np.array(cz)) + np.array(cz)) % 2))
        O = rot_global(Rm, np.array(cz))
        for Ls, Lt in zip(layers0, layers_for(sprime)):
            if maxabs(O @ Ls @ O.T - Lt) != 0.0:
                allok = False
        if sprime == (0, 0, 0):
            keep_all += 1
            keep_p += round(np.linalg.det(Rm)) > 0
    Ostats[cname] = (keep_all, keep_p)
print(f'Q5 every rotation (48) about every site class maps layer L_s to L_s\' EXACTLY (role relabelling + pattern map): {allok}')
for cname, (ka, kp) in Ostats.items():
    print(f'   centre {cname:12s}: rotations keeping the role pattern s=000: {ka}/48 ({kp}/24 proper); the rest map it to another translate')
# translations
tok = True
for e in list(np.eye(3, dtype=int)) + [np.array([1, 1, 1])]:
    y2 = site(zc + e)
    Tm = sp.csr_matrix((np.ones(NSLOT * nz), (np.concatenate([a * nz + y2 for a in range(NSLOT)]),
                        np.arange(NSLOT * nz))), shape=(NSLOT * nz, NSLOT * nz))
    sp_ = tuple(int(v) for v in e % 2)
    for Ls, Lt in zip(layers0, layers_for(sp_)):
        if maxabs(Tm @ Ls @ Tm.T - Lt) != 0.0:
            tok = False
print(f'   unit translations map L_s to L_(s+e) exactly: {tok}; patterns reached: {len(cache)} of 8 role translates')

# composed tick reach on Z^3
Ufull = (layers0[0] @ layers0[1] @ layers0[0] - sp.identity(NSLOT * nz)).tocoo()
keep = Ufull.data != 0
yr = zc[Ufull.row[keep] % nz]; yc = zc[Ufull.col[keep] % nz]
d = (yc - yr + N // 2) % N - N // 2
print(f'   composed tick C(tau/2) p(tau) C(tau/2): max Manhattan reach {np.abs(d).sum(1).max()} (three nearest-neighbour layers)')
# checkerboard: C-roles have odd role weight, p-roles even; site-centred rotations preserve the colour of every site
w = np.array([sum(int(b) for b in ((y + 0) % 2)) % 2 for y in zc])
rowsC = np.unique((layers0[0] - sp.identity(NSLOT * nz)).tocoo().row % nz)
rowsP = np.unique((layers0[1] - sp.identity(NSLOT * nz)).tocoo().row % nz)
print(f'   checkerboard colour (parity of coordinate sum) of sites updated by the C-layer: {set(w[rowsC].tolist())}; by the p-layer: {set(w[rowsP].tolist())}')
print(f'done in {time.time() - t0:.1f}s')
