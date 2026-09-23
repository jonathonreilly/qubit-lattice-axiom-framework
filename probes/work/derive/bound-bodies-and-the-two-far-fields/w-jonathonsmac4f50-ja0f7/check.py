#!/usr/bin/env python3
"""J:derive:bound-bodies-and-the-two-far-fields:a2 - worker w-jonathonsmac4f50-ja0f7.

Block 60 (open PR #8590): rates w = e^u, one length l = e^lam per site, chi = sqrt(l), N = w chi; content
crossed at sqrt(w_x w_y)/(chi_x chi_y) on bonds plus rest terms rho w on sites; the curvature member
F = -8K sum_bonds (N_y - N_x)(chi_y - chi_x) over every bond with an interior end; walls held at w = l = 1.
e_z = d<H>/du_z, tau_z = -d<H>/dlam_z, E = <H>, T = sum tau (the hop energy), ledger = E + F.
Q = -sum_interior (Delta chi) (the lengths' charge), P = sum_interior (Delta N) (the rates' charge).
Exact parts: sympy.  Parts labelled NUMERIC: floating point.
"""
import itertools
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import snlat  # noqa: E402

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


def nbrs(s):
    for a in range(3):
        for d in (1, -1):
            t = list(s)
            t[a] += d
            yield tuple(t)


# ---------------------------------------------------------------- a symbolic box: two interior sites, ten walls
I = [(1, 1, 1), (2, 1, 1)]
W = sorted({t for s in I for t in nbrs(s) if t not in I})
ALL = I + W
bonds = sorted({tuple(sorted((s, t))) for s in I for t in nbrs(s)})
wv = {s: sp.Symbol(f"w_{''.join(map(str, s))}", positive=True) for s in ALL}
cv = {s: sp.Symbol(f"c_{''.join(map(str, s))}", positive=True) for s in ALL}
K, h, r1, r2 = sp.symbols('K h rho1 rho2', positive=True)
Nv = {s: wv[s] * cv[s] for s in ALL}
hop = h * sp.sqrt(wv[I[0]] * wv[I[1]]) / (cv[I[0]] * cv[I[1]])
Ect = hop + r1 * wv[I[0]] + r2 * wv[I[1]]
Tct = hop
Ffe = -8 * K * sum((Nv[b[1]] - Nv[b[0]]) * (cv[b[1]] - cv[b[0]]) for b in bonds)
Led = Ect + Ffe
du = lambda f, s: wv[s] * sp.diff(f, wv[s])                  # d/du
dl = lambda f, s: cv[s] / 2 * sp.diff(f, cv[s])              # d/dlam
lap = lambda f, s: sum(f[t] - f[s] for t in nbrs(s))
ok = True
for z in I:
    e_z = du(Ect, z)
    tau_z = -dl(Ect, z)
    ok &= sp.simplify(du(Led, z) - (e_z + 8 * K * Nv[z] * lap(cv, z))) == 0
    ok &= sp.simplify(dl(Led, z) - (-tau_z + 4 * K * (Nv[z] * lap(cv, z) + cv[z] * lap(Nv, z)))) == 0
    # the stationary pair of equations is the supervisor's scratch result
    dc, dN = sp.symbols('dc dN')
    solz = sp.solve([e_z + 8 * K * Nv[z] * dc, -tau_z + 4 * K * (Nv[z] * dc + cv[z] * dN)], [dc, dN], dict=True)[0]
    ok &= sp.simplify(solz[dc] + e_z / (8 * K * Nv[z])) == 0
    ok &= sp.simplify(solz[dN] - (e_z + 2 * tau_z) / (8 * K * cv[z])) == 0
check('A1', ok, "(a) EXACT (symbolic box, rates and lengths free at every site, a bond energy and two rest "
      "energies): d(ledger)/du_z = e_z + 8K N_z (Delta chi)_z and d(ledger)/dlam_z = -tau_z + 4K [N_z (Delta chi)_z + "
      "chi_z (Delta N)_z]; stationarity is Delta chi = -e/(8K N), Delta N = (e + 2 tau)/(8K chi) - the "
      "supervisor's scratch result re-derived")

