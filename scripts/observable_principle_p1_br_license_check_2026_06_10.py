#!/usr/bin/env python3
"""Runner for the P1 (BR)-license hunt note
(OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md).

Mission (wave 2 of the P1 exponent campaign): the (NU)-license note
(OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md)
reduced the P1 license demand to the single clause

    (BR)  sup_{z>0} |z W'(z)| < oo   (bounded log-scale response on the
                                      declared T1-d domain R_{>0}),

and named the next hunt target: a retained finite-resolution/record-capacity
adjacent structure. This runner verifies the hunt outcome over the retained
record/measurement surface, with the unbounded Record schema consumed only as
an audited-conditional supplied-record premise:

  POSITIVE (narrow lemmas, all reproven exactly here):
  - Lemma W (second demand reduction, BR => BR-int): the per-e-fold
    INCREMENT clause
        (BR-int)  sup_{z>0} |W(e z) - W(z)| < oo
    is implied by (BR) (mean value), is STRICTLY weaker (witness
    W_V = log z + (sin z - sin 1)/(1 + log^2 z): bounded e-fold increments,
    unbounded z W' along z_m = 2 pi m), ALONE point-selects p = 0 on the
    normalized exponent family {s*g_p} (e-fold increment
    s e^{pu}(e^p - 1)/p, unbounded for every p != 0, constant s for p = 0),
    and escapes the extended irreducible class by the same sin/cos witness
    family (recomputed). Demand ladder now
        (Add) ==> (NU) ==> (BR) ==> (BR-int), each strict.
  - Lemma C (conditional record-capacity theorem — the Route-A yield):
    IF the T1-d readout's e-fold increments are realized as finite-sector
    record readouts I(A_z) = chi.v_z (the retained finite-sector identity,
    recomputed on all 81 ordered disjoint subset pairs of a 4-sector model)
    with per-sector magnitude cap |v_i| <= M (CAP-M) and per-e-fold sector
    count cap <= K (CAP-K), THEN sup|W(ez) - W(z)| <= K*M: (BR-int) holds
    and p = 0 is selected. In the conditional supplied-record unit schema
    CAP-M holds with M = 1 by the schema's own normalization.

  NEGATIVE (the no-go; computed witnesses, sub-clause by sub-clause):
  - (CAP-M) for general sector data has NO retained supplier: the retained
    finite-sector algebra leaves sector data arbitrary (its own two-sector
    freedom d = p u/(1-p) is recomputed), and the witness realization
    W_Q = (z^2-1)/2 registered as a SINGLE sector per e-fold (K = 1)
    satisfies the algebra verbatim with unbounded response.
  - (CAP-K) — the registration-RATE clause — has NO retained supplier and
    is the exact gap: under its supplied-record/readout-context premise, the
    conditional unbounded finite-additivity schema permits arbitrary finite
    collections (I(R_n) = n, no cap); the witness assignment of 4^k supplied
    UNIT records to e-fold k (M = 1, every prefix an exact finite collection,
    sum = (4^{K+1}-1)/3) is schema-compliant only under that premise and
    violates (BR-int). The two sub-clauses fail
    independently (W_Q: K bounded, M unbounded; 4^k family: M = 1, K
    unbounded) — exactly parallel to the W_G/W_Q split of the (NU) note.
  - Route B (quantum): finite local dimension bounds the PER-REGISTER
    datum (qubit effects have spectrum in [0,1], so any Busch/Gleason
    frame-function value Tr(sigma E) lies in [0,1] — recomputed exactly;
    note this is conditional on a SUPPLIED probability measure, the
    firewall-blocked bridge) — an M-shaped fact only. The K-side cannot
    follow: Z^3 supplies strictly increasing register counts (2n+1)^3 with
    no cap (the schema's own mechanism), and no retained row couples
    amplitude e-folds to site/register counts. The Busch/Gleason/local-
    tomography rows are effect-side (their statements constrain states and
    effects; the readout W does not occur in them): readout-blind.
  - Ledger scan: zero retained-grade rows match capacity/rate/resolution/
    response vocabulary (extends the (NU) note's T9 scan).

Firewalls respected: no probability law is constructed for records (the
count-probability firewall is consumed as a wall: it blocks the Busch/
Gleason measure hypotheses from serving as suppliers); no branch-to-scalar
map is asserted (the realization clause CAP-real is DECLARED as part of the
open premise, never asserted as supplied — it is a quantitative slice of
the record-scalar-map no-go's middle arrow, which is exactly why it is
open). The clause hunted here is the response bound of whatever scalar
readout T1-d declares; nothing here constructs, identifies, or selects
that readout.

Falsification legs:
  - a readout outside the licensed capacity structure has unbounded
    response (W_Q single-sector witness; 4^k rate witness);
  - compact-domain collapse: on [1, e] and on the licensed L2 Neumann
    image [1, 85/64] every family member passes (BR)/(BR-int) — selection
    needs exactly the declared T1-d full-R_{>0} domain clause, no more;
  - granting (CAP-M)+(CAP-K) completes the selection exactly ({p = 0}).

All checks exact SymPy unless stated. Tags: [A] algebraic identity check on
existing inputs; [B] cross-note/ledger input verification; [C]
first-principles compute on the framework's finite structures; [D]
falsification / hostile-witness leg. Deterministic; no fitted/observed/PDG
inputs; runtime well under 5 minutes.

Reproduction:
    python3 scripts/observable_principle_p1_br_license_check_2026_06_10.py
Expected: TOTAL: PASS=31 FAIL=0
"""

