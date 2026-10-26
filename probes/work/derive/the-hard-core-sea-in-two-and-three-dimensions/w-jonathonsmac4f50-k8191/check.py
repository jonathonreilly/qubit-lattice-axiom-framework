#!/usr/bin/env python3
"""check.py -- J:derive:the-hard-core-sea-in-two-and-three-dimensions:a1

The hard-core sea beyond the ring: exact gauge reduction of the 2D/3D walk
sigma_j D_j (block 54 walk) with one record per site to an SU(2)-symmetric
pi-flux hopping model; exact tile bounds; exact exchange-sign counterexample;
4x4 torus ground energies and rate-mode coefficient at half filling.

Labels in the printed lines:
  [exact]  integer / rational / sympy-algebraic arithmetic
  [float]  floating-point linear algebra (eigsh / CG / eigvalsh); NOT exact
Single process; numpy, scipy, sympy, mpmath only.
"""
import gc, itertools, math, sys, time
from fractions import Fraction
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as sla
import sympy as sy
import mpmath as mp

T0 = time.time()
NP = 0
NF = 0
RES = {}


def check(name, ok, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)


# ----------------------------------------------------------------------------
# lattice, bonds, gauge
# ----------------------------------------------------------------------------
def site_index(c, dims):
    i, m = 0, 1
    for k in range(len(dims)):
        i += c[k] * m
        m *= dims[k]
    return i


def all_coords(dims):
    return [tuple(c[::-1]) for c in itertools.product(*[range(L) for L in dims][::-1])]


def torus_bonds(dims):
    """gauged real model: x-link +1/2, y-link (-1)^x /2, z-link (-1)^(x+y) /2.
    returns n and list of (a, b, dir, t, coord_a) with b = a + e_dir (periodic)."""
    d = len(dims)
    n = int(np.prod(dims))
    bonds = []
    for c in all_coords(dims):
        for j in range(d):
            c2 = list(c)
            c2[j] = (c2[j] + 1) % dims[j]
            sign = 1 if j == 0 else (-1) ** sum(c[:j])
            bonds.append((site_index(c, dims), site_index(c2, dims), j, 0.5 * sign, c))
    return n, bonds


def patch_bonds(shape, base=None):
    """open rectangular patch with the same gauged signs (global position = local + base)."""
    d = len(shape)
    base = base or (0,) * d
    coords = all_coords(shape)
    idx = {c: i for i, c in enumerate(coords)}
    bonds = []
    for c in coords:
        for j in range(d):
            c2 = list(c)
            c2[j] += 1
            c2 = tuple(c2)
            if c2 in idx:
                g = tuple(c[k] + base[k] for k in range(d))
                sign = 1 if j == 0 else (-1) ** sum(g[:j])
                bonds.append((idx[c], idx[c2], j, 0.5 * sign, c))
    return len(coords), bonds


PAULI = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]).astype(complex)]


def orig_onebody(dims):
    """block-54 walk: <x|H|x+e_j> = -(i/2) sigma_j (periodic), index 2*site+coin."""
    n = int(np.prod(dims))
    h = np.zeros((2 * n, 2 * n), complex)
    for c in all_coords(dims):
        i = site_index(c, dims)
        for j in range(len(dims)):
            c2 = list(c)
            c2[j] = (c2[j] + 1) % dims[j]
            i2 = site_index(c2, dims)
            blk = -0.5j * PAULI[j]
            h[2 * i:2 * i + 2, 2 * i2:2 * i2 + 2] += blk
            h[2 * i2:2 * i2 + 2, 2 * i:2 * i + 2] += blk.conj().T
    return h


def gauge_unitary(dims):
    n = int(np.prod(dims))
    V = np.zeros((2 * n, 2 * n), complex)
    for c in all_coords(dims):
        i = site_index(c, dims)
        g = np.eye(2, dtype=complex)
        for k in range(len(dims)):
            g = g @ np.linalg.matrix_power(PAULI[k], c[k])
        V[2 * i:2 * i + 2, 2 * i:2 * i + 2] = g * (1j) ** sum(c)
    return V


def real_onebody(dims):
    n, bonds = torus_bonds(dims)
    h = np.zeros((2 * n, 2 * n))
    for (a, b, j, t, c) in bonds:
        for s in range(2):
            h[2 * a + s, 2 * b + s] += t
            h[2 * b + s, 2 * a + s] += t
    return h


# ----------------------------------------------------------------------------
# many-body hard-core generator in the gauged frame, sector (N, Nup)
# ----------------------------------------------------------------------------
def combos(n, N):
    return [sum(1 << i for i in cmb) for cmb in itertools.combinations(range(n), N)]


def sector_codes(n, N, Nup):
    codes = []
    for occ in combos(n, N):
        sites = [i for i in range(n) if occ >> i & 1]
        for sub in itertools.combinations(sites, Nup):
            up = 0
            for s in sub:
                up |= 1 << s
            codes.append(occ | (up << n))
    return np.array(sorted(codes), dtype=np.int64)


def parity(x):
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)
    return x & 1