# ---------------------------------------------------------------- A2 the two weight identities and the walls
ok = sp.simplify(sum(du(Led, s) for s in ALL) - Led) == 0                       # rates: weight one
ok &= sp.simplify(sum(dl(Led, s) for s in ALL) - (Ffe - Tct)) == 0              # lengths: hop -1, rest 0, F +1
walls1 = {wv[s]: 1 for s in W}
walls1.update({cv[s]: 1 for s in W})
wall_bonds = [(b[1], b[0]) if b[1] in I else (b[0], b[1]) for b in bonds if (b[0] in W) != (b[1] in W)]  # (interior, wall)
flux_c = sum(cv[y] - 1 for (y, x) in wall_bonds)
flux_N = sum(Nv[y] - 1 for (y, x) in wall_bonds)
ok &= sp.simplify((sum(du(Ffe, s) for s in W) - 8 * K * flux_c).subs(walls1)) == 0
ok &= sp.simplify((sum(dl(Ffe, s) for s in W) - 4 * K * (flux_c + flux_N)).subs(walls1)) == 0
ok &= sp.simplify((-sum(lap(cv, s) for s in I) - flux_c).subs(walls1)) == 0     # Gauss: Q
ok &= sp.simplify((sum(lap(Nv, s) for s in I) + flux_N).subs(walls1)) == 0      # Gauss: P
check('A2', ok, "(d) EXACT, THE FAR FIELDS AT EVERY STRENGTH: scaling every rate gives sum_all dL/du = L; scaling every "
      "length gives sum_all dL/dlam = F - T (hop energy weight -1, rest 0, the curvature member +1); at held walls "
      "the rates' identity leaves 8K x (flux of chi) = 8K Q and the lengths' leaves 4K (Q - P) (Gauss); so on "
      "every configuration stationary in the interior fields, whatever the content does: 8K Q = E + F (the "
      "ledger), P - Q = (T - F)/(4K) and P + Q = (E + T)/(4K): the rates' far field P + Q counts energy plus hop "
      "energy, the lengths' 2Q counts the ledger, and they agree iff the content's hop energy equals the field energy")

# ---------------------------------------------------------------- A3 exact solution: block 60's pinned body
n3 = 3
sites3 = list(itertools.product(range(1, n3 + 1), repeat=3))
ix = {s: i for i, s in enumerate(sites3)}
Lp = sp.zeros(len(sites3), len(sites3))
for s in sites3:
    Lp[ix[s], ix[s]] = 6
    for t in nbrs(s):
        if t in ix:
            Lp[ix[s], ix[t]] = -1
g = Lp.inv()                                    # inverse of -Delta, walls zero
cen = ix[(2, 2, 2)]
g0 = g[cen, cen]
Kv = sp.Rational(1, 2)
m = sp.Integer(3)
mu = m / (8 * Kv)
Q = (-1 + sp.sqrt(1 + 4 * g0 * mu)) / (2 * g0)
w0 = 1 / (1 + 2 * Q * g0)
P = Q * w0
chi = {s: 1 + Q * g[ix[s], cen] for s in sites3}
Nf = {s: 1 - P * g[ix[s], cen] for s in sites3}
val = lambda f, s: f[s] if s in ix else 1
bonds3 = sorted({tuple(sorted((s, t))) for s in sites3 for t in nbrs(s)})
F3 = -8 * Kv * sum((val(Nf, b[1]) - val(Nf, b[0])) * (val(chi, b[1]) - val(chi, b[0])) for b in bonds3)
E3 = m * w0
ok = sp.simplify(sp.expand(Q * (1 + Q * g0) - mu)) == 0
ok &= sp.simplify(8 * Kv * Q - (E3 + F3)) == 0
ok &= sp.simplify(P - Q - (0 - F3) / (4 * Kv)) == 0
ok &= sp.simplify(P + Q - (E3 + 0) / (4 * Kv)) == 0
check('A3', ok, "(d) EXACT ON AN EXACT SOLUTION: block 60 T4's pinned body (bare energy 3, K = 1/2, centre of the "
      "3^3 box; Q, P, w_0 in radicals) satisfies 8KQ = E + F, P - Q = -F/(4K) and P + Q = E/(4K) exactly: a pinned "
      "body has no hop energy, so P < Q by F/(4K)",
      f"Q = {sp.N(Q, 12)}, P = {sp.N(P, 12)}, F = {sp.N(F3, 12)}")