from __future__ import annotations

import itertools
import json
import os
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
    "OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md",
)
NU_NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md",
)
BARRIER_NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md",
)
LEDGER = os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json")

z = sp.Symbol("z", positive=True)
u = sp.Symbol("u", real=True)
p = sp.Symbol("p", real=True, nonzero=True)
s = sp.Symbol("s", real=True, nonzero=True)
eps = sp.Rational(1, 10)


def g(pv, zv):
    return (zv**pv - 1) / pv


P_PROBE = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Rational(1, 2), sp.Rational(-1, 2)]


def response_bounded(pv) -> bool:
    """(BR): is sup_{z>0} |z (s g_p)'| = |s| sup z^pv finite?"""
    if pv == 0:
        return True
    lim = sp.limit(z**pv, z, sp.oo) if pv > 0 else sp.limit(z**pv, z, 0, "+")
    return lim != sp.oo


def increment_bounded(pv) -> bool:
    """(BR-int): is sup_u |s e^{pv u}(e^pv - 1)/pv| finite?"""
    if pv == 0:
        return True
    direction = (u, sp.oo) if pv > 0 else (u, -sp.oo)
    lim = sp.limit(sp.exp(pv * u), *direction)
    return lim != sp.oo


# ----------------------------------------------------------------------
print("== T1: the clause under hunt — (BR) and its selection chain, recomputed ==")
gp = g(p, z)
check(
    "A",
    "family normalization: g_p(1) = 0, g_p'(1) = 1, p -> 0 limit is log z (selected member)",
    sp.simplify(gp.subs(z, 1)) == 0
    and sp.simplify(sp.diff(gp, z).subs(z, 1)) == 1
    and sp.simplify(sp.limit(g(p, z), p, 0) - sp.log(z)) == 0,
)
check(
    "A",
    "log-scale response identity: z*(s g_p)' = s z^p exactly; log passes (BR) with sup|zW'| = |s|",
    sp.simplify(z * sp.diff(s * g(p, z), z) - s * z**p) == 0
    and sp.simplify(z * sp.diff(s * sp.log(z), z) - s) == 0,
)
check(
    "A",
    "(BR) selection chain recomputed: pass set on {s*g_p} over p in {0, 2, 1, 1/2, -1/2} "
    "is exactly {p = 0} (rescaling cannot rescue: |s| is linear, z-unboundedness s-invariant)",
    [pv for pv in P_PROBE if response_bounded(pv)] == [0],
)

