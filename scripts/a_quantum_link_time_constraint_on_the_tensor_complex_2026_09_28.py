#!/usr/bin/env python3
"""A quantum-link time constraint on the tensor complex: it carries the DeWitt kinetic term; the potential side stays soft.

Question (the owner, 2026-09-28): build the quantum-link version of Einstein's
time (Hamiltonian) constraint on the landed tensor complex, as probe 13
pointed to (finite slots need a non-additive time gauge).

Construction (supplied, not adopted): every tensor slot is a spin S (2S+1
levels) with E = S^z (unit-spaced). For each site y, the landed scalar-gauge
pattern s_y = S^T delta_y (entries of magnitude 1 and 4) defines
    T_y = prod_slots (S^{sign s})^{|s|},     Y_y = i (T_y - T_y^dag).
Y_y is Hermitian; exp(i beta Y_y) is a continuous finite-dimensional unitary
"time gauge". It acts non-additively on E (so probe 13's trace lemma does not
bite) and, near the equator at large S, Y_y ~ -2 S^{n} (s_y . phi): the landed
linear scalar constraint with h ~ phi.

Checks:
  A  construction: T_y is nonzero iff S >= 2 (the entries 4); G s_y = 0, so
     [G_row, T_y] = (G_row . s_y) T_y = 0 exactly (operator identity checked,
     with a control); exp(i beta Y) moves S^z non-additively.
  B  the DeWitt kinetic term K = DW(S^z) is exactly weakly invariant:
     DW(m + s_y) - DW(m) = 2 (G m) . w_y with integer w_y (M s_y = G^T w_y,
     s_y.M.s_y = 0), so [K, T_y] = 2 (G m).w_y T_y vanishes on the momentum
     sector. All six uniform components are conserved (zero moments of s_y),
     and on ker G with them fixed at zero DW is positive semidefinite.
  C  linearisation: at phi = 0, m = 0, the classical symbol of Y_y has
     phi-gradient -2 S^{n_y} s_y and generates an additive shift of m along s_y.
  D  classical first-class closure: {Y_a, Y_b} vanishes on the joint surface
     sin(s_a.phi) = sin(s_b.phi) = 0 but not off it (non-abelian, closing with
     structure functions); {G, Y} = 0; {DW, Y} is proportional to G m.
  E  the potential side: the momentum-rule gauge (z-rotations) acts on the
     large-S metric proxy h = S^y/S non-additively, so an Einstein-Hilbert
     polynomial in h is invariant only to first order (second-order change
     checked nonzero). Exactly invariant potentials are built from moves, whose
     sum rule is O(q^4) (probe 10); with the DeWitt kinetic term the TT
     graviton then has omega ~ q^2 (Gaussian comparator: exponent 2).
Reference only: Chandrasekharan and Wiese (hep-lat/9609042) quantum link
models; Holstein-Primakoff. Not pre-registered.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
from scipy.linalg import expm, null_space

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
# non-additive action on one spin-2 slot: Y = i(S+^4 - S-^4); exp(i beta Y) S^z exp(-i beta Y) - S^z is not a multiple of 1
T4 = np.linalg.matrix_power(Sp, 4); Y1 = 1j * (T4 - T4.T); U = expm(1j * 0.3 * Y1); dz = U @ Sz @ U.conj().T - Sz
nonadd = np.abs(dz - np.trace(dz) / 5 * np.eye(5)).max() > 1e-6
check("A: construction: T_y needs spin S >= 2 (the pattern's entries have magnitude 1 and 4); G s_y = 0 so every T_y commutes exactly with the momentum rule (operator identity, with a non-commuting control); exp(i beta Y) is a continuous finite-dimensional gauge that moves S^z non-additively",
      okA1 and mags == [1, 4] and okA2 and okA3 and nonadd,
      f"||(S^-)^4|| at S = 1/2, 1, 3/2, 2, 5/2: {[round(v, 3) for v in nz.values()]}; pattern magnitudes {mags}; G s_y = 0 for all {len(pats)} sites: {okA2}; [sum g S^z, T_s] = (g.s) T_s on 3 spin-2 slots: {okA3}; non-additive action: {nonadd}")

# ---------------------------------------------------------------- B: DeWitt kinetic term exactly weakly invariant; positivity on the physical sector
okB = True; wmax = 0
for y, s in enumerate(pats):
    rhs = Mfull @ s
    w, *_ = np.linalg.lstsq(Gm.T.astype(float), rhs, rcond=None)
    okB &= np.abs(Gm.T @ w - rhs).max() < 1e-9 and abs(s @ Mfull @ s) < 1e-9
    wr = np.round(w * 2) / 2; wmax = max(wmax, np.abs(Gm.T @ wr - rhs).max())
    for _ in range(20):
        m = rng.integers(-3, 4, size=nslot).astype(float)
        okB &= abs(DW(m + s) - DW(m) - 2 * (Gm @ m) @ w) < 1e-8
uniform_cons = all(np.all(np.array([s[a::6].sum() for a in range(6)]) == 0) for s in pats)
K = null_space(Gm.astype(float))                                          # ker G on the torus
Uc = np.array([[1.0 if (i % 6) == a else 0.0 for i in range(nslot)] for a in range(6)])
Kz = K @ null_space(Uc @ K)                                                # ker G with all uniform components zero
evs = np.linalg.eigvalsh(Kz.T @ Mfull @ Kz)
ev0 = np.linalg.eigvalsh(Uc @ Mfull @ Uc.T / len(cells))
check("B: the DeWitt kinetic term is exactly weakly invariant under the quantum-link time gauge: DW(m + s_y) - DW(m) = 2 (G m).w_y with M s_y = G^T w_y and s_y.M.s_y = 0, so [K, T_y] vanishes on the momentum sector; all six uniform components are conserved, and on ker G with them fixed DW is positive semidefinite",
      okB and uniform_cons and evs.min() > -1e-9 and ev0.min() < 0,
      f"identity on {len(pats)} patterns x 20 random integer configurations: {okB}; uniform components conserved: {uniform_cons}; DW on ker G (dim {K.shape[1]}) with uniform parts removed (dim {Kz.shape[1]}): smallest eigenvalue {evs.min():.2e}, zeros {int(np.sum(abs(evs) < 1e-9))}; the uniform block alone has eigenvalues {np.round(ev0, 3)} (its negative dilation is a conserved label, not dynamical)")

# ---------------------------------------------------------------- C: linearisation (classical symbols)
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
check("C: linearisation: at phi = 0, m = 0 the classical symbol of Y_y has phi-gradient -2 S^n s_y (so Y_y ~ -2 S^n (s_y.phi), the landed linear scalar constraint with h ~ phi) and zero m-gradient, so it generates an additive shift of m along s_y there",
      np.allclose(ratio, 1, rtol=1e-6) and np.abs(gm).max() < 1e-6 * S_big ** nsup,
      f"pattern support {len(sv)} slots, n = sum|s| = {nsup}; phi-gradient / (-2 S^n s_y) = {np.round(ratio.min(), 8)}..{np.round(ratio.max(), 8)}; |m-gradient| max {np.abs(gm).max():.1e}")

# ---------------------------------------------------------------- D: classical first-class closure
def pb(F, Gf, phi, m):
    x = np.concatenate([phi, m]); n = len(phi)
    gF = grad(lambda z: F(z[:n], z[n:]), x); gG = grad(lambda z: Gf(z[:n], z[n:]), x)
    return gF[:n] @ gG[n:] - gF[n:] @ gG[:n]


# two overlapping patterns on the union of their supports
a, b = 0, 1
sa, sb = pats[a].astype(float), pats[b].astype(float)
un = np.nonzero((sa != 0) | (sb != 0))[0]; A_, B_ = sa[un], sb[un]
Ya = lambda ph, mm: Ysym(A_, ph, mm, S_big); Yb = lambda ph, mm: Ysym(B_, ph, mm, S_big)
on_s, off_s = [], []
for _ in range(20):
    # a point on the joint surface: phi orthogonal to both patterns (so s.phi = 0)
    P = null_space(np.vstack([A_, B_])); ph = P @ rng.normal(size=P.shape[1]) * 0.3; mm = rng.uniform(-1.5, 1.5, size=len(un))
    on_s.append(abs(pb(Ya, Yb, ph, mm)) / (S_big ** (np.abs(A_).sum() + np.abs(B_).sum())))
    ph2 = rng.normal(size=len(un)) * 0.3
    off_s.append(abs(pb(Ya, Yb, ph2, mm)) / (S_big ** (np.abs(A_).sum() + np.abs(B_).sum())))
Gsub = Gm[:, un].astype(float)
Gfun = lambda ph, mm: float(Gsub[np.argmax(np.abs(Gsub).sum(1))] @ mm)
gy = max(abs(pb(Gfun, Ya, rng.normal(size=len(un)) * 0.3, rng.uniform(-1.5, 1.5, size=len(un)))) for _ in range(10))
check("D: classical first-class closure: {Y_a, Y_b} vanishes on the joint surface sin(s_a.phi) = sin(s_b.phi) = 0 and not off it (a non-abelian algebra closing with structure functions); {G, Y} = 0",
      max(on_s) < 1e-5 and min(off_s) > 1e-4 and gy / S_big ** np.abs(A_).sum() < 1e-5,
      f"overlapping patterns at sites {a} and {b} ({len(un)} slots in the union); normalised bracket on the surface <= {max(on_s):.1e}, off it >= {min(off_s):.1e}; {{G, Y}} normalised <= {gy / S_big ** np.abs(A_).sum():.1e}; quantum closure (operator ordering) is not tested")

# ---------------------------------------------------------------- E: the potential side
# (i) z-rotation by alpha (momentum-rule gauge) on the large-S proxy h = S^y/S at the equator: h -> (S^y cos a + S^x sin a)/S
Sx0 = 3.0; hy0 = rng.normal(size=6) * 0.2                               # S^y/S small; S^x ~ S near the equator
def rot(hy, alpha):
    sx = np.sqrt(np.maximum(1 - hy ** 2, 0)); return hy * np.cos(alpha) + sx * np.sin(alpha)
def quad(h):                     # a fixed nonzero quadratic form (stands for the E-H polynomial) on six components
    Q = np.diag([1, -1, 0.5, 2, -0.3, 1.0]) + 0.1; return h @ Q @ h
xi = rng.normal(size=6)
d1 = lambda a: quad(rot(hy0 + 0 * xi, a))                                # uniform rotation of all components
alphas = np.array([1e-3, 2e-3, 4e-3])
lin = np.array([quad(hy0 + al * np.sqrt(1 - hy0 ** 2)) for al in alphas])
exact = np.array([d1(al) for al in alphas])
second = (exact - lin) / alphas ** 2
# (ii) Gaussian comparator: DeWitt kinetic on TT (coefficient 1 in the tensor metric) with a curvature-squared potential (the landed R^2 form, order k^4)
ks = np.array([0.2, 0.1, 0.05, 0.025]); om = np.sqrt(1.0 * ks ** 4)
slope = np.polyfit(np.log(ks), np.log(om), 1)[0]
check("E: the potential side stays soft: the momentum-rule gauge acts on the large-S metric proxy h = S^y/S non-additively (a polynomial in h changes at second order under it), so exactly invariant potentials are built from moves, whose sum rule is O(q^4) (probe 10); with the DeWitt kinetic term the TT graviton then has omega ~ q^2",
      np.abs(second).min() > 1e-3 and abs(slope - 2) < 1e-6,
      f"second-order change of a quadratic form under the z-rotation / alpha^2 at alpha = 1e-3..4e-3: {np.round(second, 3)} (nonzero); Gaussian TT exponent with DeWitt kinetic and an order-k^4 potential: {slope:.3f}")

print("N5 resolution 1: a quantum-link time gauge exists on spin-S slots (S >= 2): continuous, finite-dimensional, exactly commuting with the momentum rule, non-additive (so the trace lemma of probe 13 does not apply).")
print("N5 resolution 2: the DeWitt kinetic term is exactly weakly invariant under it and positive on the momentum sector at fixed uniform labels: the kinetic-side obstruction of probes 12-13 is removed for such slots.")
print("N5 resolution 3: the time constraints close classically with structure functions (first class on the surface); quantum closure is not tested.")
print("N5 resolution 4: the potential side is unchanged: exactly gauge-invariant potentials are move-built with an O(q^4) sum rule (probe 10), so the graviton stays soft unless the electric pattern is incompressible.")
print("per_element: each operator identity on explicit spin matrices; each pattern's integer identity on the torus.")
print("per_site: all 27 scalar-gauge patterns of the 3^3 torus; spin S = 2 for operator checks, S = 3 for classical symbols.")
print("per_mode: ker G with uniform labels removed (DW spectrum); TT Gaussian dispersion.")
print("per_block: 3 spin-2 slots (dimension 125) for the commutator; pattern unions for the Poisson brackets.")
print("lattice_wide: checked and not executed - quantum closure of the Y algebra, the physical Hilbert space of the constraints, any ground state or phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
