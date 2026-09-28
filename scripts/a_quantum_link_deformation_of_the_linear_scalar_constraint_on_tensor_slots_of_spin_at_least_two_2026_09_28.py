#!/usr/bin/env python3
"""A quantum-link deformation of the linear scalar constraint on tensor slots of spin >= 2.

Question (the owner, 2026-09-28): build the quantum-link version of Einstein's
time (scalar) constraint on the landed tensor complex, as probe 13 pointed to
(finite slots need a non-additive time gauge).

Construction (supplied, not adopted): every tensor slot is a spin S (2S+1
levels) with E = S^z (unit-spaced). For each site y, the landed scalar pattern
s_y = S^T delta_y (entries of magnitude 1 and 4) defines
    T_y = prod_slots (S^{sign s})^{|s|},     Y_y = i (T_y - T_y^dag).
Y_y is Hermitian and exp(i beta Y_y) is a continuous finite-dimensional
unitary. It is a deformation of the LINEAR scalar constraint (linearised R),
not an ADM Hamiltonian constraint: no DeWitt term is inside Y, and no lapse or
{H[N], H[M]} algebra is built.

Checks:
  A  construction: T_y is nonzero iff S >= 2 (the entries 4); G s_y = 0, so
     [G_row, T_y] = (G_row . s_y) T_y = 0 exactly (operator identity checked,
     with a control); exp(i beta Y) moves S^z non-additively.
  B  the DeWitt kinetic term DW(S^z) is exactly weakly invariant:
     DW(m + s_y) - DW(m) = 2 (G m).w_y (M s_y = G^T w_y, s_y.M.s_y = 0), so
     [DW, T_y] = T_y Delta_y(S^z) with Delta_y(m) = 2 (G m).w_y, zero on the
     momentum sector. The six uniform components are conserved by every T_y
     (and by every finitely supported move, probe 10 T2); in each sector of
     fixed uniform labels DW = DW(uniform part) + a positive semidefinite form.
     The momentum rule alone does not fix the labels; fixing them is a
     superselection choice for these local operators.
  C  linearisation (principal classical / large-S symbol, not an exact
     finite-S identity): at phi = 0, m = 0 the symbol of Y_y has phi-gradient
     -2 S^{n} s_y, n = sum|s| = 36, so Y_y / (-2 S^n) ~ s_y.phi, the landed
     linear scalar constraint S q with the canonical slot vector
     q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz) proportional to phi.
  D  classical closure: (D1) on the regular branch (every spin interior) the
     bracket {Y_a, Y_b} carries factors sin(s.phi) and vanishes there; this is
     closure with structure functions singular at the poles. (D2) the full
     constraint surface also has pole strata: a spin shared by two patterns
     with coefficients -1, +1 at its pole makes both Y vanish by amplitude;
     with G m = 0 and every other Y_c = 0, {Y_0, Y_1} != 0. So the algebra is
     not first class on the whole surface (a witness, Lie-Poisson bracket on
     the spheres; the implementation is cross-checked against the canonical
     (phi, m) bracket at a regular point).
  E  probe 10's premises hold for these operators: every s_y is finitely
     supported in ker G with vanishing zeroth and first moments (|s_hat(q)| =
     O(q^2)), so a fixed-range, uniformly bounded Hamiltonian built from T_y,
     moves and diagonal terms obeys m1 <= C q^4 in the electric channel, and
     omega_min <= q^2 sqrt(2 C_H / chi(q)). Softness needs chi bounded below,
     a property of a state that this note does not establish.
Reference only: Chandrasekharan and Wiese (hep-lat/9609042); Thiemann
(gr-qc/9606089); Bonzom and Freidel (arXiv:1101.3524); Holstein-Primakoff.
Not pre-registered.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)


def spin(S):
    d = int(round(2 * S + 1)); ms = S - np.arange(d)
    Sp = np.zeros((d, d))
    for a in range(1, d):
        Sp[a - 1, a] = np.sqrt(S * (S + 1) - ms[a] * (ms[a] + 1))
    return Sp, Sp.T.copy(), np.diag(ms)


# ---------------------------------------------------------------- landed complex on the 3^3 torus
L = 3
cells = list(itertools.product(range(L), repeat=3)); cidx = {c: i for i, c in enumerate(cells)}
nslot = 6 * len(cells)
def sl(c, a):
    return 6 * cidx[tuple(np.array(c) % L)] + a
FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}; E3 = np.eye(3, dtype=int)
Gm = np.zeros((3 * len(cells), nslot), dtype=int); Sm = np.zeros((len(cells), nslot), dtype=int)
for c in cells:
    x = np.array(c)
    for j in range(3):
        r = 3 * cidx[c] + j
        Gm[r, sl(x + E3[j], j)] += 1; Gm[r, sl(x, j)] -= 1
        for i in range(3):
            if i != j:
                f = FACE[tuple(sorted((i, j)))]; Gm[r, sl(x, f)] += 1; Gm[r, sl(x - E3[i], f)] -= 1
    r = cidx[c]
    for j in range(3):
        for i in range(3):
            if i != j:
                Sm[r, sl(x + E3[i], j)] += 1; Sm[r, sl(x - E3[i], j)] += 1; Sm[r, sl(x, j)] -= 2
    for (i, j), f in FACE.items():
        Sm[r, sl(x, f)] -= 1; Sm[r, sl(x - E3[i], f)] += 1; Sm[r, sl(x - E3[j], f)] += 1; Sm[r, sl(x - E3[i] - E3[j], f)] -= 1
pats = [Sm[y].copy() for y in range(len(cells))]                         # s_y as E-shift patterns
Mcell = np.diag([1, 1, 1, 2, 2, 2.]) - np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]) / 2
Mfull = np.kron(np.eye(len(cells)), Mcell)
DW = lambda m: float(m @ Mfull @ m)

# ---------------------------------------------------------------- A: construction
nz = {S: float(np.linalg.norm(np.linalg.matrix_power(spin(S)[1], 4))) for S in (0.5, 1, 1.5, 2, 2.5)}
okA1 = all((nz[S] > 0) == (S >= 2) for S in nz)
mags = sorted(set(abs(int(v)) for v in pats[0] if v))
okA2 = all(np.all(Gm @ s == 0) for s in pats)
# operator identity on a toy of 3 spin-2 slots: [sum g S^z, T_s] = (g.s) T_s
Sp, Sm_, Sz = spin(2); I5 = np.eye(5)
def op3(ops):
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out
def T_of(s):
    return op3([np.linalg.matrix_power(Sp if v > 0 else Sm_, abs(v)) if v else I5 for v in s])
s_toy = np.array([1, -1, 0]); g0 = np.array([1, 1, 5]); g1 = np.array([1, 0, 0])          # g0.s = 0, g1.s = 1
Z3 = [op3([Sz if k == j else I5 for k in range(3)]) for j in range(3)]
Tt = T_of(s_toy)
c0 = sum(g0[j] * Z3[j] for j in range(3)); c1 = sum(g1[j] * Z3[j] for j in range(3))
okA3 = np.abs(c0 @ Tt - Tt @ c0).max() < 1e-12 and np.abs((c1 @ Tt - Tt @ c1) - (g1 @ s_toy) * Tt).max() < 1e-12 and np.abs(Tt).max() > 0
# the ordering [f(S^z), T] = T (f(S^z + s) - f(S^z)) on the toy, with f a random quadratic form
Qf = rng.normal(size=(3, 3)); Qf = Qf + Qf.T
fz = sum(Qf[i, j] * Z3[i] @ Z3[j] for i in range(3) for j in range(3))
fz_shift = sum(Qf[i, j] * (Z3[i] + s_toy[i] * np.eye(125)) @ (Z3[j] + s_toy[j] * np.eye(125)) for i in range(3) for j in range(3))
okA4 = np.abs((fz @ Tt - Tt @ fz) - Tt @ (fz_shift - fz)).max() < 1e-9
# non-additive action on one spin-2 slot: Y = i(S+^4 - S-^4); exp(i beta Y) S^z exp(-i beta Y) - S^z is not a multiple of 1
T4 = np.linalg.matrix_power(Sp, 4); Y1 = 1j * (T4 - T4.T); U = expm(1j * 0.3 * Y1); dz = U @ Sz @ U.conj().T - Sz
nonadd = np.abs(dz - np.trace(dz) / 5 * np.eye(5)).max() > 1e-6
check("A: construction: T_y needs spin S >= 2 (the pattern's entries have magnitude 1 and 4); G s_y = 0 so every T_y commutes exactly with the momentum rule (operator identity, with a non-commuting control); [f(S^z), T] = T (f(S^z + s) - f(S^z)); exp(i beta Y) is a continuous finite-dimensional unitary moving S^z non-additively",
      okA1 and mags == [1, 4] and okA2 and okA3 and okA4 and nonadd,
      f"||(S^-)^4|| at S = 1/2, 1, 3/2, 2, 5/2: {[round(v, 3) for v in nz.values()]}; pattern magnitudes {mags}; G s_y = 0 for all {len(pats)} sites: {okA2}; [sum g S^z, T_s] = (g.s) T_s on 3 spin-2 slots: {okA3}; ordering identity: {okA4}; non-additive action: {nonadd}")

# ---------------------------------------------------------------- B: DeWitt kinetic term exactly weakly invariant; sector decomposition
okB = True; wmax = 0
for y, s in enumerate(pats):
    rhs = Mfull @ s
    w, *_ = np.linalg.lstsq(Gm.T.astype(float), rhs, rcond=None)
    okB &= np.abs(Gm.T @ w - rhs).max() < 1e-9 and abs(s @ Mfull @ s) < 1e-9
    for _ in range(20):
        m = rng.integers(-3, 4, size=nslot).astype(float)
        okB &= abs(DW(m + s) - DW(m) - 2 * (Gm @ m) @ w) < 1e-8
uniform_cons = all(np.all(np.array([s[a::6].sum() for a in range(6)]) == 0) for s in pats)
K = null_space(Gm.astype(float))                                          # ker G on the torus
Uc = np.array([[1.0 if (i % 6) == a else 0.0 for i in range(nslot)] for a in range(6)])
Kz = K @ null_space(Uc @ K)                                                # ker G with all uniform components zero
evs = np.linalg.eigvalsh(Kz.T @ Mfull @ Kz)
ev0 = np.linalg.eigvalsh(Uc @ Mfull @ Uc.T / len(cells))
# DW(u + r) = DW(u) + DW(r) for u uniform and r with zero uniform components (no cross term)
cross = max(abs((Uc.T @ rng.normal(size=6)) @ Mfull @ (Kz @ rng.normal(size=Kz.shape[1]))) for _ in range(20))
check("B: the DeWitt kinetic term is exactly weakly invariant: DW(m + s_y) - DW(m) = 2 (G m).w_y with M s_y = G^T w_y and s_y.M.s_y = 0, so [DW, T_y] = T_y Delta_y(S^z) vanishes on the momentum sector; the six uniform components are conserved by every T_y, and in each sector of fixed uniform labels DW is a constant plus a positive semidefinite form on ker G (the momentum rule alone does not fix the labels, and on all of ker G DW is indefinite)",
      okB and uniform_cons and evs.min() > -1e-9 and ev0.min() < 0 and cross < 1e-9,
      f"identity on {len(pats)} patterns x 20 random integer configurations: {okB}; uniform components conserved: {uniform_cons}; DW on ker G (dim {K.shape[1]}) with uniform parts removed (dim {Kz.shape[1]}): smallest eigenvalue {evs.min():.2e}, zeros {int(np.sum(abs(evs) < 1e-9))}; uniform block eigenvalues {np.round(ev0, 3)} (negative dilation); uniform-nonuniform cross term <= {cross:.1e}")

# ---------------------------------------------------------------- C: linearisation (principal classical symbol)
def Ysym(s, phi, m, S):
    A = np.prod([(S * S - m[k] ** 2) ** (abs(s[k]) / 2) for k in range(len(s)) if s[k]])
    return -2 * A * np.sin(s @ phi)


def grad(f, x, h=1e-6):
    g = np.zeros_like(x)
    for k in range(len(x)):
        e = np.zeros_like(x); e[k] = h; g[k] = (f(x + e) - f(x - e)) / (2 * h)
    return g


S_big = 3.0; s0 = pats[0].astype(float); nsup = int(np.sum(np.abs(s0)))
idx = np.nonzero(s0)[0]; sv = s0[idx]
gphi = grad(lambda ph: Ysym(sv, ph, np.zeros(len(sv)), S_big), np.zeros(len(sv)))
gm = grad(lambda mm: Ysym(sv, np.zeros(len(sv)), mm, S_big), np.zeros(len(sv)))
ratio = gphi / (-2 * S_big ** nsup * sv)
check("C: linearisation (principal classical symbol at large S, not an exact finite-S identity): at phi = 0, m = 0 the symbol of Y_y has phi-gradient -2 S^n s_y, so Y_y / (-2 S^n) ~ s_y.phi, the landed linear scalar constraint S q with q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz) proportional to phi; zero m-gradient, so there it generates an additive shift of m along s_y",
      np.allclose(ratio, 1, rtol=1e-6) and np.abs(gm).max() < 1e-6 * S_big ** nsup,
      f"pattern support {len(sv)} slots, n = sum|s| = {nsup}; phi-gradient / (-2 S^n s_y) = {np.round(ratio.min(), 8)}..{np.round(ratio.max(), 8)}; |m-gradient| max {np.abs(gm).max():.1e}")

# ---------------------------------------------------------------- D: classical closure — regular branch and pole strata
def pb(F, Gf, phi, m):
    x = np.concatenate([phi, m]); n = len(phi)
    gF = grad(lambda z: F(z[:n], z[n:]), x); gG = grad(lambda z: Gf(z[:n], z[n:]), x)
    return gF[:n] @ gG[n:] - gF[n:] @ gG[:n]


# D1: two overlapping patterns on the union of their supports, regular branch
a, b = 0, 1
sa, sb = pats[a].astype(float), pats[b].astype(float)
un = np.nonzero((sa != 0) | (sb != 0))[0]; A_, B_ = sa[un], sb[un]
Ya = lambda ph, mm: Ysym(A_, ph, mm, S_big); Yb = lambda ph, mm: Ysym(B_, ph, mm, S_big)
nrm = S_big ** (np.abs(A_).sum() + np.abs(B_).sum() - 1)
on_s, off_s = [], []
for _ in range(20):
    P = null_space(np.vstack([A_, B_])); ph = P @ rng.normal(size=P.shape[1]) * 0.3; mm = rng.uniform(-1.5, 1.5, size=len(un))
    on_s.append(abs(pb(Ya, Yb, ph, mm)) / nrm)
    ph2 = rng.normal(size=len(un)) * 0.3
    off_s.append(abs(pb(Ya, Yb, ph2, mm)) / nrm)
Gsub = Gm[:, un].astype(float)
Gfun = lambda ph, mm: float(Gsub[np.argmax(np.abs(Gsub).sum(1))] @ mm)
gy = max(abs(pb(Gfun, Ya, rng.normal(size=len(un)) * 0.3, rng.uniform(-1.5, 1.5, size=len(un)))) for _ in range(10))


# D2: Lie-Poisson bracket on the spheres (no coordinate singularity at the poles)
def lp_setup(Sx, Sy, Sz_):
    def Y_and_grad(s):
        idx_ = np.nonzero(s)[0]; sig = np.sign(s[idx_]); nn = np.abs(s[idx_]).astype(int)
        u = Sx[idx_] + 1j * sig * Sy[idx_]
        T = np.prod(u ** nn)
        gx = np.zeros(len(Sx), complex); gyv = np.zeros(len(Sx), complex)
        for q_, k in enumerate(idx_):
            oth = np.prod([u[r_] ** nn[r_] for r_ in range(len(idx_)) if r_ != q_])
            d = nn[q_] * u[q_] ** (nn[q_] - 1) * oth
            gx[k] = d; gyv[k] = 1j * sig[q_] * d
        return -2 * T.imag, np.stack([-2 * gx.imag, -2 * gyv.imag, np.zeros(len(Sx))], 1)
    Svec = np.stack([Sx, Sy, Sz_], 1)
    lpb = lambda g1_, g2_: float(np.sum(Svec * np.cross(g1_, g2_)))
    return Y_and_grad, lpb


# cross-check of the Lie-Poisson implementation against the canonical (phi, m) bracket at a regular point
phr = rng.normal(size=nslot) * 0.3; mr = rng.uniform(-1.5, 1.5, size=nslot); rho = np.sqrt(S_big ** 2 - mr ** 2)
Yg, lpb = lp_setup(rho * np.cos(phr), rho * np.sin(phr), mr)
lp_val = lpb(Yg(pats[a].astype(float))[1], Yg(pats[b].astype(float))[1])
can_val = pb(Ya, Yb, phr[un], mr[un])
okcross = abs(lp_val - can_val) / nrm < 1e-5 * max(1, abs(can_val) / nrm)
# the witness: slot k0 shared by patterns 0 and 1 with coefficients -1, +1, at its pole
k0 = [k for k in range(nslot) if pats[a][k] * pats[b][k] == -1][0]
cst = np.zeros(nslot); cst[k0] = -1
bounds = [(-1, 1)] * nslot; bounds[k0] = (None, None)
lp = linprog(cst, A_eq=Gm.astype(float), b_eq=np.zeros(Gm.shape[0]), bounds=bounds, method="highs")
mw = lp.x / lp.x[k0] * S_big                                              # m in ker G, m_k0 = S, every other |m| <= S / lp.x[k0]
touch = [y for y in range(len(pats)) if pats[y][k0] != 0]
restp = [y for y in range(len(pats)) if y not in touch]
Pw = null_space(np.array([pats[y] for y in restp], float)); phw = Pw @ rng.normal(size=Pw.shape[1])
rw = np.sqrt(np.maximum(S_big ** 2 - mw ** 2, 0))
Ygw, lpbw = lp_setup(rw * np.cos(phw), rw * np.sin(phw), mw)
allY = max(abs(Ygw(s.astype(float))[0]) for s in pats) / S_big ** 36
brw = lpbw(Ygw(pats[a].astype(float))[1], Ygw(pats[b].astype(float))[1]) / nrm
interior = np.delete(np.abs(mw), k0).max() / S_big
check("D: classical closure: on the regular branch (all spins interior) {Y_a, Y_b} vanishes where sin(s_a.phi) = sin(s_b.phi) = 0 (structure functions singular at the poles); on the full constraint surface it does not close: at a pole of a slot shared with coefficients -1, +1, with G m = 0 and every Y_c = 0, {Y_0, Y_1} != 0, so the algebra is not first class there; {G, Y} = 0",
      max(on_s) < 1e-5 and min(off_s) > 1e-4 and gy / S_big ** np.abs(A_).sum() < 1e-5 and okcross and lp.status == 0 and np.abs(Gm @ mw).max() < 1e-9 and interior < 1 and allY < 1e-12 and abs(brw) > 1e-2,
      f"D1 patterns {a}, {b} ({len(un)} slots): normalised bracket on the regular surface <= {max(on_s):.1e}, off it >= {min(off_s):.1e}; {{G, Y}} normalised <= {gy / S_big ** np.abs(A_).sum():.1e}; Lie-Poisson vs canonical at a regular point agree: {okcross}. D2 witness: slot {k0} at its pole, other |m|/S <= {interior:.2f}, |G m| = {np.abs(Gm @ mw).max():.1e}, max |Y_c|/S^36 over all {len(pats)} sites = {allY:.1e}, {{Y_{a}, Y_{b}}}/S^71 = {brw:.3f}")

# ---------------------------------------------------------------- E: probe 10's premises hold for these operators
# unwrapped stencil of s_y at the origin with slot positions: diagonal at the vertex, face (i, j) at x + (e_i + e_j)/2
st = []
for j in range(3):
    for i in range(3):
        if i != j:
            st += [(j, E3[i].astype(float), 1), (j, -E3[i].astype(float), 1), (j, np.zeros(3), -2)]
for (i, j), f in FACE.items():
    h = (E3[i] + E3[j]) / 2
    st += [(f, h, -1), (f, h - E3[i], 1), (f, h - E3[j], 1), (f, h - E3[i] - E3[j], -1)]
mom0 = np.array([sum(v for (t, r, v) in st if t == a_) for a_ in range(6)])
mom1 = np.array([sum(v * r for (t, r, v) in st if t == a_) for a_ in range(6)])
mom2 = max(abs(sum(v * r[0] * r[1] for (t, r, v) in st if t == 3)), abs(sum(v * r[0] ** 2 for (t, r, v) in st if t == 1)))
def shat(q):
    out = np.zeros(6, complex)
    for (t, r, v) in st:
        out[t] += v * np.exp(1j * q @ r)
    return out
dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
rat = [np.linalg.norm(shat(eps * d)) / eps ** 2 for d in dirs for eps in (1e-2, 1e-3)]
# the torus pattern equals the wrapped stencil (so the unwrapped moments are those of s_y)
wrap = np.zeros(nslot)
for (t, r, v) in st:
    cell = np.floor(r).astype(int); wrap[sl(cell, t)] += v
check("E: probe 10's premises hold for these operators: every s_y is a finitely supported pattern in ker G with vanishing zeroth and first moments (|s_hat(q)| = O(q^2)), so Hamiltonians built from T_y, moves and diagonal terms (fixed range, uniformly bounded, term-by-term sector-preserving) obey m1 <= C q^4 in the electric channel and omega_min <= q^2 sqrt(2 C_H / chi(q)); softness needs chi bounded below, a state property not established here",
      np.all(mom0 == 0) and np.abs(mom1).max() < 1e-12 and mom2 > 0 and min(rat) > 1e-3 and max(rat) < 1e3 and np.array_equal(wrap, pats[0].astype(float)),
      f"zeroth moments per slot type {mom0.tolist()}; max |first moment| {np.abs(mom1).max():.1e}; a second moment {mom2:.1f}; |s_hat(q)|/q^2 over 40 directions at q = 1e-2, 1e-3: {min(rat):.3f}..{max(rat):.3f}; unwrapped stencil = torus pattern s_0: {np.array_equal(wrap, pats[0].astype(float))}")

print("N5 resolution 1: a quantum-link deformation of the linear scalar constraint exists on spin-S slots (S >= 2): continuous, finite-dimensional, exactly commuting with the momentum rule, non-additive (so probe 13's trace lemma does not apply).")
print("N5 resolution 2: the DeWitt kinetic term is exactly weakly invariant under it; it is a constant plus a positive semidefinite form in each sector of fixed uniform labels, and indefinite on all of ker G.")
print("N5 resolution 3: the classical algebra closes on the regular branch only; pole strata of the constraint surface are not first class (explicit witness). Quantum closure is not tested.")
print("N5 resolution 4: probe 10's sum rule applies to Hamiltonians built from these operators; softness is conditional on chi(q) bounded below.")
print("per_element: each operator identity on explicit spin matrices (spin 2, dimension 125); each pattern's integer identity on the torus; the unwrapped stencil's moments.")
print("per_site: all 27 scalar patterns of the 3^3 torus for B and the witness's constraint values; spin S = 2 for operator checks, S = 3 for classical symbols.")
print("per_mode: ker G with uniform labels removed (DW spectrum); |s_hat(q)|/q^2 on 40 directions.")
print("per_block: 3 spin-2 slots for the commutators; pattern unions and the full torus for the Poisson brackets and the pole witness.")
print("lattice_wide: checked and not executed - quantum closure of the Y algebra, the physical Hilbert space of the constraints, chi(q) of any state, any phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
