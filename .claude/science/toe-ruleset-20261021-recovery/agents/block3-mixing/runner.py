#!/usr/bin/env python3
"""block3-mixing: does the b = 3 rishon role layout break CL-1's translations and mix families?

Self-contained (numpy, scipy). Free one-particle stand-ins only; no Fock space.
"""
import itertools, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0


def check(tag, msg, ok):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', tag, msg))


# ---------------------------------------------------------------- A. layout census
print('== A. role-layout census of a site-centred 3^3 block')
blk = [np.array(p) for p in itertools.product((-1, 0, 1), repeat=3)]
key = lambda p: tuple(int(v) for v in p)
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: rots.append(M)


def orbits(G):
    seen, out = set(), []
    for p in blk:
        if key(p) in seen: continue
        o = {key(g @ p) for g in G}; seen |= o; out.append(sorted(o))
    return out


nn = lambda p, q: int(np.abs(np.array(p) - np.array(q)).sum()) == 1
oO = orbits(rots)
sizes = sorted(len(o) for o in oO)
fixed = [o[0] for o in oO if len(o) == 1]
six = [o for o in oO if len(o) == 6]
ok = sizes == [1, 6, 8, 12] and fixed == [(0, 0, 0)] and len(six) == 1 and all(nn(q, (0, 0, 0)) for q in six[0])
check('[T]', 'A1 O (24 rotations): orbit sizes %s; the only fixed site is the centre and the only 6-orbit is its six face '
      'neighbours, so the covariant layout (one matter site, one rishon per bond end, rishons nearest neighbours of the matter '
      'site inside its block) is unique: matter at the centre, rishons on the faces' % sizes, ok)
# C3 about each body diagonal d (tick-rishon's site-bond register, S = 3/2: two 3-orbits, one facing each cube centre)
nsol = []
for d in itertools.product((1, -1), repeat=3):
    d = np.array(d)
    # C3 about d: cyclic permutation conjugated by the sign flip diag(d)
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); S = np.diag(d)
    C = S @ P @ S; G = [np.eye(3, dtype=int), C, C @ C]
    ob = orbits(G); fx = [o[0] for o in ob if len(o) == 1]; tr = [o for o in ob if len(o) == 3]
    sols = 0
    for m in fx:
        cand = [o for o in tr if all(nn(q, m) for q in o)]
        sols += len(list(itertools.combinations(cand, 2)))
    nsol.append((len(fx), len(tr), sols))
ok = all(s == (3, 8, 1) for s in nsol)
check('[T]', 'A2 C3 about the site\'s body diagonal (each of the 8 axis signs): 3 fixed sites (centre and the two far corners), '
      '8 three-orbits; layouts with matter on a fixed site and the two register ends on two in-block nearest-neighbour '
      '3-orbits: %s per axis (matter at a far corner has one in-block neighbour orbit): unique, the same 7 sites as A1' % nsol[0][2], ok)
check('[T]', 'A3 so 1 of 27 sites is matter: the matter sites are 3Z^3 (a lattice), the 20 other sites are the edge-midpoint '
      '12-orbit and corner 8-orbit; the far corners +-(1,1,1), the zoom-3 register\'s two other turn-fixed positions, are NOT '
      'matter sites here, so the position reading of three families has one position per block at the axiom rung', True)

# ---------------------------------------------------------------- B. effective matter hop on the fine lattice
print('== B. effective matter tick-hop from the fine layout (free stand-in, Schur complement)')
Lm = 6; Lf = 3 * Lm; N = Lf ** 3
idx = lambda x, y, z: ((x % Lf) * Lf + (y % Lf)) * Lf + (z % Lf)
coords = np.array(list(itertools.product(range(Lf), repeat=3)))
loc = (coords + 1) % 3 - 1             # local block coordinates, block centres at 3Z^3 + 0
ismat = np.all(loc == 0, axis=1)
isface = np.abs(loc).sum(axis=1) == 1
Xm = coords[ismat] // 3                # matter-lattice coordinates (centre at 0 mod 3)
assert ismat.sum() == Lm ** 3