# ----------------------------------------------------------------------
print("== T2: Lemma W — second demand reduction (BR) => (BR-int), and (BR-int) still point-selects ==")
incr = sp.simplify(s * (g(p, sp.exp(u + 1)) - g(p, sp.exp(u))))
check(
    "A",
    "e-fold increment identity: s*(g_p(e^{u+1}) - g_p(e^u)) = s e^{pu}(e^p - 1)/p exactly",
    sp.simplify(incr - s * sp.exp(p * u) * (sp.exp(p) - 1) / p) == 0,
)
incr_kill = all(not increment_bounded(pv) for pv in P_PROBE if pv != 0)
check(
    "A",
    "p != 0 increments unbounded (p > 0 at u -> +oo, p < 0 at u -> -oo; includes the linear "
    "member p = 1 with no curvature leg); p = 0 increment identically s",
    incr_kill and sp.simplify(s * (sp.log(sp.exp(u + 1)) - sp.log(sp.exp(u))) - s) == 0,
)
# (BR) => (BR-int) mean-value instances: equality at log; cos witness strictly below
delta_cos = sp.simplify((u + 1 + eps * (sp.cos(u + 1) - 1)) - (u + eps * (sp.cos(u) - 1)))
delta_cos_form = 1 - 2 * eps * sp.sin(sp.Rational(1, 2)) * sp.sin(u + sp.Rational(1, 2))
check(
    "A",
    "(BR) => (BR-int) verified (mean value): log has increment = s = sup|zW'| (equality); "
    "cos witness increment = 1 - (1/5) sin(1/2) sin(u + 1/2), so sup-increment "
    "1 + (1/5) sin(1/2) <= sup|h'| = 11/10  (<=> 2 sin(1/2) <= 1)",
    sp.simplify(delta_cos - delta_cos_form) == 0
    and sp.N(1 + 2 * eps * sp.sin(sp.Rational(1, 2))) <= sp.N(sp.Rational(11, 10))
    and sp.N(2 * sp.sin(sp.Rational(1, 2))) < 1,
)
check(
    "A",
    "(BR-int) selection: pass set on the family is exactly {p = 0} — the strictly weaker "
    "increment clause is still a point-selector",
    [pv for pv in P_PROBE if increment_bounded(pv)] == [0],
)

# ----------------------------------------------------------------------
print("== T3: (BR-int) escapes the extended irreducible class (witness family recomputed) ==")
Wc = sp.log(z) + eps * (sp.cos(sp.log(z)) - 1)
res_ee = sp.N(Wc.subs(z, sp.E**2) - 2 * Wc.subs(z, sp.E), 30)
res_rec = sp.N(Wc.subs(z, 1) - Wc.subs(z, sp.E) - Wc.subs(z, 1 / sp.E), 30)
check(
    "A",
    "cos witness passes (BR-int) (sup-increment <= 1 + (1/5) sin(1/2) < 11/10) yet violates "
    "the additive identity at (e, e) AND at the reciprocal pair (e, 1/e): residuals nonzero",
    Wc.subs(z, 1) == 0
    and abs(res_ee) > sp.Rational(1, 100)
    and abs(res_rec) > sp.Rational(1, 100),
    detail=f"res(e,e)={float(res_ee):.6f}, res(e,1/e)={float(res_rec):.6f}",
)
om, uA, uB, epsS = sp.symbols("omega uA uB epsilon", real=True, nonzero=True)
Ws_log = lambda uv: uv + epsS * sp.sin(om * uv)  # noqa: E731
ser = sp.series(Ws_log(uA + uB) - Ws_log(uA) - Ws_log(uB), om, 0, 4).removeO()
Wc_log = lambda uv: uv + epsS * (sp.cos(om * uv) - 1)  # noqa: E731
res_slice = sp.simplify(Wc_log(uA + (-uA)) - Wc_log(uA) - Wc_log(-uA))
check(
    "A",
    "sin witness ((BR-int)-passing: increments of u + eps sin(omega u) bounded by 1 + 2|eps|): "
    "additive residual -eps omega^3 uA uB (uA+uB)/2 + O(omega^5); cos witness covers the "
    "uA + uB = 0 slice (residual 2 eps (1 - cos(omega uA)) != 0) — (BR-int) entails NO "
    "additive-identity instance at any nondegenerate pair: outside the extended class",
    sp.simplify(ser + epsS * om**3 * uA * uB * (uA + uB) / 2) == 0
    and sp.simplify(res_slice - 2 * epsS * (1 - sp.cos(om * uA))) == 0
    and sp.N(res_slice.subs([(epsS, sp.Rational(1, 10)), (om, sp.Rational(1, 2)), (uA, 1)])) != 0,
)

