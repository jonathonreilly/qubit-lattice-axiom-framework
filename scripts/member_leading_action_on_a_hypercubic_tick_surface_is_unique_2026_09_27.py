#!/usr/bin/env python3
"""If the member's leading action respects the hypercubic tick surface, it is
unique: beta = -alpha and alpha = K/4 follow (a conditional classification of
leading symbols; the member's B4 and relabelling invariance are premises).

Object: a real quadratic form Q(h, k) in a symmetric 4x4 tensor h (the member's
field with its lapse h_00 and shift h_0i), homogeneous of degree two in the
4-momentum k: the dimension-4 part of any lattice action's small-k expansion,
in Euclidean form.

Symmetries compared:
- S3: the proper and improper cubic group of the three space axes, with time
  reversal (the continuous-time / level-time surface the campaign uses);
- B4: the hyperoctahedral group of Z^4 (the hypercubic tick surface; the
  approved kinetic_isotropy_primitive supplies it for matter, and placing the
  member on it is an added premise);
- G: linearised relabellings h -> h + k xi^T + xi k^T (the member's gauge
  symmetry; block 112's closure is its lattice form).

Checks (exact rational arithmetic; invariant bases built as orbit sums):
A. S3-invariant forms: 26; of these G-invariant: 2.
B. B4-invariant forms: 9; of these G-invariant: 1.
C. The unique B4 x G form is proportional to the Euclidean Fierz-Pauli form
   (1/2) k^2 h.h - |h k|^2 + (k.h.k) tr h - (1/2) k^2 (tr h)^2, which is
   O(4)-invariant (exact).
D. 3+1 read-off in block 101's parametrisation
   L = [alpha tr(hdot^2) + beta (tr hdot)^2]/wbar + K wbar (u R1 + R2) - e u:
   every S3 x G form has beta/alpha = -1 (the closure ratio of block 112 is
   forced by the gauge symmetry alone) and a free transverse-traceless speed
   (K wbar^2/(4 alpha) arbitrary); the B4 x G form has TT speed 1, the speed
   every field has on that surface, i.e. K = 4 alpha at wbar = 1.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from fractions import Fraction as Fr

AUDIT_INPUT_PATHS = (
    'docs/IF_THE_MEMBERS_LEADING_ACTION_RESPECTS_THE_HYPERCUBIC_TICK_SURFACE_IT_IS_UNIQUE_BETA_EQUALS_MINUS_ALPHA_AND_ALPHA_EQUALS_K_OVER_FOUR_FOLLOW_BOUNDED_THEOREM_NOTE_2026-09-27.md',
    'docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
AUDIT_TIMEOUT_SEC = 600

import sympy as sp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


D = 4
# a form is a dict over canonical index tuples t = (m,n,r,s,a,b) of the coefficient of h_mn h_rs k_a k_b,
# canonicalised under m<->n, r<->s, a<->b and the pair swap (mn)<->(rs).


def canon(t):
    m, n, r, s, a, b = t
    p1, p2 = tuple(sorted((m, n))), tuple(sorted((r, s)))
    if p2 < p1:
        p1, p2 = p2, p1
    return p1 + p2 + tuple(sorted((a, b)))


ALL = sorted({canon(t) for t in itertools.product(range(D), repeat=6)})
INDEX = {t: i for i, t in enumerate(ALL)}


def signed_perms(space_only):
    out = []
    if space_only:
        for perm in itertools.permutations((1, 2, 3)):
            for signs in itertools.product((1, -1), repeat=4):
                out.append(((0,) + perm, signs))
    else:
        for perm in itertools.permutations(range(4)):
            for signs in itertools.product((1, -1), repeat=4):
                out.append((perm, signs))
    return out


def act(g, t):
    """Signed permutation g = (perm, signs): axis i -> perm[i] with sign signs[i]; returns (canonical image, sign)."""
    perm, signs = g
    img = tuple(perm[i] for i in t)
    sgn = 1
    for i in t:
        sgn *= signs[i]
    return canon(img), sgn


def invariant_basis(group):
    vecs = []
    seen = set()
    for t in ALL:
        if t in seen:
            continue
        orbit = {}
        for g in group:
            img, sgn = act(g, t)
            orbit[img] = orbit.get(img, 0) + sgn
        for img in orbit:
            seen.add(img)
        v = {k: c for k, c in orbit.items() if c != 0}
        if v:
            vecs.append(v)
    return vecs


def evaluate(v, h, k):
    """Q(h,k) for a form v given on canonical tuples: sum over all ordered index tuples of the symmetric tensor."""
    tot = 0
    for t, c in v.items():
        m, n, r, s, a, b = t
        # number of ordered tuples in the canonical class
        cls = {canon(u) for u in [t]}
        orbit = set()
        for (mm, nn) in ((m, n), (n, m)):
            for (rr, ss) in ((r, s), (s, r)):
                for (aa, bb) in ((a, b), (b, a)):
                    orbit.add((mm, nn, rr, ss, aa, bb)); orbit.add((rr, ss, mm, nn, aa, bb))
        term = 0
        for (mm, nn, rr, ss, aa, bb) in orbit:
            term += h[mm][nn] * h[rr][ss] * k[aa] * k[bb]
        tot += c * term / len(orbit)
    return tot


# symbolic h, k, xi
hs = sp.symbols('h0:10')
H = [[None] * 4 for _ in range(4)]
it = iter(hs)
for m in range(4):
    for n in range(m, 4):
        H[m][n] = H[n][m] = next(it)
ks = sp.symbols('k0:4')
xis = sp.symbols('x0:4')


def gauge_conditions(basis):
    """Coefficient matrix of Q(h + k xi^T + xi k^T) - Q(h) (bilinear part) in the basis coefficients."""
    dH = [[ks[m] * xis[n] + xis[m] * ks[n] for n in range(4)] for m in range(4)]
    rows = {}
    for j, v in enumerate(basis):
        # bilinear variation: Q(h+dh) - Q(h) - Q(dh) = 2 B(h, dh); require B(h, dh) = 0 and Q(dh) = 0
        HpD = [[H[m][n] + dH[m][n] for n in range(4)] for m in range(4)]
        var = sp.expand(evaluate(v, HpD, ks) - evaluate(v, H, ks))
        poly = sp.Poly(var, *hs, *ks, *xis)
        for mono, coef in poly.terms():
            rows.setdefault(mono, {})[j] = coef
    M = sp.zeros(len(rows), len(basis))
    for i, (mono, row) in enumerate(rows.items()):
        for j, c in row.items():
            M[i, j] = c
    return M


results = {}
for name, grp in (('S3', signed_perms(True)), ('B4', signed_perms(False))):
    basis = invariant_basis(grp)
    M = gauge_conditions(basis)
    null = M.nullspace()
    results[name] = (basis, null)

nS, nB = len(results['S3'][0]), len(results['B4'][0])
gS, gB = len(results['S3'][1]), len(results['B4'][1])
check("A: cubic group of space with time reversal: 26 invariant quadratic forms, 2 of them relabelling-invariant",
      nS == 26 and gS == 2, f"{nS} invariant, {gS} gauge-invariant")
check("B: hyperoctahedral group of Z^4: 9 invariant quadratic forms, exactly 1 relabelling-invariant", nB == 9 and gB == 1,
      f"{nB} invariant, {gB} gauge-invariant")


def combine(basis, coeffs):
    out = {}
    for v, c in zip(basis, coeffs):
        for t, x in v.items():
            out[t] = out.get(t, 0) + c * x
    return out


QB = combine(results['B4'][0], list(results['B4'][1][0]))
QB_expr = sp.expand(evaluate(QB, H, ks))
k2 = sum(x ** 2 for x in ks)
trh = sum(H[i][i] for i in range(4))
hk = [sum(H[i][j] * ks[j] for j in range(4)) for i in range(4)]
FP = sp.expand(sp.Rational(1, 2) * k2 * sum(H[i][j] ** 2 for i in range(4) for j in range(4))
               - sum(x ** 2 for x in hk) + sum(ks[i] * hk[i] for i in range(4)) * trh - sp.Rational(1, 2) * k2 * trh ** 2)
ratio = sp.simplify(QB_expr / FP)
check("C: the unique form is proportional to the Euclidean Fierz-Pauli (linearised Einstein) form, exactly "
      "(the constant only reflects the null vector's normalisation)", ratio.free_symbols == set(),
      f"Q_B4 / FP = {ratio}")
# O(4) invariance of FP under an exact rational rotation (Cayley transform of an antisymmetric integer matrix)
Aant = sp.Matrix([[0, 1, 2, 0], [-1, 0, 1, 3], [-2, -1, 0, 1], [0, -3, -1, 0]])
Rm = (sp.eye(4) - Aant) * (sp.eye(4) + Aant).inv()
Hm = sp.Matrix(H)
Hr = Rm * Hm * Rm.T
kr = Rm * sp.Matrix(ks)
FP_rot = FP.subs({**{H[i][j]: sp.Symbol(f'tmp{i}{j}') for i in range(4) for j in range(i, 4)}}, simultaneous=True)
sub_back = {sp.Symbol(f'tmp{i}{j}'): Hr[i, j] for i in range(4) for j in range(i, 4)}
sub_k = {ks[i]: kr[i] for i in range(4)}
FP_rot = sp.expand(FP_rot.subs(sub_k, simultaneous=True).subs(sub_back, simultaneous=True))
check("C: spot check: Fierz-Pauli is invariant under an exact rational O(4) rotation (it is manifestly O(4)-invariant)",
      sp.simplify(FP_rot - FP) == 0, f"R orthogonal: {sp.simplify(Rm * Rm.T) == sp.eye(4)}")


def readoff(Q):
    """Block 101 read-off: spatial h only (h_0mu = 0).
    Kinetic: k = (k0,0,0,0): Q = k0^2 [A sum_ij h_ij^2 + Bt (tr h)^2] -> beta/alpha = Bt/A.
    TT speed^2 (Minkowski) = (spatial-gradient coefficient)/(time coefficient) for h_12 with p along axis 3."""
    Z = sp.Symbol('Z')
    def val(hdict, k):
        Hn = [[0] * 4 for _ in range(4)]
        for (i, j), x in hdict.items():
            Hn[i][j] = Hn[j][i] = x
        return sp.nsimplify(evaluate(Q, Hn, k))
    f1 = val({(1, 2): 1}, (1, 0, 0, 0))       # sum h^2 = 2, tr = 0
    f2 = val({(1, 1): 1}, (1, 0, 0, 0))       # sum h^2 = 1, tr = 1
    A = f1 / 2
    Bt = f2 - A
    g = val({(1, 2): 1}, (0, 0, 0, 1)) / 2
    return sp.simplify(Bt / A), sp.simplify(g / A)


ro_B = readoff(QB)
basisS, nullS = results['S3']
ro_S = [readoff(combine(basisS, list(v))) for v in nullS]
a_, b_ = sp.symbols('a b')
gen = combine(basisS, list(a_ * nullS[0] + b_ * nullS[1]))
ro_gen = readoff(gen)
check("D: every relabelling-invariant form with a kinetic part on the space-cubic surface has beta/alpha = -1 "
      "(block 112's closure ratio), with a free transverse-traceless speed",
      sp.simplify(ro_gen[0] + 1) == 0 and len(ro_gen[1].free_symbols) > 0,
      f"general combination a v0 + b v1 (one basis form is potential-only): beta/alpha = {sp.simplify(ro_gen[0])}, "
      f"TT speed^2 = {sp.simplify(ro_gen[1])}")
check("D: on the hypercubic surface the unique form has beta/alpha = -1 and TT speed^2 = 1: K = 4 alpha at wbar = 1",
      ro_B[0] == -1 and ro_B[1] == 1, f"beta/alpha = {ro_B[0]}, TT speed^2 = {ro_B[1]}")

# ---------------------------------------------------------------- E proper rotations only (the axioms name proper rotations)
from sympy.combinatorics import Permutation


def proper_elems(space_only, with_T=True):
    out = []
    for g in signed_perms(space_only):
        perm, signs = g
        if space_only:
            det = Permutation([q - 1 for q in perm[1:]]).signature() * signs[1] * signs[2] * signs[3]
            if not with_T and signs[0] == -1:
                continue
        else:
            det = Permutation(list(perm)).signature() * signs[0] * signs[1] * signs[2] * signs[3]
        if det > 0:
            out.append(g)
    return out


rowsE = []
for label, grp in (('space proper rotations with time reversal', proper_elems(True, True)),
                   ('space proper rotations without time reversal', proper_elems(True, False)),
                   ('proper hyperoctahedral group of Z^4', proper_elems(False))):
    bE = invariant_basis(grp)
    rowsE.append((label, len(grp), len(bE), len(gauge_conditions(bE).nullspace())))
check("E: with proper rotations only (as the axioms name them) the counts are unchanged: 2 relabelling-invariant forms "
      "with space rotations, 1 with the proper group of Z^4",
      [r[3] for r in rowsE] == [2, 2, 1], "; ".join(f"{l} ({n} elements): {i} invariant, {g} gauge-invariant" for l, n, i, g in rowsE))

print('per_element: every count and read-off is exact rational arithmetic.')
print('per_site: not applicable.')
print('per_mode: the forms are momentum-space symbols of the dimension-4 part of a lattice action.')
print('per_block: not applicable.')
print('lattice_wide: checked and not executed - nonlinear (interacting) lattice relabelling invariance is not treated.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