# ---------------------------------------------------------------- A4 NUMERIC: strong field, generic content
rng = np.random.default_rng(7)
n4 = 3
S4 = list(itertools.product(range(1, n4 + 1), repeat=3))
i4 = {s: i for i, s in enumerate(S4)}
NI = len(S4)
B4 = sorted({tuple(sorted((s, t))) for s in S4 for t in nbrs(s)})
CB = [b for b in B4 if b[0] in i4 and b[1] in i4]


def solve_case(hvals, rvals, K4):
    def unpack(x):
        u, lam = x[:NI], x[NI:]
        w = lambda s: np.exp(u[i4[s]]) if s in i4 else 1.0
        c = lambda s: np.exp(lam[i4[s]] / 2) if s in i4 else 1.0
        return u, lam, w, c

    def content(x):
        u, lam, w, c = unpack(x)
        e = np.zeros(NI)
        tau = np.zeros(NI)
        for b in CB:
            hb = hvals[b] * np.sqrt(w(b[0]) * w(b[1])) / (c(b[0]) * c(b[1]))
            for s in b:
                e[i4[s]] += hb / 2
                tau[i4[s]] += hb / 2
        for s in S4:
            e[i4[s]] += rvals[s] * w(s)
        return e, tau

    def resid(x):
        u, lam, w, c = unpack(x)
        e, tau = content(x)
        N = lambda s: w(s) * c(s)
        out = np.zeros(2 * NI)
        for s in S4:
            dc = sum(c(t) - c(s) for t in nbrs(s))
            dN = sum(N(t) - N(s) for t in nbrs(s))
            out[i4[s]] = e[i4[s]] + 8 * K4 * N(s) * dc
            out[NI + i4[s]] = -tau[i4[s]] + 4 * K4 * (N(s) * dc + c(s) * dN)
        return out
    sol = root(resid, np.zeros(2 * NI), method='hybr', options={'xtol': 1e-15})
    x = sol.x
    u, lam, w, c = unpack(x)
    e, tau = content(x)
    N = lambda s: w(s) * c(s)
    E = sum(e)                                # weight one: the densities sum to the energy
    T = sum(tau)
    F = -8 * K4 * sum((N(b[1]) - N(b[0])) * (c(b[1]) - c(b[0])) for b in B4)
    Qn = -sum(sum(c(t) - c(s) for t in nbrs(s)) for s in S4)
    Pn = sum(sum(N(t) - N(s) for t in nbrs(s)) for s in S4)
    sup = sum((2 * tau[i4[s]] - e[i4[s]] * (1 / w(s) - 1)) / c(s) for s in S4) / (8 * K4)
    alt = sum(tau[i4[s]] + e[i4[s]] * (1 - 1 / N(s)) for s in S4) / (4 * K4)
    a1lt = 3 * sum(e[i4[s]] * (w(s) - 1) / (w(s) * c(s)) for s in S4) / (8 * K4)
    return dict(res=np.abs(resid(x)).max(), E=E, T=T, F=F, Q=Qn, P=Pn, sup=sup, alt=alt, a1lt=a1lt, K=K4,
                umin=u.min(), eu=sum(e[i4[s]] * u[i4[s]] for s in S4))