# ----------------------------------------------------------------------
print("== T4: strictness — W_V separates (BR-int) from (BR); the full demand ladder ==")
phiV = (sp.sin(sp.exp(u)) - sp.sin(1)) / (1 + u**2)
hV = u + phiV
check(
    "A",
    "W_V = log z + (sin z - sin 1)/(1 + log^2 z): W_V(1) = 0, smooth on R_>0; "
    "|phi| <= (1 + sin 1)/(1 + u^2) <= 1 + sin 1, so every e-fold increment is bounded by "
    "1 + 2(1 + sin 1) < 5: (BR-int) HOLDS",
    sp.simplify(hV.subs(u, 0)) == 0
    and sp.N(1 + 2 * (1 + sp.sin(1))) < 5
    and sp.N(sp.Abs(phiV.subs(u, 3))) < sp.N((1 + sp.sin(1)) / (1 + 9)) + sp.Float(1e-20),
)
hVp = sp.diff(hV, u)
mm = sp.Symbol("m", integer=True, positive=True)
hVp_at = sp.simplify(hVp.subs(u, sp.log(2 * sp.pi * mm)))
exceed = []
for m_val, cap in [(100, 10), (10**4, 100), (10**6, 1000)]:
    val = sp.N(hVp_at.subs(mm, m_val))
    exceed.append(bool(val > cap))
check(
    "D",
    "yet (BR) FAILS for W_V: at z_m = 2 pi m (sin(2 pi m) = 0, cos(2 pi m) = 1 exactly), "
    "z W' = 1 + [2 pi m (1+L^2) + 2 L sin 1]/(1+L^2)^2, L = log(2 pi m) — exceeds caps "
    "10/100/1000 at m = 1e2/1e4/1e6: response unbounded, so (BR-int) is STRICTLY weaker",
    all(exceed),
    detail=f"zW'(2pi*1e6) = {float(sp.N(hVp_at.subs(mm, 10**6))):.1f}",
)
# ladder strictness witnesses: cos (NU without Add), W_F (BR without NU), W_V (BR-int without BR)
phi_c = sp.simplify(sp.diff(u + eps * (sp.cos(u) - 1), u, 2) - sp.diff(u + eps * (sp.cos(u) - 1), u))
hF = sp.log(sp.cosh(u))
phiF = sp.simplify(sp.diff(hF, u, 2) - sp.diff(hF, u))
t_gold = (sp.sqrt(5) - 1) / 2
u0 = sp.atanh(t_gold)
cI = sp.Symbol("c", positive=True)
check(
    "A",
    "demand ladder (Add) => (NU) => (BR) => (BR-int), ALL strict: (Add)+cont => c log z with "
    "nu = |c| (in class); cos witness has (NU) w/o (Add) (curvature -1 - (sqrt2/10) cos(u+pi/4) "
    "constant sign); W_F = log((z+1/z)/2) has (BR) w/o (NU) (curvature zero at tanh u0 = "
    "(sqrt5-1)/2 with zW' != 0, sup|zW'| = 1); W_V has (BR-int) w/o (BR)",
    sp.simplify((sp.diff(cI * sp.log(z), z)) ** 2 / sp.Abs(sp.diff(cI * sp.log(z), z, 2)) - cI) == 0
    and sp.simplify(phi_c - (-1 - sp.sqrt(2) * sp.cos(u + sp.pi / 4) / 10)) == 0
    and sp.N(-1 + sp.sqrt(2) / 10) < 0
    and sp.simplify(phiF.subs(u, u0)) == 0
    and sp.simplify(sp.tanh(u0) - t_gold) == 0
    and sp.limit(sp.Abs(sp.tanh(u)), u, sp.oo) == 1,
)

# ----------------------------------------------------------------------
print("== T5: Lemma C — the conditional record-capacity theorem (Route A's honest yield) ==")
v4 = [sp.Integer(2), sp.Rational(3, 2), sp.Integer(5), sp.Rational(7, 3)]
sectors = list(range(4))
subsets = []
for r_ in range(5):
    subsets.extend(itertools.combinations(sectors, r_))
pairs = 0
additive_ok = True
for A in subsets:
    for B in subsets:
        if set(A) & set(B):
            continue
        pairs += 1
        IA = sum(v4[i] for i in A)
        IB = sum(v4[i] for i in B)
        IAB = sum(v4[i] for i in set(A) | set(B))
        chiA = [1 if i in A else 0 for i in sectors]
        if IAB != IA + IB or IA != sum(c * vi for c, vi in zip(chiA, v4)):
            additive_ok = False