def build_sector(n, bonds, N, Nup, fermion, wts=None, codes=None):
    """Hard-core hopping H = sum_b w_b B_b in the sector, real symmetric CSR.  Fermion sign
    (-1)^(# occupied sites strictly between the two sites); boson sign +1."""
    if codes is None:
        codes = sector_codes(n, N, Nup)
    dim = len(codes)
    mask = (1 << n) - 1
    occ = codes & mask
    up = codes >> n
    R, C, V = [], [], []
    for bi, (a, b, j, t, c) in enumerate(bonds):
        w = 1.0 if wts is None else float(wts[bi])
        lo, hi = min(a, b), max(a, b)
        between = ((1 << hi) - 1) & ~((1 << (lo + 1)) - 1)
        for (s, e) in ((a, b), (b, a)):
            sel = np.nonzero(((occ >> s) & 1 == 1) & ((occ >> e) & 1 == 0))[0]
            if len(sel) == 0:
                continue
            o = occ[sel]
            u = up[sel]
            isup = (u >> s) & 1
            o2 = o ^ (1 << s) ^ (1 << e)
            u2 = u ^ (isup * ((1 << s) ^ (1 << e)))
            row = np.searchsorted(codes, o2 | (u2 << n))
            sg = (1 - 2 * parity(o & between)) if fermion else np.ones(len(sel), dtype=np.int64)
            R.append(row.astype(np.int32))
            C.append(sel.astype(np.int32))
            V.append(t * w * sg)
    V = np.concatenate(V)
    gc.collect()
    R = np.concatenate(R)
    C = np.concatenate(C)
    H = sps.csr_matrix((V, (R, C)), shape=(dim, dim))
    del V, R, C
    gc.collect()
    return H, codes


def lowering(n, N, Nup, codes_hi, codes_lo):
    """S^- = sum_x d^dag_{x,down} d_{x,up}: sector Nup -> Nup-1 (no fermion sign: the two modes of a
    site are adjacent in the mode order and a site holds one record)."""
    mask = (1 << n) - 1
    occ = codes_hi & mask
    up = codes_hi >> n
    R, C = [], []
    for s in range(n):
        sel = np.nonzero((up >> s) & 1 == 1)[0]
        new = occ[sel] | ((up[sel] ^ (1 << s)) << n)
        R.append(np.searchsorted(codes_lo, new))
        C.append(sel)
    r = np.concatenate(R)
    c = np.concatenate(C)
    return sps.csr_matrix((np.ones(len(r)), (r, c)), shape=(len(codes_lo), len(codes_hi)))


# ----------------------------------------------------------------------------
# original (coin-basis) hard-core generator for small N: the model of block 78 / 130
# ----------------------------------------------------------------------------
def orig_many(h, n, N, fermion):
    states = [(sites, cs) for sites in itertools.combinations(range(n), N)
              for cs in itertools.product((0, 1), repeat=N)]
    idx = {s: i for i, s in enumerate(states)}
    R, C, V = [], [], []
    nz = [(r, c, h[r, c]) for r in range(h.shape[0]) for c in np.nonzero(h[r])[0]]
    by_src = {}
    for r, c, v in nz:
        by_src.setdefault(c, []).append((r, v))
    for (sites, cs), i in idx.items():
        sset = set(sites)
        for (s, c0) in zip(sites, cs):
            for (r, amp) in by_src.get(2 * s + c0, []):
                e, c2 = divmod(r, 2)
                if e in sset:
                    continue
                new = dict(zip(sites, cs))
                del new[s]
                new[e] = c2
                ns = tuple(sorted(new))
                ncs = tuple(new[k] for k in ns)
                sg = 1
                if fermion:
                    lo, hi = min(s, e), max(s, e)
                    sg = (-1) ** sum(1 for t in sites if lo < t < hi)
                R.append(idx[(ns, ncs)])
                C.append(i)
                V.append(amp * sg)
    return sps.csr_matrix((V, (R, C)), shape=(len(states), len(states)), dtype=complex)


def trace_moments(M, kmax=6):
    """tr M^k, k=1..kmax, for sparse Hermitian M"""
    out = []
    P = {1: M}
    P[2] = M @ M
    out.append(M.diagonal().sum())
    out.append(abs(P[1]).power(2).sum())            # tr M^2 = ||M||_F^2
    out.append(P[2].multiply(M.T).sum())            # tr M^3
    out.append(abs(P[2]).power(2).sum())            # tr M^4 = ||M^2||_F^2
    if kmax >= 6:
        P[3] = P[2] @ M
        out.append(P[3].multiply(P[2].T).sum())     # tr M^5
        out.append(abs(P[3]).power(2).sum())        # tr M^6 = ||M^3||_F^2
    return np.array(out[:kmax])


# ============================================================================
print("=== S1: gauge reduction of the one-body walk (exact) ===")
for dims in [(4, 4), (4, 4, 4), (8, 8)]:
    h = orig_onebody(dims)
    V = gauge_unitary(dims)
    hh = V.conj().T @ h @ V
    hr = real_onebody(dims)
    check("S1 [exact] V^dag h V = (real pi-flux hop) x 1_coin, dims=%s" % (dims,),
          np.array_equal(hh, hr.astype(complex)) and np.array_equal(V.conj().T @ V, np.eye(V.shape[0])),
          "max|diff|=%g, V entries in {0,+-1,+-i}: %s" % (np.abs(hh - hr).max(),
                                                           set(np.unique(np.round(V.real * 1).astype(int))) <= {-1, 0, 1}))

