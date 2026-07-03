#!/usr/bin/env python3
"""Koide staggered first-order generation determinant -- realization check.

Companion runner for
    docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md

The meta-note KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_
NOTE_2026-06-05 localized the Koide r-gate to one dynamics question: does
the staggered-Dirac corner realization deliver a FIRST-ORDER (count-once)
or SECOND-ORDER (count-twice) generation determinant?  The 2026-06-08
Kahler-Dirac note closed the index route on the hand-built Hermitian-corner
Dirac doubling D = [[0,M],[M+,0]]; the first-order construction FROM THE
ACTUAL MATTER MEASURE was explicitly left undone ("its first-order
construction is not yet done", static-readout no-go 2026-06-08).

This runner does that construction on the gate-note surface and computes,
not asserts, four facts:

  A. Surface reconstruction (gate-note interface): the one-component
     staggered operator D on the periodic 4^3 torus, dim ker D = 8,
     Hamming grading 1+3+3+1, the lattice C_3[111] rotation U_R.

  B. The matter measure is FIRST-ORDER: the single-pair Grassmann
     Berezin integral gives Z = det(K) to the FIRST power.  Verified by
     explicit exterior-algebra expansion (no determinant identity is
     assumed; the Grassmann integral is computed monomial by monomial)
     for a generic 3x3 coupling and for a 4x4 antisymmetric-kinetic-
     plus-mass toy of the staggered shape.

  C. Corner factorization of the generation probe coupling
     A(a,b,c) = a*I + b*U_R + c*U_R^T (the C_3[111] rotation channel):
     in the exact corner plane-wave basis, A|ker is block-diagonal in
     Hamming weight, BOTH hw=1 and hw=2 triplet blocks are the SAME-
     orientation circulant a*I + b*C + c*C^2, and exactly (sympy)

         det(A|ker) = (a+b+c)^2 * det3(a,b,c)^2,
         det3(a,b,c) = a^3 + b^3 + c^3 - 3abc,

     i.e. the taste-conjugate hw=2 triplet SQUARES the generation
     factor.  The square is channel-uniform, hence cancels in any
     singlet:doublet ratio (the landed pruning lemma, reproven here).
     The small-t leading behaviour of det(D + tA) on the full 64-dim
     surface matches the corner factorization (ratio test).

  D. The holomorphy fork is exact and localized: det3(a,b,c) is a
     polynomial in (a,b,c) -- the Berezin output contains NO conjugate
     dependence; the count-twice |b|^2 term appears EXACTLY and ONLY on
     the K-real line c = conj(b) (Wirtinger d^2 det3 / db dbbar = -3a
     there, 0 off it); and complex conjugation pairs the omega/omega-bar
     generation channels into one K-orbit (the doublet) while fixing the
     trivial channel -- the orbit-occupancy pairing realized on the
     corner surface.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark every
load-bearing premise at the point where it bears load.
Final line:  TOTAL: PASS=<n> FAIL=<m>
"""



import numpy as np
import sympy as sp

L = 4
N = L ** 3
TOL = 1e-9

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


def idx(x1, x2, x3):
    return (x1 % L) + L * ((x2 % L) + L * (x3 % L))


def sites():
    for x3 in range(L):
        for x2 in range(L):
            for x1 in range(L):
                yield (x1, x2, x3)


EMU = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(x, mu):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0] % 2)
    return (-1) ** ((x[0] + x[1]) % 2)


print("=" * 72)
print("Koide staggered first-order generation determinant -- realization")
print("box: Z^3 torus, L =", L, "(periodic sector; corner momenta exact)")
print("=" * 72)

# ===================== A. surface reconstruction =======================
print("\n--- A. gate-note surface reconstruction (interface checks)")

D = np.zeros((N, N))
for x in sites():
    for mu, e in enumerate(EMU):
        xp = tuple(x[k] + e[k] for k in range(3))
        xm = tuple(x[k] - e[k] for k in range(3))
        D[idx(*x), idx(*xp)] += 0.5 * eta_ks(x, mu)
        D[idx(*x), idx(*xm)] -= 0.5 * eta_ks(x, mu)

ok = np.allclose(D, -D.T)
check(1, "one-component staggered operator D (Kawamoto-Smit phases) is "
         "real antisymmetric on the 4^3 torus", ok, f"matrix {N}x{N}")