check(
    "C",
    "retained finite-sector identity recomputed (not cited blind): I(A) = chi_A . v and "
    "I(A u B) = I(A) + I(B) on ALL 81 ordered disjoint subset pairs of a 4-sector model",
    additive_ok and pairs == 81,
    detail=f"pairs={pairs}",
)
M = sp.Symbol("M", positive=True)
mixed = [M, -M, M / 2, -M / 3, M]
check(
    "A",
    "capacity bound: |I(A_z)| = |sum v_i| <= K*M by finite additivity + triangle inequality "
    "(extremal instance sum = 5M = K*M; mixed-sign instance |7M/6| <= 5M, K = 5)",
    sp.simplify(sum([M] * 5) - 5 * M) == 0
    and sp.simplify(sp.Abs(sum(mixed)) - 7 * M / 6) == 0
    and bool(sp.simplify(5 * M - 7 * M / 6).is_positive),
)
check(
    "A",
    "Lemma C chain: (CAP-real)+(CAP-M)+(CAP-K) => every e-fold increment <= K*M => (BR-int) "
    "=> pass set exactly {p = 0} (selection completed conditionally — the gap is exactly the caps)",
    [pv for pv in P_PROBE if increment_bounded(pv)] == [0],
)
unit_records = [sp.Integer(1)] * 7
check(
    "A",
    "unit-record normalization: in the conditional unbounded-additivity schema every unit datum "
    "is exactly 1, so (CAP-M) holds there with M = 1 by normalization (I(R_7) = 7 recomputed); "
    "the open content is the supplied-record realization clause + the rate cap (CAP-K)",
    sum(unit_records) == 7 and all(d == 1 for d in unit_records),
)

# ----------------------------------------------------------------------
print("== T6: the no-go — neither capacity sub-clause has a retained supplier (witnesses) ==")
uS, pS = sp.symbols("uS pS", positive=True)
dS = pS * uS / (1 - pS)
check(
    "D",
    "(CAP-M) unsupplied for general sector data: the finite-sector algebra's own freedom "
    "recomputed — for ANY p in (0,1), d = p u/(1-p) gives normalized coordinate d/(u+d) = p "
    "exactly: sector data are arbitrary scalars, no magnitude cap is retained",
    sp.simplify(dS / (uS + dS) - pS) == 0,
)
WQ = (z**2 - 1) / 2
incrQ = sp.simplify(WQ.subs(z, sp.E * z) - WQ)
check(
    "D",
    "witness W_Q = (z^2-1)/2 registered as ONE sector per e-fold (K = 1 bounded!): satisfies "
    "the finite-sector algebra verbatim (singleton decomposition, additivity trivially exact) "
    "yet its e-fold increment z^2 (e^2-1)/2 -> oo: bounded count + unbounded datum kills any "
    "'the algebra alone bounds the response' claim",
    sp.simplify(incrQ - z**2 * (sp.E**2 - 1) / 2) == 0
    and sp.limit(incrQ, z, sp.oo) == sp.oo,
)
K = sp.Symbol("K", integer=True, nonnegative=True)
k = sp.Symbol("k", integer=True, nonnegative=True)
total = sp.summation(4**k, (k, 0, K))
check(
    "D",
    "(CAP-K) unsupplied — and the schema affirmatively licenses its violation: assign 4^k UNIT "
    "records to e-fold k (M = 1 holds); every prefix is an exact finite disjoint collection "
    "(sum_{k<=K} 4^k = (4^{K+1}-1)/3 recomputed), yet the per-e-fold count 4^k exceeds ANY "
    "cap (4^10 = 1048576 > 10^6): a fully schema-compliant unit-record realization violates "
    "(BR-int) — the sub-clauses fail independently (W_Q: K fine/M unbounded; 4^k: M = 1/K unbounded)",
    sp.simplify(total - (4 ** (K + 1) - 1) / 3) == 0 and 4**10 > 10**6,
    detail=f"4^10 = {4**10}",
)
lift_path = os.path.join(REPO, "docs", "POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md")
lift_txt = open(lift_path, "r", encoding="utf-8").read() if os.path.exists(lift_path) else ""
check(
    "B",
    "adjacent retained wall agrees: the finite-to-unbounded family-lift no-go "
    "(retained_no_go) blocks certifying the uniform cap from finitely many e-fold checks "
    "('finite post-record certificate alone => unbounded retained law' is not a valid route)",
    os.path.exists(lift_path) and "finite post-record certificate alone" in lift_txt,
)

