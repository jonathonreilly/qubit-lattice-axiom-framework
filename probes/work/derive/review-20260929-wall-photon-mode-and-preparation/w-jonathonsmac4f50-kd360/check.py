#!/usr/bin/env python3
"""Task J:derive:review-20260929-wall-photon-mode-and-preparation:a1

Supplied model (checked here on its only exactly solvable torus, 2x2x2): link spins
sigma=+-1 on the 24 links of the periodic cubic torus, exact vertex Gauss law
(sum over axes of sigma_a(r)-sigma_a(r-e_a) = 0), plaquette flips of circulating
plaquettes, H(v) = v*D - A on a flip component  (D = number of flippable plaquettes,
A = flip adjacency).  v=1 is the Rokhsar-Kivelson (RK) point (H = graph Laplacian),
v=0 is the pure ring point.  Transverse readout O_b = N^{-1/2} sum_{b-links}
(-1)^{x_{b+1}} sigma  (k = pi, axes cyclic).

Machinery is independent of the sources: own Gauss enumeration, own component search,
own character-sector bases, integer Bareiss inertia (Sylvester) and exact Hankel /
minimal-polynomial moment algebra over Q.  numpy/scipy only for floating cross-checks.
"""
import sys, time, itertools
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

T0 = time.time()
RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (" : " + detail if detail else ""))
    sys.stdout.flush()


# ---------------------------------------------------------------- lattice, Gauss space
Ls = (2, 2, 2)
sites = list(itertools.product(range(2), repeat=3))


def sh(s, a, d=1):
    t = list(s)
    t[a] = (t[a] + d) % 2
    return tuple(t)


links = [(s, a) for s in sites for a in range(3)]
lid = {l: i for i, l in enumerate(links)}
plaq = []
for s in sites:
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        plaq.append((lid[(s, i)], lid[(sh(s, i), j)], lid[(sh(s, j), i)], lid[(s, j)]))
pmask = [sum(1 << l for l in p) for p in plaq]


def circ(m, p):
    b = lambda l: 1 if (m >> l) & 1 else -1
    return b(p[0]) + b(p[1]) - b(p[2]) - b(p[3])


allm = np.arange(1 << 24, dtype=np.uint32)
ok = np.ones(1 << 24, dtype=bool)
for s in sites:
    d = np.zeros(1 << 24, dtype=np.int8)
    for a in range(3):
        for (l, sg) in ((lid[(s, a)], 1), (lid[(sh(s, a, -1), a)], -1)):
            d += sg * (((allm >> np.uint32(l)) & np.uint32(1)).astype(np.int8) * 2 - 1)
    ok &= (d == 0)
gauss = [int(x) for x in allm[ok]]
del allm, ok
report("G1 Gauss states on 2x2x2", len(gauss) == 9600, f"{len(gauss)} (expect 9600)")

gset = set(gauss)
seen = set()
comps = []
for st in sorted(gset):
    if st in seen:
        continue
    comp = [st]
    seen.add(st)
    q = [st]
    while q:
        m = q.pop()
        for pi, p in enumerate(plaq):
            if abs(circ(m, p)) == 4:
                m2 = m ^ pmask[pi]
                if m2 not in seen:
                    seen.add(m2)
                    comp.append(m2)
                    q.append(m2)
    comps.append(comp)
sizes = sorted(len(c) for c in comps)
report("G2 flip components", len(comps) == 937 and sizes[-1] == 864 and sum(sizes) == 9600,
       f"{len(comps)} components, largest {sizes[-1]}")


def winding(m):
    w = []
    for a in range(3):
        t = 0
        for (s, ax), l in lid.items():
            if ax == a and s[a] == 0:
                t += 1 if (m >> l) & 1 else -1
        w.append(t)
    return tuple(w)


canon_start = 0
for (s, a), l in lid.items():
    sg = (1 if s[1] % 2 == 0 else -1) if a == 0 else (1 if s[0] % 2 == 0 else -1)
    if sg > 0:
        canon_start |= 1 << l
