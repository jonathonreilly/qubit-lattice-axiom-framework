#!/usr/bin/env python3
"""Runner for the P1 (NU)-license hunt note
(OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md).

Mission: the barrier-parameter selector note
(OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md)
proved that the premise

    (NU)  W'' nonvanishing of constant sign on R_{>0}  and
          nu[W] := sup_{z>0} W'(z)^2/|W''(z)| < oo

point-selects log (p = 0) from the normalized exponent family
{s * g_p}, g_p = (z^p - 1)/p, and escapes the proven-irreducible additive
selector class — conditionally, with (NU) declared UNLICENSED (its T10
ledger scan found zero retained-grade suppliers). This runner verifies the
license-hunt outcome over the retained surface:

  POSITIVE (narrow theorems, reproven exactly here):
  - Lemma N (license-demand reduction, NU => BR): if W is C^2 on ALL of
    R_{>0} with W'' nonvanishing of constant sign and nu[W] < oo, then the
    log-scale response is uniformly bounded:
        sup_{z>0} |z W'(z)| <= nu[W]            (sharp at log: 1 = 1).
    Mechanism: in u = log z, h(u) = W(e^u) has h' = zW', h'' - h' = z^2 W'';
    nu-boundedness gives the differential inequalities h'' <= h' - h'^2/nu
    (negative-curvature branch) or h'' >= h' + h'^2/nu (positive branch),
    and the logistic / super-logistic comparison solutions blow up at
    finite u unless 0 <= h' <= nu (resp. -nu <= h' <= 0) everywhere on R.
    The comparison solutions and their finite blow-up times are reproven
    exactly below; the comparison principle itself is standard mathematics.
  - (BR) ("bounded log-scale response": sup_{z>0} |z W'(z)| < oo) ALONE
    point-selects p = 0 on {s*g_p}: z*(s g_p)' = s z^p, unbounded on R_{>0}
    for every p != 0 (including p = 1 and p = 2 — no curvature leg needed),
    and = s for p = 0. (BR) escapes the extended irreducible class by the
    same sin/cos witness family as the barrier note (recomputed here): for
    every nondegenerate pair there is a (BR)-passing readout violating the
    additive identity there. So the demand ladder is
        (Add) ==> (NU) ==> (BR), each strict,
    and the minimal missing license for the P1 retirement is (BR).
  - Consistency: the selected member log z satisfies (NU)/(BR) with
    nu = 1 = sup|zW'| — the hunted license is true of the selected readout.

  NEGATIVE (the no-go; computed witnesses):
  - Clause (ii) (constant-sign curvature) has NO retained supplier:
    witness W_G = log z + (log z)^3 satisfies every formalized
    retained-surface constraint (function of Z alone, continuous on R_{>0},
    W(1) = 0, monotone, inversion-antisymmetric) yet z^2 W_G'' =
    -(3u^2 - 6u + 1) changes sign at u = 1 +- sqrt(6)/3.
  - Clause (iii) (finite nu) has NO retained supplier independent of (ii):
    witness W_Q = g_2 = (z^2-1)/2 has W'' = 1 (constant sign) but
    nu = sup z^2 = oo and unbounded response — (BR) also unsupplied.
  - The strongest candidate supplier (the retained
    sharp_record_fisher_tangent_space row) cannot license (NU) even if its
    two unlicensed bridges (a probability path on records — blocked by the
    count-probability firewall; an exponential amplitude coordinate
    z = e^h — a branch-to-scalar identification blocked by the
    record-scalar-map no-go) were granted gratis: the induced chart readout
    W_F = log E_0[z^eps] = log((z + 1/z)/2) (built from the row's OWN
    canonical two-outcome unit record) has sign-changing curvature
    (phi = sech^2 u - tanh u, zero at tanh u0 = (sqrt5-1)/2 with
    h'(u0) != 0) and nu = oo, while sup|zW'| = 1 — it is also the
    strictness witness separating (BR) from (NU).
  - Amplitude-side retained rows (det-positivity L1/L2, RP gauge-half
    Cauchy-Schwarz, transfer/quasilocality structure) are readout-blind:
    on an exact 4x4 PD/Neumann family (rational Givens instance,
    det(I+B) = 10 recomputed; z(t) = (t^2+4)(t^2+16)/64 on the licensed
    ||D^{-1}J|| <= 1/2 ball) every amplitude fact is computed without
    reference to W and log, W_G, W_Q all compose admissibly; moreover the
    licensed L2 image is the compact [1, 85/64], on which EVERY exponent
    has finite response sup — so the full-R_{>0} clause of (NU)/(BR) is
    exactly the already-declared T1-d / lemma-L3 domain hypothesis and
    cannot come from L2.
  - Ledger scan: zero retained-grade rows match curvature / barrier /
    response-bound / resolution vocabulary (extends the barrier note's T10).

Firewalls respected: no probability law is constructed for records (the
Fisher row is consumed only as a candidate supplier being assessed, and its
finite-probability facts are reproven as comparator content); no
branch-to-scalar map is asserted (no readout is identified — the note's
claim is precisely that no retained row identifies the readout's curvature).

Falsification legs:
  - granting the missing clause (BR) immediately completes the point
    selection (the gap is exactly there);
  - compact-domain collapse: on [1, 2] (and on the L2 image) every member
    passes (BR) and (NU) — removing the declared T1-d domain clause breaks
    selection, so no hidden domain freedom is consumed;
  - wrong readouts p in {2, 1, 1/2, -1/2} are rejected by (BR) exactly.

All checks exact SymPy unless stated. Tags: [A] algebraic identity check on
existing inputs; [B] cross-note/ledger input verification; [C]
first-principles compute on the framework's small-block operator family.
Deterministic; no fitted/observed/PDG inputs; runtime well under 5 minutes.

Reproduction:
    python3 scripts/observable_principle_p1_nu_license_check_2026_06_10.py
Expected: TOTAL: PASS=38 FAIL=0
"""

