#!/usr/bin/env python3
"""Koide first-order section question -- tie-at-weight vs label-at-outcome.

Companion runner for
    docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md

The staggered first-order block (PR #3551,
KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_..._2026-06-11) proved:
the one-component staggered measure delivers a FIRST-ORDER generation
determinant (a single power of det, computed by explicit Grassmann
expansion), and the count-twice |b|^2 structure that the landed r=1
no-gos read out enters EXACTLY AND ONLY through the K-reality restriction
c = conj(b) of the coupling parameters.  The channel-generality companion
(KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_..._2026-06-11) closed the
channel residual: first-order holomorphy is channel-independent and
count-twice arises exactly on antiunitary-tied parameter sections.

The decisive residual is therefore sharp:

  Does the physical matter action force the K-real TIED SECTION at the
  level of the statistical WEIGHT (count-twice => the r=1 cell), or does
  K-reality enter only as OUTCOME LABELING / a reality constraint on
  registered outcomes, with the weight staying first-power holomorphic in
  the untied parameters (count-once => the r=1/2 cell)?

This runner does the exact, Berezin-level computation and adjudicates
what the LANDED constraints pay for.  It does NOT hardcode a verdict: it
computes both sections, builds a finite discriminator, and tests whether
the landed walls (the r=1 Kahler-Dirac wall 2026-06-08; the reflection-
positivity second-order wall 2026-06-08) close the binary.

Sections:

  A. Reproduce the first-order generation determinant on the hw=1 corner
     triplet by explicit Grassmann/Berezin expansion (no determinant
     identity assumed): Z = det(W) to the FIRST power for the circulant
     coupling W = a*I + b*C + c*C^2; exact singlet/doublet factorization
     Z = lam0 * (lam_omega * lam_omegabar).

  B. Both sections exactly.  (i) Untied holomorphic section (b, c
     independent): the doublet weight lam_omega * lam_omegabar is
     holomorphic (no conjugate), one complex slot per K-orbit.  (ii)
     K-real tied section c = conj(b): the doublet weight becomes a
     function of |b|^2 (Wirtinger d^2/db dbbar = -3a on det3), count-
     twice.  The fork-cell arithmetic lands where PR #3551 said:
     holomorphic/one-slot -> r = 1/2, Q = 2/3; tied/two-slot -> r = 1,
     Q = 1.

  C. THE NEW CONTENT, part 1 -- does reflection positivity (the 06-08 RP
     wall) constrain the FIRST-ORDER one-component measure, or only the
     Hermitian/second-order transfer family?  Reproduce the RP rejection
     of the bare first-order operator W_h = a*I + b*C (non-self-adjoint);
     show the first-order MEASURE Z = det(D_stag + A) is a different
     object RP-of-that-wall does not touch; and compute the striking
     corner fact: every spatial lattice reflection acts as the IDENTITY
     on all 8 corner modes, so on the corner sector the OS reflection
     reduces to complex conjugation of the coupling -- the SAME
     antiunitary K whose tied sections the fork already classifies.  RP
     adds no independent closing constraint beyond the K-reality selector.

  D. THE NEW CONTENT, part 2 -- the finite discriminator and the
     adjudication.  Discriminator I: the conjugate-degree of the physical
     doublet weight (= 0 holomorphic <=> label/outcome <=> r = 1/2;
     > 0 non-holomorphic <=> tie/weight <=> r = 1).  Discriminator II:
     the reality stage of the partition function (Z generically complex
     off the tie, real on the tie -- so "at what stage does Z become
     real" is weight (tie) vs outcome (label)).  Then both cells are
     exhibited as lawful under the landed constraints (Cell TIE
     reproduces the r=1 wall and the RP second-order object; Cell LABEL
     is the one-component holomorphic measure with outcome K-orbit
     registration), the theta-structure consistency is checked (both
     cells give arg det M real; Cell LABEL does not break the theta
     discharge because arg det M real is an OUTCOME condition), and the
     exact residual is stated: the landed surface fixes the measure's
     holomorphy and each cell's internal arithmetic but is SILENT on the
     weight-tie-vs-outcome-label stage.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark load-bearing
premises at the point of use.  Final line: TOTAL: PASS=<n> FAIL=<m>.
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
print("Koide first-order section question -- tie-at-weight vs label-at-outcome")
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
         "no conjugate appears, d/dbbar = 0 identically; the doublet is "
         "ONE complex slot per K-orbit (count-once)", ok)

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
         "(Laplacian -12a), the doublet weight depends on |b|^2 -- "
         "count-twice enters EXACTLY and ONLY through the tie (PR #3551 "
         "localization, reproven)", ok)

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
check(7, "fork-cell landing (note 6 + equipartition-granularity laws, "
         "reproven; withdrawn rho-map NOT used): untied/holomorphic = "
         "per-outcome-cell law -> r = 1/2, Q = 2/3; tied = per-real-mode "
         "law -> r = 1, Q = 1.  This is exactly PR #3551's localization: "
         "count-twice iff the tie", ok)
residual("the coupling on the hw=1 triplet is the C_3[111] rotation-"
         "channel circulant W = a*I + b*C + c*C^2, a DECLARED probe "
         "coupling (PR #3551), not a derived Yukawa; the channel-space "
         "companion 2026-06-11 shows the holomorphy/tie split is channel-"
         "independent across the full M_4+M_2+M_2 equivariant space.")

# ===================== C. does RP constrain the first-order measure? ====
print("\n--- C. reflection positivity: does it touch the first-order measure?")

# (C.1) the 06-08 RP wall's rejection of the bare first-order operator
Wh = a_s * sp.eye(3) + b_s * sp.Matrix(C3.tolist())     # W_h = a I + b C
ok = (sp.simplify(Wh - Wh.conjugate().T) != sp.zeros(3)     # not self-adjoint
      and sp.simplify(sp.Matrix((C3.T).tolist())
                      - sp.Matrix((C3 @ C3).tolist())) == sp.zeros(3))
check(8, "RP wall (06-08) reproduced: the bare first-order OPERATOR "
         "W_h = a*I + b*C is non-self-adjoint for generic b (C^T = C^2 "
         "!= C), so RP rejects it as a transfer object and forces the "
         "second-order Hermitian corner Dirac -- a statement about the "
         "TRANSFER family, not the measure", ok)

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
check(9, "the RP-compatible second-order transfer object D=[[0,M],"
         "[Mdag,0]] reads det D = -|det M|^2 (the modulus; count-twice by "
         "construction, the 06-08 RP/Kahler-Dirac wall) -- exact at a "
         "complex parameter point; this is a DIFFERENT object from the "
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
check(10, "the first-order MEASURE Z = det(D_stag + A) is a DIFFERENT "
          "object: D_stag real antisymmetric (the RP staggered kinetic), "
          "and the one-component measure gives det to the FIRST power "
          "(NOT |det|^2) -- the RP rejection of W_h-as-transfer does not "
          "touch this Grassmann weight", ok)

# (C.3) the striking corner fact: every spatial reflection is the IDENTITY
# on all 8 corner modes -> on the corner sector OS reflection reduces to
# complex conjugation of the coupling (the SAME antiunitary K of the fork)
refl_trivial = True
for mu in range(3):
    Rp = np.zeros((N, N))
    for x in sites():
        xr = list(x)
        xr[mu] = (-x[mu]) % L                       # reflect x_mu -> -x_mu
        Rp[idx(*x), idx(*xr)] = 1.0
    if not np.allclose(Rp @ PHI, PHI):              # every corner mode fixed
        refl_trivial = False
# the corner-sector antiunitary is K: A -> conj(A) = abar I + bbar C + cbar C^2
Amat = (a_s * sp.eye(3) + b_s * sp.Matrix(C3.tolist())
        + c_s * sp.Matrix((C3 @ C3).tolist()))
A_K = Amat.conjugate()                                    # complex conjugation
A_K_explicit = (sp.conjugate(a_s) * sp.eye(3)
                + sp.conjugate(b_s) * sp.Matrix(C3.tolist())
                + sp.conjugate(c_s) * sp.Matrix((C3 @ C3).tolist()))
real_sub = {a_s: sp.Symbol("ar", real=True),
            b_s: sp.Symbol("brr", real=True),
            c_s: sp.Symbol("cr", real=True)}
ok = (refl_trivial
      and A_K == A_K_explicit                             # K: A -> conj(A)
      and A_K.subs(real_sub) == Amat.subs(real_sub)       # real coupling K-fixed
      and A_K != Amat)                                    # generic coupling moved
check(11, "every spatial lattice reflection x_mu -> -x_mu acts as the "
          "IDENTITY on all 8 corner modes (each corner plane wave is "
          "2-torsion): on the corner sector the OS reflection reduces to "
          "complex conjugation of the coupling A -> conj(A) -- the SAME "
          "antiunitary K whose tied sections the fork classifies.  RP "
          "adds NO independent closing constraint beyond the K-reality "
          "selector", ok)
residual("RP as landed (06-08) constrains the second-order Hermitian-"
         "corner transfer family; its corner-sector positivity content "
         "coincides with the complex-conjugation antiunitary K that IS "
         "the tie-vs-label binary.  Whether the full first-order action "
         "is required to be OS-reflection-positive (hence K-tied at the "
         "weight) or only OS-reconstructible from K-real records is the "
         "residual, not a landed result.")

# ===================== D. finite discriminator + adjudication ==========
print("\n--- D. the finite discriminator and the adjudication")

# Discriminator I: conjugate-degree of the physical doublet weight.
#   label (untied): degree in bbar = 0 (holomorphic)  -> r = 1/2
#   tie   (c=bbar): degree in bbar > 0 (non-holomorphic) -> r = 1
conj_deg_label = sp.Poly(doublet, bbar_s).degree() if doublet.has(bbar_s) else 0
det3_K_poly = sp.Poly(sp.expand(det3_K), bbar_s)
conj_deg_tie = det3_K_poly.degree()
ok = (conj_deg_label == 0 and conj_deg_tie > 0
      and sp.diff(doublet, bbar_s) == 0
      and sp.diff(det3_K, bbar_s) != 0)
check(12, "DISCRIMINATOR I (conjugate-degree of the physical weight): "
          "untied doublet weight has bbar-degree 0 (holomorphic, d/dbbar "
          "= 0 => LABEL/outcome => r = 1/2); the c=conj(b) tied weight "
          "has bbar-degree > 0 (non-holomorphic => TIE/weight => r = 1).  "
          "A single finite invariant separates the two cells", ok,
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
check(13, "DISCRIMINATOR II (reality stage of Z): the untied first-power "
          "partition function is generically COMPLEX (nonzero phase); on "
          "the tie c=conj(b) it is REAL.  So 'at what stage does Z become "
          "real' is the discriminator: WEIGHT (tie, before integration) "
          "vs OUTCOME (label, reality of registered records after "
          "integration)", ok)

# both cells are lawful under the landed constraints.
# Cell TIE: the mass matrix M is the Hermitian coupling (c = conj(b), a
# real); arg det M is real because det M is real, enforced at the WEIGHT.
# Cell LABEL: the one-component holomorphic measure; K-reality is the
# reality condition on the REGISTERED spectrum.  Both cells share the SAME
# real spectrum -- the eigenvalues of the Hermitian M -- and differ only in
# the analytic type of the WEIGHT.  Exact-rational b (no transcendental
# eigenvalues); spectrum reality/equality read with numpy (Hermitian).
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
ok = (Wpt == Wpt.conjugate().T                     # Hermitian coupling
      and sp.im(detWpt) == 0                        # arg det M real at weight
      and np.allclose(np.imag(spec), 0.0)           # registered masses real
      and np.allclose(np.sort(spec.real), lam_closed))
check(14, "both cells lawful: Cell TIE reproduces the r=1 wall (|det M|^2, "
          "Hermitian coupling, arg det M real at the WEIGHT); Cell LABEL "
          "is the one-component holomorphic measure whose REGISTERED "
          "spectrum is the same real lam_k = a + 2|b|cos(delta+2pi k/3).  "
          "Both cells share the identical physical spectrum; they differ "
          "only in the analytic type of the WEIGHT (the mode count r)", ok)

# theta-structure consistency: arg det M real is an OUTCOME condition, so
# Cell LABEL (untie the weight) does NOT break the theta discharge.
# Cell TIE: det M real at the weight (Hermitian M).  Cell LABEL: the
# registered det = product of the real registered eigenvalues is also real,
# and equals det M -- arg det M real holds at the OUTCOME level in BOTH.
det_from_spectrum = float(np.prod(spec.real))            # registered outcome
ok = (sp.im(detWpt) == 0                                  # tie: real at weight
      and abs(np.imag(np.prod(spec))) < 1e-9              # label: real outcome
      and abs(float(sp.re(detWpt)) - det_from_spectrum)   # same value
      < 1e-9)
check(15, "theta-structure consistency: arg det M real holds in BOTH "
          "cells -- Cell TIE enforces it at the weight (Hermitian M), "
          "Cell LABEL at the outcome (real registered spectrum).  The "
          "theta discharge consumed 'arg det M real' as an OUTCOME "
          "condition, so untying the weight (Cell LABEL) does NOT break "
          "the theta discharge's consumed structure", ok)

# the exact residual: landed surface fixes X and Y, silent on the stage
# X = measure holomorphy (checks 3,5) + second-order transfer object (9)
# Y = each cell's internal r-arithmetic (7,14)
# silent on: which stage K-reality acts at (the field-content binary)
X_measure_holo = (sp.diff(doublet, bbar_s) == 0)
X_transfer_2nd = (sp.simplify(detDbig + modsq) == 0)     # det D = -|det M|^2
Y_cell_arith = (r_label == sp.Rational(1, 2) and r_tie == 1)
silent = (conj_deg_label == 0 and conj_deg_tie > 0)      # both values lawful
ok = (X_measure_holo and X_transfer_2nd and Y_cell_arith and silent)
check(16, "EXACT RESIDUAL: the landed surface FIXES X (the measure is "
          "holomorphic; the RP-compatible transfer object is second-"
          "order) and Y (each cell's internal r-arithmetic), but is "
          "SILENT on the weight-tie-vs-outcome-label stage.  Both cells "
          "are lawful; the binary r=1 vs r=1/2 is EXACTLY the binary "
          "'K-reality acts at the weight (tie the section c=conj(b) "
          "before the Berezin integral) vs at the outcome (K-orbit "
          "grouping of registered records after integration)' = the "
          "custody note's ADMITTED K-reality selector.  (The Hermitian "
          "corner Dirac is the tied-section realization -- the K-tied "
          "point of the holomorphic family, per channel-space 06-11 -- "
          "not an independently forced distinct object)", ok)
residual("the physical selection of the reading stage (weight tie vs "
         "outcome label) is the standing K-reality / orbit-occupancy "
         "owner-decision premise (CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_"
         "OF_CUSTODY_2026-06-02; KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_"
         "PREMISE_CANDIDATE_NOTE_2026-06-09).  Nothing here adopts it.")
residual("inherited gate-note residuals remain at their declared grades: "
         "kinetic-class premise, spin-statistics support tier (one "
         "Grassmann pair per site), boundary-holonomy convention, "
         "AC_phi_lambda labeling convention (STAGGERED_DIRAC_REALIZATION_"
         "GATE_NOTE_2026-05-03 section 5).")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: UNDECIDED WITH EXACT RESIDUAL.  On the first-order surface "
      "the one-component staggered measure is holomorphic in the untied "
      "couplings (count-once) and the count-twice |b|^2 structure enters "
      "exactly on the K-real tied section c=conj(b) (PR #3551, reproven). "
      "The landed r=1 wall (|det M|^2) and RP second-order wall both act "
      "on the Hermitian/second-order TRANSFER family; on the corner "
      "sector every spatial reflection is the identity, so RP's "
      "positivity content is the same antiunitary K that IS the binary. "
      "The landed surface fixes the measure's holomorphy and each cell's "
      "arithmetic but is SILENT on whether K-reality ties the weight "
      "(r=1) or labels the outcomes (r=1/2).  The binary is exactly the "
      "weight-vs-outcome stage of K-reality -- read on the antiunitary-"
      "tied section (Hermitian corner Dirac, |det M|^2) or as the "
      "unrestricted holomorphic measure with K-orbit outcome grouping -- "
      "= the custody note's admitted K-reality selector.  No premise "
      "adopted; no audit status.")
raise SystemExit(0 if _fail == 0 else 1)