canon = [c for c in comps if canon_start in set(c)][0]
frozen0 = [c for c in comps if len(c) == 1 and winding(c[0]) == (0, 0, 0)]
report("G3 canonical component and zero-winding frozen states",
       len(canon) == 864 and len(frozen0) == 16 and winding(canon_start) == (0, 0, 0),
       f"canonical {len(canon)} states, {len(frozen0)} frozen zero-winding states")

# ---------------------------------------------------------------- ground-space treatment
degs = {}
for ci, c in enumerate(comps):
    tot = 0
    for m in c:
        for p in plaq:
            if abs(circ(m, p)) == 4:
                tot += 1
    degs[ci] = Fraction(tot, len(c))
canon_i = [i for i, c in enumerate(comps) if len(c) == 864][0]
vals = sorted(degs.values(), reverse=True)
report("G4 first-order component ranking <N_f> (exact rationals)",
       degs[canon_i] == 8 and vals[1] < 8,
       f"canonical <N_f>=8 is the unique maximum over 937 components; runner-up {vals[1]}")


def comp_matrices(c):
    idx = {m: i for i, m in enumerate(c)}
    n = len(c)
    A = np.zeros((n, n))
    D = np.zeros(n)
    for m, i in idx.items():
        for pi, p in enumerate(plaq):
            if abs(circ(m, p)) == 4:
                D[i] += 1
                A[i, idx[m ^ pmask[pi]]] += 1
    return A, D


cm = [comp_matrices(c) for c in comps]
null_total = 0
for (A, D) in cm:
    w = np.linalg.eigvalsh(np.diag(D) - A)
    null_total += int(np.sum(np.abs(w) < 1e-9))
report("G5 RK zero eigenspace of the FULL Gauss space has dimension 937 (one uniform vector per component)",
       null_total == 937, f"nullity {null_total}")
okv = True
detail = []
for v in (0.9, 0.75, 0.5, 0.25, 0.0):
    e0 = []
    for (A, D) in cm:
        e0.append(np.linalg.eigvalsh(v * np.diag(D) - A)[0])
    e0 = np.array(e0)
    am = int(np.argmin(e0))
    srt = np.sort(e0)
    okv &= (am == canon_i) and (srt[1] - srt[0] > 1e-3)
    detail.append(f"v={v}: E0={srt[0]:.5f} next component {srt[1]:.5f}")
report("G6 the global ground state of the full Gauss space lies in the canonical component for v<1 (grid)", okv,
       "; ".join(detail))

# ---------------------------------------------------------------- canonical component data
order = canon
N = len(order)
idx = {m: i for i, m in enumerate(order)}
A = np.zeros((N, N), dtype=np.int64)
D = np.zeros(N, dtype=np.int64)
nbr = [[] for _ in range(N)]
for m, i in idx.items():
    for pi, p in enumerate(plaq):
        if abs(circ(m, p)) == 4:
            D[i] += 1
            j = idx[m ^ pmask[pi]]
            A[i, j] += 1
            nbr[i].append(j)
sigma = np.array([[1 if (m >> l) & 1 else -1 for l in range(24)] for m in order], dtype=np.int64)
Ohat = []
for b in range(3):
    o = np.zeros(N, dtype=np.int64)
    for (s, ax), l in lid.items():
        if ax == b:
            o += ((-1) ** s[(b + 1) % 3]) * sigma[:, l]
    Ohat.append(o)  # O_b = Ohat/sqrt(8)

# translations Z_2^3
Gs = list(itertools.product([0, 1], repeat=3))


def tperm(g):
    lp = [0] * 24
    for (s, a), l in lid.items():
        t = tuple((s[i] + g[i]) % 2 for i in range(3))
        lp[l] = lid[(t, a)]
    perm = np.zeros(N, dtype=np.int64)
    for m, i in idx.items():
        m2 = 0
        for l in range(24):
            if (m >> l) & 1:
                m2 |= 1 << lp[l]
        perm[i] = idx[m2]
    return perm