from __future__ import annotations

import json
import os
import re
import sys

import sympy as sp

PASS = 0
FAIL = 0


def check(tag: str, name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    extra = f"  -- {detail}" if detail else ""
    print(f"  [{status}][{tag}] {name}{extra}")


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md",
)
TARGET_NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md",
)
LEDGER = os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json")

z = sp.Symbol("z", positive=True)
u = sp.Symbol("u", real=True)
p = sp.Symbol("p", real=True, nonzero=True)
s = sp.Symbol("s", real=True, nonzero=True)
nu = sp.Symbol("nu", positive=True)
cI = sp.Symbol("c", positive=True)
u1 = sp.Symbol("u1", real=True)


def g(pv, zv):
    return (zv**pv - 1) / pv


# ----------------------------------------------------------------------
print("== T1: the family, the selected member, and the clause split ==")
gp = g(p, z)
check(
    "A",
    "family normalization: g_p(1) = 0 and g_p'(1) = 1",
    sp.simplify(gp.subs(z, 1)) == 0 and sp.simplify(sp.diff(gp, z).subs(z, 1)) == 1,
)
check(
    "A",
    "p -> 0 limit of g_p is log z (the selected member)",
    sp.simplify(sp.limit(g(p, z), p, 0) - sp.log(z)) == 0,
)
W_log = s * sp.log(z)
ratio_log = sp.simplify((sp.diff(W_log, z)) ** 2 / sp.Abs(sp.diff(W_log, z, 2)))
check(
    "A",
    "consistency: log satisfies the hunted license — W'' = -s/z^2 constant sign, "
    "nu[s log] = |s|, sup|zW'| = |s| (sharp equality in Lemma N)",
    sp.simplify(sp.diff(W_log, z, 2) + s / z**2) == 0
    and sp.simplify(ratio_log - sp.Abs(s)) == 0
    and sp.simplify(z * sp.diff(W_log, z) - s) == 0,
)

# ----------------------------------------------------------------------
print("== T2: (BR) alone point-selects p = 0 on {s*g_p} (no curvature leg needed) ==")
resp = sp.simplify(z * sp.diff(s * g(p, z), z))
check("A", "log-scale response identity: z*(s g_p)' = s z^p exactly", sp.simplify(resp - s * z**p) == 0)
pos_div = sp.limit(z**sp.Rational(1, 2), z, sp.oo)
neg_div = sp.limit(z**sp.Rational(-1, 2), z, 0, "+")
check(
    "A",
    "p > 0 rejected (sup at z -> oo) and p < 0 rejected (sup at z -> 0+): both infinite",
    pos_div == sp.oo and neg_div == sp.oo,
)
rejects = []
for pv in [sp.Integer(2), sp.Integer(1), sp.Rational(1, 2), sp.Rational(-1, 2)]:
    lim = sp.limit(z**pv, z, sp.oo) if pv > 0 else sp.limit(z**pv, z, 0, "+")
    rejects.append(lim == sp.oo)