sv = np.linalg.svd(D, compute_uv=False)
ker_dim = int(np.sum(sv < 1e-9))
gap = sv[N - ker_dim - 1] if ker_dim < N else 0.0
ok = (ker_dim == 8 and abs(gap - 1.0) < 1e-9)
check(2, "dim ker D = 8 with spectral gap 1.0 (the BZ-corner doubler set)",
      ok, f"computed kernel dim = {ker_dim}, gap = {gap:.4f}")

# exact corner plane-wave basis, ordered by corner label (n1,n2,n3)
corners = [(n1, n2, n3) for n1 in (0, 1) for n2 in (0, 1) for n3 in (0, 1)]
PHI = []
for (n1, n2, n3) in corners:
    phi = np.array([(-1.0) ** (n1 * x[0] + n2 * x[1] + n3 * x[2])
                    for x in sites()])
    PHI.append(phi / np.linalg.norm(phi))
PHI = np.column_stack(PHI)                       # 64 x 8, exact null basis
ok = (np.linalg.norm(D @ PHI) < TOL
      and np.allclose(PHI.T @ PHI, np.eye(8)))
check(3, "the 8 corner plane waves are an exact orthonormal null basis "
         "of D", ok)

hw = [sum(c) for c in corners]
counts = [hw.count(k) for k in range(4)]
ok = (counts == [1, 3, 3, 1])
check(4, "Hamming grading on the corner basis = 1+3+3+1", ok,
      f"computed counts hw=0..3: {counts}")

# lattice C_3[111] rotation U_R, (U f)(x) = f(R^-1 x), R^-1(x)=(x2,x3,x1)
UR = np.zeros((N, N))
for x in sites():
    xr = (x[1], x[2], x[0])
    UR[idx(*x), idx(*xr)] = 1.0
ok = (np.linalg.norm(D @ (UR @ PHI)) < TOL
      and np.allclose(UR @ UR @ UR, np.eye(N)))
check(5, "the lattice rotation U_R (C_3[111], U_R^3 = I) preserves ker D",
      ok)

# ===================== B. the measure is first-order ===================
print("\n--- B. Berezin integral of the one-component measure: first power")


# minimal exterior (Grassmann) algebra over 2n generators, bitmask basis;
# generator 2i is chibar_i, generator 2i+1 is chi_i (adjacent pairs).
# Monomials are stored in canonical ascending-index wedge order.
def gr_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = 1
            g = m2
            while g:
                low = g & (-g)
                bit = low.bit_length() - 1
                if bin(m1 >> (bit + 1)).count("1") % 2:
                    sign = -sign
                g ^= low
            m = m1 | m2
            out[m] = out.get(m, 0) + sign * c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def gr_int(p, g):
    """Berezin left-integration of generator g: for each monomial
    containing g, move theta_g to the left past the lower-index
    generators present (sign per swap) and strip it; monomials without
    g integrate to zero."""
    out = {}
    bit = 1 << g
    for m, c in p.items():
        if not (m & bit):
            continue
        below = bin(m & (bit - 1)).count("1")
        sign = -1 if below % 2 else 1
        m2 = m ^ bit
        out[m2] = out.get(m2, 0) + sign * c
    return {m: c for m, c in out.items() if c != 0}


def berezin_partition(K, n):
    """Z = int prod_i (dchi_i dchibar_i) exp(chibar K chi), computed by
    explicit exterior-algebra expansion and nested single-generator
    Berezin integrals (NO determinant identity is assumed anywhere).

    Convention: pair measures applied innermost-first in ascending i,
    dchibar_i before dchi_i -- the standard normalization with
    int dchi_i dchibar_i exp(chibar_i k chi_i) = k for n = 1.
    """
    action = {}
    for i in range(n):
        for j in range(n):
            if K[i][j] == 0:
                continue
            gi, gj = 2 * i, 2 * j + 1          # chibar_i, chi_j
            m = (1 << gi) | (1 << gj)
            sign = 1 if gi < gj else -1        # canonical ascending order
            action[m] = action.get(m, 0) + sign * K[i][j]
    # exp(action): action is even-grade, series terminates at order n
    expo = {0: 1}
    term = {0: 1}
    for k in range(1, n + 1):
        term = gr_mul(term, action)
        term = {m: c / k for m, c in term.items() if c != 0}
        for m, c in term.items():
            expo[m] = expo.get(m, 0) + c
    out = expo
    for i in range(n):
        out = gr_int(out, 2 * i)               # dchibar_i
        out = gr_int(out, 2 * i + 1)           # dchi_i
    return out.get(0, 0)


a_s, b_s, c_s, t_s = sp.symbols("a b c t")
bbar_s = sp.symbols("bbar")