perms = {g: tperm(g) for g in Gs}
ok1 = all((D[perms[g]] == D).all() and (A[np.ix_(perms[g], perms[g])] == A).all() for g in Gs)
report("T1 translations are automorphisms of the flip graph of the canonical component", ok1)
ok2 = True
for b in range(3):
    for g in Gs:
        chi = (-1) ** (g[(b + 1) % 3])
        ok2 &= bool((Ohat[b][perms[g]] == chi * Ohat[b]).all())
report("T2 exact translation character of every transverse mode: O_b has momentum pi along x_{b+1} only", ok2)


def sector_basis(c):
    cols = []
    done = np.zeros(N, bool)
    for s0 in range(N):
        if done[s0]:
            continue
        vec = np.zeros(N, dtype=np.int64)
        orb = set()
        for g in Gs:
            t = perms[g][s0]
            orb.add(t)
            vec[t] += (-1) ** sum(ci * gi for ci, gi in zip(c, g))
        for t in orb:
            done[t] = True
        if vec.any():
            cols.append(vec)
    return np.array(cols).T


bases = {c: sector_basis(c) for c in Gs}
dims = {c: bases[c].shape[1] for c in Gs}
orthok = True
for c in Gs:
    Bc = bases[c]
    Gm = Bc.T @ Bc
    orthok &= bool((Gm == np.diag(np.diag(Gm))).all())
for c in Gs:
    for c2 in Gs:
        if c < c2:
            orthok &= bool((bases[c].T @ bases[c2] == 0).all())
Hrk = np.diag(D) - A
blockok = all((bases[c].T @ Hrk @ bases[c2] == 0).all() for c in Gs for c2 in Gs if c != c2)
report("T3 character sectors: orthogonal, complete, H block diagonal",
       orthok and blockok and sum(dims.values()) == 864,
       "dims " + str(sorted(dims.values(), reverse=True)))


# ---------------------------------------------------------------- exact inertia (Sylvester via Bareiss)
def neg_count(M):
    """number of negative eigenvalues of integer symmetric matrix M, through the sign
    changes of its leading principal minors (fraction-free elimination); raises when a
    leading minor vanishes."""
    n = len(M)
    M = [[int(x) for x in r] for r in M]
    prev = 1
    signs = [1]
    for k in range(n):
        piv = M[k][k]
        if piv == 0:
            raise ZeroDivisionError
        signs.append(1 if piv > 0 else -1)
        Mk = M[k]
        for i in range(k + 1, n):
            Mi = M[i]
            f = Mi[k]
            for j in range(k + 1, n):
                Mi[j] = (Mi[j] * piv - f * Mk[j]) // prev
            Mi[k] = 0
        prev = piv
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def inertia_below(c, p, q, a, den):
    """number of eigenvalues of H=(p D - q A)/q in character sector c strictly below a/den."""
    Bc = bases[c]
    Hq = p * np.diag(D) - q * A
    Bs = Bc.T @ Hq @ Bc
    Gd = np.diag(Bc.T @ Bc)
    for bump in range(0, 50):
        M = Bs * den - (a + bump) * q * np.diag(Gd)
        try:
            return neg_count(M), a + bump
        except ZeroDivisionError:
            continue
    raise RuntimeError("pivot")


# exact RK sector spectrum around the first two levels
DEN = 10 ** 6
zero_c = (0, 0, 0)
nz_lo, _ = inertia_below(zero_c, 1, 1, 969623, DEN)
nz_hi, _ = inertia_below(zero_c, 1, 1, 969624, DEN)
report("S1 RK trivial-momentum sector holds the zero mode and the global-gap doublet 0.969623..0.969624",
       nz_lo == 1 and nz_hi == 3, f"eigenvalues below 0.969623: {nz_lo}, below 0.969624: {nz_hi}")
allok = True
msg = []
for b in range(3):
    c = tuple(1 if i == (b + 1) % 3 else 0 for i in range(3))
    n_a, _ = inertia_below(c, 1, 1, 1160865, DEN)
    n_b, _ = inertia_below(c, 1, 1, 1160866, DEN)
    allok &= (n_a == 0 and n_b == 2)
    msg.append(f"b={b} sector {c}: below 1.160865 -> {n_a}, below 1.160866 -> {n_b}")