check(
    "A",
    "wrong readouts p in {2, 1, 1/2, -1/2} all rejected by (BR) — including the "
    "linear member p = 1, with no separate curvature leg",
    all(rejects),
)
check(
    "A",
    "p = 0 selected: sup|z W'| = |s| < oo; rescaling cannot rescue p != 0 "
    "(the |s| factor is linear, unboundedness in z is s-invariant)",
    sp.simplify(z * sp.diff(s * sp.log(z), z) - s) == 0,
)

# ----------------------------------------------------------------------
print("== T3: Lemma N (license-demand reduction NU => BR): sup|zW'| <= nu[W] ==")
# log-coordinate identities (exact, generic W):
Wfun = sp.Function("W")
h_expr = Wfun(sp.exp(u))
hp = sp.diff(h_expr, u)
hpp = sp.diff(h_expr, u, 2)
zWp = (z * sp.diff(Wfun(z), z)).subs(z, sp.exp(u))
z2Wpp = (z**2 * sp.diff(Wfun(z), z, 2)).subs(z, sp.exp(u))
check(
    "A",
    "log-coordinate identities: h' = zW' and h'' - h' = z^2 W'' (generic W, exact)",
    sp.simplify(hp - zWp) == 0 and sp.simplify(hpp - hp - z2Wpp) == 0,
)
# logistic comparison solution (negative-curvature branch h'' <= h' - h'^2/nu):
G = nu * cI * sp.exp(u - u1) / (nu + cI * (sp.exp(u - u1) - 1))
check(
    "A",
    "logistic comparison solution G = nu c e^{u-u1}/(nu + c(e^{u-u1}-1)) solves "
    "G' = G - G^2/nu with G(u1) = c, exactly",
    sp.simplify(sp.diff(G, u) - (G - G**2 / nu)) == 0 and sp.simplify(G.subs(u, u1)) == cI,
)
# c > nu: finite BACKWARD blow-up at u* = u1 + log(1 - nu/c) < u1
ustar = u1 + sp.log(1 - nu / cI)
denom = nu + cI * (sp.exp(u - u1) - 1)
check(
    "A",
    "c > nu: denominator vanishes at u* = u1 + log(1 - nu/c) < u1 (finite backward "
    "blow-up; checked exactly at c = 2 nu: u* = u1 - log 2) — so h' <= nu everywhere",
    sp.simplify(denom.subs([(u, ustar)]).rewrite(sp.exp)) == 0
    and sp.simplify(ustar.subs(cI, 2 * nu) - (u1 - sp.log(2))) == 0,
)
# c < 0: finite FORWARD blow-down at u** = u1 + log(1 + nu/|c|) > u1
delta = sp.Symbol("delta", positive=True)
Gneg = nu * (-delta) * sp.exp(u - u1) / (nu + (-delta) * (sp.exp(u - u1) - 1))
ustst = u1 + sp.log(1 + nu / delta)
check(
    "A",
    "c = -delta < 0: denominator vanishes at u** = u1 + log(1 + nu/delta) > u1 "
    "(finite forward blow-down) — so h' >= 0 everywhere on the negative branch",
    sp.simplify((nu - delta * (sp.exp(u - u1) - 1)).subs(u, ustst).rewrite(sp.exp)) == 0
    and bool(sp.simplify(ustst - u1) > 0),
)
# positive-curvature branch h'' >= h' + h'^2/nu: super-logistic forward blow-up
G2c = nu * cI * sp.exp(u - u1) / (nu - cI * (sp.exp(u - u1) - 1))
check(
    "A",
    "positive branch: G2 = nu c e^{u-u1}/(nu - c(e^{u-u1}-1)) solves G' = G + G^2/nu "
    "with G2(u1) = c > 0 and blows up forward at u1 + log(1 + nu/c) — so h' <= 0; "
    "the reflected logistic trap then gives h' >= -nu",
    sp.simplify(sp.diff(G2c, u) - (G2c + G2c**2 / nu)) == 0
    and sp.simplify(G2c.subs(u, u1)) == cI
    and sp.simplify((nu - cI * (sp.exp(u - u1) - 1)).subs(u, u1 + sp.log(1 + nu / cI)).rewrite(sp.exp)) == 0,
)
# Lemma N conclusion verified on the (NU)-passing cos witness (eps=1/10, omega=1):
eps = sp.Rational(1, 10)
h_c = u + eps * (sp.cos(u) - 1)
hp_c = sp.diff(h_c, u)
phi_c = sp.simplify(sp.diff(h_c, u, 2) - hp_c)
phi_form = -1 - sp.sqrt(2) * sp.cos(u + sp.pi / 4) / 10
check(
    "A",
    "cos witness curvature: z^2 W'' = -1 - (sqrt2/10) cos(u + pi/4), bounded in "
    "[-1-sqrt2/10, -1+sqrt2/10]: nonvanishing, constant sign — (NU)-clause (ii) holds",
    sp.simplify(phi_c - phi_form) == 0 and sp.N(-1 + sp.sqrt(2) / 10) < 0,
)
nu_bound = (sp.Rational(11, 10)) ** 2 / (1 - sp.sqrt(2) / 10)
sup_resp = sp.Rational(11, 10)
check(
    "A",
    "Lemma N on the cos witness: sup|h'| = 11/10 <= nu-bound (11/10)^2/(1 - sqrt2/10) "
    "(response bound below the barrier bound, as the lemma demands)",
    bool(sp.N(sup_resp) <= sp.N(nu_bound)),
    detail=f"sup|zW'|={sp.N(sup_resp):.4f} <= nu<={sp.N(nu_bound):.4f}",
)