hv = {b: rng.uniform(-0.3, 0.6) for b in CB}
rv = {s: rng.uniform(0.0, 0.8) for s in S4}
r = solve_case(hv, rv, 0.5)
Kq = r['K']
ok = r['res'] < 1e-11
ok &= abs(8 * Kq * r['Q'] - (r['E'] + r['F'])) < 1e-9
ok &= abs((r['P'] - r['Q']) - (r['T'] - r['F']) / (4 * Kq)) < 1e-9
ok &= abs((r['P'] + r['Q']) - (r['E'] + r['T']) / (4 * Kq)) < 1e-9
ok &= abs((r['P'] - r['Q']) - r['sup']) < 1e-9 and abs((r['P'] - r['Q']) - r['alt']) < 1e-9
rl = solve_case(hv, {s: 0.0 for s in S4}, 0.5)                 # light-like: no rest term
okl = rl['res'] < 1e-11 and abs(rl['E'] - rl['T']) < 1e-12
okl &= abs((rl['P'] - 3 * rl['Q']) + rl['F'] / (2 * Kq)) < 1e-9 and abs((rl['P'] - 3 * rl['Q']) - rl['a1lt']) < 1e-9
check('A4', ok and okl, "(a)-(d) NUMERIC (3^3 box, 54 unknowns solved to 1e-11 at STRONG field, random bond and "
      "rest energies): the identities of A2 hold, P - Q equals the supervisor's (1/8K) sum [2 tau - e(1/w - 1)]/chi and "
      "the exact form (1/4K) sum [tau + e(1 - 1/N)] (F = sum e(1/N - 1) on solutions); with no rest term (e = tau "
      "everywhere) P - 3Q = -F/(2K) exactly, which equals attempt a1's (3/8K) sum e(w - 1)/(w chi)",
      f"min u = {r['umin']:.3f}; P - Q = {r['P'] - r['Q']:.12f}, (T - F)/4K = {(r['T'] - r['F']) / (4 * Kq):.12f}; "
      f"light-like P - 3Q = {rl['P'] - 3 * rl['Q']:.12f}, -F/2K = {-rl['F'] / (2 * Kq):.12f}")

# ---------------------------------------------------------------- B1 weak field
eps_rows = []
for eps in (1e-2, 1e-3):
    rw = solve_case({b: eps ** 2 * hv[b] for b in CB}, {s: eps * rv[s] for s in S4}, 0.5)   # a bound body: tau/e of order eps
    lhs = rw['P'] - rw['Q']
    rhs = (2 * rw['T'] + rw['eu']) / (8 * Kq)
    eps_rows.append((eps, lhs, rhs, abs(lhs - rhs) / abs(rhs)))
ok = eps_rows[1][3] < eps_rows[0][3] / 5 and eps_rows[1][3] < 5e-3
check('B1', ok, "(b) at weak field P - Q = (1/8K)(2T + sum e u) + higher order (from the exact (1/4K) sum [tau + "
      "e(1 - 1/N)] with N - 1 = u/2 + O(tau)): P = Q at leading order iff 2 T = -sum e u, i.e. iff T = F with "
      "F = -(1/2) sum e u - the virial balance 2 E_kin + W = 0 once T = 2 E_kin (B2); checked NUMERIC at content "
      "strength 1e-2 and 1e-3 with hop energies of order strength^2, as for a bound body (the relative mismatch falls with the strength)",
      "; ".join(f"eps={a}: P-Q={b:.3e} vs {c:.3e} (rel {d:.1e})" for a, b, c, d in eps_rows))

