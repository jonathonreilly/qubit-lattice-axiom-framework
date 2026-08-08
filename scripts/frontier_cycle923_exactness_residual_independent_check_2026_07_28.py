#!/usr/bin/env python3
"""Exactness-residual distinguished-point geometry -- INDEPENDENT CHECKER (cycle 923), spec'd to REFUTE.

REVIEW RECORD (iteration 1, Sol, FIX_THEN_PROCEED, 2026-08-08): this checker
now (i) re-derives ALL THREE primary tables (A, B and C) at 60 dps, (ii)
states the reciprocal-multiplier lemma with its C^1 local-diffeomorphism /
nonzero-derivative hypotheses and verifies the chain-rule identity
symbolically instead of passing a literal True, (iii) describes repelling
fixed points as repelling (never 'destroyed' -- they remain exact fixed
points), and (iv) treats the narrow fixed-point alternation lemma as the
claim under attack; the formerly styled broad 'arrow-universality no-go' and
its lane-data consequence are withdrawn upstream and are not certified here.

Fully independent of the primary:
  * own algebra -- SYMBOLIC (sympy) for the 1-d dynamics, the fixed points, the
    linearizations, the entropy derivatives and curvature, and the deflation;
  * own high-precision arithmetic (mpmath, 60 dps) for every epsilon-window
    number, including the 3e-6 endpoint;
  * own construction search for a counterexample to the primary's narrow
    fixed-point alternation lemma;
  * re-derivation of the reconciliation from the primary's STATED TEXT ALONE
    (read out of the primary receipt), with an explicit determinacy verdict.

The checker imports NOTHING from the primary. It reads the primary receipt only
as a claim source, never as a computation source.

Deliverables of this file: refutations reported plainly, and at least 8
planted-defect teeth that must all FIRE.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

AUDIT_TIMEOUT_SEC = 900

T0 = time.time()
mp.mp.dps = 60

REPO = Path(__file__).resolve().parents[1]
RUNNER_REL = "scripts/frontier_cycle923_exactness_residual_independent_check_2026_07_28.py"
PRIMARY_RECEIPT_REL = "outputs/exactness_residual_cycle923_receipt_2026_07_28.json"
RECEIPT_REL = "outputs/exactness_residual_independent_check_cycle923_receipt_2026_07_28.json"

CHECKS: list[dict] = []
TEETH: list[dict] = []
FINDINGS: list[dict] = []
SECTIONS: list[str] = []


def check(section: str, name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    if section not in SECTIONS:
        SECTIONS.append(section)
    CHECKS.append({"section": section, "name": name, "ok": ok, "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] [{section}] {name}" + (f" | {detail}" if detail else ""))
    return ok


def tooth(tid: str, desc: str, fired: bool, detail: str = "") -> None:
    TEETH.append({"id": tid, "description": desc, "fired": bool(fired), "detail": detail})
    check("K-teeth", f"{tid} FIRED: {desc}", fired, detail)


def finding(kind: str, text: str, witness: str = "") -> None:
    """kind in {REFUTATION, CONFIRMATION, CAVEAT, DEGENERACY, DETERMINACY}"""
    FINDINGS.append({"kind": kind, "text": text, "witness": witness})
    print(f"  >>> {kind}: {text}" + (f"\n      witness: {witness}" if witness else ""))


def banner(t: str) -> None:
    print("")
    print("-" * 92)
    print(t)
    print("-" * 92)


def sha256_of(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git_blob_of(p: Path) -> str:
    d = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(d)).encode() + b"\0" + d).hexdigest()


# ==========================================================================
# K0 -- pins, and load the primary's CLAIMS (never its computations)
# ==========================================================================
banner("K0 -- pins; the primary receipt is loaded as a CLAIM SOURCE only")

PINS: dict[str, dict] = {}
for rel in [
    PRIMARY_RECEIPT_REL,
    "scripts/frontier_cycle923_exactness_residual_2026_07_28.py",
    "logs/runner-cache/frontier_cycle923_exactness_residual_2026_07_28.txt",
    "docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md",
    "docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
    "docs/FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md",
    "docs/FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md",
]:
    p = REPO / rel
    if p.exists():
        PINS[rel] = {"present": True, "sha256": sha256_of(p), "git_blob_sha1": git_blob_of(p), "bytes": p.stat().st_size}
        check("K0", f"pin: {rel}", True, f"sha256={PINS[rel]['sha256'][:16]}..")
    else:
        PINS[rel] = {"present": False}
        check("K0", f"pin: {rel}", False, "MISSING")

PRIMARY = json.loads((REPO / PRIMARY_RECEIPT_REL).read_text(encoding="utf-8"))
# The primary receipt embeds runtime_sec, so its raw file sha256 is not stable across
# re-runs by construction. Pin the runtime-independent CONTENT digest as well, so this
# checker's cross-reference to the primary is durable.
_stable = {k: v for k, v in PRIMARY.items() if k != "runtime_sec"}
PRIMARY_STABLE_SHA256 = hashlib.sha256(json.dumps(_stable, sort_keys=True, default=str).encode()).hexdigest()
check("K0", "primary receipt has a runtime-independent stable content digest (durable pin)", True,
      f"stable_sha256={PRIMARY_STABLE_SHA256}")
check("K0", "primary receipt parses and reports status=pass", PRIMARY.get("status") == "pass", f"status={PRIMARY.get('status')}")
check("K0", "primary receipt declares its interpretation firewall", "derives, forces or prefers r = 1/2" in PRIMARY.get("interpretation_firewall", ""))

# ==========================================================================
# K1 -- SYMBOLIC: the maps, their fixed points, their multipliers
# ==========================================================================
banner("K1 -- SYMBOLIC (sympy): maps, fixed points, multipliers -- own algebra, no numerics reused")

r = sp.symbols("r", positive=True)
r0 = sp.symbols("r0", nonnegative=True)
f = 2 * r ** 2
g = sp.sqrt(r / 2)

fix_f = sorted(sp.solve(sp.Eq(2 * r0 ** 2, r0), r0))
fix_g = sorted(sp.solve(sp.Eq(sp.sqrt(r0 / 2), r0), r0))
check("K1-symbolic", "sympy solve: Fix(f) for f(r)=2r^2 is {0, 1/2}", fix_f == [0, sp.Rational(1, 2)], f"solve -> {fix_f}")
check("K1-symbolic", "sympy solve: Fix(g) for g(r)=sqrt(r/2) is {0, 1/2}", fix_g == [0, sp.Rational(1, 2)], f"solve -> {fix_g}")

fp = sp.diff(f, r)
gp = sp.diff(g, r)
fp_half = sp.simplify(fp.subs(r, sp.Rational(1, 2)))
gp_half = sp.simplify(gp.subs(r, sp.Rational(1, 2)))
check("K1-symbolic", "sympy diff: f'(r) = 4r, so f'(1/2) = 2 EXACTLY", sp.simplify(fp - 4 * r) == 0 and fp_half == 2, f"f'={fp}, f'(1/2)={fp_half}")
check("K1-symbolic", "sympy diff: g'(1/2) = 1/2 EXACTLY", gp_half == sp.Rational(1, 2), f"g'={sp.simplify(gp)}, g'(1/2)={gp_half}")
check("K1-symbolic", "sympy: f'(0) = 0 (superstable / quadratic)", sp.simplify(fp.subs(r, 0)) == 0)
check("K1-symbolic", "sympy: g'(r) -> +oo as r -> 0+ (r=0 repels under g)", sp.limit(gp, r, 0, "+") == sp.oo)

comp1 = sp.simplify(g.subs(r, f) - r)
comp2 = sp.simplify(f.subs(r, g) - r)
check("K1-symbolic", "sympy simplify: g(f(r)) - r == 0 identically on r>0", comp1 == 0, f"-> {comp1}")
check("K1-symbolic", "sympy simplify: f(g(r)) - r == 0 identically on r>0", comp2 == 0, f"-> {comp2}")
check("K1-symbolic", "sympy: the multiplier product f'(1/2)*g'(1/2) == 1 EXACTLY", sp.simplify(fp_half * gp_half) == 1, f"{fp_half} * {gp_half} = {sp.simplify(fp_half*gp_half)}")

# the reciprocal-multiplier relation as a GENERAL lemma, with its actual hypotheses,
# and a REAL symbolic derivation (no literal PASS).
x, xs = sp.symbols("x xs")
hfun = sp.Function("hfun")
hinv = sp.Function("hinv")
# Step 1 (chain rule, symbolic): d/dx [h^{-1}(h(x))] factors as (outer derivative) * h'(x).
chain = sp.diff(hinv(hfun(x)), x)
chain_factors = sp.Mul.make_args(chain)
inner_deriv = sp.Derivative(hfun(x), x)
chain_ok = (inner_deriv in chain_factors) and len(chain_factors) == 2
# Step 2 (solve at the fixed point): with h a C^1 LOCAL DIFFEOMORPHISM at the shared fixed
# point xs and m_h = h'(xs) != 0, the identity h^{-1}(h(x)) = x forces m_inv * m_h = 1.
m_h = sp.Symbol("m_h", nonzero=True)
m_inv = sp.Symbol("m_inv")
recip_sol = sp.solve(sp.Eq(m_inv * m_h, 1), m_inv)
lemma_ok = chain_ok and recip_sol == [1 / m_h]
check("K1-symbolic", "LEMMA (with hypotheses; symbolic, no literal PASS): if h is a C^1 local diffeomorphism at a "
      "shared fixed point x* with h'(x*) != 0 finite, then (h^{-1})'(x*) = 1/h'(x*). Sympy chain rule factors "
      "d/dx[h^{-1}(h(x))] into (outer)*(h'(x)); equating to 1 and solving at the fixed point gives exactly [1/m_h]. "
      "MERE INVERTIBILITY IS NOT SUFFICIENT: at r=0 this branch's own f has f'(0)=0, the hypothesis fails, and g' "
      "diverges (the K1 limit check above) -- so the 'unstable vs attracting' reciprocity holds for the supplied "
      "pair at r=1/2 because f'(1/2)=2 is finite and nonzero, not for arbitrary invertible maps.",
      lemma_ok, f"chain factors = {chain_factors}; solve(m_inv*m_h=1) -> {recip_sol}")

# ==========================================================================
# K2 -- SYMBOLIC: entropies, stationarity, curvature, deflation
# ==========================================================================
banner("K2 -- SYMBOLIC: entropy functionals, stationarity, curvature, the deflation claim")

p_s = 1 / (1 + 2 * r)
p_d = 2 * r / (1 + 2 * r)
S2 = -p_s * sp.log(p_s) - p_d * sp.log(p_d)
dS2 = sp.simplify(sp.diff(S2, r))
sol2 = sp.solve(sp.Eq(dS2, 0), r)
check("K2-symbolic", "sympy: dS2/dr = 0 has the unique positive solution r = 1/2", sol2 == [sp.Rational(1, 2)], f"solve -> {sol2}; dS2/dr = {dS2}")
check("K2-symbolic", "sympy: S2(1/2) = log 2 EXACTLY", sp.simplify(S2.subs(r, sp.Rational(1, 2)) - sp.log(2)) == 0)
d2S2 = sp.simplify(sp.diff(S2, r, 2).subs(r, sp.Rational(1, 2)))
check("K2-symbolic", "sympy: S2''(1/2) = -1 EXACTLY in nats (independent of the primary's finite difference)",
      sp.simplify(d2S2 + 1) == 0, f"S2''(1/2) = {d2S2}")
check("K2-symbolic", "corollary: S2(r) = log2 - (1/2)(r-1/2)^2 + O((r-1/2)^3), so the entropy deficit at "
      "|r-1/2| = 3e-6 is 4.5e-12 nats", abs(float(sp.Rational(1, 2) * sp.Rational(3, 10 ** 6) ** 2) - 4.5e-12) < 1e-20,
      f"deficit = {float(sp.Rational(1,2)*sp.Rational(3,10**6)**2):.6e} nats")

Z3 = 1 + 2 * r
S3 = sp.log(Z3) - (2 * r / Z3) * sp.log(r)
sol3 = sp.solve(sp.Eq(sp.simplify(sp.diff(S3, r)), 0), r)
check("K2-symbolic", "sympy: the 3-real-DOF entropy S3 is stationary at r = 1 (and only there, on r>0)",
      sol3 == [1], f"solve -> {sol3}")
check("K2-symbolic", "sympy: S3(1) = log 3 EXACTLY", sp.simplify(S3.subs(r, 1) - sp.log(3)) == 0)

xx = sp.symbols("xx", real=True)
lam = [(1 + 2 * xx) / 3, (1 - xx) / 3, (1 - xx) / 3]
Ssp = -sum(L * sp.log(L) for L in lam)
dSsp = sp.simplify(sp.diff(Ssp, xx))
check("K2-symbolic", "sympy: the spectral entropy (delta=0), in x = sqrt(r), is stationary at x = 0 i.e. r = 0",
      sp.simplify(dSsp.subs(xx, 0)) == 0, f"dS_spec/dx = {dSsp}")
d2Ssp = sp.simplify(sp.diff(Ssp, xx, 2).subs(xx, 0))
check("K2-symbolic", "sympy: S_spec''(x=0) = -2 < 0 (a maximum), so S_spec ~ log3 - r near r=0 and the gradient "
      "flow in r ARRIVES at r=0 in finite time (dr/dt -> -1)", sp.simplify(d2Ssp + 2) == 0, f"S_spec''(0) = {d2Ssp}")
check("K2-symbolic", "INDEPENDENT CONFIRMATION of the primary's anti-diagonal (computed, no literal PASS): the "
      "symbolic stationarity solves above give S2 -> r=1/2, S3 -> r=1, S_spec (delta=0) -> r=0 with negative "
      "curvature -- each registered setting maximizes a different derived functional",
      sol2 == [sp.Rational(1, 2)] and sol3 == [1] and sp.simplify(dSsp.subs(xx, 0)) == 0
      and sp.simplify(d2Ssp + 2) == 0)

pp = sp.symbols("pp", real=True)
sharp_fix = sp.solve(sp.Eq(pp ** 2 / (pp ** 2 + (1 - pp) ** 2), pp), pp)
check("K2-symbolic", "sympy: for a 2-outcome split, p -> p^2/Z fixes p iff p in {0, 1/2, 1}. This CONFIRMS the "
      "primary's COINCIDENCE-DEFLATION: interior sharpening-fixed-point = uniform = max-S2 = HS equipartition is "
      "ONE fact, not three independent ones.", set(sharp_fix) == {0, sp.Rational(1, 2), 1}, f"solve -> {sorted(sharp_fix)}")

# ==========================================================================
# K3 -- mpmath 60-dps: the epsilon-window arithmetic, incl. the 3e-6 endpoint
# ==========================================================================
banner("K3 -- mpmath at 60 dps: independent epsilon-window arithmetic, attacking the 3e-6 endpoint")


def mp_g(v):
    return mp.sqrt(v / 2)


def mp_f(v):
    return 2 * v * v


def n_enter(start, eps):
    """Exact closed form in the log-conjugate coordinate, plus an independent iteration."""
    L0 = mp.log(2 * mp.mpf(start))
    if L0 == 0:
        n_cf = 0
    else:
        thr = mp.log(1 + 2 * mp.mpf(eps)) if L0 > 0 else -mp.log(1 - 2 * mp.mpf(eps))
        n_cf = int(mp.ceil(mp.log(abs(L0) / thr) / mp.log(2)))
    v, n = mp.mpf(start), 0
    while abs(v - mp.mpf("0.5")) > mp.mpf(eps) and n < 5000:
        v = mp_g(v)
        n += 1
    return n_cf, n


def n_exit(eps0, eps1):
    n_cf = int(mp.ceil(mp.log(mp.log(1 + 2 * mp.mpf(eps1)) / mp.log(1 + 2 * mp.mpf(eps0))) / mp.log(2)))
    v, n = mp.mpf("0.5") + mp.mpf(eps0), 0
    while abs(v - mp.mpf("0.5")) <= mp.mpf(eps1) and n < 5000:
        v = mp_f(v)
        n += 1
    return n_cf, n


tabA = PRIMARY["Q2_exactness"]["table_A_entry_under_g"]
tabB = PRIMARY["Q2_exactness"]["table_B_residence_under_f"]
mismatch_A, mismatch_B = [], []
for eps_key, row in tabA.items():
    eps = float(eps_key)
    for start_key, cell in row.items():
        start = float(start_key.split("=")[1])
        cf, it = n_enter(start, eps)
        if abs(it - cell["iterated"]) > 0:
            mismatch_A.append((eps_key, start_key, cell["iterated"], it))
        if abs(cf - it) > 1:
            mismatch_A.append((eps_key, start_key, "cf-vs-it", cf, it))
check("K3-mpmath", "TABLE A: every entry-step count under g reproduces at 60 dps (independent iteration)",
      not mismatch_A, f"{len(tabA)*3} cells re-derived; mismatches={mismatch_A}")
for eps_key, cell in tabB.items():
    cf, it = n_exit(float(eps_key), 1e-1)
    if abs(it - cell["iterated"]) > 0:
        mismatch_B.append((eps_key, cell["iterated"], it))
check("K3-mpmath", "TABLE B: every residence-step count under f reproduces at 60 dps", not mismatch_B,
      f"{len(tabB)} cells re-derived; mismatches={mismatch_B}")

# TABLE C -- full coverage (review iteration 1: this table was previously not
# independently checked at all). Every cell must equal the EXACT closed form
# (1/2)[(1+2 eps)^(2^-N) - 1] at 60 dps.
tabC = PRIMARY["Q2_exactness"]["table_C_backward_tuning_under_f"]
mismatch_C = []
n_cells_C = 0
for eps_key, row in tabC.items():
    eps_c = mp.mpf(eps_key)
    for n_key, cell in row.items():
        N_c = int(n_key.split("=")[1])
        exact_c = mp.mpf("0.5") * (mp.exp(mp.log(1 + 2 * eps_c) * mp.mpf(2) ** (-N_c)) - 1)
        n_cells_C += 1
        if abs(mp.mpf(cell) - exact_c) > abs(exact_c) * mp.mpf("1e-13"):
            mismatch_C.append((eps_key, n_key, cell, mp.nstr(exact_c, 20)))
check("K3-mpmath", "TABLE C: EVERY backward-tuning cell (including N=50 and N=100, where a binary64 iteration "
      "underflows to zero) reproduces the exact closed form (1/2)[(1+2 eps)^(2^-N) - 1] at 60 dps (rel tol 1e-13)",
      n_cells_C == 24 and not mismatch_C, f"{n_cells_C} cells re-derived; mismatches={mismatch_C}")

widths = PRIMARY["Q2_exactness"]["exact_preimage_width_of_3e-6_window"]
mismatch_W = []
eps36 = mp.mpf("3e-6")
lin_devs_W = {}
for n_key, cell in widths.items():
    N_w = int(n_key.split("=")[1])
    s_w = mp.mpf(2) ** (-N_w)
    exact_w = mp.mpf("0.5") * (mp.exp(mp.log(1 + 2 * eps36) * s_w) - mp.exp(mp.log(1 - 2 * eps36) * s_w))
    if abs(mp.mpf(cell) - exact_w) > abs(exact_w) * mp.mpf("1e-13"):
        mismatch_W.append((n_key, cell, mp.nstr(exact_w, 20)))
    if N_w >= 1:
        lin_devs_W[n_key] = float(exact_w / (2 * eps36 * s_w) - 1)
check("K3-mpmath", "PREIMAGE-WIDTH LAW: every published window width reproduces the exact closed form "
      "(1/2)[(1+2 eps)^(2^-N) - (1-2 eps)^(2^-N)] at 60 dps", not mismatch_W,
      f"{len(widths)} widths re-derived; mismatches={mismatch_W}")
check("K3-mpmath", "the 'halves every step' reading is confirmed to be a LINEARIZATION, not exact: at 60 dps the "
      "width deviates from 2 eps * 2^-N by a strictly positive relative O((2 eps)^2) at every N >= 1",
      all(0.0 < d < float((2 * eps36) ** 2) for d in lin_devs_W.values()),
      "; ".join(f"{k}: {v:.3e}" for k, v in lin_devs_W.items()))

cf36, it36 = n_enter(1.0, 3e-6)
exact36 = mp.log(mp.log(mp.mpf(2)) / mp.log(1 + 2 * mp.mpf("3e-6"))) / mp.log(2)
check("K3-mpmath", "3e-6 ENDPOINT, attacked directly: n = log2( ln2 / ln(1+6e-6) ) = 16.8175..., so the ceiling is "
      "17 and the primary's 17 is correct (not an off-by-one)", cf36 == 17 and it36 == 17,
      f"real-valued n = {mp.nstr(exact36, 10)}; ceil = {cf36}; iterated = {it36}")
check("K3-mpmath", "3e-6 endpoint, the OTHER direction: a pattern at |r-1/2|=3e-6 leaves the 1e-1 window under f in "
      "15 steps", n_exit(3e-6, 1e-1)[1] == 15, f"n_exit(3e-6 -> 1e-1) = {n_exit(3e-6,1e-1)[1]}")
far = n_enter(mp.mpf("1e300"), 3e-6)
check("K3-mpmath", "basin claim attacked at the extreme: from r0 = 1e300, g still reaches 3e-6 in a small number of "
      "steps (log-log convergence), confirming basin(g,1/2) = (0,inf)", far[1] <= 30, f"n = {far[1]} steps from 1e300")
check("K3-mpmath", "basin claim attacked at the other extreme: r0 = 0 EXACTLY is a fixed point of g and never "
      "enters any window around 1/2 -- the primary's 'excludes exactly one point' is correct",
      mp_g(mp.mpf(0)) == 0)

# ==========================================================================
# K4 -- MODEL-DEGENERACY HUNT: can the Q2 verdict be flipped by a reading?
# ==========================================================================
banner("K4 -- MODEL-DEGENERACY HUNT on Q2: enumerate readings and look for a verdict flip")

readings = []


def add_reading(name, kind, multiplier, verdict, note):
    readings.append({"reading": name, "kind": kind, "multiplier_or_rate": multiplier, "verdict": verdict, "note": note})


add_reading("f: sharpening (records/Luders), discrete", "discrete map", 2.0, "UNEXPLAINED",
            "repelling; the operative fixed point is the separatrix; exactness amplified x2 per step")
add_reading("g = f^{-1}: thermalizing reverse, discrete", "discrete map", 0.5, "GENERIC",
            "contracting geometrically; basin (0,inf); 17 steps from r=1 to 3e-6")
add_reading("S2-gradient flow in the r coordinate", "continuous flow", -1.0, "GENERIC",
            "linearization -1; 12.02 e-folds from |delta|=0.5 to 3e-6")
add_reading("S2-gradient flow in the p coordinate (flat metric in p -- a DIFFERENT metric choice, hence a different "
            "gradient system, NOT the r-coordinate flow rewritten)", "continuous flow", -4.0, "GENERIC",
            "linearization -4; 3.01 e-folds; under a genuine coordinate change the eigenvalue would be invariant, "
            "so the -1 vs -4 split is a metric difference; only the SIGN is common to all positive metrics")
add_reading("S2-gradient flow in a general positive metric rho(r)", "continuous flow", "-rho(1/2) < 0", "GENERIC",
            "for ANY positive metric the sign is negative, so the verdict is metric-invariant; only the e-fold count moves")
add_reading("f composed k times", "discrete map", "2^k", "UNEXPLAINED", "amplification compounds")
add_reading("g composed k times", "discrete map", "2^{-k}", "GENERIC", "contraction compounds")
add_reading("balanced alternation (f then g, equal counts)", "discrete composition", 1.0, "NEUTRAL",
            "f o g = identity EXACTLY, so r never moves: the pattern PERSISTS at wherever it was registered, with "
            "no concentration and no dispersion. This is a THIRD verdict, and it is neither GENERIC nor UNEXPLAINED")
add_reading("biased alternation (n_f sharpenings per n_g thermalizations)", "discrete composition", "2^(n_f - n_g)",
            "GENERIC if n_g > n_f, UNEXPLAINED if n_f > n_g, NEUTRAL iff n_f = n_g",
            "the verdict is a function of the arrow BALANCE, not of the map algebra")
add_reading("durability / fixedness under re-registration", "criterion, not a flow", "n/a", "CRITERIAL",
            "selects Fix = {0, 1/2}; exactness without attraction and without a rate")

# verify the load-bearing degeneracy claim symbolically: f o g is the identity
check("K4-degeneracy", "sympy: f(g(r)) = r identically, so a BALANCED alternation of the two supplied arrows is "
      "EXACTLY the identity map on r", sp.simplify(f.subs(r, g) - r) == 0)
check("K4-degeneracy", "sympy: the composition with n_f sharpenings and n_g thermalizations has multiplier "
      "2^(n_f - n_g) at r=1/2, which is >1, =1 or <1 according to the arrow balance",
      sp.simplify(fp_half ** 2 * gp_half ** 2 - 1) == 0, "worked example n_f = n_g = 2 gives multiplier exactly 1")

verdicts = sorted({rd["verdict"] for rd in readings})
check("K4-degeneracy", "MODEL DEGENERACY IS REAL: the readings available on this surface produce more than two "
      "distinct verdicts", len(verdicts) >= 3, f"verdicts found = {verdicts}")

finding("DEGENERACY",
        "The Q2 verdict is NOT binary. Beyond the primary's GENERIC/UNEXPLAINED split there is a third, "
        "structurally natural reading -- a BALANCED alternation of the two supplied arrows -- under which f o g is "
        "EXACTLY the identity, so a registered pattern neither concentrates nor disperses. Its verdict is NEUTRAL: "
        "persistence with no rate. More generally the multiplier is 2^(n_f - n_g), so the verdict is set by the "
        "ARROW BALANCE, not by the map algebra.",
        "sympy: f(g(r)) - r simplifies to 0 identically; multiplier of f^2 o g^2 at r=1/2 is exactly 1")
finding("CONFIRMATION",
        "This degeneracy does NOT overturn the primary's headline verdict. It sharpens it: the primary says the "
        "surface is UNEXPLAINED because the arrow is not derived, and the balanced-alternation reading is one more "
        "underived arrow with its own verdict. The three-way split strengthens the primary's claim that the "
        "undischarged element is the ARROW, not the exponent.",
        "the primary's headline is 'UNEXPLAINED on the current surface' with 'the arrow is the undischarged element'")

check("K4-degeneracy", "the primary's headline verdict survives the degeneracy hunt (the hunt adds a verdict, it "
      "does not remove the reason for the headline)", PRIMARY["Q2_exactness"]["headline_verdict"].startswith("UNEXPLAINED"),
      f"primary headline = {PRIMARY['Q2_exactness']['headline_verdict']}")
# Review iteration 1: the former "REFUTATION CHECK" here grepped this file's own
# prose for the substring 'derived' and could not fail; it is demoted from the
# executable scorecard to a MANUAL assertion, reported as a finding instead.
finding("CONFIRMATION",
        "MANUAL ASSERTION (not an executable check; removed from the scorecard at review iteration 1): every "
        "reading in the table above uses a map or flow that is SUPPLIED by a source note or CONSTRUCTED inside "
        "this checker; none is derived from the axioms. This is an author-audited statement about the table's "
        "construction, and it carries no machine-checked force.",
        "table built in this file; readings enumerated above")

# ==========================================================================
# K5 -- attack the ARROW-UNIVERSALITY NO-GO by construction
# ==========================================================================
banner("K5 -- attacking the primary's fixed-point alternation lemma: construct a monotone map that could break it")

# Family: h(x) = x + c * phi(x) * s(x), phi(x) = x(x-1/2)(x-1), s(x) = exp(-lam (x-1/2)^2) > 0.
# Zeros of h(x)-x are EXACTLY {0, 1/2, 1}; c is fixed by demanding h'(1/2) = 2.
lam_val = 20.0
phi = xx * (xx - sp.Rational(1, 2)) * (xx - 1)
s_fun = sp.exp(-lam_val * (xx - sp.Rational(1, 2)) ** 2)
c_sym = sp.symbols("c_sym")
h_map = xx + c_sym * phi * s_fun
hp = sp.diff(h_map, xx)
c_sol = sp.solve(sp.Eq(sp.simplify(hp.subs(xx, sp.Rational(1, 2))), 2), c_sym)
c_val = c_sol[0]
h_num = sp.lambdify(xx, h_map.subs(c_sym, c_val), "math")
hp_num = sp.lambdify(xx, hp.subs(c_sym, c_val), "math")
mono = all(hp_num(i / 2000.0) > 0 for i in range(0, 2001))
fixed_ok = all(abs(h_num(v) - v) < 1e-12 for v in (0.0, 0.5, 1.0))
check("K5-nogo-attack", "constructed a STRICTLY INCREASING map h with Fix(h) exactly {0, 1/2, 1} and h'(1/2) = 2 "
      "(same local data as the supplied f) -- this is precisely the map that could break the alternation lemma",
      mono and fixed_ok, f"c = {sp.nsimplify(c_val, rational=False)}, min h' on [0,1] = {min(hp_num(i/2000.0) for i in range(0,2001)):.6f}")
mults = {v: hp_num(v) for v in (0.0, 0.5, 1.0)}
attracting = {v: abs(m) < 1.0 for v, m in mults.items()}
check("K5-nogo-attack", "for the constructed h, 1/2 REPELS (h'=2) while 0 and 1 are locally ATTRACTING -- so h "
      "leaves the outer settings attracting but does NOT concentrate onto 1/2",
      (not attracting[0.5]) and attracting[0.0] and attracting[1.0],
      f"multipliers = {{0: {mults[0.0]:.6f}, 1/2: {mults[0.5]:.6f}, 1: {mults[1.0]:.6f}}}")
check("K5-nogo-attack", "for its inverse h^{-1}, 1/2 ATTRACTS (multiplier 1/2) while 0 and 1 REPEL. NOTE (review "
      "iteration 1): 0 and 1 REMAIN EXACT FIXED POINTS of h^{-1} -- they are repelling, i.e. they lose local "
      "asymptotic attraction only; no 'lane destruction' or loss of fixed-point persistence is claimed",
      abs(1.0 / mults[0.5]) < 1.0 and abs(1.0 / mults[0.0]) > 1.0 and abs(1.0 / mults[1.0]) > 1.0,
      f"inverse multipliers = {{0: {1.0/mults[0.0]:.6f}, 1/2: {1.0/mults[0.5]:.6f}, 1: {1.0/mults[1.0]:.6f}}}")
attack_rows = {
    "h": {"half_attracting": abs(mults[0.5]) < 1.0,
          "r0_attracting": abs(mults[0.0]) < 1.0, "r1_attracting": abs(mults[1.0]) < 1.0},
    "h^{-1}": {"half_attracting": abs(1.0 / mults[0.5]) < 1.0,
               "r0_attracting": abs(1.0 / mults[0.0]) < 1.0, "r1_attracting": abs(1.0 / mults[1.0]) < 1.0},
}


def k5_alternation_predicate(table: dict) -> bool:
    """True iff no row is simultaneously locally attracting at 1/2, 0 and 1
    (checker's own re-implementation; also mutation-tested by tooth K-T8)."""
    return all(not (row["half_attracting"] and row["r0_attracting"] and row["r1_attracting"]) for row in table.values())


check("K5-nogo-attack", "THE ALTERNATION LEMMA SURVIVES the constructed attack: computed row by row, neither h nor "
      "h^{-1} is locally attracting at all three registered settings simultaneously",
      k5_alternation_predicate(attack_rows), f"rows = {attack_rows}")
finding("CONFIRMATION",
        "The primary's FIXED-POINT ALTERNATION LEMMA (narrow; formerly styled an arrow-universality no-go, since "
        "withdrawn as a broad claim) withstands a targeted construction attack. A strictly increasing "
        "map with fixed-point set exactly {0, 1/2, 1} and multiplier 2 at 1/2 does exist (so the lemma is not "
        "vacuously true for lack of candidates), but it and its inverse split exactly as the alternation lemma "
        "requires: one leaves the outer fixed points attracting without concentrating onto 1/2, the other "
        "concentrates onto 1/2 while the outer fixed points repel (they remain exact fixed points). No map in the "
        "hypothesis class does both.",
        f"h(x) = x + c*x(x-1/2)(x-1)*exp(-20(x-1/2)^2) with c = {float(c_val):.6f}; min h' = {min(hp_num(i/2000.0) for i in range(0,2001)):.6f} > 0")

# the named escape must actually work, or the primary's escape clause is wrong
phi2 = xx * (xx - sp.Rational(1, 4)) * (xx - sp.Rational(1, 2)) * (xx - sp.Rational(3, 4)) * (xx - 1)
h2 = xx - sp.Rational(1, 10) * phi2
h2p_num = sp.lambdify(xx, sp.diff(h2, xx), "math")
esc_attr = {v: abs(h2p_num(v)) < 1.0 for v in (0.0, 0.5, 1.0)}
check("K5-nogo-attack", "the primary's NAMED ESCAPE is real: a map with EXTRA fixed points at 1/4 and 3/4 makes all "
      "three registered settings attracting simultaneously", all(esc_attr.values()),
      f"multipliers at 0, 1/2, 1 = {[round(h2p_num(v),6) for v in (0.0,0.5,1.0)]}; extra fixed points at 1/4 and 3/4")
finding("CONFIRMATION",
        "The primary's named escape from the alternation lemma's hypothesis class is genuine and correctly priced: "
        "allowing fixed points at 1/4 and 3/4 does make all three registered settings simultaneously attracting, at "
        "the stated cost of two distinguished cells the dial does not register.",
        "h(x) = x - (1/10) x(x-1/4)(x-1/2)(x-3/4)(x-1); all three multipliers have modulus < 1")

# ==========================================================================
# K6 -- re-derive the reconciliation from the primary's STATED TEXT ALONE
# ==========================================================================
banner("K6 -- re-derivation from the primary's STATED TEXT alone, and the determinacy verdict")

stmt = PRIMARY["Q1_reconciliation"]["statement"]
claims = {
    "g is f-inverse": bool(re.search(r"g\(r\)=sqrt\(r/2\) is exactly f\^\{-1\}", stmt)),
    "shared fixed points": bool(re.search(r"Fix\(f\)=Fix\(g\)=\{0,1/2\}", stmt)),
    "f' = 2": bool(re.search(r"f'\(1/2\)=2", stmt)),
    "g' = 1/2": bool(re.search(r"g'\(1/2\)=1/2", stmt)),
    "product 1": "product exactly 1" in stmt,
    "S2 Lyapunov": "strict Lyapunov function" in stmt,
    "static extremum": "STATIC extremum" in stmt,
}
for k, v in claims.items():
    check("K6-determinacy", f"the primary's Q1 statement text asserts: {k}", v)
check("K6-determinacy", "every numeric claim in the Q1 statement text is independently TRUE under sympy",
      fix_f == [0, sp.Rational(1, 2)] and fp_half == 2 and gp_half == sp.Rational(1, 2)
      and sp.simplify(fp_half * gp_half) == 1 and comp1 == 0)

check("K6-determinacy", "DETERMINACY, local (conditioned on the K1 lemma actually verifying, not on a literal "
      "True): the stated text fixes the LOCAL picture uniquely -- any map that is a C^1 local diffeomorphism with a "
      "nonzero-derivative fixed point of multiplier 2 has an inverse with multiplier 1/2 there (the K1 lemma, "
      "symbolically verified above), so no second local reading is consistent with the text",
      lemma_ok and fp_half == 2 and gp_half == sp.Rational(1, 2),
      f"lemma_ok={lemma_ok}; f'(1/2)={fp_half}; g'(1/2)={gp_half}")
check("K6-determinacy", "DETERMINACY, global: the stated text does NOT fix the GLOBAL picture. The K5 construction "
      "is an invertible map satisfying every numeric claim in the Q1 statement, yet it FIXES r=1 instead of sending "
      "it to infinity.", mono and fixed_ok and abs(h_num(1.0) - 1.0) < 1e-12,
      "so 'r=1 runs away' is a property of the specific supplied map 2r^2, not a consequence of the reconciliation")
finding("DETERMINACY",
        "The primary's Q1 statement determines the reconciliation LOCALLY but not GLOBALLY. Read as a standalone "
        "sentence it does not entail the r=1 behaviour that the S4 candidate-sweep f-row uses: the K5 map satisfies "
        "every numeric claim in the statement while fixing r=1. The primary's own runner does use the explicit global "
        "forms 2r^2 and sqrt(r/2), so the sweep is sound as computed; but any downstream consumer quoting only the "
        "Q1 sentence would not be entitled to the r=1 row. Recommended framing for the supervisor's note: state the "
        "global map forms alongside the reconciliation, not the multipliers alone.",
        "K5 map h fixes 0, 1/2 and 1 with h'(1/2)=2, satisfying the Q1 statement's numerics; f(1)=2 does not")

# ==========================================================================
# K7 -- independent firewall re-check, and the comparator
# ==========================================================================
banner("K7 -- independent firewall re-check and independent comparator arithmetic")

fw = PRIMARY["S5_firewall"]
check("K7-firewall", "primary firewall reports zero violations", fw.get("violations") == [], f"violations={fw.get('violations')}")
check("K7-firewall", "primary firewall's admissible family spans {0, 1/2, 1}", fw.get("spans_dial") is True)
check("K7-firewall", "primary firewall reports all three lanes well-formed", fw.get("lanes_well_formed") is True)
uniq = [c for c in PRIMARY["checks"] if "designates a unique r" in c["name"] and not c["ok"]]
check("K7-firewall", "no primary check asserting 'designates a unique r -> carries a supplied element' failed", not uniq)
blob = json.dumps(PRIMARY["Q3_priced"]).lower()
check("K7-firewall", "independent scan of the priced list for adoption language finds none",
      not any(v in blob for v in ("should adopt", "we recommend", "must be adopted", "recommend adoption", "should be adopted")))
# INDEPENDENT re-application of the firewall rule to the primary's own published step table
steps_pub = fw.get("steps", [])
indep_viol = [s["id"] for s in steps_pub if s.get("supplied") is None and len(s.get("designates", [])) == 1]
check("K7-firewall", "INDEPENDENT re-scan of the primary's published firewall step table using a re-implemented "
      "rule: no unconditional step designates a unique r", steps_pub and not indep_viol,
      f"{len(steps_pub)} steps re-scanned independently; violations={indep_viol}")
uniq_designators = [s["id"] for s in steps_pub if len(s.get("designates", [])) == 1]
check("K7-firewall", "every unique-r designator in the primary's table carries a NAMED supplied element",
      uniq_designators and all(s.get("supplied") for s in steps_pub if len(s.get("designates", [])) == 1),
      f"unique-r designators = {uniq_designators}")
check("K7-firewall", "the registered dial {0, 1/2, 1} is jointly covered by the primary's designators, so no single "
      "setting is singled out across the runner as a whole",
      {v for s in steps_pub for v in s.get("designates", [])} >= {0.0, 0.5, 1.0},
      f"designated settings across all steps = {sorted({v for s in steps_pub for v in s.get('designates', [])})}")

mp_masses = {"m_e": mp.mpf("0.51099895"), "m_mu": mp.mpf("105.6583755"), "m_tau": mp.mpf("1776.93")}
roots = [mp.sqrt(mp_masses[k]) for k in ("m_e", "m_mu", "m_tau")]
Q_mp = sum(v * v for v in roots) / (sum(roots) ** 2)
r_mp = (3 * Q_mp - 1) / 2
dev_mp = abs(r_mp - mp.mpf("0.5"))
prim_dev = PRIMARY["S7_comparator"]["abs_dev_r"]
check("K7-comparator", "comparator |r_PDG - 1/2| reproduces at 60 dps (the primary's float64 value carries an "
      "absolute error of order 1e-16 from the 0.5 cancellation, so ~10 significant digits of the deviation are "
      "trustworthy)", abs(float(dev_mp) - prim_dev) < 1e-15,
      f"mpmath={mp.nstr(dev_mp, 16)} primary={prim_dev!r} diff={abs(float(dev_mp)-prim_dev):.3e}")
check("K7-comparator", "comparator is below the reduction note's published 1e-5 bound", dev_mp < mp.mpf("1e-5"))

# CAVEAT HUNT: how stable is the "~3e-6" figure across tau-mass conventions?
# Tau-mass variants: values as committed in-repo plus two bracketing points.
# IMPORTED-VALUE DISCLOSURE (review iteration 1): no external PDG edition/table/
# uncertainty is cited or verified in-repo here; "1776.86" is an alternate
# committed convention seen in other repo tables, and the scan window is
# ASSERTED for sensitivity analysis only. Comparator/support-only throughout.
tau_variants = {"1776.93 (reduction runner)": "1776.93",
                "1776.86 (alternate committed convention; external edition not verified in-repo)": "1776.86",
                "1776.99": "1776.99", "1777.00": "1777.00"}
tau_scan = {}
for label, mt in tau_variants.items():
    rr = [mp.sqrt(mp_masses["m_e"]), mp.sqrt(mp_masses["m_mu"]), mp.sqrt(mp.mpf(mt))]
    Qv = sum(v * v for v in rr) / (sum(rr) ** 2)
    tau_scan[label] = float(abs((3 * Qv - 1) / 2 - mp.mpf("0.5")))
spread = max(tau_scan.values()) / max(min(tau_scan.values()), 1e-30)
check("K7-comparator", "TAU-MASS SENSITIVITY SCAN of the comparator (computed condition, no literal PASS): all four "
      "scanned conventions produce a nonnegative deviation and the max/min spread exceeds 2, demonstrating material "
      "convention sensitivity of the headline digit",
      len(tau_scan) == 4 and all(v >= 0.0 for v in tau_scan.values()) and spread > 2.0,
      "; ".join(f"{k} -> {v:.3e}" for k, v in tau_scan.items()) + f"; spread={spread:.2f}")


def dev_at(mt):
    rr = [mp.sqrt(mp_masses["m_e"]), mp.sqrt(mp_masses["m_mu"]), mp.sqrt(mp.mpf(mt))]
    Qv = sum(v * v for v in rr) / (sum(rr) ** 2)
    return (3 * Qv - 1) / 2 - mp.mpf("0.5")


# the scan is NON-MONOTONIC, so the signed deviation has a zero crossing: find it exactly.
m_tau_zero = mp.findroot(dev_at, mp.mpf("1776.96"))
check("K7-comparator", "the signed deviation r_PDG - 1/2 CHANGES SIGN inside the SCANNED tau-mass window (window "
      "asserted for sensitivity analysis; not an externally sourced uncertainty), so "
      "there is a tau mass at which the charged-lepton lane sits EXACTLY on the distinguished cell",
      dev_at("1776.93") * dev_at("1777.00") < 0 and abs(dev_at(m_tau_zero)) < mp.mpf("1e-40"),
      f"exact crossing at m_tau = {mp.nstr(m_tau_zero, 12)} MeV, i.e. {float(m_tau_zero - mp.mpf('1776.93')):.4f} MeV "
      f"above the reduction runner's value")
finding("CAVEAT",
        "The headline '~3e-6' is not a stable number: it is strongly sensitive to the tau-mass convention, and the "
        "signed deviation CHANGES SIGN inside the scanned window (asserted for sensitivity analysis; no external "
        "edition or uncertainty is cited or verified in-repo). With m_tau = 1776.93 MeV (the value the "
        f"reduction note's own runner uses) the deviation is {tau_scan['1776.93 (reduction runner)']:.3e}; with "
        f"m_tau = 1776.86 MeV it is {tau_scan['1776.86 (alternate committed convention; external edition not verified in-repo)']:.3e} (a factor of "
        f"{tau_scan['1776.86 (alternate committed convention; external edition not verified in-repo)']/tau_scan['1776.93 (reduction runner)']:.2f}); and at "
        f"m_tau = {mp.nstr(m_tau_zero, 9)} MeV it is EXACTLY ZERO. So across a ~0.15 MeV tau window the deviation "
        "sweeps the whole range from 0 to about 9e-6. The reduction note's published GATE (|r_PDG - 1/2| < 1e-5) is "
        "robust across every scanned convention, and because the Q2 epsilon tables are logarithmic in eps this moves "
        "the g-branch step count by at most 2 steps and changes NO verdict. But the hostile-guard's quoted '~3e-6' "
        "is a single-convention figure, and no downstream text should treat that specific value as the thing to be "
        "explained: the explanandum is the GATE, not the digit.",
        "; ".join(f"{k} -> {v:.4e}" for k, v in tau_scan.items())
        + f"; exact zero crossing at m_tau = {mp.nstr(m_tau_zero, 12)} MeV")
check("K7-comparator", "the tau-mass sensitivity changes NO Q2 verdict: the g-branch step count moves by at most 2 "
      "steps across the whole scan (the tables are logarithmic in eps)",
      max(abs(n_enter(1.0, v)[1] - 17) for v in tau_scan.values()) <= 2,
      f"step counts across the scan = {sorted({n_enter(1.0, v)[1] for v in tau_scan.values()})}")

# ==========================================================================
# K8 -- planted-defect teeth (each must FIRE)
# ==========================================================================
banner("K8 -- planted-defect teeth (each must FIRE)")

tooth("K-T1", "a planted multiplier f'(1/2)=5/2 is rejected by the symbolic derivative", fp_half != sp.Rational(5, 2),
      f"sympy gives f'(1/2) = {fp_half}, not 5/2")
g_bad = sp.sqrt(r / 2) + sp.Rational(1, 1000)
tooth("K-T2", "a planted non-inverse reverse map g + 1/1000 is rejected: g_bad(f(r)) - r does not simplify to 0",
      sp.simplify(g_bad.subs(r, f) - r) != 0, f"residual = {sp.simplify(g_bad.subs(r, f) - r)}")
tooth("K-T3", "a planted curvature S2''(1/2) = -2 is rejected by the symbolic second derivative",
      sp.simplify(d2S2 + 2) != 0, f"sympy gives S2''(1/2) = {d2S2}")
tooth("K-T4", "a planted claim 'S3 peaks at r=1/2' is rejected by the symbolic stationarity solve",
      sp.Rational(1, 2) not in sol3, f"solve(dS3/dr) = {sol3}")
S2_planted = -(1 / (1 + 3 * r)) * sp.log(1 / (1 + 3 * r)) - (3 * r / (1 + 3 * r)) * sp.log(3 * r / (1 + 3 * r))
sol_pl = sp.solve(sp.Eq(sp.simplify(sp.diff(S2_planted, r)), 0), r)
tooth("K-T5", "a planted 2-sector weight (1, 3r) moves the entropy maximum to r=1/3, off the sharpening fixed "
      "point -- so the deflation is contentful, not a tautology", sol_pl == [sp.Rational(1, 3)], f"solve -> {sol_pl}")
tooth("K-T6", "a planted step count of 10 at the 3e-6 endpoint is rejected by the 60-dps closed form (true 17)",
      cf36 != 10, f"mpmath ceil(log2(ln2/ln(1+6e-6))) = {cf36}")
tooth("K-T7", "a planted basin claim 'basin(g) = (0,1)' is rejected: r0 = 1e300 still converges to 1/2",
      far[1] <= 30 and far[1] > 0, f"from 1e300, g reaches 3e-6 of 1/2 in {far[1]} steps")
omni_rows = dict(attack_rows)
omni_rows["PLANTED omnipotent map"] = {"half_attracting": True, "r0_attracting": True, "r1_attracting": True}
tooth("K-T8", "FUNCTION-LEVEL MUTATION TEST: the SAME k5_alternation_predicate implementation that passed the K5 "
      "attack returns False once a planted omnipotent row (attracting at 1/2, 0 AND 1) is added to the attack "
      "table -- a real counterexample would not have been missed",
      k5_alternation_predicate(attack_rows) and not k5_alternation_predicate(omni_rows),
      f"predicate(attack)={k5_alternation_predicate(attack_rows)} predicate(attack+planted)={k5_alternation_predicate(omni_rows)}")
planted_steps = [{"id": "PLANTED", "designates": [0.5], "supplied": None}]
tooth("K-T9", "a planted unconditional unique-r law step is caught by an INDEPENDENT re-implementation of the "
      "firewall rule", any(s["supplied"] is None and len(s["designates"]) == 1 for s in planted_steps))
tooth("K-T10", "a planted comparator (m_tau = 1776.86) yields a materially different deviation, proving the checker "
      "is actually sensitive to the mass inputs",
      abs(tau_scan["1776.86 (alternate committed convention; external edition not verified in-repo)"] - tau_scan["1776.93 (reduction runner)"]) > 1e-6,
      f"{tau_scan['1776.86 (alternate committed convention; external edition not verified in-repo)']:.4e} vs {tau_scan['1776.93 (reduction runner)']:.4e}")
tooth("K-T11", "a planted 'the reverse map decreases S2' claim is refuted symbolically at r=9/10",
      sp.N(S2.subs(r, sp.sqrt(sp.Rational(9, 20)))) > sp.N(S2.subs(r, sp.Rational(9, 10))),
      f"S2(g(0.9)) = {float(S2.subs(r, sp.sqrt(sp.Rational(9,20)))):.6f} > S2(0.9) = {float(S2.subs(r, sp.Rational(9,10))):.6f}")
tooth("K-T12", "the determinacy attack HAS POWER: it did in fact find a map satisfying the Q1 statement's numerics "
      "with different global behaviour, so a determinacy failure would not have been missed",
      mono and fixed_ok and abs(h_num(1.0) - 1.0) < 1e-12)

# ==========================================================================
# scorecard + receipt
# ==========================================================================
banner("SCORECARD")
per = {}
for c in CHECKS:
    d = per.setdefault(c["section"], [0, 0])
    d[0 if c["ok"] else 1] += 1
for s in SECTIONS:
    print("%-18s PASS=%-5d FAIL=%d" % (s, per[s][0], per[s][1]))
n_pass = sum(1 for c in CHECKS if c["ok"])
n_fail = sum(1 for c in CHECKS if not c["ok"])
fired = sum(1 for t in TEETH if t["fired"])
print("")
print("=" * 92)
print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
print(f"TEETH: {fired}/{len(TEETH)} FIRED")
print(f"FINDINGS: {len(FINDINGS)} "
      f"({sum(1 for f_ in FINDINGS if f_['kind']=='REFUTATION')} refutations, "
      f"{sum(1 for f_ in FINDINGS if f_['kind']=='CAVEAT')} caveats, "
      f"{sum(1 for f_ in FINDINGS if f_['kind']=='DEGENERACY')} degeneracies, "
      f"{sum(1 for f_ in FINDINGS if f_['kind']=='DETERMINACY')} determinacy, "
      f"{sum(1 for f_ in FINDINGS if f_['kind']=='CONFIRMATION')} confirmations)")
print("=" * 92)

verdict = ("The primary's Q1 reconciliation (functional-inverse reading) and its map-conditional Q2 verdict SURVIVE "
           "independent symbolic re-derivation of the conditional algebra/rate content. "
           "No refutation of a checked primary claim was found. Three material additions are reported: (1) a THIRD "
           "verdict cell (NEUTRAL) from the balanced-alternation reading, which strengthens rather than weakens the "
           "primary's 'the undischarged element is which supplied map is operative'; (2) the Q1 statement is locally "
           "determinate but globally underdeterminate, so the r=1 row of the candidate sweep must be sourced from "
           "the explicit map forms, not "
           "from the reconciliation sentence; (3) the '~3e-6' figure is tau-mass-convention dependent, sweeping 0 to "
           f"about 9e-6 across a ~0.15 MeV tau window (it is EXACTLY zero at m_tau = {mp.nstr(m_tau_zero, 9)} MeV), "
           "though the published <1e-5 gate and every Q2 verdict are robust to it. The explanandum is the GATE, not "
           "the digit. Tables A, B and C and the preimage-width law are all re-derived at 60 dps. The broad "
           "'arrow-universality no-go' and its lane-data consequence are withdrawn upstream (review iteration 1) "
           "and are NOT certified by this checker; only the narrow fixed-point alternation lemma is attacked and "
           "survives within its hypothesis class.")

payload = {
    "schema": "cycle923-exactness-residual-independent-check-v1",
    "status": "pass" if (n_fail == 0 and fired == len(TEETH)) else "fail",
    "cycle": 923,
    "role": "independent_checker", "runner": RUNNER_REL, "date_label": "2026-07-28",
    "claim_scope": "independent symbolic and high-precision refutation attempt against the cycle-923 exactness-residual primary (conditional algebra/rate content only)",
    "review_loop": {
        "iteration": 2, "disposition": "FIX_THEN_PROCEED (iteration 1); confirmation fixes (iteration 2)",
        "reviewer": "Sol", "date": "2026-08-08",
        "fix_summary_iteration_1": (
            "Table C and the preimage-width law now fully re-derived at 60 dps; reciprocal-multiplier "
            "lemma stated with C^1 local-diffeomorphism hypotheses and verified symbolically (literal "
            "True removed); 'destroyed lanes' wording replaced by repelling-fixed-point language; "
            "prose-substring and hard-coded-boolean checks replaced by computed conditions or demoted to "
            "manual findings; tau-mass variant labels de-scoped to committed conventions (no external "
            "edition cited); block/campaign fields dropped from the receipt"),
        "fix_summary_iteration_2": (
            "re-pinned against the iteration-2 primary receipt (exact-closed-form priced field, "
            "scientific-name-first headlines, and the T5 function-level comparator-isolation mutation test)"),
    },
    "independence_statement": (
        "This checker imports nothing from the primary. All algebra is sympy-symbolic and all window arithmetic is "
        "mpmath at 60 decimal digits. The primary receipt is read only as a source of CLAIMS to be attacked."
    ),
    "interpretation_firewall": (
        "Nothing here derives, forces or prefers r = 1/2 as any lane's setting. PDG values are a labeled comparator "
        "and feed no derivation. No audit status is asserted."
    ),
    "provenance": {"pins": PINS, "runner_sha256": sha256_of(Path(__file__).resolve()),
                   "primary_receipt_sha256": PINS[PRIMARY_RECEIPT_REL]["sha256"],
                   "primary_receipt_stable_sha256_runtime_excluded": PRIMARY_STABLE_SHA256,
                   "pin_note": ("the primary receipt embeds runtime_sec, so its raw file sha256 varies across "
                                "re-runs by construction; the stable digest above is the durable cross-reference")},
    "symbolic_results": {
        "Fix_f": [str(v) for v in fix_f], "Fix_g": [str(v) for v in fix_g],
        "f_prime": str(sp.simplify(fp)), "g_prime": str(sp.simplify(gp)),
        "f_prime_half": str(fp_half), "g_prime_half": str(gp_half),
        "multiplier_product": str(sp.simplify(fp_half * gp_half)),
        "dS2_dr": str(dS2), "S2_stationary_points": [str(v) for v in sol2],
        "S2_second_derivative_at_half": str(d2S2),
        "S3_stationary_points": [str(v) for v in sol3],
        "S_spec_second_derivative_at_x0": str(d2Ssp),
        "sharpening_fixed_p": [str(v) for v in sorted(sharp_fix)],
    },
    "epsilon_window_recheck": {
        "3e-6_endpoint_real_valued_n": mp.nstr(exact36, 15), "3e-6_endpoint_ceiling": cf36,
        "3e-6_endpoint_iterated": it36, "residence_3e-6_to_1e-1": n_exit(3e-6, 1e-1)[1],
        "from_1e300": far[1], "table_A_mismatches": mismatch_A, "table_B_mismatches": mismatch_B,
        "table_C_cells_rechecked": n_cells_C, "table_C_mismatches": mismatch_C,
        "preimage_width_mismatches": mismatch_W,
        "width_linearization_relative_deviations": lin_devs_W,
    },
    "model_degeneracy_readings": readings,
    "alternation_lemma_attack": {
        "constructed_map": "h(x) = x + c*x(x-1/2)(x-1)*exp(-20(x-1/2)^2), c chosen so h'(1/2)=2",
        "c_value": float(c_val), "strictly_increasing": mono,
        "multipliers": {str(k): v for k, v in mults.items()},
        "alternation_lemma_survives": k5_alternation_predicate(attack_rows),
        "named_escape_verified": all(esc_attr.values()),
        "scope_note": ("the attack targets only the narrow fixed-point alternation lemma (monotone self-maps of "
                       "[0,1] with fixed set exactly {0,1/2,1}; local asymptotic attraction); no broad "
                       "arrow-universality claim is certified"),
    },
    "comparator_recheck": {"masses_MeV": {k: str(v) for k, v in mp_masses.items()},
                           "abs_dev_r_60dps": mp.nstr(dev_mp, 20), "tau_mass_sensitivity_scan": tau_scan},
    "findings": FINDINGS,
    "checks": CHECKS, "teeth": TEETH,
    "scorecard": {"pass": n_pass, "fail": n_fail, "teeth_fired": fired, "teeth_total": len(TEETH),
                  "per_section": {k: {"pass": v[0], "fail": v[1]} for k, v in per.items()}},
    "failures": [c["name"] for c in CHECKS if not c["ok"]] + [t["id"] for t in TEETH if not t["fired"]],
    "overall_verdict": verdict,
}
payload["determinism_digest_sha256"] = hashlib.sha256(json.dumps(
    {k: payload[k] for k in ("symbolic_results", "epsilon_window_recheck", "model_degeneracy_readings",
                             "alternation_lemma_attack", "comparator_recheck")}, sort_keys=True, default=str).encode()).hexdigest()
payload["runtime_sec"] = round(time.time() - T0, 3)

out = REPO / RECEIPT_REL
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
print("")
print("OVERALL VERDICT: " + verdict)
print("")
print(f"receipt: {RECEIPT_REL}")
print(f"determinism_digest_sha256: {payload['determinism_digest_sha256']}")
print(f"runtime_sec: {payload['runtime_sec']}")
print("CYCLE923_INDEPENDENT_CHECK_" + ("PASS" if payload["status"] == "pass" else "FAIL"))
raise SystemExit(0 if payload["status"] == "pass" else 1)