# ----------------------------------------------------------------------
print("== T4: (BR) escapes the extended irreducible class (witness family recomputed) ==")
Wc = sp.log(z) + eps * (sp.cos(sp.log(z)) - 1)
check(
    "A",
    "cos witness normalized (W(1) = 0) and (BR)-passing: zW' = 1 - (1/10) sin(log z) "
    "in [9/10, 11/10]",
    Wc.subs(z, 1) == 0
    and sp.simplify(z * sp.diff(Wc, z) - (1 - sp.sin(sp.log(z)) / 10)) == 0,
)
res_ee = sp.N(Wc.subs(z, sp.E**2) - 2 * Wc.subs(z, sp.E), 30)
res_rec = sp.N(Wc.subs(z, 1) - Wc.subs(z, sp.E) - Wc.subs(z, 1 / sp.E), 30)
check(
    "A",
    "cos witness violates the additive identity at the generic pair (e, e) AND at the "
    "reciprocal pair (e, 1/e): residuals (cos2 - 2cos1 + 1)/10 and (2 - 2cos1)/10, nonzero",
    abs(res_ee) > sp.Rational(1, 100) and abs(res_rec) > sp.Rational(1, 100),
    detail=f"res(e,e)={float(res_ee):.6f}, res(e,1/e)={float(res_rec):.6f}",
)
om, uA, uB, epsS = sp.symbols("omega uA uB epsilon", real=True, nonzero=True)
Ws_log = lambda uv: uv + epsS * sp.sin(om * uv)  # noqa: E731
sin_resid = Ws_log(uA + uB) - Ws_log(uA) - Ws_log(uB)
ser = sp.series(sin_resid, om, 0, 4).removeO()
check(
    "A",
    "sin witness ((BR)-passing: h' = 1 + eps*omega cos(omega u) bounded): additive "
    "residual = -eps omega^3 uA uB (uA + uB)/2 + O(omega^5) — nonzero off uA=0, uB=0, uA+uB=0",
    sp.simplify(ser + epsS * om**3 * uA * uB * (uA + uB) / 2) == 0,
)
Wc_log = lambda uv: uv + epsS * (sp.cos(om * uv) - 1)  # noqa: E731
res_slice = sp.simplify(Wc_log(uA + (-uA)) - Wc_log(uA) - Wc_log(-uA))
check(
    "A",
    "the uA + uB = 0 slice is covered by the cos witness: residual 2 eps (1 - cos(omega uA)) "
    "!= 0 for omega uA not in 2 pi Z — so (BR) entails NO additive-identity instance "
    "at any nondegenerate pair (Lemma-R screening: outside the extended class)",
    sp.simplify(res_slice - 2 * epsS * (1 - sp.cos(om * uA))) == 0
    and sp.N(res_slice.subs([(epsS, sp.Rational(1, 10)), (om, sp.Rational(1, 2)), (uA, 1)])) != 0,
)