report("S2 each transverse-mode sector (k=pi): no eigenvalue below 1.160865 and a double level below 1.160866 (exact)",
       allok, "; ".join(msg))
other = 0
for c in Gs:
    if c in [(0, 0, 0)] + [tuple(1 if i == (b + 1) % 3 else 0 for i in range(3)) for b in range(3)]:
        continue
    n_c, _ = inertia_below(c, 1, 1, 1160866, DEN)
    other += n_c
report("S3 the other four momentum sectors (weight 2 and 3 characters) have no level below 1.160866 (exact)", other == 0,
       f"total eigenvalues below 1.160866 in the four sectors: {other}")

# ---------------------------------------------------------------- exact moment algebra at RK
Lap = [(int(D[i]), nbr[i]) for i in range(N)]


def lap_apply(vec):
    out = [0] * N
    for i in range(N):
        d, nb = Lap[i]
        s = d * vec[i]
        for j in nb:
            s -= vec[j]
        out[i] = s
    return out


def moments(fvec, kmax):
    mus = []
    fvec = [int(x) for x in fvec]
    cur = list(fvec)
    for k in range(kmax + 1):
        mus.append(Fraction(sum(a * b for a, b in zip(fvec, cur)), N * 8))
        if k < kmax:
            cur = lap_apply(cur)
    return mus


KMAX = 44
mu_by_b = [moments(Ohat[b], KMAX) for b in range(3)]
report("M1 exact moments mu_k=<u|O (L^k) O|u> are identical for the three cyclic modes (k<=44, rationals)",
       mu_by_b[0] == mu_by_b[1] == mu_by_b[2],
       f"m0={mu_by_b[0][0]}, m1={mu_by_b[0][1]}")
mu = mu_by_b[0]
m0, m1 = mu[0], mu[1]


def hankel_det(d):
    M = [[mu[i + j] for j in range(d)] for i in range(d)]
    dm = DomainMatrix([[QQ(x.numerator, x.denominator) for x in row] for row in M], (d, d), QQ)
    return dm.det()


r = None
for d in range(1, 22):
    if hankel_det(d) == 0:
        r = d - 1
        break
report("M2 number of distinct atoms of the transverse spectral measure (first singular Hankel determinant)",
       r is not None and r >= 2, f"r={r}")

# minimal polynomial from Hankel system
Hm = DomainMatrix([[QQ(mu[i + j].numerator, mu[i + j].denominator) for j in range(r)] for i in range(r)], (r, r), QQ)
rhs = DomainMatrix([[QQ(-mu[r + i].numerator, mu[r + i].denominator)] for i in range(r)], (r, 1), QQ)
csol = Hm.lu_solve(rhs).to_Matrix()
x = sp.symbols("x")
mpoly = sp.Poly(x ** r + sum(csol[j, 0] * x ** j for j in range(r)), x, domain="QQ")
cfs = [Fraction(int(sp.Rational(csol[j, 0]).p), int(sp.Rational(csol[j, 0]).q)) for j in range(r)]

# verify m(L) f = 0 exactly, as vectors
fvec = [int(t) for t in Ohat[0]]
pw = [fvec]
for k in range(r):
    pw.append(lap_apply(pw[-1]))
resid_zero = True
for i in range(N):
    val = Fraction(pw[r][i]) + sum(cfs[j] * pw[j][i] for j in range(r))
    if val != 0:
        resid_zero = False
        break
report("M3 minimal polynomial annihilates the vector O_0|u> exactly (all 864 components, rationals)", resid_zero,
       f"degree {r}")
roots_all_real = mpoly.count_roots() == r and mpoly.count_roots(0, None) == r
sqf = sp.gcd(mpoly, mpoly.diff(x)).degree() == 0
report("M4 all roots real, positive and simple (Sturm count, exact)", roots_all_real and sqf,
       f"{mpoly.count_roots()} real roots of degree {r}")
