#!/usr/bin/env python3
"""Koide first-order section fork: weight-stage versus outcome-stage K-reality.

Companion runner for
    docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md

The runner verifies four bounded statements:

1. A one-component Grassmann integral gives one power of the circulant
   determinant ``det3(a,b,c)``.
2. Keeping ``b,c`` independent gives a holomorphic polynomial, whereas
   imposing ``c=conj(b)`` before analytic classification introduces
   conjugate dependence with mixed derivative ``-3a``.
3. The conditional endpoint arithmetic is ``r=1/2`` for the supplied
   per-outcome-cell law and ``r=1`` for the supplied per-real-mode law.
   The code does not derive either weighting law or its physical pairing
   with a K-reality stage.
4. Site- and link-centered spatial reflections act differently on corner
   modes.  The finite corner calculation therefore cannot replace a full
   Osterwalder--Schrader positivity test of the matter action.

The two stage prescriptions agree pointwise after restriction to the same
K-real locus, while differing in when conjugacy is imposed.  Consequently
the result is UNDECIDED WITH EXACT RESIDUAL: the source-defined fork is the
weight-stage versus outcome-stage placement of K-reality, but neither that
stage nor the associated weighting law is selected here.

PASS/FAIL lines certify only the algebra stated in each check.  RESIDUAL
lines name imported or still-open inputs.  No audit status is asserted.
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


# ---------------------------------------------------------------------------
# minimal finite exterior (Grassmann) algebra over 2n generators; generator
# 2i is chibar_i, generator 2i+1 is chi_i.  Berezin partition computed by
# explicit expansion and nested single-generator integrals -- NO determinant
# identity is assumed anywhere.  (Engine reproduced from PR #3551 block01.)
# ---------------------------------------------------------------------------
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
    """Z = int prod_i (dchi_i dchibar_i) exp(chibar K chi), by explicit
    exterior-algebra expansion (no determinant identity used)."""
    action = {}
    for i in range(n):
        for j in range(n):
            if K[i][j] == 0:
                continue
            gi, gj = 2 * i, 2 * j + 1
            m = (1 << gi) | (1 << gj)
            sign = 1 if gi < gj else -1
            action[m] = action.get(m, 0) + sign * K[i][j]
    expo = {0: 1}
    term = {0: 1}
    for k in range(1, n + 1):
        term = gr_mul(term, action)
        term = {m: c / k for m, c in term.items() if c != 0}
        for m, c in term.items():
            expo[m] = expo.get(m, 0) + c
    out = expo
    for i in range(n):
        out = gr_int(out, 2 * i)
        out = gr_int(out, 2 * i + 1)
    return out.get(0, 0)


print("=" * 72)
print("Koide first-order section fork -- weight-stage vs outcome-stage K-reality")
print("box: Z^3 torus, L =", L, "(periodic sector; corner momenta exact)")
print("=" * 72)

# ===================== surface (interface, reused) =====================
D = np.zeros((N, N))
for x in sites():
    for mu, e in enumerate(EMU):
        xp = tuple(x[k] + e[k] for k in range(3))
        xm = tuple(x[k] - e[k] for k in range(3))
        D[idx(*x), idx(*xp)] += 0.5 * eta_ks(x, mu)
        D[idx(*x), idx(*xm)] -= 0.5 * eta_ks(x, mu)

corners = [(n1, n2, n3) for n1 in (0, 1) for n2 in (0, 1) for n3 in (0, 1)]
PHI = []
for (n1, n2, n3) in corners:
    phi = np.array([(-1.0) ** (n1 * x[0] + n2 * x[1] + n3 * x[2])
                    for x in sites()])
    PHI.append(phi / np.linalg.norm(phi))
PHI = np.column_stack(PHI)
hw = [sum(c) for c in corners]

UR = np.zeros((N, N))
for x in sites():
    xr = (x[1], x[2], x[0])
    UR[idx(*x), idx(*xr)] = 1.0
P8 = np.rint(PHI.T @ UR @ PHI).astype(int)

# the hw=1 corner triplet carries the generation regular rep
hw1_idx = [corners.index(c) for c in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
C3 = P8[np.ix_(hw1_idx, hw1_idx)]            # the C_3 cycle on the hw=1 triplet

# symbols
a_s, b_s, c_s, t_s = sp.symbols("a b c t")
bbar_s = sp.Symbol("bbar")
br, bi = sp.symbols("br bi", real=True)
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2       # exact primitive cube root
det3 = a_s ** 3 + b_s ** 3 + c_s ** 3 - 3 * a_s * b_s * c_s
lam0 = a_s + b_s + c_s
lam_w = a_s + b_s * w + c_s * w ** 2
lam_wb = a_s + b_s * w ** 2 + c_s * w

# ===================== A. first-order determinant, hw=1 triplet =========
print("\n--- A. first-order generation determinant on the hw=1 corner triplet")

# sanity: the engine gives det to first power for a generic 3x3
K3 = [[sp.Symbol(f"k{i}{j}") for j in range(3)] for i in range(3)]
Z3 = berezin_partition(K3, 3)
ok = sp.simplify(Z3 - sp.Matrix(K3).det()) == 0
check(1, "Grassmann/Berezin engine: Z = int dchibar dchi exp(chibar K chi) "
         "= det K to the FIRST power (generic 3x3, explicit exterior-"
         "algebra expansion; NO determinant identity assumed)", ok)

# the hw=1 corner triplet IS the C_3 cycle; W = a*I + b*C + c*C^2
ok = (C3.shape == (3, 3)
      and np.array_equal(np.linalg.matrix_power(C3, 3), np.eye(3, dtype=int))
      and not np.array_equal(C3, C3.T))
check(2, "the hw=1 corner triplet carries the generation C_3 cycle C "
         "(C^3 = I, C not symmetric): the one-component measure's coupling "
         "there is the circulant W = a*I + b*C + c*C^2", ok)

Wmat = (a_s * sp.eye(3) + b_s * sp.Matrix(C3.tolist())
        + c_s * sp.Matrix((C3 @ C3).tolist()))
ZW = berezin_partition(Wmat.tolist(), 3)
ok = (sp.simplify(ZW - Wmat.det()) == 0
      and sp.simplify(ZW - det3) == 0)
check(3, "explicit Berezin partition of W on the hw=1 triplet = det(W) to "
         "the FIRST power = det3(a,b,c) = a^3+b^3+c^3-3abc (single power; "
         "the measure does NOT produce |det|^2)", ok)

# exact singlet/doublet factorization Z = lam0 * (lam_omega * lam_omegabar)
ok = (sp.simplify(det3 - lam0 * lam_w * lam_wb) == 0
      and sp.simplify(sp.expand(lam_w * lam_wb)
                      - (a_s ** 2 + b_s ** 2 + c_s ** 2
                         - a_s * b_s - b_s * c_s - a_s * c_s)) == 0)
check(4, "exact isotype factorization: Z = lam0 * (lam_omega * "
         "lam_omegabar), singlet lam0 = a+b+c and the DOUBLET factor "
         "lam_omega * lam_omegabar (the omega/omega-bar pair) -- one "
         "Berezin power each, first-order", ok)

# ===================== B. both sections exactly ========================
print("\n--- B. untied holomorphic section vs K-real tied section")

# (i) untied: b, c independent -> the doublet weight is holomorphic
doublet = sp.expand(lam_w * lam_wb)
ddb_bar_untied = sp.diff(doublet, bbar_s)             # bbar is not present
ok = (doublet.free_symbols <= {a_s, b_s, c_s}
      and ddb_bar_untied == 0
      and sp.Poly(doublet, a_s, b_s, c_s).total_degree() == 2)
check(5, "UNTIED section (b, c independent): the doublet weight "
         "lam_omega*lam_omegabar is a HOLOMORPHIC polynomial in (a,b,c) -- "
         "no conjugate appears and d/dbbar = 0 identically. This is the "
         "candidate outcome-stage analytic prescription; no weighting law "
         "is inferred", ok)

# (ii) K-real tied section c = conj(b): the doublet weight becomes a
# function of |b|^2 -- count-twice (Wirtinger localization, PR #3551)
det3_K = det3.subs(c_s, bbar_s)
mixed_tied = sp.diff(det3_K, b_s, bbar_s)
f_on = det3.subs({b_s: br + sp.I * bi, c_s: br - sp.I * bi})
lap_on = sp.simplify(sp.diff(f_on, br, 2) + sp.diff(f_on, bi, 2))
doublet_K = sp.expand(doublet.subs(c_s, bbar_s))
ok = (sp.simplify(mixed_tied + 3 * a_s) == 0
      and sp.simplify(lap_on + 12 * a_s) == 0
      and sp.diff(doublet_K, bbar_s) != 0)
check(6, "K-REAL TIED section c = conj(b): the first-power weight becomes "
         "NON-holomorphic -- Wirtinger d^2 det3/db dbbar = -3a "
         "(Laplacian -12a), and the doublet weight contains b*bbar. This "
         "is the candidate weight-stage analytic prescription", ok)

# fork-cell landing (PR #3551 / note 6): section -> granularity -> (r, Q).
# The r-endpoints are re-derived from the two realized-state equipartition
# laws (the corrected attribution of the 2026-07-11 repairs; the WITHDRAWN
# rho-map / Z-ratio arithmetic is NOT used anywhere in this runner):
#   untied holomorphic section = one complex slot per K-orbit = per-OUTCOME-
#     CELL law  E_s = E_d  (3a^2 = 6|b|^2)   =>  r = 1/2, Q = 2/3
#   K-real tied section = doublet weight a function of |b|^2 over two real
#     parameters = per-REAL-MODE law  E_s = eps, E_d = 2 eps  =>  r = 1, Q = 1
def q_from_r(r):
    return (1 + 2 * r) / 3


a_eq, b2_eq, eps_eq = sp.symbols("a_eq b2_eq eps_eq", positive=True)
sol_cell = sp.solve([sp.Eq(3 * a_eq**2, eps_eq), sp.Eq(6 * b2_eq, eps_eq)],
                    [b2_eq, eps_eq], dict=True)[0]
r_label = sp.simplify(sol_cell[b2_eq] / a_eq**2)   # per-outcome-cell law
sol_mode = sp.solve([sp.Eq(3 * a_eq**2, eps_eq), sp.Eq(6 * b2_eq, 2 * eps_eq)],
                    [b2_eq, eps_eq], dict=True)[0]
r_tie = sp.simplify(sol_mode[b2_eq] / a_eq**2)     # per-real-mode law
ok = (r_label == sp.Rational(1, 2) and q_from_r(r_label) == sp.Rational(2, 3)
      and r_tie == 1 and q_from_r(r_tie) == 1)
check(7, "conditional endpoint arithmetic (withdrawn rho-map not used): "
         "the supplied per-outcome-cell law gives r=1/2, Q=2/3, while the "
         "supplied per-real-mode law gives r=1, Q=1. The equations do not "
         "derive either law or pair it physically with a K-reality stage", ok)
residual("the coupling on the hw=1 triplet is the C_3[111] rotation-"
         "channel circulant W = a*I + b*C + c*C^2, a DECLARED probe "
         "coupling, not a derived Yukawa. The source-side channel-space "
         "companion is currently unaudited; its broader classification is "
         "not reproven by this runner.")
residual("the per-outcome-cell and per-real-mode equipartition laws are "
         "alternative conditional inputs. Their association with outcome-"
         "stage and weight-stage K-reality is not derived by check 7.")

# ===================== C. does RP constrain the first-order measure? ====
print("\n--- C. reflection positivity: does it touch the first-order measure?")

# (C.1) the 06-08 RP wall's rejection of the bare first-order operator
Wh = a_s * sp.eye(3) + b_s * sp.Matrix(C3.tolist())     # W_h = a I + b C
ok = (sp.simplify(Wh - Wh.conjugate().T) != sp.zeros(3)     # not self-adjoint
      and sp.simplify(sp.Matrix((C3.T).tolist())
                      - sp.Matrix((C3 @ C3).tolist())) == sp.zeros(3))
check(8, "algebraic input used by the source-side RP wall: the bare first-order "
         "W_h = a*I + b*C is non-self-adjoint for generic b (C^T = C^2 "
         "!= C). This check alone is not a full reflection-positivity test", ok)

# the RP-compatible second-order object: D = [[0,M],[Mdag,0]] -> |det M|^2
Mmat = a_s * sp.eye(3) + b_s * sp.Matrix(C3.tolist()) + \
    c_s * sp.Matrix((C3 @ C3).tolist())
# evaluate at an exact complex point to read the modulus structure exactly
subs_pt = {a_s: sp.Rational(4, 5), b_s: sp.Rational(3, 10) + sp.I * sp.Rational(1, 5),
           c_s: sp.Rational(1, 2) - sp.I * sp.Rational(1, 10)}
Mn = Mmat.subs(subs_pt)
Dbig = sp.Matrix(sp.BlockMatrix([[sp.zeros(3), Mn],
                                 [Mn.conjugate().T, sp.zeros(3)]]))
detDbig = sp.expand(Dbig.det())
modsq = sp.expand(Mn.det() * sp.conjugate(Mn.det()))
# for the 3+3 antidiagonal block, det D = (-1)^3 |det M|^2 = -|det M|^2
# (the exact sign recorded in the 06-08 RP no-go); the modulus is the
# count-twice content.
ok = (sp.simplify(detDbig + modsq) == 0 and sp.im(modsq) == 0
      and modsq > 0)
check(9, "second-order Hermitian block object D=[[0,M],"
         "[Mdag,0]] reads det D = -|det M|^2 (the modulus; count-twice by "
         "construction) -- exact at a complex parameter point; this is a "
         "different object from the "
         "first-order measure Z = det(D_stag + A)", ok)

# (C.2) the first-order measure Z = det(D_stag + A) is first power, and
# D_stag is the reflection-positive staggered kinetic (real antisymmetric)
Dt = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0],
                [0, 0, 0, 1], [0, 0, -1, 0]])
At = sp.Matrix([[a_s, 0, b_s, 0], [0, a_s, 0, c_s],
                [b_s, 0, a_s, 0], [0, c_s, 0, a_s]])
Zt = berezin_partition((Dt + At).tolist(), 4)
ok = (sp.simplify(Zt - (Dt + At).det()) == 0
      and Dt == -Dt.T)
check(10, "the toy first-order measure Z = det(D_stag + A) is a different "
          "object: D_stag is real antisymmetric, "
          "and the one-component measure gives det to the FIRST power "
          "(not |det|^2). This algebra does not establish OS positivity of "
          "the physical first-order action", ok)

# (C.3) reflection-center sensitivity on corner modes. The site-centered
# reflection x_mu -> -x_mu fixes all corner waves, whereas the link-centered
# reflection x_mu -> 1-x_mu contributes (-1)^n_mu. Thus a corner calculation
# cannot silently identify "spatial reflection" with the identity.
site_trivial = True
link_actions = []
for mu in range(3):
    R_site = np.zeros((N, N))
    R_link = np.zeros((N, N))
    for x in sites():
        xs = list(x)
        xl = list(x)
        xs[mu] = (-x[mu]) % L
        xl[mu] = (1 - x[mu]) % L
        R_site[idx(*x), idx(*xs)] = 1.0
        R_link[idx(*x), idx(*xl)] = 1.0
    site_repr = PHI.T @ R_site @ PHI
    link_repr = PHI.T @ R_link @ PHI
    site_trivial = site_trivial and np.allclose(site_repr, np.eye(8))
    expected = np.diag([(-1.0) ** corner[mu] for corner in corners])
    link_actions.append(np.allclose(link_repr, expected))
ok = site_trivial and all(link_actions)
check(11, "corner reflection action depends on the reflection center: "
          "x_mu->-x_mu is identity, while x_mu->1-x_mu acts by "
          "(-1)^n_mu. Therefore this spatial corner calculation does not "
          "reduce a full OS reflection to coupling conjugation or decide "
          "the K-reality stage", ok)
residual("a full Osterwalder--Schrader analysis requires the chosen reflection "
         "center, field transformation, time direction, measure, and positivity "
         "form. The finite spatial corner calculation supplies none of those "
         "missing links.")

# ===================== D. finite discriminator + adjudication ==========
print("\n--- D. the finite discriminator and the adjudication")

# Discriminator I: conjugate-degree of the two analytic prescriptions.
# This distinguishes when the restriction is imposed; it does not select a
# physical prescription or derive an r value.
conj_deg_label = sp.Poly(doublet, bbar_s).degree() if doublet.has(bbar_s) else 0
det3_K_poly = sp.Poly(sp.expand(det3_K), bbar_s)
conj_deg_tie = det3_K_poly.degree()
ok = (conj_deg_label == 0 and conj_deg_tie > 0
      and sp.diff(doublet, bbar_s) == 0
      and sp.diff(det3_K, bbar_s) != 0)
check(12, "stage classifier I (conjugate degree): "
          "untied doublet weight has bbar-degree 0 (holomorphic, d/dbbar "
          "= 0), while imposing c=conj(b) first gives bbar-degree > 0. "
          "This separates the candidate outcome-stage and weight-stage "
          "analytic prescriptions but does not choose one", ok,
      f"conj-degree label = {conj_deg_label}, tie = {conj_deg_tie}")

# Discriminator II: the reality STAGE of the partition function.
Z_generic = sp.expand(det3.subs(
    {a_s: sp.Rational(4, 5),
     b_s: sp.Rational(3, 10) + sp.I * sp.Rational(1, 5),
     c_s: sp.Rational(1, 2) - sp.I * sp.Rational(1, 10)}))
Z_tied = sp.expand(det3_K.subs(
    {a_s: sp.Rational(4, 5),
     b_s: sp.Rational(3, 10) + sp.I * sp.Rational(1, 5),
     bbar_s: sp.Rational(3, 10) - sp.I * sp.Rational(1, 5)}))
ok = (sp.im(Z_generic) != 0                        # generic untied Z complex
      and sp.im(Z_tied) == 0)                      # tied Z real
check(13, "stage classifier II (reality locus of Z): the untied first-power "
          "partition function is generically COMPLEX (nonzero phase); on "
          "the restriction c=conj(b) it is REAL. This locates the stage "
          "question but does not establish when the physical action imposes "
          "the restriction", ok)

# Restricting the holomorphic result after integration and imposing the same
# restriction before evaluation agree pointwise on the K-real locus. This is
# why K-real spectral data alone cannot identify the stage.
Z_restrict_after = sp.expand(det3).subs(c_s, bbar_s)
Z_tie_before = det3_K
avv = sp.Rational(4, 5)
b_pt = sp.Rational(3, 10) + sp.I * sp.Rational(1, 5)
Wpt = (avv * sp.eye(3) + b_pt * sp.Matrix(C3.tolist())
       + sp.conjugate(b_pt) * sp.Matrix((C3 @ C3).tolist()))
detWpt = sp.expand(Wpt.det())                      # exact rational-complex
# registered spectrum: real eigenvalues of the Hermitian M (numpy, exact
# Hermitian so eigvalsh is real by construction)
bnum = 0.3 + 0.2j
Wnum = (0.8 * np.eye(3) + bnum * C3 + np.conj(bnum) * (C3 @ C3))
spec = np.linalg.eigvalsh(Wnum)                    # real registered masses
# closed-form lam_k = a + 2|b| cos(delta + 2 pi k/3), same b
delta = np.angle(bnum)
modb = abs(bnum)
lam_closed = sorted(0.8 + 2 * modb * np.cos(delta + 2 * np.pi * k / 3)
                    for k in range(3))
ok = (sp.simplify(Z_restrict_after - Z_tie_before) == 0
      and Wpt == Wpt.conjugate().T                  # Hermitian restriction
      and sp.im(detWpt) == 0                        # arg det M real at weight
      and np.allclose(np.imag(spec), 0.0)           # registered masses real
      and np.allclose(np.sort(spec.real), lam_closed))
check(14, "pointwise K-real data are stage-blind: restricting the holomorphic "
          "determinant after integration equals imposing c=conj(b) before "
          "evaluation, and the common Hermitian restriction has the real "
          "spectrum a+2|b|cos(delta+2pi k/3). This does not prove that an "
          "untied physical action is lawful", ok)

det_from_spectrum = float(np.prod(spec.real))
ok = (sp.im(detWpt) == 0
      and abs(np.imag(np.prod(spec))) < 1e-9
      and abs(float(sp.re(detWpt)) - det_from_spectrum) < 1e-9
      and sp.im(Z_generic) != 0)
check(15, "a real determinant on the K-real locus is not a stage selector: "
          "the determinant equals the product of the common real spectrum, "
          "whereas a generic untied point is complex. No theta-sector or "
          "physical-mass identification is inferred from this algebra", ok)

# The exact residual: the algebra classifies the two analytic stages and the
# two conditional endpoint equations, but supplies no stage-selection or
# weighting-law theorem.
X_measure_holo = (sp.diff(doublet, bbar_s) == 0)
X_transfer_2nd = (sp.simplify(detDbig + modsq) == 0)
Y_conditional_arith = (r_label == sp.Rational(1, 2) and r_tie == 1)
stage_classified = (conj_deg_label == 0 and conj_deg_tie > 0
                    and sp.simplify(Z_restrict_after - Z_tie_before) == 0)
ok = (X_measure_holo and X_transfer_2nd and Y_conditional_arith
      and stage_classified and site_trivial and all(link_actions))
check(16, "UNDECIDED WITH EXACT RESIDUAL: within the source-defined two-cell "
          "fork, K-reality is placed at the weight (restrict before analytic "
          "classification) or at the outcome (restrict after the holomorphic "
          "calculation). The checked algebra localizes that stage difference "
          "but does not select a stage, derive either equipartition law, or "
          "upgrade the conditional r=1 versus r=1/2 endpoints", ok)
residual("the physical selection of the reading stage (weight tie vs "
         "outcome label) is an open K-reality / orbit-occupancy question "
         "(CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_"
         "OF_CUSTODY_2026-06-02; KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_"
         "PREMISE_CANDIDATE_NOTE_2026-06-09). No admission premise class "
         "exists, and nothing here adopts a premise.")
residual("inherited gate-note residuals remain at their declared grades: "
         "kinetic-class premise, spin-statistics support tier (one "
         "Grassmann pair per site), boundary-holonomy convention, "
         "AC_phi_lambda labeling convention (STAGGERED_DIRAC_REALIZATION_"
         "GATE_NOTE_2026-05-03 section 5).")
residual("all cited source-note rows used for the fork, transfer walls, and "
         "occupancy alternatives are currently unaudited; this runner imports "
         "no audit grade from them.")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: UNDECIDED WITH EXACT RESIDUAL. The determinant algebra "
      "distinguishes imposing K-reality before analytic classification "
      "(weight stage) from imposing the same restriction after the "
      "holomorphic calculation (outcome stage), while the two prescriptions "
      "agree pointwise on the K-real locus. The supplied per-real-mode and "
      "per-outcome-cell laws conditionally give r=1 and r=1/2, respectively, "
      "but neither law nor its pairing with a physical stage is derived. "
      "Spatial corner reflections are center-dependent and do not replace "
      "a full OS test. No premise adopted; no audit status.")
raise SystemExit(0 if _fail == 0 else 1)