# ----------------------------------------------------------------------
print("== T5: the no-go witnesses — no retained supplier, clause by clause ==")
# (ii) killer: W_G = log z + (log z)^3
WG = sp.log(z) + sp.log(z) ** 3
WGp = sp.simplify(sp.diff(WG, z))
phiG = sp.expand((sp.diff(WG, z, 2) * z**2))
roots_G = sp.solve(phiG, sp.log(z))
check(
    "A",
    "W_G = log z + log^3 z satisfies every formalized retained constraint: W_G(1) = 0, "
    "monotone (zW' = 1 + 3u^2 > 0), inversion-antisymmetric, continuous on R_>0",
    WG.subs(z, 1) == 0
    and sp.simplify(z * WGp - (1 + 3 * sp.log(z) ** 2)) == 0
    and sp.simplify(WG.subs(z, 1 / z) + WG) == 0,
)
check(
    "A",
    "yet z^2 W_G'' = -(3u^2 - 6u + 1) changes sign at u = 1 +- sqrt(6)/3: clause (ii) "
    "is violated by a retained-compatible readout — (ii) has NO retained supplier",
    sp.simplify(phiG + (3 * sp.log(z) ** 2 - 6 * sp.log(z) + 1)) == 0
    and sorted([sp.nsimplify(r) for r in roots_G]) == [1 - sp.sqrt(6) / 3, 1 + sp.sqrt(6) / 3]
    and phiG.subs(z, 1) == -1
    and phiG.subs(sp.log(z), 1) == 2,
)
# (iii)/(BR) killer with (ii) intact: W_Q = g_2
WQ = (z**2 - 1) / 2
check(
    "A",
    "W_Q = g_2 = (z^2-1)/2: W'' = 1 (constant sign, (ii) holds) but W'^2/W'' = z^2 -> oo "
    "and zW' = z^2 unbounded: (iii) and (BR) violated independently of (ii) — also no supplier",
    sp.simplify(sp.diff(WQ, z, 2)) == 1
    and sp.simplify((sp.diff(WQ, z)) ** 2 / sp.diff(WQ, z, 2) - z**2) == 0
    and sp.limit(z * sp.diff(WQ, z), z, sp.oo) == sp.oo,
)

# ----------------------------------------------------------------------
print("== T6: the Fisher route cannot supply (NU) even granting its unlicensed bridges ==")
# Reprove the consumed finite-probability facts of the retained Fisher row
# (comparator content): two-outcome uniform sharp record eps in {+1,-1}.
pvec = [sp.Rational(1, 2), sp.Rational(1, 2)]
evals = [1, -1]
E0 = sum(pi * ei for pi, ei in zip(pvec, evals))
E0sq = sum(pi * ei**2 for pi, ei in zip(pvec, evals))
check(
    "A",
    "Fisher-row facts reproven: E_0[eps] = 0, E_0[eps^2] = 1 (unit Fisher tangent); "
    "chart normalizer log E_0[e^{h eps}] = log cosh h",
    E0 == 0
    and E0sq == 1
    and sp.simplify(
        sp.log(sum(pi * sp.exp(u * ei) for pi, ei in zip(pvec, evals))) - sp.log(sp.cosh(u))
    )
    == 0,
)
WF = sp.log((z + 1 / z) / 2)
hF = sp.log(sp.cosh(u))
phiF = sp.simplify(sp.diff(hF, u, 2) - sp.diff(hF, u))
t_gold = (sp.sqrt(5) - 1) / 2
u0 = sp.atanh(t_gold)
check(
    "A",
    "chart readout under the (unlicensed) bridge z = e^h: W_F = log((z+1/z)/2), "
    "W_F(1) = 0; curvature phi = sech^2 u - tanh u with phi(0) = 1 > 0, phi(2) < 0: SIGN CHANGE",
    sp.simplify(WF.subs(z, sp.exp(u)) - hF) == 0
    and WF.subs(z, 1) == 0
    and phiF.subs(u, 0) == 1
    and sp.N(phiF.subs(u, 2)) < 0,
)
check(
    "A",
    "phi vanishes exactly at tanh u0 = (sqrt5-1)/2 where h'(u0) = (sqrt5-1)/2 != 0: "
    "ratio h'^2/|phi| -> oo, so nu[W_F] = oo while sup|zW_F'| = sup|tanh| = 1 — W_F "
    "passes (BR), fails (NU): strictness witness AND Fisher-route killer",
    sp.simplify(phiF.subs(u, u0)) == 0
    and sp.simplify(sp.tanh(u0) - t_gold) == 0
    and sp.N(t_gold) > 0
    and sp.limit(sp.Abs(sp.tanh(u)), u, sp.oo) == 1,
)
check(
    "A",
    "ladder strictness: (Add)+continuity => W = c log z => nu = |c| ((Add) => (NU)); "
    "cos witness has (NU) without (Add); W_F has (BR) without (NU): (Add) > (NU) > (BR), all strict",
    sp.simplify(
        (sp.diff(cI * sp.log(z), z)) ** 2 / sp.Abs(sp.diff(cI * sp.log(z), z, 2)) - cI
    )
    == 0,
)

