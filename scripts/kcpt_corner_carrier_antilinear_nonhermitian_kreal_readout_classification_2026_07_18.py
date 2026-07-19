#!/usr/bin/env python3
"""Exact-arithmetic verifier for the KCPT corner-carrier antilinear and
non-Hermitian K-real readout classification (bounded theorem, 2026-07-18).

Every gate is exact: sympy symbolic algebra on the 3-dim corner carrier and
integer numpy / exact sympy rank on the 4^3 staggered lattice delivery. No
floating point enters any decision. Each gate prints a single line
``PASS <id> <desc>`` or ``FAIL <id> <desc>`` and the run ends with
``TOTAL: PASS=N FAIL=0``.

Run from the worktree root:
    python3 scripts/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py
"""

from pathlib import Path
import re

import numpy as np
import sympy as sp
from sympy import I, Matrix, Rational, conjugate, eye, sqrt, symbols, zeros

AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Paths of this unit and its four dependencies (relative to the worktree root)
# ---------------------------------------------------------------------------
NOTE_REL = (
    "docs/KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_"
    "CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
DEP_DELIVERY = (
    "docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_"
    "POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
)
DEP_SPECTRAL = (
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_"
    "SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
DEP_MECHANISM = (
    "docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_"
    "PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
DEP_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"

REGISTRY_ID = (
    "kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_"
    "classification_bounded_theorem_note_2026-07-18"
)

LEDGER_RIDS = [
    "kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17",
    "kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_bounded_theorem_note_2026-07-16",
    "kcpt_orbit_constant_registered_occupancy_weights_derivable_protocol_class_bounded_theorem_note_2026-07-12",
    "minimal_axioms",
]

# ---------------------------------------------------------------------------
# Gate bookkeeping and exact-zero helpers
# ---------------------------------------------------------------------------
PASS = 0
FAIL = 0
FAILURES = []


def check(block, desc, condition):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
        FAILURES.append(f"{block} {desc}")
    print(f"{status} {block} {desc}")


def zc(expr):
    """Exact scalar zero test."""
    return sp.simplify(sp.expand_complex(sp.expand(expr))) == 0


def mz(M):
    """Exact entrywise matrix zero test."""
    return all(zc(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def eqm(A, B):
    return mz(A - B)


def norm_ws(s):
    return " ".join(s.split())


def read_flat(rel):
    return norm_ws((ROOT / rel).read_text(encoding="utf-8"))


# ===========================================================================
# Carrier constants (exact)
# ===========================================================================
C3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
w = Rational(-1, 2) + sqrt(3) / 2 * I
wb = Rational(-1, 2) - sqrt(3) / 2 * I
v0 = Matrix([1, 1, 1])
vw = Matrix([1, conjugate(w), conjugate(w) ** 2])
vwb = vw.conjugate()


def herm(u, v):
    return (u.H * v)[0, 0]


def bil(u, v):
    return (u.T * v)[0, 0]


def E_lin(A, psi):
    """Linear functional E_A(psi) = psi^dag A psi."""
    return (psi.H * A * psi)[0, 0]


def F_anti(A, psi):
    """Antilinear functional F_B(psi) = psi^dag conj(A) conj(psi), B = K o A."""
    return (psi.H * A.conjugate() * psi.conjugate())[0, 0]


P_w = (eye(3) + conjugate(w) * C3 + conjugate(w) ** 2 * C3 ** 2) / 3
P_wb = (eye(3) + conjugate(wb) * C3 + conjugate(wb) ** 2 * C3 ** 2) / 3

# ===========================================================================
# B1 - Corner carrier setup
# ===========================================================================
check("B1.1", "carrier C^3 = I_3", eqm(C3 ** 3, eye(3)))
check("B1.2", "carrier transpose C^T = C^2", eqm(C3.T, C3 ** 2))
check("B1.3", "carrier is real: K C K = conj(C) = C", eqm(C3.conjugate(), C3))
check("B1.4", "cube-root identity 1 + w + w^2 = 0 and w^3 = 1",
      zc(1 + w + w ** 2) and zc(w ** 3 - 1))
check("B1.5", "conj(w) = w^2 and w*conj(w) = 1", zc(conjugate(w) - w ** 2) and zc(w * conjugate(w) - 1))
check("B1.6", "doublet eigen C vw = w vw", mz(C3 * vw - w * vw))
check("B1.7", "conjugate doublet eigen C vwb = conj(w) vwb", mz(C3 * vwb - conjugate(w) * vwb))
check("B1.8", "singlet eigen C v0 = v0", mz(C3 * v0 - v0))
check("B1.9", "conjugation swaps doublet vectors conj(vw) = vwb", mz(vw.conjugate() - vwb))
check("B1.10", "Hermitian orthogonality <vw,vwb> = 0", zc(herm(vw, vwb)))
check("B1.11", "Hermitian norms <vw,vw> = 3 and <v0,v0> = 3",
      zc(herm(vw, vw) - 3) and zc(herm(v0, v0) - 3))
check("B1.12", "cyclotomic bilinear self-sums vw^T vw = 0 and vwb^T vwb = 0",
      zc(bil(vw, vw)) and zc(bil(vwb, vwb)))
check("B1.13", "cyclotomic bilinear cross-sum vwb^T vw = 3", zc(bil(vwb, vw) - 3))

# ===========================================================================
# B2 - T1 Hermitian-decomposition bridge (6) + T2 linear non-Hermitian face (9)
# ===========================================================================
ar = symbols("ar0:9", real=True)
ai = symbols("ai0:9", real=True)
A_gen = Matrix(3, 3, [ar[k] + I * ai[k] for k in range(9)])
A_real = Matrix(3, 3, [ar[k] for k in range(9)])
H1 = (A_gen + A_gen.H) / 2
H2 = (A_gen - A_gen.H) / (2 * I)

# -- T1 bridge --
check("B2.1", "bridge parts H1, H2 are Hermitian (generic complex A)",
      mz(H1 - H1.H) and mz(H2 - H2.H))
check("B2.2", "bridge reconstruction A = H1 + i H2 (generic complex A)",
      mz(A_gen - (H1 + I * H2)))
# uniqueness: any Hermitian G with i*G also Hermitian must vanish (Herm cap anti-Herm = 0)
gr = symbols("gr0:9", real=True)
gi = symbols("gi0:9", real=True)
G = Matrix(3, 3, [gr[k] + I * gi[k] for k in range(9)])
herm_eqs = []
for i in range(3):
    for j in range(3):
        e = (G - G.H)[i, j]
        herm_eqs += [sp.re(sp.expand_complex(e)), sp.im(sp.expand_complex(e))]
        e2 = (I * G - (I * G).H)[i, j]
        herm_eqs += [sp.re(sp.expand_complex(e2)), sp.im(sp.expand_complex(e2))]
allsym = list(gr) + list(gi)
Muni = sp.Matrix([[sp.diff(e, s) for s in allsym] for e in herm_eqs])
check("B2.3", "bridge uniqueness: Hermitian and anti-Hermitian force zero (rank 18)",
      Muni.rank() == 18)
H1r = (A_real + A_real.H) / 2
H2r = (A_real - A_real.H) / (2 * I)
check("B2.4", "real A: symmetric part H1 is K-even (conj H1 = H1)", mz(H1r.conjugate() - H1r))
check("B2.5", "real A: skew part H2 is K-odd (conj H2 = -H2) and i H2 is real",
      mz(H2r.conjugate() + H2r) and mz((I * H2r).conjugate() - (I * H2r)))
# converse: K-even/K-odd component conditions are equivalent to entrywise-real A
check("B2.6", "bridge converse: conj(A)-A = (H1-conjH1) + i(H2+conjH2), so K-even+K-odd => real A",
      mz((A_gen - A_gen.conjugate())
         - ((H1 - H1.conjugate()) + I * (H2 + H2.conjugate()))))

# -- T2 linear non-Hermitian K-real face --
pr = symbols("pr0:3", real=True)
pi_ = symbols("pi0:3", real=True)
psi = Matrix([pr[k] + I * pi_[k] for k in range(3)])
check("B2.7", "conjugate-values law E_A(K psi) = conj(E_A(psi)) (real A, generic psi)",
      zc(E_lin(A_real, psi.conjugate()) - conjugate(E_lin(A_real, psi))))
Evw_re = E_lin(A_real, vw)
Evwb_re = E_lin(A_real, vwb)
check("B2.8", "doublet values are conjugates E_A(vwb) = conj(E_A(vw)); equal real parts",
      zc(Evwb_re - conjugate(Evw_re)) and zc(sp.re(Evw_re) - sp.re(Evwb_re)))
A_sym = (A_real + A_real.T) / 2
A_skew = (A_real - A_real.T) / 2
check("B2.9", "symmetric part gives equal doublet values E_sym(vw) = E_sym(vwb)",
      zc(E_lin(A_sym, vw) - E_lin(A_sym, vwb)))
check("B2.10", "skew part gives opposite imaginary values E_skew(vwb) = -E_skew(vw), purely imaginary",
      zc(E_lin(A_skew, vwb) + E_lin(A_skew, vw)) and zc(sp.re(E_lin(A_skew, vw))))
check("B2.11", "separation E_A(vw)-E_A(vwb) = 2 i Im E_A(vw) carried entirely by the skew part",
      zc((Evw_re - Evwb_re) - 2 * I * sp.im(Evw_re))
      and zc((Evw_re - Evwb_re) - (E_lin(A_skew, vw) - E_lin(A_skew, vwb))))
Awit = C3 - C3 ** 2
check("B2.12", "escape witness A = C - C^2 gives E(vw) = 3*i*sqrt(3)",
      zc(E_lin(Awit, vw) - 3 * I * sqrt(3)))
check("B2.13", "escape witness A = C - C^2 gives E(vwb) = -3*i*sqrt(3)",
      zc(E_lin(Awit, vwb) + 3 * I * sqrt(3)))
check("B2.14", "character projector P_w = vw vw^dag / 3 is Hermitian idempotent with C P_w = w P_w",
      mz(P_w - vw * vw.H / 3) and mz(P_w - P_w.H) and mz(P_w * P_w - P_w) and mz(C3 * P_w - w * P_w))
check("B2.15", "polarization identity i(C - C^2) = -sqrt(3) (P_w - P_wb)",
      mz(I * (C3 - C3 ** 2) + sqrt(3) * (P_w - P_wb)))
# supporting extra: witness A = C - C^2 is real (K-real) yet non-Hermitian
check("B2.16", "linear escape witness is K-real (conj A = A) yet non-Hermitian (A != A^dag)",
      mz(Awit.conjugate() - Awit) and not mz(Awit - Awit.H))
Hwit = I * Awit
check("B2.17", "Hermitian equality requires K-reality: i(C-C^2) is Hermitian, K-odd, and separates the pair",
      mz(Hwit - Hwit.H) and mz(Hwit.conjugate() + Hwit)
      and zc(E_lin(Hwit, vw) + 3 * sqrt(3))
      and zc(E_lin(Hwit, vwb) - 3 * sqrt(3)))

# ===========================================================================
# B3 - T3 antilinear equivariant face
# ===========================================================================
a, b, c = symbols("a b c")
A_span = a * eye(3) + b * C3 + c * C3 ** 2
# commutant of C (equivariance transports to conj(A) in commutant of C)
comm = A_gen * C3 - C3 * A_gen
lin = []
for i in range(3):
    for j in range(3):
        e = sp.expand_complex(comm[i, j])
        lin += [sp.re(e), sp.im(e)]
allA = list(ar) + list(ai)
Mcomm = sp.Matrix([[sp.diff(l, s) for s in allA] for l in lin])
check("B3.1", "commutant of C has complex dimension 3 (real solution space dim 6)",
      18 - Mcomm.rank() == 6)
check("B3.2", "the three powers {I, C, C^2} are linearly independent",
      Matrix([list(eye(3)), list(C3), list(C3 ** 2)]).rank() == 3)
# equivariance forward: antilinear B = K o A with A in span commutes with C on every vector
vr = symbols("vr0:3", real=True)
vi = symbols("vi0:3", real=True)
vv = Matrix([vr[k] + I * vi[k] for k in range(3)])


def Bop(A, z):
    return A.conjugate() * z.conjugate()


check("B3.3", "equivariance forward: A in span{I,C,C^2} gives B(C psi) = C(B psi)",
      mz(Bop(A_span, C3 * vv) - C3 * Bop(A_span, vv)))
# equivariance reverse: generic A with B C = C B forces conj(A) in commutant => A in span
comm2 = A_gen.conjugate() * C3 - C3 * A_gen.conjugate()
lin2 = []
for i in range(3):
    for j in range(3):
        e = sp.expand_complex(comm2[i, j])
        lin2 += [sp.re(e), sp.im(e)]
Mcomm2 = sp.Matrix([[sp.diff(l, s) for s in allA] for l in lin2])
check("B3.4", "equivariance reverse: B C = C B forces A into the 3-dim span (real dim 6)",
      18 - Mcomm2.rank() == 6)
check("B3.5", "doublet transport B vw = conj(a + b w + c w^2) vwb and singlet B v0 = conj(a+b+c) v0",
      mz(Bop(A_span, vw) - conjugate(a + b * w + c * w ** 2) * vwb)
      and mz(Bop(A_span, v0) - conjugate(a + b + c) * v0))
check("B3.6", "equivariant antilinear functional vanishes on both doublet lines F_B(vw)=F_B(vwb)=0",
      zc(F_anti(A_span, vw)) and zc(F_anti(A_span, vwb)))
check("B3.7", "singlet value stays free F_B(v0) = 3 conj(a + b + c)",
      zc(F_anti(A_span, v0) - 3 * conjugate(a + b + c)))

# ===========================================================================
# B4 - T4 antilinear K-real face (equivariance dropped)
# ===========================================================================
def K_map(z):
    return z.conjugate()


def B_map(A, z):
    return A.conjugate() * z.conjugate()


KBKv = K_map(B_map(A_gen, K_map(vv)))
check("B4.1", "structural (K B K)(v) = A conj(v): composing K, B, K on a generic complex A",
      mz(KBKv - A_gen * vv.conjugate()))
check("B4.2", "structural (K B K - B)(v) = (A - conj(A)) conj(v)",
      mz((KBKv - B_map(A_gen, vv)) - (A_gen - A_gen.conjugate()) * vv.conjugate()))
# K-reality K B K = B  <=>  A entrywise real (both directions, via defect A - conj A)
defect = A_gen - A_gen.conjugate()
lin3 = []
for i in range(3):
    for j in range(3):
        e = sp.expand_complex(defect[i, j])
        lin3 += [sp.re(e), sp.im(e)]
Mdef = sp.Matrix([[sp.diff(l, s) for s in allA] for l in lin3])
check("B4.3", "K-reality K B K = B iff A entrywise real (defect A - conj A vanishes on 9 imag dofs)",
      18 - Mdef.rank() == 9)
check("B4.4", "K-real antilinear functional is the bilinear form F_B(vw) = vwb^T A vwb (real A)",
      zc(F_anti(A_real, vw) - bil(vwb, A_real * vwb)))
check("B4.5", "only the symmetric part contributes: skew A gives F_B(vw)=0, F_B(vw)=vwb^T A_sym vwb",
      zc(bil(vwb, A_skew * vwb)) and zc(F_anti(A_real, vw) - bil(vwb, A_sym * vwb)))
check("B4.6", "conjugate law F_B(vwb) = conj(F_B(vw)) (real A)",
      zc(F_anti(A_real, vwb) - conjugate(F_anti(A_real, vw))))
check("B4.7", "equal moduli |F_B(vw)| = |F_B(vwb)| (real A)",
      zc(F_anti(A_real, vw) * conjugate(F_anti(A_real, vw))
         - F_anti(A_real, vwb) * conjugate(F_anti(A_real, vwb))))
cr, ci = symbols("cr ci", real=True)
cc = cr + I * ci
check("B4.8", "phase covariance F_B(c psi) = conj(c)^2 F_B(psi) (generic c, psi, real A)",
      zc(F_anti(A_real, cc * vv) - conjugate(cc) ** 2 * F_anti(A_real, vv)))
check("B4.9", "phase covariance at c = w: F_B(w vw) = conj(w)^2 F_B(vw)",
      zc(F_anti(A_real, w * vw) - conjugate(w) ** 2 * F_anti(A_real, vw)))
A_esc = vwb * vwb.T
check("B4.10", "escape witness A = vwb vwb^T gives F_B(vw) = 9", zc(F_anti(A_esc, vw) - 9))
check("B4.11", "escape witness A = vwb vwb^T gives F_B(vwb) = 0", zc(F_anti(A_esc, vwb)))
A_mir = vw * vw.T
check("B4.12", "mirror witness A = vw vw^T gives F_B(vw) = 0 and F_B(vwb) = 9",
      zc(F_anti(A_mir, vw)) and zc(F_anti(A_mir, vwb) - 9))
check("B4.13", "both witnesses are non-K-real (conj A != A)",
      (not mz(A_esc.conjugate() - A_esc)) and (not mz(A_mir.conjugate() - A_mir)))
check("B4.14", "both witnesses break equivariance (C A != A C)",
      (not mz(C3 * A_esc - A_esc * C3)) and (not mz(C3 * A_mir - A_mir * C3)))
E11 = zeros(3, 3)
E11[0, 0] = 1
check("B4.15", "rejector A = E11 is K-real and non-equivariant and gives the non-null pair (1,1)",
      mz(E11.conjugate() - E11) and not mz(C3 * E11 - E11 * C3)
      and zc(F_anti(E11, vw) - 1) and zc(F_anti(E11, vwb) - 1))
A_phase = zeros(3, 3)
A_phase[0, 1] = 1
A_phase[1, 0] = 1
check("B4.16", "K-real phase witness has distinct conjugate values 2w and 2conj(w) but equal modulus squared 4",
      mz(A_phase.conjugate() - A_phase)
      and zc(F_anti(A_phase, vw) - 2 * w)
      and zc(F_anti(A_phase, vwb) - 2 * conjugate(w))
      and zc(F_anti(A_phase, vw) * conjugate(F_anti(A_phase, vw)) - 4)
      and zc(F_anti(A_phase, vwb) * conjugate(F_anti(A_phase, vwb)) - 4))

# ===========================================================================
# B5 - T5 free values, orientation-neutrality, r-neutrality
# ===========================================================================
al, be, ga = symbols("al be ga", real=True)
A_free = al * eye(3) + be * (C3 + C3 ** 2) + ga * (C3 - C3 ** 2)
Ev0 = E_lin(A_free, v0)
Evw = E_lin(A_free, vw)
check("B5.1", "closed form E(v0) = 3(al + 2 be)", zc(Ev0 - 3 * (al + 2 * be)))
check("B5.2", "closed form E(vw) = 3(al - be) + 3*sqrt(3)*ga*i",
      zc(Evw - (3 * (al - be) + 3 * sqrt(3) * ga * I)))
# normalization-invariant channel values (E divided by the norm-squared) and their Jacobian
mu0 = sp.simplify(Ev0 / herm(v0, v0))
muw = sp.simplify(Evw / herm(vw, vw))
Jchan = Matrix([mu0, sp.re(muw), sp.im(muw)]).jacobian([al, be, ga])
check("B5.3", "channel-value map (al,be,ga)->(mu0, Re mu_w, Im mu_w) has determinant -3*sqrt(3)",
      zc(Jchan.det() + 3 * sqrt(3)))
# antilinear singlet freedom: F_B(v0) = v0^T A v0, real for real A, surjective onto R
t = symbols("t", real=True)
check("B5.4", "antilinear singlet value F_B(v0) = v0^T A v0 is real and reaches every real t (A = t E11)",
      zc(F_anti(A_real, v0) - bil(v0, A_real * v0))
      and zc(sp.im(F_anti(A_real, v0)))
      and zc(F_anti(t * E11, v0) - t))
check("B5.5", "orientation swap on linear escape: values 3*i*sqrt(3) and -3*i*sqrt(3) are conjugate partners",
      zc(E_lin(Awit, vwb) - conjugate(E_lin(Awit, vw)))
      and zc(E_lin(Awit, vw) + E_lin(Awit, vwb)))
# A -> conj(A) sends the (9,0) escape to the (0,9) mirror and back
check("B5.6", "orientation swap A->conj(A) sends escape (9,0) to (0,9)",
      zc(F_anti(A_esc.conjugate(), vw)) and zc(F_anti(A_esc.conjugate(), vwb) - 9))
check("B5.7", "orientation swap A->conj(A) sends mirror (0,9) to (9,0)",
      zc(F_anti(A_mir.conjugate(), vw) - 9) and zc(F_anti(A_mir.conjugate(), vwb)))
check("B5.8", "no class condition references the sign of i: real-A and span{I,C,C^2} are conj-closed",
      mz(A_real.conjugate() - Matrix(3, 3, [ar[k] for k in range(9)]))
      and mz(A_span.conjugate() - (conjugate(a) * eye(3) + conjugate(b) * C3 + conjugate(c) * C3 ** 2)))
# joint relabeling w <-> conj(w) swaps the doublet vectors
vw_sub = vw.subs(sqrt(3), -sqrt(3))
check("B5.9", "joint relabeling w <-> conj(w) swaps vw <-> vwb",
      mz(sp.expand_complex(vw_sub) - vwb))

# ===========================================================================
# B6 - T6 lattice delivery on the landed 4^3 staggered surface (exact integers)
# ===========================================================================
L = 4
N = 64


def idx(x1, x2, x3):
    return (x1 * L + x2) * L + x3


def eta(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0])
    return (-1) ** (x[0] + x[1])


D2 = np.zeros((N, N), dtype=np.int64)
Vnp = np.zeros((N, 3), dtype=np.int64)
URnp = np.zeros((N, N), dtype=np.int64)
for x1 in range(L):
    for x2 in range(L):
        for x3 in range(L):
            x = (x1, x2, x3)
            aidx = idx(*x)
            for mu, d in ((0, (1, 0, 0)), (1, (0, 1, 0)), (2, (0, 0, 1))):
                xp = ((x[0] + d[0]) % L, (x[1] + d[1]) % L, (x[2] + d[2]) % L)
                xm = ((x[0] - d[0]) % L, (x[1] - d[1]) % L, (x[2] - d[2]) % L)
                D2[aidx, idx(*xp)] += eta(mu, x)
                D2[aidx, idx(*xm)] -= eta(mu, x)
            for mu in range(3):
                Vnp[aidx, mu] = (-1) ** x[mu]
            xr = (x[1], x[2], x[0])
            URnp[aidx, idx(*xr)] = 1

Cint = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=np.int64)
Ident64 = np.eye(N, dtype=np.int64)

check("B6.1", "staggered D2 is an integer antisymmetric matrix with entries in {-1,0,1}",
      np.array_equal(D2, -D2.T) and set(np.unique(D2)).issubset({-1, 0, 1}))
check("B6.2", "staggered operator exact rank D2 = 56", sp.Matrix(D2.tolist()).rank() == 56)
check("B6.3", "hw=1 triplet overlap V64^T V64 = 64 I_3", np.array_equal(Vnp.T @ Vnp, 64 * np.eye(3, dtype=np.int64)))
check("B6.4", "hw=1 triplet lies in the kernel D2 @ V64 = 0", np.array_equal(D2 @ Vnp, np.zeros((N, 3), dtype=np.int64)))
check("B6.5", "rotation UR is a permutation (UR^T UR = I_64, UR^3 = I_64)",
      np.array_equal(URnp.T @ URnp, Ident64) and np.array_equal(URnp @ URnp @ URnp, Ident64))
check("B6.6", "rotation intertwines the carrier UR @ V64 = V64 @ C", np.array_equal(URnp @ Vnp, Vnp @ Cint))

# nine elementary deliveries compress with scale 4096 = 64^2
comp_ok = True
for i in range(3):
    for j in range(3):
        Eij = np.zeros((3, 3), dtype=np.int64)
        Eij[i, j] = 1
        A_amb = Vnp @ Eij @ Vnp.T
        comp = Vnp.T @ A_amb @ Vnp
        ok_ij = np.array_equal(comp, 4096 * Eij)
        comp_ok = comp_ok and ok_ij
        check(f"B6.{7 + 3 * i + j}", f"elementary delivery E_{i}{j} compresses to 4096 * E_{i}{j} (4096 = 64^2)", ok_ij)

# symbolic delivery layer built on the exact integer carrier lift V64
Vs = Matrix(Vnp.tolist())


def amb_lin_E(Acar, z):
    psiv = Vs * z
    applied = Vs * (Acar * (Vs.T * psiv))
    return (psiv.H * applied)[0, 0]


def amb_anti_F(Acar, z):
    psiv = Vs * z
    applied = Vs * (Acar.conjugate() * (Vs.T * psiv.conjugate()))
    return (psiv.H * applied)[0, 0]


check("B6.16", "conjugation commutes with the lift: conj(V64 z) = V64 conj(z)",
      mz((Vs * vw).conjugate() - Vs * vw.conjugate()))
check("B6.17", "delivered doublet norm |V64 vw|^2 = 192 = 64 * 3",
      zc(herm(Vs * vw, Vs * vw) - 192) and 192 == 64 * 3)
check("B6.18", "delivered linear escape W = V64 (C - C^2) V64^T gives E(psi_w) = 4096 * 3 * i * sqrt(3)",
      zc(amb_lin_E(C3 - C3 ** 2, vw) - 4096 * 3 * I * sqrt(3)))
check("B6.19", "delivered conjugate-values law E(conj psi_w) = conj(E(psi_w))",
      zc(amb_lin_E(C3 - C3 ** 2, vwb) - conjugate(amb_lin_E(C3 - C3 ** 2, vw))))
A_amb_eq = 2 * eye(3) - C3 + 5 * C3 ** 2
check("B6.20", "delivered equivariant antilinear is doublet-null and gives F(psi_0) = 4096*3*(2-1+5)",
      zc(amb_anti_F(A_amb_eq, vw)) and zc(amb_anti_F(A_amb_eq, vwb))
      and zc(amb_anti_F(A_amb_eq, v0) - 4096 * 3 * (2 - 1 + 5)))
check("B6.21", "delivered K-real antilinear compresses to 4096 * (carrier K-real face) on the doublet channel",
      zc(amb_anti_F(A_real, vw) - 4096 * F_anti(A_real, vw)))
check("B6.22", "delivered non-K-real witness V64 vwb vwb^T V64^T gives F(psi_w)=36864=4096*9, F(psi_wb)=0",
      zc(amb_anti_F(A_esc, vw) - 36864) and 36864 == 4096 * 9 and zc(amb_anti_F(A_esc, vwb)))
check("B6.23", "delivered class equals the carrier K-real class: V64^T V64 = 64 I forces the 4096 scale",
      np.array_equal(Vnp.T @ Vnp, 64 * np.eye(3, dtype=np.int64))
      and mz(Vs.T * Vs - 64 * eye(3)))

# ===========================================================================
# B7 - Negative controls (each must fire against a deliberately wrong object)
# ===========================================================================
check("B7.1", "rejector fires: F_B(vw) = 1 is nonzero where the equivariant class is null",
      not zc(F_anti(E11, vw)))
check("B7.2", "non-K-real witnesses fail the K-reality membership test (conj A != A)",
      (not mz(A_esc.conjugate() - A_esc)) and (not mz(A_mir.conjugate() - A_mir)))
check("B7.3", "wrong-sign polarization is rejected: i(C - C^2) != +sqrt(3)(P_w - P_wb)",
      not mz(I * (C3 - C3 ** 2) - sqrt(3) * (P_w - P_wb)))
E00 = np.zeros((3, 3), dtype=np.int64)
E00[0, 0] = 1
check("B7.4", "wrong-scale compression is rejected: elementary delivery E_00 != 4095 * E_00",
      not np.array_equal(Vnp.T @ (Vnp @ E00 @ Vnp.T) @ Vnp, 4095 * E00))
check("B7.5", "transpose-convention rotation fails delivery: UR^T @ V64 = V64 @ C^2 != V64 @ C",
      np.array_equal(URnp.T @ Vnp, Vnp @ (Cint @ Cint))
      and not np.array_equal(URnp.T @ Vnp, Vnp @ Cint))
check("B7.6", "wrong doublet chirality is rejected: C vw != conj(w) vw",
      not mz(C3 * vw - conjugate(w) * vw))

# ===========================================================================
# B8 - Verbatim dependency quotes (8) + ledger shard existence (4)
# ===========================================================================
Q1 = ("Antilinear and non-Hermitian functionals, interacting extensions, and "
      "lattice-wide readouts are untested and outside the claim.")
Q2 = ("Further paths include classifying antilinear and non-Hermitian functionals, "
      "extending beyond the free composed kernel, and deriving the corner surface "
      "at the mechanism-note origin.")
Q3 = ("Hardening: dropping equivariance entirely, every real symmetric operator has "
      "exactly equal expectation values on the two conjugate doublet lines.")
Q4 = ("`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`. `2D` is an "
      "integer antisymmetric matrix with entries in `{-1, 0, 1}`; its exact rank is `56`,")
Q5 = ("The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character projectors "
      "`P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for `chi in {1, w, conj(w)}`, "
      "`w = -1/2 + (sqrt(3)/2)*i`, and entrywise conjugation `K` in the canonical basis.")
Q5b = "**R2 — K-real derivable initial data.** Derivable initial data is K-real."
Q6 = ("the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and "
      "exchange every K-odd seed. The memo's live Qualification leaves the unfixed choice "
      "conditional/open.")
Q7 = ("Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
      "adjacency, standard translations, and proper cubic rotations about each site.")

flat_delivery = read_flat(DEP_DELIVERY)
flat_spectral = read_flat(DEP_SPECTRAL)
flat_mechanism = read_flat(DEP_MECHANISM)
flat_axioms = read_flat(DEP_AXIOMS)

check("B8.1", "quote Q1 (untested antilinear/non-Hermitian row) present in the delivery note",
      norm_ws(Q1) in flat_delivery)
check("B8.2", "quote Q2 (further-paths classification) present in the delivery note",
      norm_ws(Q2) in flat_delivery)
check("B8.3", "quote Q3 (hardening: equal doublet expectation values) present in the delivery note",
      norm_ws(Q3) in flat_delivery)
check("B8.4", "quote Q4 (Kawamoto-Smit phases and exact rank 56) present in the delivery note",
      norm_ws(Q4) in flat_delivery)
check("B8.5", "quote Q5 (corner carrier, character projectors, K) present in the spectral-pairing note",
      norm_ws(Q5) in flat_spectral)
check("B8.6", "quote Q5b (K-real derivable initial data) present in the spectral-pairing note",
      norm_ws(Q5b) in flat_spectral)
check("B8.7", "quote Q6 (entrywise-conjugate presentations, live Qualification) present in the mechanism note",
      norm_ws(Q6) in flat_mechanism)
check("B8.8", "quote Q7 (cubic lattice sites, proper cubic rotations) present in the axiom memo",
      norm_ws(Q7) in flat_axioms)
for k, rid in enumerate(LEDGER_RIDS):
    shard = ROOT / "docs" / "audit" / "data" / "ledger" / rid[:2] / f"{rid}.json"
    check(f"B8.{9 + k}", f"ledger shard exists for dependency {rid[:24]}...", shard.is_file())

# ===========================================================================
# B9 - Note hygiene for the paired note
# ===========================================================================
RAW = (ROOT / NOTE_REL).read_text(encoding="utf-8")
RAW_LOW = RAW.lower()

FORBID_CLOSING = ["only route", "last route", "exhaust", "closes the", "closed off",
                  "no other way", "final classification", "completes the classification"]
FORBID_AUDIT = ["retained", "audited", "will be audited", "audit grade", "unaudited"]
FORBID_UNLANDED = ["kernel-induced", "|g| = 96", "pr #5526"]
FORBID_META = ["preserve verbatim", "must be absent", "acceptance contract", "this spec", "the spec"]

check("B9.1", "note omits closing/over-claim language",
      all(p not in RAW_LOW for p in FORBID_CLOSING))
check("B9.2", "note omits audit-status language",
      all(p not in RAW_LOW for p in FORBID_AUDIT))
check("B9.3", "note omits unlanded-material references",
      all(p not in RAW_LOW for p in FORBID_UNLANDED))
check("B9.4", "note omits spec meta-language",
      all(p not in RAW_LOW for p in FORBID_META))

# no bare decimal literals (allow the dependency/runner/cache filenames and dates)
allow = [NOTE_REL, DEP_DELIVERY, DEP_SPECTRAL, DEP_MECHANISM, DEP_AXIOMS,
         "kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py",
         "kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.txt",
         REGISTRY_ID]
scrub = RAW
for s in allow:
    scrub = scrub.replace(s, " ")
scrub = re.sub(r"20\d\d-\d\d-\d\d", " ", scrub)
scrub = re.sub(r"20\d\d_\d\d_\d\d", " ", scrub)
check("B9.5", "note has no bare decimal literals", re.search(r"[0-9]\.[0-9]", scrub) is None)

# dependency markdown-link inventory == exactly the four dependency .md files
md_targets = re.findall(r"\]\(([^)]+\.md)\)", RAW)
expected_md = {
    "KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "MINIMAL_AXIOMS_2026-06-29.md",
}
check("B9.6", "note links exactly the four dependency markdown files",
      set(md_targets) == expected_md and len(md_targets) == 4)

# staggered gate note appears only as a backticked handle, never a markdown link
gate_handle = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03"
check("B9.7", "staggered gate note appears as a backticked handle and not as a markdown link",
      f"`{gate_handle}`" in RAW and f"{gate_handle}.md)" not in RAW and f"]({gate_handle}" not in RAW)

BOUNDARY = [
    ("This is a classification of named readout-functional faces on the supplied corner "
     "carrier and its landed lattice delivery, not a nonderivability, "
     "universal-degeneracy, or indistinguishability claim: the K-real non-Hermitian face "
     "already separates full complex values, and K-odd, non-K-real, or non-equivariant "
     "escapes remain explicit."),
    ("No orientation is selected: every statement is invariant under the joint relabeling "
     "`w <-> conj(w)`, and the mechanism note's two-model FLAG and live Qualification stand "
     "unchanged."),
    ("Nothing here forces, derives, or prefers any value of `r`: the classified functional "
     "values on the singlet and shared doublet channels remain free."),
    ("Lattice-wide readout on non-kernel states, superoperator and completely positive faces, "
     "and interacting extensions are untested here and are the next paths this opens."),
]
flat_note = norm_ws(RAW)
check("B9.8", "note carries all four required boundary sentences verbatim",
      all(norm_ws(s) in flat_note for s in BOUNDARY))
check("B9.9", "registry id appears exactly once in the note header",
      RAW.count(REGISTRY_ID) == 1)
check("B9.10", "note declares the bounded-theorem claim type and points at runner and cache",
      "bounded_theorem" in RAW
      and "kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py" in RAW
      and "logs/runner-cache/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.txt" in RAW)
check("B9.11", "note states the narrowed face-specific classification and its internal complex-value separation",
      "Hermitian linear `K`-real" in flat_note
      and "full complex values can differ" in flat_note
      and "antilinear equivariant (`K`-reality not required)" in flat_note
      and "not a universal degeneracy or indistinguishability claim" in flat_note)

# ===========================================================================
# Summary
# ===========================================================================
if FAILURES:
    print("FAILED CHECKS: " + ", ".join(FAILURES))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