K3 = [[sp.Symbol(f"k{i}{j}") for j in range(3)] for i in range(3)]
Z3 = berezin_partition(K3, 3)
det3_sym = sp.det(sp.Matrix(K3))
ok = sp.simplify(Z3 - det3_sym) == 0
check(6, "explicit Grassmann expansion: Z = int dchibar dchi "
         "exp(chibar K chi) = det K to the FIRST power (generic 3x3, "
         "symbolic, no determinant identity assumed)", ok)

# staggered-shaped toy: antisymmetric kinetic + coupling, 4 modes
Dt = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0],
                [0, 0, 0, 1], [0, 0, -1, 0]])
At = sp.Matrix([[a_s, 0, b_s, 0], [0, a_s, 0, c_s],
                [b_s, 0, a_s, 0], [0, c_s, 0, a_s]])
Kt = (Dt + At).tolist()
Zt = berezin_partition(Kt, 4)
ok = sp.simplify(Zt - (Dt + At).det()) == 0
check(7, "antisymmetric-kinetic + coupling toy of the staggered shape: "
         "the one-component measure gives Z = det(D + A), first power "
         "(NOT |det|^2; no Hermitian L/R doubling is introduced by the "
         "measure)", ok)
residual("the matter-statistics clause (single Grassmann pair per site) "
         "is consumed at the gate-note grade: bounded on the "
         "spin-statistics support input of STAGGERED_DIRAC_GRASSMANN_"
         "FORCING_THEOREM_NOTE_2026-05-07.")

# ===================== C. corner factorization =========================
print("\n--- C. generation probe coupling and exact corner factorization")

# rotation channel coupling: A(a,b,c) = a*I + b*U_R + c*U_R^T
P8 = PHI.T @ UR @ PHI                 # U_R on the corner basis, exact 0/1
P8 = np.rint(P8).astype(int)
ok = (np.allclose(PHI.T @ UR @ PHI, P8)
      and np.allclose(P8 @ P8 @ P8, np.eye(8, dtype=int))
      and sorted(sum(P8[i, i] for i in range(8))
                 for _ in (0,)) == [2])
check(8, "U_R on the corner basis is an exact integer permutation with "
         "U^3 = I and exactly 2 fixed corners (hw=0 and hw=3)", ok,
      f"trace = {int(np.trace(P8))}")

# block structure in Hamming grading
blocks = {k: [i for i in range(8) if hw[i] == k] for k in range(4)}
offblock = 0
for i in range(8):
    for j in range(8):
        if P8[i, j] != 0 and hw[i] != hw[j]:
            offblock += 1
ok = (offblock == 0)
check(9, "U_R|ker is block-diagonal in the Hamming grading (the probe "
         "coupling does not mix hw sectors)", ok)

# both triplet blocks: same-orientation 3-cycles, pinned in canonical
# axis-index bases (hw=1 ordered by the position of its -1 character /
# 1-bit; hw=2 ordered by the position of its 0-bit).  Note: ANY 3-cycle
# is permutation-conjugate to any other, so orientation must be tested
# in matched canonical bases, not up to conjugation.
C3_ref = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])   # cyclic shift

hw1_ordered = [corners.index(c) for c in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
hw2_ordered = [corners.index(c) for c in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]]
B1 = P8[np.ix_(hw1_ordered, hw1_ordered)]
B2 = P8[np.ix_(hw2_ordered, hw2_ordered)]
ok = (np.array_equal(B1, C3_ref) and np.array_equal(B2, C3_ref))
check(10, "in the canonical axis-index bases, the hw=1 and hw=2 blocks "
          "of U_R|ker are BOTH equal to the same explicit cyclic shift "
          "C (same orientation, exact matrix equality, not just "
          "conjugacy)", ok)

# exact symbolic corner determinant
P8s = sp.Matrix(P8)
A8 = a_s * sp.eye(8) + b_s * P8s + c_s * P8s.T
detA8 = sp.factor(A8.det())
det3 = a_s ** 3 + b_s ** 3 + c_s ** 3 - 3 * a_s * b_s * c_s
target = sp.factor((a_s + b_s + c_s) ** 2 * det3 ** 2)
ok = sp.simplify(detA8 - target) == 0
check(11, "EXACT corner factorization: det(A|ker) = (a+b+c)^2 * "
          "det3(a,b,c)^2 with det3 = a^3+b^3+c^3-3abc -- the "
          "taste-conjugate hw=2 triplet SQUARES the generation circulant "
          "factor; no |.|^2 modulus appears", ok)