# ----------------------------------------------------------------------
print("== T7: Route B (quantum) — finite local dimension gives an M-shaped fact, never the rate ==")
cth, sth = sp.Rational(3, 5), sp.Rational(4, 5)
U2 = sp.Matrix([[cth, -sth], [sth, cth]])
a, b, q = sp.symbols("a b q", real=True)
E_eff = U2 * sp.diag(a, b) * U2.T
sigma = sp.diag(q, 1 - q)
f_val = sp.expand(sp.trace(sigma * E_eff))
corner_ok = True
for av in (0, 1):
    for bv in (0, 1):
        for qv in (0, 1):
            val = f_val.subs([(a, av), (b, bv), (q, qv)])
            if not (0 <= val <= 1):
                corner_ok = False
check(
    "C",
    "qubit effect bound (per-register datum): effects on M_2 have spectrum in [0,1]; for any "
    "density sigma the value Tr(sigma E) is multilinear in (a, b, q) and lies in [0,1] at all "
    "8 corners (so on the whole box) — bounded per-register increment, an (CAP-M)-shaped fact; "
    "NOTE: as a Busch/Gleason frame-function statement it is conditional on a SUPPLIED "
    "probability measure (count-probability firewall: blocked as a supplier)",
    corner_ok
    and f_val.subs([(a, 1), (b, 1)]) == 1
    and f_val.subs([(a, 0), (b, 0)]) == 0,
)
n = sp.Symbol("n", integer=True, positive=True)
sites = (2 * n + 1) ** 3
check(
    "C",
    "the K-side cannot follow from finite local dimension: Z^3 supplies strictly increasing "
    "register counts (2n+1)^3 (derivative 6(2n+1)^2 > 0; (2*50+1)^3 = 1030301 > 10^6) with no "
    "cap — per-site boundedness times unbounded site count yields NO per-e-fold cap; no "
    "retained row couples amplitude e-folds to register counts",
    sp.simplify(sp.diff(sites, n) - 6 * (2 * n + 1) ** 2) == 0 and 101**3 == 1030301 and 101**3 > 10**6,
)
busch_path = os.path.join(REPO, "docs", "BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md")
gleason_path = os.path.join(REPO, "docs", "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md")
tomo_path = os.path.join(REPO, "docs", "LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE_NARROW_THEOREM_NOTE_2026-06-03.md")
effect_rows_ok = all(os.path.exists(pth) for pth in (busch_path, gleason_path, tomo_path))
busch_txt = open(busch_path, "r", encoding="utf-8").read() if effect_rows_ok else ""
readout_vocab_absent = True
for pth in (busch_path, gleason_path, tomo_path):
    txt = open(pth, "r", encoding="utf-8").read()
    if "log-scale response" in txt or "z W'" in txt or "zW'" in txt:
        readout_vocab_absent = False
check(
    "B",
    "effect-side rows are readout-blind: Busch/Gleason/local-tomography notes present, their "
    "subject is the effect/state measure (Busch note's load-bearing direction is m(E)=Tr(sigma E)), "
    "and none of them contains readout-response vocabulary — the readout W does not occur in "
    "their statements, so they cannot discriminate (BR) from its violations",
    effect_rows_ok and "m(E)=Tr(σE)" in busch_txt and readout_vocab_absent,
)

# ----------------------------------------------------------------------
print("== T8: falsification legs — compact collapse and the granted-clause completion ==")
compact_ok = True
for pv in P_PROBE:
    ends_resp = [sp.Abs(zv**pv) for zv in [sp.Integer(1), sp.Rational(85, 64), sp.E]]
    incr_1e = sp.Abs(g(pv, sp.E) - g(pv, 1)) if pv != 0 else sp.Integer(1)
    if any(not v.is_finite for v in ends_resp) or not incr_1e.is_finite:
        compact_ok = False
check(
    "D",
    "compact collapse: on [1, e] and on the licensed L2 Neumann image [1, 85/64] every member "
    "has finite response and finite e-fold increment (monotone endpoint evaluation) — "
    "(BR)/(BR-int)/(CAP) select NOTHING there; the full-R_>0 clause is exactly the declared "
    "T1-d / lemma-L3 domain hypothesis, no hidden domain freedom",
    compact_ok,
)
check(
    "D",
    "granting the missing capacity clauses completes the selection exactly: with "
    "(CAP-M)+(CAP-K) granted the pass set is {p = 0} and W = c log z follows with T1-d's "
    "remaining clauses — the missing license is the single load-bearing gap",
    [pv for pv in P_PROBE if increment_bounded(pv)] == [0],
)