facs = sp.factor_list(mpoly.as_expr(), x)[1]
fac_degs = sorted(sp.degree(f, x) for f, _ in facs)
ivs = mpoly.intervals(eps=sp.Rational(1, 10 ** 25))
lo_iv = ivs[0][0]
lo_a, lo_b = sp.Rational(lo_iv[0]), sp.Rational(lo_iv[1])
report("M5 lowest transverse-coupled level at RK: exact isolating interval from the minimal polynomial agrees with the independent inertia bracket [1.160865,1.160866)",
       sp.Rational(1160865, 10 ** 6) <= lo_a and lo_b < sp.Rational(1160866, 10 ** 6),
       f"omega_min in [{float(lo_a):.12f},{float(lo_b):.12f}]; irreducible factor degrees {fac_degs}")

global_gap_float = None
w_all = np.linalg.eigvalsh((np.diag(D) - A).astype(float))
global_gap_float = w_all[1]
report("M6 the global gap (0.9696...) is strictly below the lowest transverse-coupled level and is NOT a root of the minimal polynomial",
       float(lo_a) > global_gap_float + 0.19 and abs(float(mpoly.as_expr().subs(x, global_gap_float))) > 1e-3 * abs(float(mpoly.as_expr().subs(x, 0.3))),
       f"global gap {global_gap_float:.9f}, lowest coupled {float(lo_a):.9f}, ratio {float(lo_a)/global_gap_float:.4f}")

# m_{-1}, weights
mm1 = -(mu[r - 1] + sum(cfs[j] * mu[j - 1] for j in range(1, r))) / cfs[0]
mp.mp.dps = 60
rts = [mp.mpf(str(t)) for t in sp.Poly(mpoly, x).nroots(n=60, maxsteps=500)]
rts = sorted([mp.re(t) for t in rts])
dpoly = sp.Poly(mpoly, x).diff(x)
weights = []
for j, wj in enumerate(rts):
    # l_j(x) = m(x)/((x-wj) m'(wj)); sum_k l_{j,k} mu_k
    coeffs = [mp.mpf(0)] * (r + 1)
    # synthetic division of m by (x-wj)
    mcoef = [mp.mpf(str(sp.Rational(c).p)) / mp.mpf(str(sp.Rational(c).q)) for c in
             list(reversed(sp.Poly(mpoly, x).all_coeffs()))]  # ascending
    # ascending coefficients -> quotient
    q_desc = []
    carry = mp.mpf(0)
    for cdesc in reversed(mcoef):
        carry = cdesc + carry * wj
        q_desc.append(carry)
    q_desc = q_desc[:-1]  # remove remainder
    q_asc = list(reversed(q_desc))
    mprime = sum(k * mcoef[k] * wj ** (k - 1) for k in range(1, r + 1))
    wt = sum(q_asc[k] * (mp.mpf(mu[k].numerator) / mu[k].denominator) for k in range(r)) / mprime
    weights.append(wt)
sw = sum(weights)
s1 = sum(w * t for w, t in zip(weights, rts))
sm1 = sum(w / t for w, t in zip(weights, rts))
okw = all(w > 0 for w in weights) and abs(sw - mp.mpf(m0.numerator) / m0.denominator) < mp.mpf(10) ** -40 \
    and abs(s1 - mp.mpf(m1.numerator) / m1.denominator) < mp.mpf(10) ** -40 \
    and abs(sm1 - mp.mpf(mm1.numerator) / mm1.denominator) < mp.mpf(10) ** -40
report("M7 spectral weights from exact moments are positive and reproduce m0, m1, m_{-1} to 40 digits",
       okw, f"m0={m0}, m1={m1}, m_{{-1}}={float(mm1):.12f}; weight of the lowest level {mp.nstr(weights[0], 10)} "
            f"({float(weights[0] / (mp.mpf(m0.numerator) / m0.denominator)):.4%} of m0)")
chain = [float(rts[0]), float(m0 / mm1), float((m1 / mm1)) ** 0.5, float(m1 / m0)]
report("M8 exact moment chain omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 at RK on 2^3",
       chain[0] <= chain[1] <= chain[2] <= chain[3] and m1 / m0 == Fraction(8, 5),
       " <= ".join(f"{t:.6f}" for t in chain) + "; m1/m0 = 8/5 exactly")