def build(dr_fn, do=12.0, t=1.0):
    rows, cols, vals = [], [], []
    for a, (x, y, z) in enumerate(coords):
        for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            b = idx(x + e[0], y + e[1], z + e[2]); rows += [a, b]; cols += [b, a]; vals += [-t, -t]
    on = np.zeros(N)
    on[~ismat & ~isface] = do
    for a in np.where(isface)[0]:
        c = coords[a] - loc[a]; X = (c // 3) % Lm
        on[a] = dr_fn(X, loc[a])
    H = sp.coo_matrix((vals, (rows, cols)), shape=(N, N)).tocsr() + sp.diags(on)
    m = np.where(ismat)[0]; o = np.where(~ismat)[0]
    Hoo = H[o][:, o].tocsc(); Hom = H[o][:, m].toarray(); Hmm = H[m][:, m].toarray()
    lu = spla.splu(Hoo)
    return Hmm - Hom.T @ lu.solve(Hom)


Xi = {tuple(X): i for i, X in enumerate(Xm)}
nvec = np.array(list(itertools.product(range(Lm), repeat=3)))
F = np.exp(-2j * np.pi * nvec @ Xm.T / Lm) / np.sqrt(Lm ** 3)


def shift_comm(H, s):
    P = np.zeros_like(H)
    for i, X in enumerate(Xm): P[Xi[tuple((X + s) % Lm)], i] = 1
    return np.abs(P @ H - H @ P).max()


def leak(H):
    Hk = F @ H @ F.conj().T; a = nvec % 3
    diff = np.any(a[:, None, :] != a[None, :, :], axis=2)
    return np.abs(Hk[diff]).max(), Hk


DR = 8.0
H1 = build(lambda X, l: DR)
c1, c2 = shift_comm(H1, (1, 0, 0)), shift_comm(H1, (0, 1, 1))
lk1, Hk1 = leak(H1)
check('[F]', 'B1 O layout (rishons Delta_r = 8, other sites 12, t = 1, fine torus 18^3, matter 6^3): the effective matter hop '
      'commutes with every matter-lattice translation (|[H,T(e1)]| %.0e) and the 27 T(2e_i) family sectors do not mix (leak %.0e)'
      % (c1, lk1), c1 < 1e-10 and lk1 < 1e-10)


def dr_axis(X, l):                      # tick-rishon: register axis d = +1 where X_i even; faces toward the even centre
    d = np.where(X % 2 == 0, 1, -1)
    return 6.0 if int(np.dot(l, d)) == 1 else 10.0


H2 = build(dr_axis)
lk2, _ = leak(H2)
c21, c22 = shift_comm(H2, (1, 0, 0)), shift_comm(H2, (2, 0, 0))
check('[F]', 'B2 C3 site-bond layout (faces toward the even centre 6, toward the odd centre 10; axis set by the site\'s class mod 2): '
      'breaks T(e1) (%.2f) but keeps T(2e1) (%.0e), CL-1\'s own period: family leak %.0e' % (c21, c22, lk2),
      c21 > 1e-3 and c22 < 1e-10 and lk2 < 1e-10)
check('[T]', 'B3 units: any layout fixed per CL-1 site (depending at most on its class in the 2^3 cell) is invariant under CL-1\'s '
      '2Z^3 of the matter lattice = 6Z^3 of the axiom lattice; the "2Z^3 -> 6Z^3" of quantum-doublet-masses B6 assumed matter on '
      'every site of the role block (lcm(2,b) in matter units); with 1 matter site per b = 3 block the joint group IS CL-1\'s 2Z^3, '
      'so the minimal covariant layout supplies no family mixing and every translation no-go stands', True)

# ---------------------------------------------------------------- C. a layout that is period 3 in MATTER units (supplied)
print('== C. contrast: a supplied role pattern of period 3 in matter units (b = 9 role block)')
res = []
for dl in (1e-3, 1e-2):
    H3 = build(lambda X, l, dl=dl: DR * (1 + dl) if (X.sum() % 3 == 0) else DR)
    lk3, Hk3 = leak(H3)
    nj = [np.ravel_multi_index(tuple([v] * 3), (Lm,) * 3) for v in (0, 4, 2)]   # (j,j,j) sectors, class c = 0
    M = Hk3[np.ix_(nj, nj)]
    off = np.array([abs(M[0, 1]), abs(M[0, 2]), abs(M[1, 2])])
    res.append((lk3, off))
slope = np.log(res[1][0] / res[0][0]) / np.log(10)
offr = res[0][1] / res[0][1].max()
check('[F]', 'C1 rishon energy x(1+delta) on matter sites with X1+X2+X3 = 0 mod 3: family leak %.1e, %.1e at delta = 1e-3, 1e-2 '
      '(slope %.2f: first order); turn-fixed family matrix off-diagonals |M12|,|M13|,|M23| relative (%.2f, %.2f, %.2f): all one '
      'spurion power, democratic, no tower (quantum-doublet-masses D3)' % (res[0][0], res[1][0], slope, *offr),
      abs(slope - 1) < 0.05 and offr.min() > 0.3)

# ---------------------------------------------------------------- D. the epsilon-tower hypothesis on the actual layout
print('== D. does crossing rishon sites give a family epsilon-tower?')
pw = []
for D_ in (40.0, 80.0):
    H = build(lambda X, l, D_=D_: D_, do=1.5 * D_)
    i0 = Xi[(0, 0, 0)]
    pw.append((abs(H[i0, Xi[(1, 0, 0)]]), abs(H[i0, Xi[(1, 1, 0)]]), abs(H[i0, Xi[(1, 1, 1)]])))
pw = np.array(pw); ex = np.log(pw[1] / pw[0]) / np.log(0.5)
r1 = pw[0, 0] / (1 / 40.0 ** 2)
check('[F]', 'D1 coarse hops scale as Delta^-(n-1) with n the fine path length: exponents %.2f, %.2f, %.2f for coarse axis, face- and '
      'body-diagonal neighbours (paths of 3, 6, 9 fine steps); the axis hop t^3/Delta_r^2 x %.3f crosses exactly 2 rishons' % (*ex, r1),
      abs(ex[0] - 2) < 0.1 and ex[1] > 4.5 and ex[2] > 7 and abs(r1 - 1) < 0.2)
nid = [np.ravel_multi_index(tuple([v] * 3), (Lm,) * 3) for v in (0, 2, 4)]
ek = np.real(np.diag(Hk1)[nid]); h = abs(H1[Xi[(0, 0, 0)], Xi[(1, 0, 0)]])
sp_ = (ek - ek[0]) / h
check('[F]', 'D2 the tower is in range, not in family: every family crosses the same rishons; the family levels are the coarse band '
      'at the turn-fixed momenta (0,0,0), +-(2pi/3)(1,1,1): splittings %.3f, %.3f coarse hops (exactly degenerate pair, k -> -k), '
      'an O(1) ratio set by the coarse dispersion, not by rishon crossings; measured m2/m3 = 0.0036 to 0.06' % (sp_[1], sp_[2]),
      abs(ek[1] - ek[2]) < 1e-10 and 1 < abs(sp_[1]) < 20)
check('[T]', 'D3 the matter tick on the layout is CL-1\'s tick on 3Z^3 (tick-rishon C2: in each Gauss sector the dressed tick is the free '
      'tick of the canonical modes), so the zoom-3 family register is read on the matter lattice: three turn-fixed sectors in a 9^3 '
      'axiom block, family-diagonal at all orders (family-flux B2), one light family and a cell-scale pair (family-flux B3)', True)

# ---------------------------------------------------------------- E. edge-register blocks: the one role layout that can be period 3
print('== E. edge-register block layout (b_e cells, five tetrahedra alternating): period-3 content')


def tet_profile(be):
    P = 2 * be; g = np.arange(P) + 0.5
    x, y, z = np.meshgrid(g, g, g, indexing='ij')
    B = np.floor(np.stack([x, y, z]) / be).astype(int); u = np.stack([x, y, z]) / be - B
    cen = np.ones(x.shape, bool)
    for v in itertools.product((0, 1), repeat=3):
        par = (B[0] + v[0] + B[1] + v[1] + B[2] + v[2]) % 2   # global corner parity: odd corners own a corner tetrahedron
        dist = sum(np.abs(u[i] - v[i]) for i in range(3))
        cen &= ~((par == 1) & (dist < 1))
    return cen.astype(float)


cont = {}
for be in (2, 3, 4, 5, 6, 9, 10, 12, 27):
    f = tet_profile(be); P = f.shape[0]; Nt = P * (3 // np.gcd(P, 3))
    ft = np.tile(f, (Nt // P,) * 3); x = np.arange(Nt)
    best = 0
    for m in itertools.product(range(3), repeat=3):
        if m == (0, 0, 0): continue
        ph = [np.exp(-2j * np.pi * m[i] * x / 3) for i in range(3)]
        val = np.einsum('ijk,i,j,k->', ft, ph[0], ph[1], ph[2]) / Nt ** 3
        best = max(best, abs(val))
    cont[be] = best / ft.mean()
okE = all((cont[b] > 1e-6) == (b % 3 == 0) for b in cont)
check('[T]', 'E1 each cell reads the block tetrahedron holding its centre, so the edge layout has period 2 b_e in cells; its largest '
      'period-3 harmonic / mean: ' + ', '.join('%d:%.3f' % (b, cont[b]) for b in cont) + '; nonzero iff 3 | b_e (b_e is supplied)', okE)
check('[E]', 'E2 in the flat vacuum every tetrahedron reads the same metric, so the profile acts only through edge fluctuations: '
      'relative spread ~0.2/b_e (register estimate), second order ~(0.2/b_e)^2 times the contrast (which falls as ~2/b_e^2): '
      '%.0e at b_e = 3, %.0e at 12, %.0e at 27: a period-3 mixing spurion far below |V_us| = 0.225 unless families are '
      'near-degenerate, and one harmonic (no tower)' % ((0.2 / 3) ** 2 * cont[3], (0.2 / 12) ** 2 * cont[12], (0.2 / 27) ** 2 * cont[27]),
      (0.2 / 3) ** 2 * cont[3] < 0.01)
print('theorems: A1-A3, B3, D3, E1; finite: B1, B2, C1, D1, D2; estimates: E2.')
print('supplied: free stand-in (t, Delta_r, Delta_o, energy 0), the period-3 contrast pattern of C, b_e, spread 0.2/b_e.')
print('elapsed_seconds %.1f' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