# plaquette holonomy -1 everywhere on the gauged lattice (exact)
for dims in [(4, 4), (4, 4, 4)]:
    n, bonds = torus_bonds(dims)
    t = {}
    for (a, b, j, tt, c) in bonds:
        t[(a, b)] = tt
        t[(b, a)] = tt
    ok = True
    for c in all_coords(dims):
        for j in range(len(dims)):
            for k in range(j + 1, len(dims)):
                def mv(cc, d_):
                    c2 = list(cc)
                    c2[d_] = (c2[d_] + 1) % dims[d_]
                    return tuple(c2)
                p = [c, mv(c, j), mv(mv(c, j), k), mv(c, k)]
                prod = 1.0
                for u in range(4):
                    prod *= t[(site_index(p[u], dims), site_index(p[(u + 1) % 4], dims))] * 2
                ok &= (prod == -1.0)
    check("S1 [exact] every plaquette of the gauged model carries flux pi (product of hops = -(1/2)^4), dims=%s" % (dims,), ok)

# ----------------------------------------------------------------------------
print("=== S2: many-body gauge check against the original coin-basis generator ===")
n16, b16 = torus_bonds((4, 4))
h2d = orig_onebody((4, 4))
for N in (2, 3):
    for ferm in (True, False):
        M = orig_many(h2d, 16, N, ferm)
        herm = abs(M - M.getH()).max() == 0
        km = 6 if N == 2 else 4
        mo = trace_moments(M, km)
        mg = np.zeros(km, complex)
        for Nup in range(N + 1):
            Hs, _ = build_sector(16, b16, N, Nup, ferm)
            mg += trace_moments(Hs.astype(complex), km)
        d = np.abs(mo - mg).max()
        check("S2 [exact] tr H^k, k=1..%d of the original hard-core generator = sum over Nup of gauged sectors, "
              "4x4 torus N=%d %s" % (km, N, "fermion" if ferm else "boson"), herm and d < 1e-9, "max diff %.2e" % d)
# ring sanity vs block 130: L=8, N=4 gives -csc(pi/8) for both exchange signs
h1d = orig_onebody((8,))
for ferm in (True, False):
    M = orig_many(h1d, 8, 4, ferm)
    e0 = np.linalg.eigvalsh(M.toarray())[0]
    check("S2 [float] ring L=8, N=4, %s: ground = -csc(pi/8) (block 130 T4a)" % ("fermion" if ferm else "boson"),
          abs(e0 + 1 / math.sin(math.pi / 8)) < 1e-12, "E0=%.12f" % e0)

# ----------------------------------------------------------------------------
print("=== S3: SU(2) invariance of the gauged hard-core generator (exact, integer entries of 2H) ===")
for (N, Nup) in [(3, 2), (4, 2), (5, 3)]:
    for ferm in (True, False):
        Hh, ch = build_sector(16, b16, N, Nup, ferm)
        Hl, cl = build_sector(16, b16, N, Nup - 1, ferm)
        Sm = lowering(16, N, Nup, ch, cl)
        D = (Sm @ (2 * Hh) - (2 * Hl) @ Sm)
        check("S3 [exact] S^- H = H S^-, 4x4 torus N=%d Nup=%d %s" % (N, Nup, "F" if ferm else "B"),
              abs(D).max() == 0 and np.all(np.abs((2 * Hh).data - np.round((2 * Hh).data)) == 0))

# ----------------------------------------------------------------------------
print("=== S4: exact small-cluster results ===")
x = sy.symbols("x")


def exact_min_eig(shape, ferm, N, Nup, base=None):
    n, b = patch_bonds(shape, base)
    H, _ = build_sector(n, b, N, Nup, ferm)
    A = sy.Matrix((2 * H).toarray().round().astype(int).tolist())
    cp = A.charpoly(x).as_expr()
    best = None
    for fac, m in sy.factor_list(cp)[1]:
        rts = sy.Poly(fac, x).real_roots()
        if rts:
            r = min(rts, key=lambda z: float(z.evalf(30)))
            if best is None or float(r.evalf(30)) < float(best.evalf(30)):
                best = r
    return best / 2