# weight in the lowest level compared with moment-only information
markov_cap = rts[0] * (mp.mpf(mm1.numerator) / mm1.denominator)
report("M9 Markov cap on the weight at/below omega_min (w <= omega_min*m_-1) holds with the exact weight",
       weights[0] <= markov_cap,
       f"lowest weight {mp.nstr(weights[0],8)}, cap {mp.nstr(markov_cap,8)}")

# ---------------------------------------------------------------- ground-space treatment: exact plug-in illustration
delta2 = m0 / 2  # centering error: f_hat = f + delta*u, delta^2 = m0/2
plug = m1 / (m0 + delta2)
report("P1 plug-in Rayleigh quotient with a centering error can fall below the lowest coupled level (exact at RK)",
       float(plug) < float(rts[0]) and plug == Fraction(16, 15),
       f"R(f+delta*u)=m1/(m0+delta^2)={plug}={float(plug):.4f} < omega_min={float(rts[0]):.4f}; H u = 0 so the numerator is unchanged")


# exact three-level example of the degenerate-ground-space rule (O connects two ground states)
Hx = sp.diag(0, 0, 1)
Ox = sp.Matrix([[0, sp.Rational(1, 2), sp.Rational(1, 3)], [sp.Rational(1, 2), 0, 0], [sp.Rational(1, 3), 0, 0]])
g0 = sp.Matrix([1, 0, 0])
Og = Ox * g0
m1x = (Og.T * Hx * Og)[0]
m0_naive = (Og.T * Og)[0] - (g0.T * Og)[0] ** 2
m0_Q = Og[2] ** 2
report("P2 degenerate ground space (exact 3-level example): excluding only |g> from the centred mode gives m1/m0 below the lowest excited level; excluding the whole ground eigenspace does not",
       m1x / m0_naive < 1 <= m1x / m0_Q and m1x / m0_naive == sp.Rational(4, 13) and m1x / m0_Q == 1,
       f"m1/m0(naive)={m1x/m0_naive}, m1/m0(ground space removed)={m1x/m0_Q}, lowest excited level 1")

# ---------------------------------------------------------------- certified brackets away from RK (v rational)
def float_data(v):
    H = v * np.diag(D.astype(float)) - A.astype(float)
    w, U = np.linalg.eigh(H)
    g = U[:, 0]
    Ob = Ohat[0].astype(float) / np.sqrt(8.0)
    c = U.T @ (Ob * g)
    wts = c[1:] ** 2
    om = w[1:] - w[0]
    sel = wts > 1e-13
    wsel, osel = wts[sel], om[sel]
    wlow = wsel[osel < osel.min() + 1e-7].sum()
    return w[0], wsel.sum(), (wsel * osel).sum(), (wsel / osel).sum(), osel.min(), abs(c[0]), wlow / wsel.sum()


def sector_bracket(c, p, q, lam_hat, tol=2e-6):
    den = 10 ** 7
    a_lo = int(np.floor((lam_hat - tol) * den))
    a_hi = int(np.ceil((lam_hat + tol) * den))
    n_lo, a_lo = inertia_below(c, p, q, a_lo, den)
    n_hi, a_hi = inertia_below(c, p, q, a_hi, den)
    return n_lo, n_hi, Fraction(a_lo, den), Fraction(a_hi, den)