# ---------------------------------------------------------------- B2 the heavy walker's hop share (exact)
s1, s2, s3, mm = sp.symbols('s1 s2 s3 m', positive=True)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
sig = s1 * sx + s2 * sy + s3 * sz
Hk = sp.BlockMatrix([[sig, mm * sp.eye(2)], [mm * sp.eye(2), -sig]]).as_explicit()      # k and k + pi(111), staggered mass
hopk = sp.BlockMatrix([[sig, sp.zeros(2)], [sp.zeros(2), -sig]]).as_explicit()
Ek = sp.sqrt(mm ** 2 + s1 ** 2 + s2 ** 2 + s3 ** 2)
Pplus = (sp.eye(4) + Hk / Ek) / 2
ok = sp.simplify(Hk * Hk - Ek ** 2 * sp.eye(4)) == sp.zeros(4)
ok &= sp.simplify((Pplus * hopk).trace() / 2 - (s1 ** 2 + s2 ** 2 + s3 ** 2) / Ek) == 0
check('B2', ok, "(b) EXACT: with block 77's staggered rest term the walk pairs k with k + pi(111) and "
      "(H + m eps)^2 = s^2 + m^2; on the positive branch the hop energy per state is s^2/sqrt(m^2 + s^2): for a heavy "
      "body T = <S^2>/m + O(1/m^3) = 2 E_kin, E_kin = <S^2>/(2m), so at leading order T - F = 2 E_kin + W with "
      "W = (1/2) sum e u")

# ---------------------------------------------------------------- B3 block 66 with xi = x on a box
Lx, Ly, Lz = 3, 2, 2
dim = Lx * Ly * Lz
site = lambda x, y, z: x + Lx * (y + Ly * z)


def shift(a):
    Tm = sp.zeros(dim, dim)
    for x in range(Lx):
        for y in range(Ly):
            for z in range(Lz):
                p = [x, y, z]
                q = list(p)
                q[a] += 1
                if q[a] < (Lx, Ly, Lz)[a]:
                    Tm[site(*p), site(*q)] = 1          # (T psi)(p) = psi(p + e_a), truncated
    return Tm