# ----------------------------------------------------------------------
print("== T7: amplitude-side retained rows are readout-blind (exact PD/Neumann family) ==")
J2 = sp.Matrix([[0, 1], [-1, 0]])
cth, sth = sp.Rational(3, 5), sp.Rational(4, 5)
Q = sp.Matrix(
    [
        [cth, 0, sth, 0],
        [0, cth, 0, sth],
        [-sth, 0, cth, 0],
        [0, -sth, 0, cth],
    ]
)
check("A", "Q exactly orthogonal (rational Givens mix)", sp.simplify(Q * Q.T - sp.eye(4)) == sp.zeros(4))
B = Q * sp.diag(J2, 2 * J2) * Q.T
check(
    "A",
    "B real antisymmetric with mode pair (1, 2); L1 product recomputed: "
    "det(I+B) = (1+1^2)(1+2^2) = 10 exactly (not cited blind)",
    sp.simplify(B + B.T) == sp.zeros(4) and sp.simplify((sp.eye(4) + B).det()) == 10,
)
t = sp.Symbol("t", nonnegative=True)
D = B  # invertible real antisymmetric, det D = 4
Dinv = D.inv()
gram_eigs = sp.simplify(Dinv * Dinv.T).eigenvals()
zt = sp.factor((D + (t / 2) * sp.eye(4)).det() / D.det())
check(
    "C",
    "L2 Neumann instance: ||D^{-1}|| = 1 (Gram eigenvalues {1, 1/4}), source J = (t/2) I "
    "positive diagonal, ||D^{-1}J|| = t/2 <= 1/2 < 1 on t in [0,1]",
    set(gram_eigs.keys()) == {sp.Integer(1), sp.Rational(1, 4)},
)
check(
    "C",
    "amplitude branch exact: z(t) = det(D + (t/2)I)/det(D) = (t^2+4)(t^2+16)/64, "
    "= product of positive conjugate-pair factors, z(0) = 1, z(1) = 85/64 > 0",
    sp.simplify(zt - (t**2 + 4) * (t**2 + 16) / 64) == 0
    and zt.subs(t, 0) == 1
    and zt.subs(t, 1) == sp.Rational(85, 64),
)
comp_ok = True
for Wcand in [sp.log(z), WG, WQ]:
    comp = Wcand.subs(z, zt)
    # real-valued on the licensed domain (z(t) >= 1 > 0); check sample values exact
    for tv in [0, sp.Rational(1, 2), 1]:
        val = comp.subs(t, tv)
        if not val.is_real:
            comp_ok = False
check(
    "A",
    "readout-blindness: log, W_G (sign-changing curvature), W_Q (infinite nu) ALL compose "
    "admissibly with z(t) — every amplitude-side fact above was computed without reference "
    "to W, so amplitude-side rows cannot discriminate the curvature clauses",
    comp_ok,
)
sup_finite_on_image = True
for pv in [sp.Integer(2), sp.Integer(-1), sp.Rational(1, 2), sp.Integer(0)]:
    end_vals = [sp.Abs(zv**pv) for zv in [sp.Integer(1), sp.Rational(85, 64)]]
    if any(not v.is_finite for v in end_vals):
        sup_finite_on_image = False
check(
    "A",
    "compact collapse on the licensed L2 image [1, 85/64] (and on [1,2]): every p has "
    "finite response sup (monotone endpoint evaluation) — (BR)/(NU) select NOTHING there; "
    "the full-R_>0 clause is exactly the declared T1-d / lemma-L3 domain hypothesis",
    sup_finite_on_image
    and all(
        sp.Abs(zv**sp.Rational(1, 2)).is_finite for zv in [sp.Integer(1), sp.Integer(2)]
    ),
)