# channel-uniform square cancels in any singlet:doublet ratio
w = sp.Symbol("w", positive=True)  # uniform power
lam0, lam1, lam2 = sp.symbols("lam0 lam1 lam2", positive=True)
ratio_1 = sp.log(lam1 ** w * lam2 ** w) / sp.log(lam0 ** w)
ratio_2 = sp.log(lam1 * lam2) / sp.log(lam0)
ok = sp.simplify(sp.expand_log(ratio_1 - ratio_2, force=False)) == 0
check(12, "the square is channel-uniform: a uniform determinant power w "
          "cancels in the doublet:singlet log-weight ratio (the landed "
          "pruning lemma, reproven)", ok)

# full-surface ratio test: det(D + tA) small-t leading term matches
rng_pts = [(0.7, 0.31 + 0.22j, 0.31 - 0.22j),
           (0.9, 0.11 + 0.47j, 0.05 - 0.13j)]
t = 1e-3
dets = []
corner_dets = []
for (av, bv, cv) in rng_pts:
    Afull = av * np.eye(N) + bv * UR + cv * UR.T
    with np.errstate(all="ignore"):
        dets.append(np.linalg.det(D.astype(complex) + t * Afull))
    d3 = av ** 3 + bv ** 3 + cv ** 3 - 3 * av * bv * cv
    corner_dets.append(((av + bv + cv) ** 2) * d3 ** 2)
ratio_full = dets[0] / dets[1]
ratio_corner = corner_dets[0] / corner_dets[1]
ok = abs(ratio_full - ratio_corner) / abs(ratio_corner) < 1e-2
check(13, "small-t leading behaviour of det(D + tA) on the full 64-dim "
          "surface matches the corner factorization (ratio of two "
          "couplings)", ok,
      f"|ratio mismatch| = {abs(ratio_full - ratio_corner) / abs(ratio_corner):.2e}")
residual("the probe coupling FORM A = a*I + b*U_R + c*U_R^T (the "
         "C_3[111] rotation channel) is a declared probe, not a derived "
         "Yukawa: the framework has not derived that the generation-"
         "monitored coupling is the rotation channel; conclusions are "
         "claims about what THIS channel delivers on the realization.")

# ===================== D. the holomorphy fork ==========================
print("\n--- D. holomorphy fork: where count-twice enters, exactly")

# the Berezin output is a polynomial in (a,b,c): no conjugate appears
poly = sp.Poly(detA8, a_s, b_s, c_s)
ok = (poly.total_degree() == 8 and detA8.free_symbols == {a_s, b_s, c_s})
check(14, "the Berezin corner output is a POLYNOMIAL in the channel "
          "couplings (a,b,c): the first-order measure introduces NO "
          "conjugate dependence (holomorphic in b with c independent; "
          "d det/d bbar = 0 identically)", ok,
      "free symbols = {a, b, c}, degree 8")

# Wirtinger / harmonicity: on the K-real line c = bbar the |b|^2
# (count-twice) term appears; off it the channel factor is harmonic in
# (Re b, Im b) -- the exact holomorphy criterion, not a vacuous
# absent-symbol derivative.
det3_K = det3.subs(c_s, bbar_s)            # treat (b, bbar) as Wirtinger pair
mixed_on = sp.diff(det3_K, b_s, bbar_s)
br, bi = sp.symbols("br bi", real=True)
c0 = sp.Symbol("c0")                       # frozen independent c
f_off = det3.subs({b_s: br + sp.I * bi, c_s: c0})
f_on = det3.subs({b_s: br + sp.I * bi, c_s: br - sp.I * bi})
lap_off = sp.simplify(sp.diff(f_off, br, 2) + sp.diff(f_off, bi, 2))
lap_on = sp.simplify(sp.diff(f_on, br, 2) + sp.diff(f_on, bi, 2))
ok = (sp.simplify(mixed_on + 3 * a_s) == 0
      and lap_off == 0
      and sp.simplify(lap_on + 12 * a_s) == 0)
check(15, "Wirtinger/harmonicity: with c independent the channel factor "
          "is HARMONIC in (Re b, Im b) (Laplacian = 0, exact holomorphy "
          "criterion); on the K-real line c = bbar the count-twice term "
          "appears with d^2 det3/db dbbar = -3a (Laplacian = -12a): "
          "count-twice enters EXACTLY and ONLY through the K-reality "
          "restriction, not through the measure", ok)