Ts = [shift(a) for a in range(3)]
Sa = [(T - T.T) / (2 * sp.I) for T in Ts]
Ca = [(T + T.T) / 2 for T in Ts]
Xs = [sp.diag(*[(i % Lx, (i // Lx) % Ly, i // (Lx * Ly))[a] for i in range(dim)]) for a in range(3)]
Hs = sum((sp.kronecker_product(Sa[a], M) for a, M in enumerate((sx, sy, sz))), sp.zeros(2 * dim, 2 * dim))
Gx = sum((sp.kronecker_product((Xs[a] * Sa[a] + Sa[a] * Xs[a]) / 2, sp.eye(2)) for a in range(3)), sp.zeros(2 * dim, 2 * dim))
H2 = sum((sp.kronecker_product((Ts[a] ** 2 - (Ts[a].T) ** 2) / (4 * sp.I), M) for a, M in enumerate((sx, sy, sz))), sp.zeros(2 * dim, 2 * dim))
ok = sp.simplify(sp.I * (Hs * Gx - Gx * Hs) - H2) == sp.zeros(2 * dim, 2 * dim)
check('B3', ok, "(b) EXACT (3x2x2 box, truncated shifts): i[H, G_x] = sum_a sigma_a (T_a^2 - T_a^dag^2)/(4i) with "
      "no wall operator (attempt a1's B2 re-checked independently): block 66's virial with xi = x balances the "
      "TWO-STEP hop against the force moment, so on the lattice it does not give 2T = -sum e u exactly")

# ---------------------------------------------------------------- B4 NUMERIC: self-bound bodies on the lattice
rows = []
t0 = time.time()
for beta, Wc, R0 in ((16, 12, 4.8), (12, 17, 6.5), (10, 21, 7.7), (8, 26, 9.7)):
    rr = snlat.solve_infinite(beta, Wc, R0)
    rows.append(('extended', beta, rr['R'], rr['v'], rr['resid']))
for beta, Wc, R0 in ((12, 8, 0.4), (16, 8, 0.4), (30, 8, 0.3), (60, 6, 0.3), (400, 6, 0.3)):
    rr = snlat.solve_infinite(beta, Wc, R0)
    rows.append(('compact', beta, rr['R'], rr['v'], rr['resid']))
ext = [r_ for r_ in rows if r_[0] == 'extended']
cmp_ = [r_ for r_ in rows if r_[0] == 'compact']
vR2 = [r_[3] * r_[2] ** 2 for r_ in ext]
ok = all(r_[4] < 1e-9 for r_ in rows)
ok &= all(r_[2] > 5 for r_ in ext) and all(r_[2] < 1 for r_ in cmp_)
ok &= max(vR2) - min(vR2) < 0.2 and 5.0 < np.mean(vR2) < 5.5 and all(r_[3] > 0 for r_ in ext)
ok &= cmp_[0][3] > 0.5 and cmp_[2][3] < -0.2 and cmp_[4][3] < -0.9
check('B4', ok, "(b) EXECUTED, NOT CLAIMED (NUMERIC; infinite lattice, no walls): the heavy walker bound by its own "
      "weak field (the leading-order reduction of ATTEMPT step 7: lattice Schrodinger-Newton on one parity class, "
      "shape set by beta = m^3/(2K) alone) has virial defect v = (2 E_kin + W)/|W|, so (P - Q)/Q = v x O(u): on the "
      "EXTENDED branch v R^2 is constant (v about 5.2 (a/R)^2) - P = Q at leading order only as R/a grows; on the "
      "COMPACT branch (a body held on about one site by its own well, beta above about 12) v runs from +0.7 through "
      "0 to -1 - P = Q fails at leading order, and for heavy compact bodies P -> Q w as for a pinned body",
      "; ".join(f"{k} beta={b}: R={R:.2f} v={v:+.4f}" for k, b, R, v, _ in rows) + f"; v R^2 (extended) = {[round(x, 3) for x in vR2]} ({time.time() - t0:.0f}s)")

# ---------------------------------------------------------------- B5 NUMERIC: what held walls add
box = []
for L in (49, 73, 97):
    rb = snlat.solve_box(16, L, 4.8)
    box.append((L, rb['v']))
vinf = ext[0][3]
ok = box[0][1] > box[1][1] > box[2][1] > vinf and all(b_[1] - vinf > 0 for b_ in box)
slope = [(b_[1] - vinf) * b_[0] for b_ in box]
ok &= max(slope) / min(slope) < 1.6
check('B5', ok, "(b) EXECUTED, NOT CLAIMED (NUMERIC): with the walls held at a finite box (Dirichlet G, beta = 16) the "
      "defect is the infinite lattice's plus a wall term falling roughly as 1/L (the walls' images make the "
      "field's energy non-homogeneous); the walls add no operator to the content's virial (B3) but add this to "
      "the field side",
      f"v(L) = {[(L_, round(v_, 4)) for L_, v_ in box]}, infinite lattice {vinf:.4f}; (v - v_inf) L = {[round(x, 2) for x in slope]}")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: for block 60's curvature member with held walls and ANY content (bond and rest "
      "energies) in stationary fields, at every strength, 8K Q = E + F, P - Q = (T - F)/(4K), P + Q = (E + T)/(4K) "
      "(T the hop energy, F the field energy), F = sum e(1/N - 1) on solutions; so the two far fields agree iff "
      "T = F, which at weak field is 2T = -sum e u, and light-like content has P - 3Q = -F/(2K) exactly; the lattice "
      "breaks the virial that would make T = F for a self-bound body: executed at leading order, the defect is "
      "about 5.2 (a/R)^2 for extended bodies and of order one for bodies held on about one site")
if all(RESULTS):
    print("HIT: for block 60's curvature member with walls held, every content with bond and rest energies in "
          "stationary fields has, at every strength, 8K Q = E + F and P - Q = (T - F)/(4K) (T the content's hop "
          "energy, F the field energy; P + Q = (E + T)/(4K)): the far fields of lengths and rates agree iff the hop "
          "energy equals the field energy; for a self-bound heavy walker this is a virial balance that the lattice "
          "breaks - executed at leading order, P = Q fails for bodies held on about one site (defect of order one, "
          "P -> Q w as for a pinned body) and holds for extended bodies only up to about 5.2 (a/R)^2")