# plaquette (2x2, flux pi): every sector, both statistics
for ferm in (True, False):
    mins = []
    for N in range(1, 4):
        mins.append(exact_min_eig((2, 2), ferm, N, N // 2))
    lam = min(mins, key=lambda z: float(z.evalf(30)))
    check("S4 [exact charpoly, 60-digit root] plaquette (2x2, flux pi) hard-core, %s: min over all N and spins = -sqrt(2)" % ("F" if ferm else "B"),
          abs((lam + sy.sqrt(2)).evalf(60)) < sy.Float(10) ** -50, "sector minima (N=1..3) %s" % [str(sy.N(m, 12)) for m in mins])
    RES["plaq"] = -math.sqrt(2)

def orig_onebody_patch(shape):
    coords = all_coords(shape)
    idx = {c: i for i, c in enumerate(coords)}
    n = len(coords)
    h = np.zeros((2 * n, 2 * n), complex)
    for c in coords:
        for j in range(len(shape)):
            c2 = list(c)
            c2[j] += 1
            c2 = tuple(c2)
            if c2 in idx:
                i, i2 = idx[c], idx[c2]
                blk = -0.5j * PAULI[j]
                h[2 * i:2 * i + 2, 2 * i2:2 * i2 + 2] += blk
                h[2 * i2:2 * i2 + 2, 2 * i:2 * i + 2] += blk.conj().T
    return h


# the 2x3 cluster is a cluster of the ORIGINAL walk: spectrum of the coin-basis generator = union of gauged Sz sectors
hp = orig_onebody_patch((2, 3))
nP, bP = patch_bonds((2, 3))
for ferm in (True, False):
    M = orig_many(hp, nP, 3, ferm)
    ev0 = np.sort(np.linalg.eigvalsh(M.toarray()))
    evg = np.sort(np.concatenate([np.linalg.eigvalsh(build_sector(nP, bP, 3, Nup, ferm)[0].toarray()) for Nup in range(4)]))
    check("S4 [float] 2x3 patch N=3 %s: spectrum of the original coin-basis generator = union of gauged Sz sectors" % ("F" if ferm else "B"),
          len(ev0) == len(evg) and np.abs(ev0 - evg).max() < 1e-12, "dim %d, max diff %.1e" % (len(ev0), np.abs(ev0 - evg).max()))

# the 2x2x2 cube (3D walk sigma_1 D_x + sigma_2 D_y + sigma_3 D_z) is a cluster of the original 3D walk as well
hc = orig_onebody_patch((2, 2, 2))
nC, bC = patch_bonds((2, 2, 2))
for ferm in (True, False):
    for Ncube in (3, 4):
        if Ncube == 4 and not ferm:
            continue
        M = orig_many(hc, nC, Ncube, ferm)
        ev0 = np.sort(np.linalg.eigvalsh(M.toarray()))
        evg = np.sort(np.concatenate([np.linalg.eigvalsh(build_sector(nC, bC, Ncube, Nup, ferm)[0].toarray()) for Nup in range(Ncube + 1)]))
        check("S4 [float] 2x2x2 cube N=%d %s: spectrum of the original 3D coin-basis generator = union of gauged Sz sectors" % (Ncube, "F" if ferm else "B"),
              len(ev0) == len(evg) and np.abs(ev0 - evg).max() < 1e-11, "dim %d, max diff %.1e, E0=%.9f" % (len(ev0), np.abs(ev0 - evg).max(), ev0[0]))

# 2x3 patch, N=3 records: exchange signs differ (exact)
lamF = exact_min_eig((2, 3), True, 3, 1)
lamB = exact_min_eig((2, 3), False, 3, 1)
check("S4 [exact charpoly, 60-digit root] 2x3 patch N=3 fermion ground energy = -1/2 - sqrt(3)",
      abs((lamF + sy.Rational(1, 2) + sy.sqrt(3)).evalf(60)) < sy.Float(10) ** -50, "~ %.12f" % float(lamF.evalf(30)))
check("S4 [exact charpoly] 2x3 patch N=3 boson ground energy = least real root of an integer degree-9 polynomial, ~ -2.11263305",
      abs(float(lamB.evalf(30)) + 2.1126330530577455) < 1e-12, "%.15f" % float(lamB.evalf(30)))
check("S4 [exact charpoly] 2x3 patch N=3: fermion ground < boson ground (exchange sign matters beyond the ring)",
      float(lamF.evalf(30)) < float(lamB.evalf(30)) - 0.1,
      "difference %.6f" % (float(lamB.evalf(30)) - float(lamF.evalf(30))))

# ----------------------------------------------------------------------------
print("=== S5: tile lower bounds and cluster upper bounds [float, all N, all spin sectors] ===")


def patch_min(shape, ferm, base=None):
    n, b = patch_bonds(shape, base)
    out = {}
    for N in range(1, n):
        H, _ = build_sector(n, b, N, N // 2, ferm)
        if H.shape[0] <= 2500:
            out[N] = np.linalg.eigvalsh(H.toarray())[0]
        else:
            out[N] = sla.eigsh(H, k=1, which="SA", tol=1e-11)[0][0]
    return out


tile = {}
for shape, nb in [((2, 2), None), ((3, 3), None), ((2, 2, 2), None)]:
    for ferm in (True, False):
        o = patch_min(shape, ferm)
        lam = min(o.values())
        tile[(shape, ferm)] = lam
        print("   patch %s %s: min over N,S = %.12f at N=%d" % (shape, "F" if ferm else "B", lam, min(o, key=o.get)), flush=True)
# gauge independence of cube value (flux pattern is the same up to site signs)
for base in [(1, 0, 0), (0, 1, 0), (1, 1, 1)]:
    for ferm in (True, False):
        o = patch_min((2, 2, 2), ferm, base)
        check("S4 [float] cube spectrum minimum independent of base position %s (%s)" % (base, "F" if ferm else "B"),
              abs(min(o.values()) - tile[((2, 2, 2), ferm)]) < 1e-9)
check("S5 [float] cube fermion tile minimum = -2*sqrt(3) (spin-polarized spinless sea)",
      abs(tile[((2, 2, 2), True)] + 2 * math.sqrt(3)) < 1e-9, "%.12f" % tile[((2, 2, 2), True)])
check("S5 [float] 3x3 fermion tile minimum = -(2+sqrt(2)) = -3.41421356..", abs(tile[((3, 3), True)] + 2 + math.sqrt(2)) < 1e-9,
      "%.12f" % tile[((3, 3), True)])

# sliding-window weights (uniform): bond multiplicity of a k^d window
def mult(k, d):
    return (k - 1) * k ** (d - 1)


bounds = {}
for (shape, ferm), lam in tile.items():
    k = shape[0]
    d = len(shape)
    bounds[(d, k, ferm)] = lam / mult(k, d)
print("   per-site LOWER bounds on c0 from k^d tiles (each bond covered with total weight 1):")
for key, v in sorted(bounds.items()):
    print("     d=%d k=%d %s: c0 >= %.10f" % (key[0], key[1], "F" if key[2] else "B", v))
# product-cluster UPPER bounds: partition into k^d blocks
ub = {}
for (shape, ferm), lam in tile.items():
    ub[(len(shape), shape[0], ferm)] = lam / shape[0] ** len(shape)
print("   per-site UPPER bounds on c0 from product states of disjoint k^d clusters:")
for key, v in sorted(ub.items()):
    print("     d=%d k=%d %s: c0 <= %.10f" % (key[0], key[1], "F" if key[2] else "B", v))

# ----------------------------------------------------------------------------
print("=== S6: free sea and spin-polarized spinless sea (comparators / rigorous bracket for fermions) ===")
def eps_mean_2d():
    f = lambda a: mp.sqrt(1 + a) * mp.ellipe(1 / (1 + a))
    # mean over ky of sqrt(a + sin^2 ky) = (2/pi) sqrt(1+a) E(1/(1+a)); then average over kx
    val = mp.quad(lambda kx: (2 / mp.pi) * f(mp.sin(kx) ** 2), [0, mp.pi / 2]) / (mp.pi / 2)
    return val
mp.mp.dps = 25
c2 = eps_mean_2d()
print("   free 2-coin sea per site, d=2: c0_free = -%s" % mp.nstr(c2, 15))
def eps_mean_grid(d, M):
    k = (np.arange(M) + 0.5) * 2 * np.pi / M
    g = np.meshgrid(*([k] * d), indexing="ij")
    return float(np.sqrt(sum(np.sin(a) ** 2 for a in g)).mean())
c3a, c3b = eps_mean_grid(3, 96), eps_mean_grid(3, 192)
print("   free 2-coin sea per site, d=3: c0_free = -%.5f (midpoint grids 96,192: %.6f, %.6f; numeric only)" % (c3b, c3a, c3b))
# exact finite-torus sums for L=4
S2 = (8 + 4 * sy.sqrt(2)) / 16
S3 = sy.Rational(1, 8) * (3 + 3 * sy.sqrt(2) + sy.sqrt(3))
check("S6 [exact] 4x4 torus: free 2-coin sea per site = -(2+sqrt2)/4 *... = -(8+4 sqrt2)/16; spin-polarized spinless sea is exactly half",
      abs(float(S2) - 13.656854249492381 / 16) < 1e-12, "free %.10f, polarized %.10f" % (-float(S2), -float(S2) / 2))
h16 = np.zeros((16, 16))
for (a, b, j, t, c) in b16:
    h16[a, b] += t
    h16[b, a] += t
hs = np.linalg.eigvalsh(h16)
hfree = np.linalg.eigvalsh(real_onebody((4, 4)))
ev_orig = np.linalg.eigvalsh(orig_onebody((4, 4)))
check("S6 [float] gauged one-body spectrum (16x16 spinless pi-flux hop) is the original 32-level spectrum with each level taken once; "
      "spinless sea = half the 2-coin sea = -(4+2 sqrt2)",
      np.abs(np.sort(np.concatenate([hs, hs])) - ev_orig).max() < 1e-12 and np.abs(np.sort(np.concatenate([hs, hs])) - hfree).max() < 1e-12
      and abs(hs[hs < -1e-12].sum() + 4 + 2 * math.sqrt(2)) < 1e-12, "spinless sea %.10f" % hs[hs < -1e-12].sum())
RES["freeL4_2d"] = float(S2)
RES["freeL4_3d"] = float(S3)
print("   4^3 torus: free sea per site = -%.10f, polarized = -%.10f" % (float(S3), float(S3) / 2))

# ----------------------------------------------------------------------------
print("=== S7: 4x4 torus at half filling N=8, Sz=0 sector (all spins), both exchange signs ===")
N8 = 8
codes8 = sector_codes(16, N8, 4)
check("S7 sector dimension N=8,Nup=4 equals C(16,8)*C(8,4)=900900", len(codes8) == math.comb(16, 8) * math.comb(8, 4))


def alphas(bonds, qm):
    q = [math.pi / 2 * m for m in qm]
    al = []
    for (a, b, j, t, c) in bonds:
        c2 = list(c)
        c2[j] += 1
        al.append((math.cos(sum(q[k] * c[k] for k in range(len(q)))) + math.cos(sum(q[k] * c2[k] for k in range(len(q))))) / 2)
    return np.array(al)


def rayleigh_exact(H, psi):
    """exact rational Rayleigh quotient of the 2^28-rounded vector (integers); rigorous upper bound on lambda_min.
    Also exact residual-based eigenvalue enclosure."""
    v = np.round(psi * 2 ** 28).astype(np.int64)
    A = sps.csr_matrix((np.round(2 * H.data).astype(np.int64), H.indices, H.indptr), shape=H.shape)
    assert np.array_equal(2 * H.data, np.round(2 * H.data))
    w = A @ v
    num = 0
    den = 0
    step = 10 ** 4
    for s in range(0, len(v), step):
        vs = v[s:s + step]
        num += int(np.dot(vs, w[s:s + step]))
        den += int(np.dot(vs, vs))
    rho = Fraction(num, 2 * den)           # v^T H v / v^T v, H = A/2
    # residual ||(H - rho) v||^2 / ||v||^2 exactly
    vo = v.astype(object)
    wo = w.astype(object)
    res2 = sum((den * wo[i] - num * vo[i]) ** 2 for i in range(len(v)))   # = (2 den)^2 * ||(H-rho)v||^2 * ... scaled
    # (A v - (num/den) v) = (den*w - num*v)/den  ;  H-rho = (A - 2rho)/2 ; 2rho = num/den
    r2 = Fraction(int(res2), 4 * den * den * den)  # ||(H-rho)v||^2/||v||^2 = sum((den w-num v)^2)/(4 den^2) / den
    return rho, r2


torus = {}
for ferm in (True, False):
    tag = "F" if ferm else "B"
    t0 = time.time()
    H, _ = build_sector(16, b16, N8, 4, ferm, codes=codes8)
    w1, v1 = sla.eigsh(H, k=3, which="SA", tol=1e-13, v0=np.random.default_rng(1).standard_normal(H.shape[0]))
    o = np.argsort(w1)
    w1, v1 = w1[o], v1[:, o]
    w2 = sla.eigsh(H, k=1, which="SA", tol=1e-13, v0=np.random.default_rng(2).standard_normal(H.shape[0]))[0][0]
    E0 = w1[0]
    psi = v1[:, 0]
    resid = np.linalg.norm(H @ psi - E0 * psi)
    check("S7 [float] %s N=8 ground energy: two independent Lanczos runs agree, residual < 1e-11" % tag,
          abs(w2 - E0) < 1e-11 and resid < 1e-11, "E0=%.12f (2nd run %.12f) resid %.1e" % (E0, w2, resid))
    check("S7 [float] %s N=8 ground state nondegenerate in the Sz=0 sector (gap > 1e-3)" % tag, w1[1] - E0 > 1e-3,
          "gap %.6f (next levels %.6f %.6f)" % (w1[1] - E0, w1[1], w1[2]))
    rho, r2 = rayleigh_exact(H, psi)
    r = math.sqrt(float(r2))
    check("S7 [exact] %s N=8: exact rational Rayleigh quotient (rigorous upper bound on the ground energy) and exact residual enclosure" % tag,
          abs(float(rho) - E0) < 1e-10 and r < 1e-5,
          "E0 <= %s ~ %.12f ; an eigenvalue lies within %.2e of it" % (rho, float(rho), r))
    # <S^2> of ground state
    codes_lo = sector_codes(16, N8, 3)
    Sm = lowering(16, N8, 4, codes8, codes_lo)
    s2 = float(np.linalg.norm(Sm @ psi) ** 2)
    print("   %s ground state <S^2> = %.3e (Sz=0 so S(S+1)=|S^- psi|^2)" % (tag, s2))
    # bond energies per direction
    ex = psi @ (build_sector(16, b16, N8, 4, ferm, wts=[1.0 if bd[2] == 0 else 0.0 for bd in b16], codes=codes8)[0] @ psi)
    ey = psi @ (build_sector(16, b16, N8, 4, ferm, wts=[1.0 if bd[2] == 1 else 0.0 for bd in b16], codes=codes8)[0] @ psi)
    check("S7 [float] %s bond energies equal in the two directions, sum to E0" % tag, abs(ex - ey) < 1e-9 and abs(ex + ey - E0) < 1e-9,
          "e_x=%.9f e_y=%.9f" % (ex, ey))
    torus[tag] = dict(E0=E0, psi=psi, rho=rho, gap=w1[1] - E0, s2=s2, ex=ex, ey=ey)
    # rate-mode second-order coefficient
    out = {}
    for qm in [(1, 0), (2, 0), (1, 1), (2, 1), (2, 2)]:
        al = alphas(b16, qm)
        H1 = build_sector(16, b16, N8, 4, ferm, wts=al, codes=codes8)[0]
        g = H1 @ psi
        del H1
        gc.collect()
        first = float(psi @ g)
        H2 = build_sector(16, b16, N8, 4, ferm, wts=al ** 2 / 2, codes=codes8)[0]
        held = float(psi @ (H2 @ psi))
        del H2
        gc.collect()
        rhs = g - psi * first
        A = sla.LinearOperator(H.shape, matvec=lambda z: H @ z - E0 * z + psi * (psi @ z), dtype=float)
        sol, info = sla.cg(A, rhs, rtol=1e-12, atol=0, maxiter=5000)
        relax = -float(rhs @ sol)
        out[qm] = dict(first=first, held=held, relax=relax, Pi=(held + relax) / 16, info=info)
        print("   %s q=(%d,%d)*pi/2: first-order %.1e, held/n %.10f, relax/n %.10f, Pi=E2/n %.10f (cg info %d)" %
              (tag, qm[0], qm[1], first, held / 16, relax / 16, (held + relax) / 16, info), flush=True)
    torus[tag]["q"] = out
    check("S7 [float] %s first-order response of the ground energy vanishes at all tested q (second-order coefficient exists)" % tag,
          all(abs(out[q]["first"]) < 1e-10 and out[q]["info"] == 0 for q in out))
    check("S7 [float] %s Pi(pi,pi) = 0 exactly (chessboard of clocks is invisible: held and relaxation both 0)" % tag,
          abs(out[(2, 2)]["held"]) < 1e-10 and abs(out[(2, 2)]["relax"]) < 1e-10)
    check("S7 [float] %s relaxation term <= 0 (concavity of E0 in the bond weights)" % tag, all(out[q]["relax"] <= 1e-12 for q in out))
    # held term identity: held/n = (1/4) sum_j (e_j/n) cos^2(q_j/2)... (q in units pi/2)
    ok = True
    for qm in [(1, 0), (2, 0)]:
        # exact structure: sum_b alpha_b^2/2 * <B_b> ; with equal bond energies per direction this is below
        al = alphas(b16, qm)
        pred2 = 0.0
        for bi, bd in enumerate(b16):
            pred2 += 0.5 * al[bi] ** 2 * ((ex if bd[2] == 0 else ey) / (16))   # <B_b> = e_dir / 16 if translation invariant
        ok &= abs(pred2 - out[qm]["held"]) < 1e-7
    check("S7 [float] %s held term equals (1/2) sum_b alpha_b^2 <B_b> with <B_b> = e_dir/16 (translation-invariant bond energy)" % tag, ok)
    # finite-difference cross-check of Pi(pi/2,0)
    eps = 0.02
    al = alphas(b16, (1, 0))
    Ep = sla.eigsh(build_sector(16, b16, N8, 4, ferm, wts=np.exp(eps * al), codes=codes8)[0], k=1, which="SA", tol=1e-13,
                   v0=psi)[0][0]
    Em = sla.eigsh(build_sector(16, b16, N8, 4, ferm, wts=np.exp(-eps * al), codes=codes8)[0], k=1, which="SA", tol=1e-13,
                   v0=psi)[0][0]
    fd = (Ep + Em - 2 * E0) / (2 * eps ** 2) / 16
    check("S7 [float] %s finite-difference (eps=0.02) agrees with perturbation theory for Pi(pi/2,0)" % tag,
          abs(fd - out[(1, 0)]["Pi"]) < 3e-4, "FD %.8f vs PT %.8f" % (fd, out[(1, 0)]["Pi"]))
    del H
    H7 = build_sector(16, b16, 7, 3, ferm)[0]
    E7 = sla.eigsh(H7, k=1, which="SA", tol=1e-10)[0][0]
    del H7
    check("S7 [float] %s: N=7 sector (Sz=1/2, all spins) ground energy is above the N=8 value (neighbouring filling)" % tag, E7 > E0 + 1e-3,
          "E(7)=%.9f > E(8)=%.9f" % (E7, E0))
    print("   [%s] elapsed %.0fs" % (tag, time.time() - T0), flush=True)

# free-sea Pi on the same torus (one-body, finite difference)
def free_Pi(qm, eps=0.005):
    def Eneg(e):
        al = alphas(b16, qm)
        h = np.zeros((16, 16))
        for bi, (a, b, j, t, c) in enumerate(b16):
            h[a, b] += t * math.exp(e * al[bi])
            h[b, a] += t * math.exp(e * al[bi])
        ev = np.linalg.eigvalsh(h)
        return 2 * ev[ev < 0].sum()
    return (Eneg(eps) + Eneg(-eps) - 2 * Eneg(0)) / (2 * eps ** 2) / 16
PiFree = {qm: free_Pi(qm) for qm in [(1, 0), (2, 0), (1, 1), (2, 1), (2, 2)]}
print("   free 2-coin sea Pi_free(pi/2,0)=%.8f, (pi,0)=%.8f, (pi,pi)=%.2e; c0_free/4=%.8f" %
      (PiFree[(1, 0)], PiFree[(2, 0)], PiFree[(2, 2)], -13.656854249492381 / 16 / 4))

# ----------------------------------------------------------------------------
print("=== S8: summary of per-site volume term c0 = E0/n and stiffness indicator ===")
cF = torus["F"]["E0"] / 16
cB = torus["B"]["E0"] / 16
print("   4x4 torus, N=8: c0(F)=%.10f  c0(B)=%.10f  free=%.10f  polarized=%.10f" % (cF, cB, -float(S2), -float(S2) / 2))
for tag, c in (("F", cF), ("B", cB)):
    Pi = torus[tag]["q"][(1, 0)]["Pi"]
    print("   %s: Pi(pi/2,0)=%.8f  c0/4=%.8f  difference=%.8f  Pi(pi,0)=%.8f" % (tag, Pi, c / 4, Pi - c / 4, torus[tag]["q"][(2, 0)]["Pi"]))
    check("S8 [float] %s: Pi(pi/2,0) > c0/4 on the 4x4 torus (positive stiffness indicator, same sign as the ring)" % tag, Pi - c / 4 > 0)
    tab = {qm: torus[tag]["q"][qm]["Pi"] - c / 4 for qm in torus[tag]["q"]}
    print("   %s: Pi(q)-c0/4 at q*(2/pi) in %s" % (tag, {k: round(v, 6) for k, v in tab.items()}))
    print("   %s: kappa_eff = 4 (Pi-c0/4)/|q|^2_lat at q=(pi/2,0), |q|^2_lat = 2(1-cos q) = 2: %.5f" % (tag, 4 * (Pi - c / 4) / 2))
check("S8 [float] exchange signs give different half-filled energies on the 4x4 torus", abs(cF - cB) > 1e-3, "c0F-c0B = %.8f" % (cF - cB))
ring_q = math.pi / 2
ring_Pi = -math.cos(ring_q / 2) ** 2 * math.log(1 / math.cos(ring_q / 2) + math.tan(ring_q / 2)) / (4 * math.pi * math.sin(ring_q / 2))
print("   ring (block 130 closed form) at q=pi/2: Pi=%.8f, c0/4=%.8f, difference %.8f, kappa_eff=%.5f (kappa->1/(6pi)=%.5f as q->0)" %
      (ring_Pi, -1 / (4 * math.pi), ring_Pi + 1 / (4 * math.pi), 4 * (ring_Pi + 1 / (4 * math.pi)) / 2, 1 / (6 * math.pi)))
print("   free 2-coin sea on the 4x4 torus: Pi_free - c0_free/4 at q (pi/2,0), (pi/2,pi/2), (pi,pi/2), (pi,0): %s" %
      [round(PiFree[k] + 13.656854249492381 / 16 / 4, 6) for k in [(1, 0), (1, 1), (2, 1), (2, 0)]])
# inclusion in the rigorous brackets
lowF2 = bounds[(2, 3, True)]
lowB2 = bounds[(2, 3, False)]
check("S8 [float] torus value of c0(F) within [3x3-tile lower bound, spin-polarized upper bound]",
      lowF2 <= cF <= -float(S2) / 2, "%.6f <= %.6f <= %.6f" % (lowF2, cF, -float(S2) / 2))
check("S8 [float] torus value of c0(B) above the 3x3-tile lower bound and below the 3x3-cluster-product upper bound's complement (torus beats clusters)",
      lowB2 <= cB <= ub[(2, 3, False)], "%.6f <= %.6f <= %.6f" % (lowB2, cB, ub[(2, 3, False)]))

print("=== rigorous-bracket table (per site) ===")
print("   d=2, both signs: lower -1/sqrt(2) = %.6f [exact, plaquette tile]; 3x3-tile (float): F %.6f, B %.6f" % (-1 / math.sqrt(2), bounds[(2, 3, True)], bounds[(2, 3, False)]))
print("   d=2 fermion upper: c0_free/2 = -%.6f (half the free 2-coin sea; Slater state of one coin, exact reduction)" % (float(c2) / 2))
print("   d=2 boson  upper: plaquette-product -sqrt(2)/4 = %.6f [exact]; 3x3-cluster (float) %.6f" % (-math.sqrt(2) / 4, ub[(2, 3, False)]))
print("   d=3 lower: (3/4)(-sqrt2) = %.6f [exact, plaquette tiles]; cube tile (float): F %.6f, B %.6f" % (-0.75 * math.sqrt(2), bounds[(3, 2, True)], bounds[(3, 2, False)]))
print("   d=3 fermion upper: c0_free/2 = -%.5f (numeric quadrature)" % (c3b / 2))
print("   d=3 boson upper: cube-product (float) %.6f ; plaquette-product -sqrt(2)/4 = %.6f [exact]" % (ub[(3, 2, False)], -math.sqrt(2) / 4))

# exact bracket checks that are pure arithmetic
tot = f"TOTAL: PASS={NP} FAIL={NF}"
print(tot)
print("runtime %.0fs" % (time.time() - T0))
print("HIT: scoped exact partial results for the 2D/3D hard-core sea (walk sigma_j D_j, one record per site): "
      "(i) exact gauge reduction to an SU(2)-invariant pi-flux real hopping model (L even), hence ground energy over all spins is read in the Sz<=1/2 sector; "
      "(ii) exact bracket c0 in [-1/sqrt2, c0_free/2] (d=2, fermionic) and [-1/sqrt2, -sqrt2/4] (d=2, bosonic), lower (3/4)(-sqrt2) in d=3; "
      "(iii) exact 2x3-cluster counterexample: the exchange signs have different ground energies in 2D "
      "(-1/2-sqrt3 vs -2.1126...) so block 130's one-twist-set statement does not extend; "
      "(iv) float-only on the 4x4 torus at half filling: E0/n = %.9f (F), %.9f (B), Pi(pi/2,0) = %.8f (F), %.8f (B), Pi(pi,pi)=0, relaxation <= 0."
      % (cF, cB, torus["F"]["q"][(1, 0)]["Pi"], torus["B"]["q"][(1, 0)]["Pi"]))
print("SUMMARY: PARTIAL the 2D/3D hard-core walk is exactly an SU(2)-symmetric pi-flux problem; exact two-sided bounds and an exact "
      "exchange-sign counterexample are shown, and the 4x4 torus half-filled energies and rate-mode coefficients are computed in floating point only; "
      "the exact torus value and the infinite-volume stiffness sign are not certified.")
sys.exit(0 if NF == 0 else 1)