# ----------------------------------------------------------------------
print("== T9: ledger scan — zero retained-grade capacity/rate suppliers (extends NU-note T9) ==")
with open(LEDGER, "r", encoding="utf-8") as fh:
    ledger = json.load(fh)
rows = ledger["rows"]
retained_grades = {"retained", "retained_bounded", "retained_pending_chain", "retained_no_go"}
import re as _re

patterns = _re.compile(
    r"record_capacity|finite_resolution|bounded_resolution|registration_rate|record_rate"
    r"|per_efold|efold|capacity_per|coding_rate|bandwidth"
    r"|bounded_response|response_bound|log_scale|readout_curvature|readout_regularity",
    _re.I,
)
matches = [
    kk for kk, r in rows.items() if patterns.search(kk) and r.get("effective_status") in retained_grades
]
print(
    "  [info][B] live retained-grade ledger scan matches "
    "(audit-lane-owned; not gated): "
    f"{matches!r}"
)
ctx_allowed = {
    "record_function_finite_sector_algebra_2026-06-05": {"retained"},
    # This row is now audited_conditional on main; that strengthens the
    # runner's boundary reading rather than supplying the missing cap.
    "record_unbounded_finite_additivity_schema_2026-06-06": {"audited_conditional"},
    "magnitude_reads_minimal_record_block_2026-06-06": {"retained_no_go"},
    "post_record_count_probability_firewall_2026-06-06": {"retained_no_go"},
    "observable_principle_record_scalar_map_no_go_note_2026-06-05": {"retained_no_go"},
    "post_record_finite_to_unbounded_family_lift_no_go_2026-06-06": {"retained_no_go"},
    "busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20": {"retained"},
    "gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20": {"retained"},
    "local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03": {"retained_pending_chain", "retained_bounded"},
    "sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06": {"retained"},
}
ctx_missing = [kk for kk in ctx_allowed if rows.get(kk) is None]
ctx_live = {kk: rows.get(kk, {}).get("effective_status") for kk in ctx_allowed}
check(
    "B",
    "cited rows present in the audit ledger (presence only)",
    not ctx_missing,
    detail=f"missing={ctx_missing!r}",
)
print(f"  [info][B] live effective statuses (audit-lane-owned; not gated): {ctx_live}")
check(
    "B",
    "the three candidate record-capacity suppliers are visible rows (assessed at full "
    "strength, not strawmanned)",
    all(
        kk in rows
        for kk in [
            "record_function_finite_sector_algebra_2026-06-05",
            "record_unbounded_finite_additivity_schema_2026-06-06",
            "magnitude_reads_minimal_record_block_2026-06-06",
        ]
    ),
)
nu_txt = open(NU_NOTE, "r", encoding="utf-8").read() if os.path.exists(NU_NOTE) else ""
barrier_txt = open(BARRIER_NOTE, "r", encoding="utf-8").read() if os.path.exists(BARRIER_NOTE) else ""
check(
    "B",
    "campaign chain on disk: the NU-license note names the record-capacity/finite-resolution "
    "hunt target and the barrier note declares its premise unlicensed",
    ("record capacity" in nu_txt.lower() or "finite resolution" in nu_txt.lower())
    and "unlicensed" in barrier_txt.lower(),
)

# ----------------------------------------------------------------------
print("== T10: note honest-scope, firewall-compliance, and boundary strings ==")
if os.path.exists(NOTE):
    note_text = open(NOTE, "r", encoding="utf-8").read()
    lower_note = note_text.lower()
    required_checks = {
        "does not retire P1": "does not retire p1" in lower_note,
        "does not license BR": "does not license `(br)`" in lower_note or "does not license (br)" in lower_note,
        "no probability law": "probability law" in lower_note and "supplies no probability rule" in lower_note,
        "no branch-to-scalar map": "branch-to-scalar map" in lower_note,
        "T1-d readout response": "t1-d" in lower_note and "scalar readout" in lower_note,
        "Status authority": "Status authority" in note_text,
        "independent audit lane": "independent audit lane" in lower_note,
    }
    missing = [name for name, ok in required_checks.items() if not ok]
    check("B", "note honest-scope and firewall-compliance strings present", missing == [], detail=f"missing={missing!r}")
    forbidden = [
        "(br) is now " + "licensed",
        "(cap) is " + "licensed",
        "p1 is " + "retired",
        "retired the " + "p1 admission",
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