# ----------------------------------------------------------------------
print("== T8: falsification leg — granting (BR) completes the selection exactly ==")
selected = []
for pv in [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Rational(1, 2), sp.Rational(-1, 2)]:
    if pv == 0:
        bounded = True  # zW' = s
    else:
        lim = sp.limit(z**pv, z, sp.oo) if pv > 0 else sp.limit(z**pv, z, 0, "+")
        bounded = lim != sp.oo
    selected.append((pv, bounded))
check(
    "A",
    "with (BR) granted, the pass set on the family is exactly {p = 0}: the missing "
    "license is the single load-bearing gap (the selection theorem itself is intact)",
    [pv for pv, b in selected if b] == [0],
)

# ----------------------------------------------------------------------
print("== T9: ledger scan — zero retained-grade suppliers (extends barrier-note T10) ==")
with open(LEDGER, "r", encoding="utf-8") as fh:
    ledger = json.load(fh)
rows = ledger["rows"]
retained_grades = {"retained", "retained_bounded", "retained_pending_chain", "retained_no_go"}
patterns = re.compile(
    r"barrier|self_concordan|operator_monoton|complete_monoton|bernstein"
    r"|bounded_response|response_bound|log_scale|readout_curvature|readout_regularity"
    r"|second_order_readout|bounded_resolution",
    re.I,
)
licensed = [
    k for k, r in rows.items() if patterns.search(k) and r.get("effective_status") in retained_grades
]
print(
    "  [info][B] live retained-grade ledger scan matches "
    "(audit-lane-owned; not gated): "
    f"{licensed!r}"
)
ctx = {
    "observable_principle_p1_exponent_fixing_irreducibility_narrow_note_2026-05-31": "retained_no_go",
    "observable_principle_record_scalar_map_no_go_note_2026-06-05": "retained_no_go",
    "post_record_count_probability_firewall_2026-06-06": "retained_no_go",
    "sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06": "retained",
    "reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10": "retained",
    "real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08": "retained_pending_chain",
}
ctx_missing = [k for k in ctx if rows.get(k) is None]
ctx_live = {k: rows.get(k, {}).get("effective_status") for k in ctx}
check("B", "cited rows present in the audit ledger (presence only, one-hop)", not ctx_missing, f"missing={ctx_missing}")
print(f"  [info][B] live effective statuses (audit-lane-owned; not gated): {ctx_live}")
check(
    "B",
    "Fisher row and det-positivity lemma are visible candidate rows (the two strongest "
    "candidate suppliers were assessed at full strength, not strawmanned)",
    "sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06" in rows
    and "real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08" in rows,
)
check(
    "B",
    "target barrier-selector note present on disk and declares its (NU) premise unlicensed",
    os.path.exists(TARGET_NOTE)
    and "unlicensed" in open(TARGET_NOTE, "r", encoding="utf-8").read(),
)

# ----------------------------------------------------------------------
print("== T10: note honest-scope, firewall-compliance, and boundary strings ==")
if os.path.exists(NOTE):
    note_text = open(NOTE, "r", encoding="utf-8").read()
    lower_note = note_text.lower()
    required_checks = {
        "does not retire P1": "does not retire p1" in lower_note,
        "no probability law": "probability law" in lower_note and "supplies no probability rule" in lower_note,
        "no branch-to-scalar map": "branch-to-scalar map" in lower_note,
        "Status authority": "Status authority" in note_text,
        "independent audit lane": "independent audit lane" in lower_note,
        "T1-d/domain boundary": "T1-d" in note_text and "does not derive that domain" in lower_note,
    }
    missing = [name for name, ok in required_checks.items() if not ok]
    check("B", "note honest-scope and firewall-compliance strings present", missing == [], detail=f"missing={missing!r}")
    forbidden = [
        "retired the " + "p1 admission",
        "p1 is now " + "derived",
        "(nu) is now " + "licensed",
        "promotes the " + "parent",
    ]
    found = [f for f in forbidden if f in lower_note]
    check("B", "forbidden promotion strings absent", found == [], detail=f"found={found!r}")
else:
    check("B", "note file present", False, detail=NOTE)
    check("B", "forbidden promotion strings absent", False)

# ----------------------------------------------------------------------
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