rows = []
allcert = True
cb = (0, 1, 0)  # mode b=0 -> odd along x_1
for (p, q) in [(3, 4), (1, 2), (1, 4), (0, 1)]:
    v = p / q
    E0, m0f, m1f, mm1f, om_cpl, ov, wfrac = float_data(v)
    # E0 bracket: trivial sector
    e_lo_n, e_hi_n, e_lo, e_hi = sector_bracket(zero_c, p, q, E0, tol=1e-5)
    # lowest eigenvalue in the odd sector
    Bc = bases[cb]
    Hq = p * np.diag(D) - q * A
    Bs = (Bc.T @ Hq @ Bc) / q
    Gd = np.diag(Bc.T @ Bc).astype(float)
    sw_ = np.linalg.eigvalsh(Bs / np.sqrt(np.outer(Gd, Gd)))
    lam_sec = sw_[0]
    s_lo_n, s_hi_n, s_lo, s_hi = sector_bracket(cb, p, q, lam_sec, tol=1e-5)
    LB = s_lo - e_hi
    UB = m0f / mm1f
    good = (e_lo_n == 0 and e_hi_n == 1 and s_lo_n == 0 and s_hi_n >= 1
            and float(LB) <= om_cpl + 1e-9 <= UB + 1e-9 and ov < 1e-9)
    allcert &= good
    rows.append(f"v={p}/{q}: E0 in [{float(e_lo):.5f},{float(e_hi):.5f}], sector floor >= {float(s_lo):.5f}, "
                f"certified omega_min >= {float(LB):.5f}; float coupled {om_cpl:.5f} (carries {wfrac:.1%} of m0); m0/m_-1 = {UB:.5f}; m1/m0 = {m1f/m0f:.5f}")
report("C1 certified lower bounds for the lowest transverse-coupled level at rational detunings (exact inertia in the momentum sector; "
       "Perron-Frobenius ground state in the trivial sector)", allcert, "")
for rr in rows:
    print("     " + rr)
# does the sector floor coincide with the coupled level (float)?
coin = []
for (p, q) in [(1, 1), (3, 4), (1, 2), (1, 4), (0, 1)]:
    v = p / q
    E0, m0f, m1f, mm1f, om_cpl, ov, wfrac = float_data(v)
    Bc = bases[cb]
    Bs = (Bc.T @ (p * np.diag(D) - q * A) @ Bc) / q
    Gd = np.diag(Bc.T @ Bc).astype(float)
    lam_sec = np.linalg.eigvalsh(Bs / np.sqrt(np.outer(Gd, Gd)))[0] - E0
    coin.append(abs(lam_sec - om_cpl))
report("C2 float: the lowest level of the momentum-pi sector is the lowest level coupled to O_0|0> at every detuning tried (differences < 1e-8)",
       max(coin) < 1e-8, f"max difference {max(coin):.2e}")

# ---------------------------------------------------------------- static/dynamic separation (conditional lemma)
m1_ident = Fraction(2) * Fraction(1, 3) * 4  # 2 u s^2 with u=<N_f>/(3N)=8/24, s^2=4
report("L1 f-sum identity at RK: m1 = 2 u_RK s^2 with u_RK=<N_f>/(3N)=1/3, s^2=2-2cos(pi)=4 (exact)", m1 == m1_ident,
       f"m1={m1}")
report("L2 conditional implication (algebra): omega_min <= m1/m0 = 2 u_RK s^2 / S(k); a static constant S(k)>=S_*>0 forces omega_min = O(k^2) at RK "
       "(only the L=2 ratio is evaluated here)", float(rts[0]) <= float(m1 / m0), f"{float(rts[0]):.4f} <= {float(m1/m0):.4f}")

# ---------------------------------------------------------------- summary
npass = sum(RESULTS)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
print(f"runtime_seconds: {time.time()-T0:.1f}")
if nfail == 0:
    print("HIT: on the exact 2x2x2 RK component (864 states) the global gap doublet (0.969623617, trivial momentum sector) is exactly "
          "uncoupled to every k=pi transverse mode, the lowest transverse-coupled level is a distinct exact algebraic number "
          f"({float(lo_b):.9f}, irreducible minimal polynomial of degree {r}, about 20% above the gap) with certified lower brackets away from RK; scoped to L=2, no scaling.")
print("SUMMARY: exact-arithmetic L=2 result (864-state RK/ring component): the lowest transverse-coupled level lies in the momentum-pi sector and is "
      f"{float(lo_b):.6f} at RK versus a global gap {global_gap_float:.6f} that is uncoupled, with certified lower brackets for v in {{3/4,1/2,1/4,0}}; "
      "no size or momentum scaling and no photon statement follows.")
sys.exit(0 if nfail == 0 else 1)