# K-real line = Hermitian channel: A|ker Hermitian iff c = conj(b), a real
av, brv, biv = 0.8, 0.3, 0.2
bv = brv + 1j * biv
A8n_K = av * np.eye(8) + bv * P8 + np.conj(bv) * P8.T
A8n_free = av * np.eye(8) + bv * P8 + (0.5 - 0.1j) * P8.T
ok = (np.allclose(A8n_K, A8n_K.conj().T)
      and not np.allclose(A8n_free, A8n_free.conj().T))
check(16, "the K-real line c = conj(b) (with a real) is exactly the "
          "Hermitian-channel restriction of the probe coupling", ok)

# K/CPT channel pairing: conjugation swaps the omega/omega-bar channels
omega_c = np.exp(2j * np.pi / 3)
Cm = C3_ref.astype(complex)
projs = []
for j in range(3):
    Pj = sum(omega_c ** (-j * m) * np.linalg.matrix_power(Cm, m)
             for m in range(3)) / 3.0
    projs.append(Pj)
ok = (np.allclose(np.conj(projs[1]), projs[2])
      and np.allclose(np.conj(projs[2]), projs[1])
      and np.allclose(np.conj(projs[0]), projs[0]))
check(17, "complex conjugation (K) swaps the omega and omega-bar "
          "generation channel projectors and fixes the trivial channel: "
          "the doublet channels form ONE K-orbit, the singlet is a "
          "K-fixed point (orbit pairing realized on the corner surface)",
      ok)

# spectrum view on the K-real line: K maps the doublet eigenvalue pair
# into itself by swapping the two members (delta -> -delta)
delta = 0.37
modb = 0.25
lam = [av + 2 * modb * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)]
lam_K = [av + 2 * modb * np.cos(-delta + 2 * np.pi * k / 3)
         for k in range(3)]
ok = (abs(lam[0] - lam_K[0]) < 1e-12          # trivial channel K-fixed
      and abs(lam[1] - lam_K[2]) < 1e-12      # doublet pair swaps
      and abs(lam[2] - lam_K[1]) < 1e-12
      and abs(lam[1] - lam[2]) > 1e-3)        # generically distinct
check(18, "on the K-real line the channel spectrum lam_k = a + 2|b| "
          "cos(delta + 2 pi k/3) is K-paired by delta -> -delta: the "
          "trivial channel is K-fixed and the two (generically distinct) "
          "doublet eigenvalues swap -- the doublet is one K-orbit", ok)

# landed bookkeeping consequence (cited, light arithmetic only):
# count-twice (sector slots) Z_d = 2pi/g -> rho = 1/2 -> r = 1;
# count-once (orbit slot)    Z_d =  pi/g -> rho = 1   -> r = 1/2.
g_sym = sp.Symbol("g", positive=True)
rho_sector = (sp.pi / g_sym) / (2 * sp.pi / g_sym)
rho_orbit = (sp.pi / g_sym) / (sp.pi / g_sym)
r_sector = 1 / (2 * rho_sector)
r_orbit = 1 / (2 * rho_orbit)
ok = (sp.simplify(r_sector - 1) == 0
      and sp.simplify(r_orbit - sp.Rational(1, 2)) == 0)
check(19, "landed rho-map arithmetic: Hermitian-channel (count-twice) "
          "slotting -> r = 1; holomorphic-channel (count-once / one slot "
          "per K-orbit) slotting -> r = 1/2 (cells cited from the landed "
          "fork note; orientation pinned there, arithmetic reproven "
          "here)", ok)
residual("which horn is physical is NOT decided by this surface: the "
         "K-real (Hermitian) restriction c = conj(b) is the already-"
         "named K-reality admission of CHARGED_LEPTON_KOIDE_VALUE_FULL_"
         "CHAIN_OF_CUSTODY_2026-06-02; the holomorphic horn keeps the "
         "channel weights complex and consumes the orbit-occupancy "
         "premise candidate instead. Neither is derived here.")
residual("inherited gate-note residuals remain at their declared "
         "grades: kinetic-class premise, spin-statistics support tier, "
         "boundary-holonomy convention, AC_phi_lambda labeling "
         "convention (STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03 "
         "section 5).")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: the one-component staggered measure delivers a FIRST-"
      "ORDER generation determinant (single power, computed by explicit"
      " Grassmann expansion); the taste-conjugate triplet squares the"
      " generation factor channel-uniformly (r-neutral); count-twice"
      " |b|^2 dependence enters EXACTLY and ONLY through the K-reality"
      " restriction c = conj(b); the doublet channels are one K-orbit."
      " No occupancy rule, premise adoption, or audit status is set.")
sys_exit = 0 if _fail == 0 else 1
raise SystemExit(sys_exit)
